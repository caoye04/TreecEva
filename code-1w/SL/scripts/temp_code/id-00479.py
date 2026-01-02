def calculate_final_score(raw_data, limits):
    temp_results = []
    anomaly_count = 0
    normalization_factor = 0.85
    scaling_offset = 12
    
    # Preprocess and filter data using modular arithmetic and conditional logic
    for index, (value, flag) in enumerate(zip(raw_data, [x % 2 == 0 for x in raw_data])):
        if value < 0:
            adjusted = abs(value) * normalization_factor
        else:
            adjusted = (value + scaling_offset) ** 0.5
        
        # Conditional branching with red herring computation
        if index % 3 == 0:
            dummy_shift = adjusted * 0.1
            adjusted -= dummy_shift  # Slight distraction

        if adjusted > limits[index % len(limits)]:
            temp_results.append(adjusted * 0.9)
            anomaly_count += 1
        else:
            temp_results.append(adjusted)

    # Secondary processing with lambda (used idiomatically)
    filtered_vals = list(filter(lambda x: x > 5, temp_results))
    
    # Irrelevant aggregation (distractor)
    avg_filtered = sum(filtered_vals) / len(filtered_vals) if filtered_vals else 0
    max_val = max(temp_results) if temp_results else 0
    
    # Core logic: weighted contribution based on position parity
    weighted_sum = 0
    for i, val in enumerate(temp_results):
        weight = 1.1 if i % 2 == 0 else 0.9
        weighted_sum += val * weight
    
    # Final score calculation - this is the key line
    final_score = int(weighted_sum - (anomaly_count * 2.5))
    
    # Dead code path (never executed, but plausible)
    if anomaly_count > 100:
        final_score = -1  # Impossible under input constraints
        
    return final_score

# Input setup
input_data = [16, -9, 25, 4, -13, 36, 7, -4, 18]
thresholds = [7.5, 6.0, 8.2]

# Execution
result = calculate_final_score(input_data, thresholds)
print(f"Result: {result}")