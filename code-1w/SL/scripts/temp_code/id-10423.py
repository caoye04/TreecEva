def calculate_final_score(raw_data, limits):
    # Preprocessing: filter and transform data
    processed = []
    temp_sum = 0
    outlier_count = 0  # distractor: not used in final logic

    for i, (name, val) in enumerate(zip([f'item_{j}' for j in range(len(raw_data))], raw_data)):
        if val < 0:  # skip negative values
            continue
        adjusted = val * (i + 1)  # position-based weighting
        temp_sum += adjusted
        if adjusted > limits['high']:
            outlier_count += 1
        processed.append(adjusted)

    # Secondary computation: irrelevant average
    avg_val = sum(processed) / len(processed) if processed else 0
    dummy_list = [x for x in processed if x > avg_val]  # distractor list

    # Scoring logic with lambda filter
    passing = list(filter(lambda x: x >= limits['medium'], processed))
    bonus = len(passing) * 5 if len(passing) % 2 == 0 else 0  # conditional bonus

    base_score = 0
    for idx, v in enumerate(processed):
        if v < limits['low']:
            base_score -= v // 10
        else:
            base_score += v // 5

    # Final adjustment using dictionary lookup
    modifiers = {'A': 1.1, 'B': 1.05, 'C': 1.0}
    category = 'B'
    scaling_factor = modifiers.get(category, 1.0)

    # Dead code path (not executed due to category='B')
    if category == 'X':
        scaling_factor *= 0.9  # unreachable

    final_score = int((base_score + bonus) * scaling_factor)

    # Unrelated string operation (distractor)
    status_msg = "Processing Complete".lower().replace(" ", "_")
    msg_length = len(status_msg)  # unused

    return final_score

# Main execution
sensor_readings = [12, -5, 8, 15, 3, 22]
thresholds = {'low': 10, 'medium': 15, 'high': 20}
data = sensor_readings.copy()

# Call function and store result
target_result = calculate_final_score(data, thresholds)
print(f"Result: {target_result}")