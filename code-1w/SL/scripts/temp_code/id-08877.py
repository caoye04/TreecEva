def calculate_final_score(data_map, threshold):
    # Irrelevant accumulator for distraction
    temp_sum = 0
    for key in data_map:
        temp_sum += len(key)  # Distractor: not used later

    # Semi-relevant transformation
    normalized_values = []
    base_offset = sum(data_map.values()) / len(data_map) if data_map else 1
    
    for val in data_map.values():
        adjusted = val - base_offset
        if abs(adjusted) > 0.1:
            normalized_values.append(abs(adjusted))
    
    # Dead code path (never executed under current logic)
    outlier_flag = False
    if len(normalized_values) > 100:
        outlier_flag = True  # Unreachable due to input size

    # Core logic: count how many original values exceed threshold
    valid_entries = set()
    for k, v in data_map.items():
        if v >= threshold:
            valid_entries.add(k)
    
    # Additional distraction with set operations
    extra_filter = {k.upper() for k in data_map.keys()}
    shadow_count = len(extra_filter.intersection({'A', 'X', 'Z'}))  # Unused

    # Actual answer computation
    raw_total = sum(data_map[k] for k in valid_entries)
    penalty = len([v for v in data_map.values() if v < 5])
    final_score = raw_total - penalty * 2

    return final_score

# Main execution
config_data = {
    'alpha': 12,
    'beta': 8,
    'gamma': 4,
    'delta': 15,
    'epsilon': 3
}
threshold = 5

# Misleading pre-processing
buffer = [x * 1.5 for x in config_data.values()]
aggregate = sum(buffer) / len(buffer)
dummy_dict = {k: aggregate for k in ['temp', 'hold', 'spare']}

final_score = calculate_final_score(config_data, threshold)
print(f"Result: {final_score}")