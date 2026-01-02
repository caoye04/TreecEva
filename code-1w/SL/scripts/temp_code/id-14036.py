def calculate_efficiency(readings, limits):
    filtered_data = [x for x in readings if x > limits['min'] and x < limits['max']]
    adjusted_values = []
    
    temp_offset = 0.0
    cumulative_shift = 0
    
    for i, val in enumerate(filtered_data):
        if i % 2 == 0:
            shifted = val * 1.1 + temp_offset
        else:
            shifted = val * 0.9 - temp_offset
        
        # Irrelevant intermediate tracking
        cumulative_shift += abs(shifted - val)
        adjusted_values.append(shifted)

    # Dead computation - does not affect final result
    outlier_count = sum(1 for x in readings if x < limits['min'] or x > limits['max'])
    stability_ratio = len(readings) / (outlier_count + 1)

    base_efficiency = sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0
    
    # Secondary adjustment using tuple unpacking and logical masking
    factor_tuple = (1.05, 0.95)
    boost_enabled, penalty_active = True, False
    
    if len(adjusted_values) > 5 and base_efficiency > 75:
        multiplier = factor_tuple[boost_enabled and not penalty_active]
    else:
        multiplier = factor_tuple[penalty_active]

    final_efficiency = base_efficiency * multiplier
    
    # Key derived variable
    thermal_output = int(final_efficiency // 1)
    
    # Red herring variables
    energy_fragments = {f'frag_{i}': v * 0.01 for i, v in enumerate(readings)}
    total_dissipation = sum(v for k, v in energy_fragments.items() if 'frag_2' not in k)
    
    return thermal_output

# Main execution context
energy_sequence = [68, 72, 76, 81, 64, 77, 85, 73]
threshold_map = {'min': 65, 'max': 83}

# Misleading pre-computations
avg_input = sum(energy_sequence) / len(energy_sequence)
deviation_score = sum(abs(x - avg_input) for x in energy_sequence)

thermal_output = calculate_efficiency(energy_sequence, threshold_map)
print(f"Result: {thermal_output}")