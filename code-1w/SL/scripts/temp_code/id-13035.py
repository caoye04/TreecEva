def calculate_grid_efficiency(phase_voltages, phase_loads):
    base_efficiency = 0.85
    adjusted_powers = []
    
    for i, (voltage, load) in enumerate(zip(phase_voltages, phase_loads)):
        raw_power = voltage * load
        loss_factor = 1 - (load / 100) * 0.15
        
        if load > 80:
            safety_margin = 0.9
        else:
            safety_margin = 1.0
        
        adjusted_power = raw_power * loss_factor * safety_margin * base_efficiency
        adjusted_powers.append(round(adjusted_power, 3))
    
    total_phase_power = sum(adjusted_powers)
    return total_phase_power

# Simulated three-phase electrical grid data
voltages = [230, 232, 228]
loads = [75, 92, 64]

result = calculate_grid_efficiency(voltages, loads)
print(f"Result: {result}")