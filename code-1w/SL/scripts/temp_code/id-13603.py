def analyze_temperatures(temp_list):
    """Irrelevant helper function for temperature analysis."""
    avg = sum(temp_list) / len(temp_list)
    anomalies = [t for t in temp_list if abs(t - avg) > 10]
    return len(anomalies)


def preprocess_strings(str_list):
    """Distractor: Processes strings but not used in final computation."""
    cleaned = [s.strip().lower() for s in str_list]
    tokenized = [list(zip(s, enumerate(s))) for s in cleaned if s]
    return tokenized


def validate_checksum(sequence):
    """Red herring function that computes a checksum but isn't part of main logic."""
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) * 3
    return checksum == 42  # Rarely true, misleading


def compute_weighted_sum(values, factors):
    """Used in main path, computes weighted accumulation."""
    total = 0.0
    for idx, (v, f) in enumerate(zip(values, factors)):
        if v < 0:
            total -= v * f ** 2
        else:
            total += v * (f + idx % 3)
    return total


def filter_outliers_and_shift(data, threshold=50):
    """Modifies data by filtering and bit-shifting irrelevant components."""
    filtered = [x for x in data if abs(x) <= threshold]
    shifted = []
    for val in filtered:
        if val > 0:
            shifted.append(val << 1)
        else:
            shifted.append(val >> 1)
    return shifted


def calculate_final_score(log_entries, importance_weights):
    """Core function that determines the answer."""
    base_magnitude = sum(abs(x) for x in log_entries) // 10
    
    # Step 1: Apply transformation using string method as distractor
    dummy_labels = ["Entry_" + str(i).zfill(3) for i in range(len(log_entries))]
    labeled_count = len([lbl for lbl in dummy_labels if '00' in lbl])  # Red herring
    
    # Step 2: Filter and shift (some side effect operations)
    processed_data = filter_outliers_and_shift(log_entries, threshold=60)
    
    # Step 3: Compute primary accumulation
    raw_score = compute_weighted_sum(processed_data, importance_weights[:len(processed_data)])
    
    # Step 4: Add adjustment based on enumeration logic
    adjustment = 0
    for index, value in enumerate(processed_data):
        if index % 2 == 0 and value > 0:
            adjustment += value.bit_length()
    
    # Step 5: Final composition
    final_score = int(raw_score + adjustment + base_magnitude)
    
    # Dead code branch — never executed due to fixed condition
    if validate_checksum([base_magnitude, adjustment, len(importance_weights)]):
        final_score *= 2  # Misleading multiplication
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Irrelevant data
    weather_readings = [23, 18, 92, 24, 17, 88, 26]
    text_fragments = ["  DataPoint A  ", "  B  ", "", " PointC "]
    
    # Distractor variables
    temp_anomalies = analyze_temperatures(weather_readings)
    structured_tokens = preprocess_strings(text_fragments)
    
    # Key input data
    data_log = [12, -7, 34, 5, -21, 18, 44, -3, 9, 25]
    weights = [1.5, 0.8, 2.1, 1.0, 0.5, 1.3, 2.0, 0.7, 1.1, 1.9]
    
    # Unused intermediate calculations
    dummy_sum = sum(w ** 2 for w in weights) / len(weights)
    max_log_value = max(data_log)
    min_weight = min(weights)
    
    # Core computation
    final_score = calculate_final_score(data_log, weights)
    
    # Output result
    print(f"Result: {final_score}")