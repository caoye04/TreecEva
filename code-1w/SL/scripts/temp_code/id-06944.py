def calculate_final_score(raw_data, limits):
    # Preprocess: extract and normalize values
    normalized = [x / max(raw_data) * 100 for x in raw_data if x > 0]
    
    # Irrelevant transformation: string-based distraction
    labels = ['val_' + str(i) for i in range(len(raw_data))]
    labeled_map = {lbl: val for lbl, val in zip(labels, raw_data)}
    unused_stats = ''.join([lbl.upper() for lbl in labels if '3' in lbl or '7' in lbl])

    # Core logic: count how many exceed each threshold, then combine
    threshold_met = []
    for limit in limits:
        count = 0
        for val in normalized:
            if val >= limit:
                count += 1
        threshold_met.append(count)
    
    # Accumulate weighted score
    cumulative = 0
    weights = [1.5, 2.0, 0.5]
    for i in range(len(threshold_met)):
        cumulative += weights[i] * threshold_met[i]
    
    # Distractor: complex string operation with no effect
    debug_str = "Debug" + "_".join([str(int(x)) for x in normalized[::len(normalized)//4+1]])
    temp_sum = sum([len(debug_str) for _ in range(2)])  # Unused computation
    
    # Final adjustment based on data characteristics
    peak_index = normalized.index(max(normalized))
    adjustment = (peak_index % 3) * 1.25
    final_score = cumulative + adjustment
    
    return final_score

# Input data
sensor_readings = [12, -5, 30, 8, 45, 22, 60, -10, 18]
thresh_values = [50, 25, 75]

# Execute
final_score = calculate_final_score(sensor_readings, thresh_values)
print(f"Target result: {final_score}")