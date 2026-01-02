import itertools

def analyze_pattern(sequence):
    count = 0
    for a, b in itertools.pairwise(sequence):
        if abs(a - b) > 2:
            count += 1
    return count

def normalize_data(data_list):
    min_val = min(data_list)
    max_val = max(data_list)
    range_val = max_val - min_val
    normalized = [(x - min_val) / range_val for x in data_list]
    scaling_factor = sum(normalized) / len(normalized)
    return [x * scaling_factor for x in normalized]

def adjust_thermal(matrix, limit):
    flat_data = list(itertools.chain.from_iterable(matrix))
    filtered = [x for x in flat_data if x > limit]
    if not filtered:
        return 0
    
    # Irrelevant string processing (distractor)
    status_msg = "Processing thermal data..."
    status_clean = status_msg.lower().replace("...", "").strip()
    log_entry = f"Status: {status_clean} | Samples: {len(filtered)}"
    
    # Semi-relevant normalization
    processed = normalize_data(filtered)
    
    # Key computation
    base_score = sum(processed)
    
    # Dead code path (distractor)
    if len(processed) > 100:
        anomaly_flag = True
        correction = 0.95
    else:
        correction = 1.0  # Never applied due to condition
    
    # Another distractor: unused variable with complex derivation
    entropy_proxy = 0
    for i in range(1, len(processed)):
        diff = abs(processed[i] - processed[i-1])
        entropy_proxy += diff * diff

    # Actual logic step: apply pattern analysis as adjustment factor
    raw_pattern_score = analyze_pattern([int(x * 100) for x in processed])
    adjustment = 1 + (raw_pattern_score / 100)
    final_capacity = base_score * adjustment
    
    return int(final_capacity)

# Main execution
sensor_readings = [
    [12, 15, 30, 8],
    [5, 18, 22, 40],
    [7, 11, 9, 50]
]

calibration_key = "ABC123-X"
diagnostic_mode = False
threshold = 10

energy_matrix = []
for row in sensor_readings:
    updated_row = []
    for val in row:
        if val >= threshold:
            updated_row.append(val ** 0.5 * 3.2)
        else:
            updated_row.append(val * 0.8)
    energy_matrix.append(updated_row)

# Secondary irrelevant transformation
string_data = [str(int(x)) for x in itertools.chain.from_iterable(energy_matrix)]
joined_data = "-".join(string_data)
split_back = [int(s) for s in joined_data.split('-') if s.isdigit()]

thermal_capacity = adjust_thermal(energy_matrix, threshold)

# Output result
print(f"Result: {thermal_capacity}")