def calculate_phase_load(voltages, currents, thresholds):
    """
    Calculate adjusted power across electrical phases with dynamic thresholding.
    """
    base_powers = [v * i for v, i in zip(voltages, currents)]
    
    # Determine adaptive threshold based on median voltage
    sorted_voltages = sorted(voltages)
    median_voltage = sorted_voltages[len(sorted_voltages) // 2]
    adaptive_threshold = median_voltage * 0.75
    
    # Irrelevant diagnostic variable (minimal interference)
    diagnostic_mode = False
    
    # Adjust power values based on current thresholds and voltage conditions
    adjusted_powers = []
    for idx, (power, current, threshold) in enumerate(zip(base_powers, currents, thresholds)):
        if voltages[idx] > adaptive_threshold:
            adjustment_factor = 1.2 if current > threshold else 1.0
n            adjusted_power = power * adjustment_factor
        else:
            adjusted_power = power * 0.8
        adjusted_powers.append(round(adjusted_power, 3))
    
    total_phase_power = sum(adjusted_powers)
    return total_phase_power

# Input data
phase_voltages = [120, 240, 208]
current_draws = [15.5, 22.0, 18.3]
overload_limits = [20, 25, 20]

result = calculate_phase_load(phase_voltages, current_draws, overload_limits)
print(f"Result: {result}")