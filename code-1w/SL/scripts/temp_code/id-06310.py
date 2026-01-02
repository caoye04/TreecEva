def calculate_grid_efficiency(phases, base_loads, peak_multiplier=1.2):
    adjusted_powers = []
    temp_buffer = []  # unused buffer, minor distraction

    for i, (phase, load) in enumerate(zip(phases, base_loads)):
        if phase == 'critical':
            adjusted_load = load * peak_multiplier
        else:
            adjusted_load = load * 0.85
        
        # Normalize using integer division and rounding
        normalized = int(round(adjusted_load // 1.1))
        adjusted_powers.append(normalized)
    
    total_phase_power = sum(adjusted_powers)
    return total_phase_power

# Simulate power grid phase loads
phases_status = ['normal', 'critical', 'normal', 'critical']
base_power_loads = [120, 200, 150, 180]

result = calculate_grid_efficiency(phases_status, base_power_loads)
total_phase_power = result
print(f"Result: {total_phase_power}")