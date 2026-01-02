def calculate_thermal_capacity(data, limit):
    filtered_readings = [x for x in data if x > limit]
    indices = [i for i, _ in enumerate(data) if _ > limit]
    paired_data = list(zip(filtered_readings, indices))
    
    # Distractor: Irrelevant transformation on squared values
    squared_deltas = [((x - limit) ** 2) for x in data]
    average_square = sum(squared_deltas) / len(squared_deltas) if squared_deltas else 0
    
    # Semi-relevant preprocessing
    offset_values = [data[i] - i for i in range(len(data))]
    valid_offsets = [v for v in offset_values if v > limit - 10]
    
    # Core logic: weighted sum based on position and value
    weighted_sum = 0
    for val, idx in paired_data:
        if idx % 2 == 0:
            weighted_sum += val * 1.5
        else:
            weighted_sum += val * 0.8
    
    # Secondary distractor: unused statistical calculation
    total_variance = 0
    if filtered_readings:
        mean_val = sum(filtered_readings) / len(filtered_readings)
        total_variance = sum((x - mean_val) ** 2 for x in filtered_readings)

    # Final capacity calculation (only depends on weighted_sum)
    adjustment_factor = 1.2 if len(indices) > 3 else 0.9
    thermal_capacity = int(weighted_sum * adjustment_factor)
    
    return thermal_capacity

# Main execution
flux_data = [12, 7, 15, 23, 8, 19, 4, 11]
baseline = 10
threshold = baseline + 1

# Unused auxiliary variables (distractors)
peak_moment = max(enumerate(flux_data), key=lambda x: x[1])
decay_sequence = flux_data[::-1]

thermal_capacity = calculate_thermal_capacity(flux_data, threshold)

# Output result as required
print(f"Result: {thermal_capacity}")