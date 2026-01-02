def analyze_performance(raw_data, threshold=50):
    # Initialize tracking variables
    count_above = 0
    total_sum = 0
    temp_buffer = []
    outlier_count = 0

    # Process raw data and filter valid entries
    for value in raw_data:
        if value < 0:
            outlier_count += 1
            continue
        if value > threshold * 2:
            temp_buffer.append(value * 0.8)  # discounted heavy weights
        else:
            temp_buffer.append(value)

    # Compute average for normalization base
    valid_values = [v for v in temp_buffer if v >= threshold]
    if valid_values:
        avg_valid = sum(valid_values) / len(valid_values)
    else:
        avg_valid = threshold

    # Normalize all buffer values using average
    normalized = []
    for val in temp_buffer:
        norm_val = val / avg_valid * 100
        normalized.append(int(norm_val))

    # Introduce distraction: unused smoothing routine
    smoothed = []
    for i in range(len(normalized)):
        window = normalized[max(0, i-1):min(i+2, len(normalized))]
        smoothed.append(sum(window) / len(window))

    # Core logic: use set to deduplicate normalized scores
    normalized_set = set(normalized)
    redundant_check = len(normalized) - len(normalized_set)

    # Remove extremely low performers from consideration
    filtered_set = {x for x in normalized_set if x >= 40}

    # Secondary distraction: compute but do not use statistical spread
    if filtered_set:
        spread = max(filtered_set) - min(filtered_set)
        mid_point = (max(filtered_set) + min(filtered_set)) / 2
    
    # Final scoring uses only the maximum of the normalized set
    final_score = max(normalized_set, default=0)

    # Unrelated audit trail (dead code path for interference)
    audit_log = []
    if outlier_count > 5:
        audit_log.append("high_outliers")
    if redundant_check > 3:
        audit_log.append("high_redundancy")

    # Irrelevant transformation chain
    transformed = 0
    for x in range(3):
        transformed = (transformed + x) * 2
    
    return final_score

# Simulated dataset
data_stream = [45, 60, 75, 80, 40, 90, 95, 100, -5, 85, 85, 200, 180]

result = analyze_performance(data_stream)
print(f"Result: {result}")