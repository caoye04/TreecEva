def calculate_grid_efficiency(phases, base_load, threshold):
    phase_names = ['alpha', 'beta', 'gamma']
    frequency_shift = 0.85
    total_phase_power = 0
    raw_powers = []
    
    for idx, load in enumerate(phases):
        adjusted_load = (load + base_load) * (idx + 1)
        if adjusted_load > threshold:
            adjusted_load = adjusted_load % threshold
        raw_powers.append(adjusted_load)
    
    scaled_powers = [p * frequency_shift for p in raw_powers]
    status_flags = [1 if p > 50 else 0 for p in scaled_powers]
    
    adjusted_powers = []
    for i, power in enumerate(scaled_powers):
        correction_factor = 1.1 if status_flags[i] else 0.95
        final_power = power * correction_factor
        adjusted_powers.append(round(final_power, 2))
    
    total_phase_power = sum(adjusted_powers)
    
    return total_phase_power

phases_input = [23, 45, 67]
base_load_val = 12
threshold_limit = 80
total_phase_power = calculate_grid_efficiency(phases_input, base_load_val, threshold_limit)
print(f"Result: {total_phase_power}")