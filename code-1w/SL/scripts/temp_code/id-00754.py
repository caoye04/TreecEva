from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def preprocess_data(raw):
    processed = []
    noise_offset = 0.3
    temp_sum = 0
    count_map = defaultdict(int)
    
    for val in raw:
        if val < 0:  # Invalid reading
            continue
        normalized = round(val - noise_offset, 2)
        temp_sum += normalized
        count_map[normalized] += 1
        processed.append(normalized)
    
    # Misleading statistic (not used later)
    average_raw = temp_sum / len(processed) if processed else 0
    return processed, count_map

# Identify frequent patterns (mostly irrelevant for final score)
def analyze_repetition(seq):
    freq_counter = Counter(seq)
    repeated_values = [k for k, v in freq_counter.items() if v > 1]
    pattern_score = len(repeated_values) * 0.2
    return pattern_score, repeated_values

# Core calculation with masking and weighted aggregation
def apply_weight_mask(values, mask):
    masked = []
    for i in range(len(values)):
        index_key = i % len(mask)
        applied = values[i] * mask[index_key]
        masked.append(applied)
    return masked

# Final scoring logic
def calculate_final_score(dataset, importance_weights):
    cleaned_data, occurrences = preprocess_data(dataset)
    
    # Red herring: analyze repetition but result not used
    rep_score, common_vals = analyze_repetition(cleaned_data)
    
    # Apply transformation using bitwise adjustment (obscure but valid)
    adjusted = []
    for x in cleaned_data:
        int_x = int(x * 10)
        flipped = int_x ^ 15  # Bitwise XOR with constant
        adjusted.append(flipped / 10.0)
    
    # Weighted combination
    weighted_adjusted = apply_weight_mask(adjusted, importance_weights)
    
    # Aggregate with offset based on length (actual contributor)
    base_total = sum(weighted_adjusted)
    length_factor = len(weighted_adjusted) * 0.5
    penalty = 0
    
    # Spurious conditional check (never triggers in this input)
    if any(x < -5 for x in weighted_adjusted):
        penalty = 10
    
    # Actual answer computation
    final_score = int(base_total + length_factor - penalty)
    
    # Extra unused variables to increase cognitive load
    debug_info = {
        'size': len(dataset),
        'valid_count': len(cleaned_data),
        'mask_used': importance_weights.copy()
    }
    
    return final_score

# Input data (simulated IoT sensor stream)
sensor_readings = [2.3, 1.8, 2.3, 4.1, -0.5, 3.9, 4.1, 2.2, 5.0]
weights = [0.8, 1.2, 0.5, 1.0]

# Execute critical statement
cleaned, _ = preprocess_data(sensor_readings)
repetition_metric, _ = analyze_repetition(cleaned)
final_score = calculate_final_score(sensor_readings, weights)

print(f"Result: {final_score}")