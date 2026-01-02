def calculate_thermal_output(profile, limit):
    filtered_data = [x for x in profile if x > limit]
    normalized = [x / sum(filtered_data) for x in filtered_data]
    
    # Irrelevant transformation (distractor)
    mirrored = normalized[::-1]
    average_mirror = sum(mirrored) / len(mirrored)
    
    # Semi-relevant preprocessing
    weighted_sum = 0
    for i, val in enumerate(normalized):
        weighted_sum += val * (i + 1)
    
    # Core calculation branch
    if len(filtered_data) > 3:
        segment = normalized[1:-1]  # slicing central portion
        adjustment_factor = sum(segment) * 0.85
    else:
        adjustment_factor = 1.0
    
    base_output = sum(normalized)
    thermal_capacity = (base_output * weighted_sum) + adjustment_factor
    
    # Dead code path (distractor)
    secondary_metric = 0
    for x in profile:
        if x < 0:
            secondary_metric += x ** 2
    
    return thermal_capacity

# Main execution context
energy_profile = [12, 7, 15, 4, 23, 9, 18]
threshold = 8
temperature_buffer = [t**2 for t in energy_profile if t < 5]
baseline_shift = max(energy_profile) - min(energy_profile)

# Key statement
thermal_capacity = calculate_thermal_output(energy_profile, threshold)

print(f"Result: {thermal_capacity}")