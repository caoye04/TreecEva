def compute_scaled_median_value():
    raw_values = [45, 12, 78, 23, 56, 89, 34, 67]
    scaling_factor = 2.5
    offset = 10  # Irrelevant variable for slight distraction
    
    processed_data = [x + 1 for x in raw_values]
    sorted_data = sorted(processed_data)
    mid_index = len(sorted_data) // 2
    temp_debug = sorted_data[:3]  # Slicing used, minor distractor
    result = sorted_data[mid_index] * scaling_factor
    
    debug_msg = "Processing complete"  # Unused string, low interference
    return result

output = compute_scaled_median_value()
print(f"Result: {output}")