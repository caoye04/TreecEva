def calculate_efficiency(data, limit):
    filtered_entries = [row for row in data if sum(row) > limit]
    scaling_factor = 1.75
    offset_correction = 0.23
    temp_buffer = []
    
    for entry in filtered_entries:
        adjusted = [x * scaling_factor + offset_correction for x in entry]
        temp_buffer.append(adjusted)
    
    # Irrelevant aggregation (distractor)
    average_row_length = sum(len(row) for row in temp_buffer) / len(temp_buffer) if temp_buffer else 0
    max_value = max(max(row) for row in temp_buffer) if temp_buffer else 0
    
    # Core computation path
    cumulative_score = 0
    for processed in temp_buffer:
        segment_total = 0
        for val in processed:
            if val > 5.0:
                segment_total += val ** 0.5  # root contribution
            else:
                segment_total += val / 2.0
        cumulative_score += segment_total

    # Secondary irrelevant transformation
    noise_adjusted = [x - 0.1 for x in [cumulative_score] if x > 10]
    
    # Final efficiency model with fixed bias
    raw_efficiency = cumulative_score * 0.87
    bias_correction = len(filtered_entries) * 0.15
    final_efficiency = raw_efficiency + bias_correction
    
    return int(final_efficiency)

# System configuration
threshold = 12
profile_matrix = [
    [2, 3, 4],
    [5, 6, 7],
    [1, 1, 1],  # Will be filtered out
    [4, 4, 5],
    [3, 3, 7]
]

# Diagnostic variables (not affecting result)
diagnostic_mode = True
log_entries = len(profile_matrix)
baseline_reference = sum(sum(row) for row in profile_matrix)

# Critical execution point
thermal_capacity = calculate_efficiency(profile_matrix, threshold)

# Output result
print(f"Result: {thermal_capacity}")