def calculate_thermal_output(energy_levels, efficiency_curve):
    thermal_capacity = 0
    transient_buffer = 0
    baseline_shift = 1.0
    
    # Preprocess efficiency weights using enumerate for index-aware adjustment
    adjusted_efficiency = []
    for idx, eff in enumerate(efficiency_curve):
        if idx % 2 == 0:
            adjusted_efficiency.append(eff * 1.1)
        else:
            adjusted_efficiency.append(eff * 0.95)
    
    # Secondary buffer calculation - partially irrelevant
    buffer_accumulator = 0
    for val in energy_levels:
        buffer_accumulator += val ** 0.5
    normalization_factor = max(buffer_accumulator, 1)

    # Core logic with zip and conditional state updates
    for energy, adj_eff in zip(energy_levels, adjusted_efficiency):
        raw_contribution = energy * adj_eff
        penalty_factor = 1.0
        
        if raw_contribution > 50:
            penalty_factor = 0.8
            transient_buffer += raw_contribution * 0.1
        elif raw_contribution < 10:
            penalty_factor = 1.2
            baseline_shift -= 0.05
        
        thermal_capacity += raw_contribution * penalty_factor
        
        # Early termination if threshold met (rarely triggered)
        if thermal_capacity > 300:
            thermal_capacity *= 0.9
            break
    
    # Irrelevant post-processing on dead variable
    final_buffer_state = transient_buffer * baseline_shift / (normalization_factor + 1e-5)
    
    return int(thermal_capacity)  # Final cast to integer

# Input data
energy_profile = [12, 45, 67, 8, 52, 31]
efficiency_map = [0.88, 0.75, 0.92, 0.68, 0.81, 0.77]

# Key assignment statement
thermal_capacity = calculate_thermal_output(energy_profile, efficiency_map)

print(f"Result: {thermal_capacity}")