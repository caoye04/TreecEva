def calculate_thermal_output(efficiency, gradient):
    base_output = 12.5 * gradient
    loss_factor = 0.87 if efficiency > 0.75 else 0.94
    adjusted_output = base_output * efficiency * loss_factor
    
    # Irrelevant signal processing simulation (distractor)
    signal_strength = 4.2
    noise_floor = 0.15
    snr = signal_strength / noise_floor  # Unused in final result
    filtered_estimate = snr * 0.63  # Dead code path
    
    return round(adjusted_output, 4)

# System calibration parameters (some irrelevant)
calibration_mode = True
reference_voltage = 3.3
baseline_offset = 0.02  # Unused

# Main physical parameters
temperature_gradient = 18.4  # Kelvin per meter
efficiency_factor = 0.82

# Auxiliary environmental monitoring (distraction block)
humidity_levels = [45, 52, 58, 49, 61]
avg_humidity = sum(humidity_levels) / len(humidity_levels)
dew_point_estimate = avg_humidity * 0.6 + 5.5  # Not used

# State tracking for non-critical subsystem
status_flags = [False, True, False]
active_sensors = sum(1 for flag in status_flags if flag)  # Distractor computation

# Key physics-based calculation
thermal_capacity = calculate_thermal_output(efficiency_factor, temperature_gradient)

# Additional unrelated transformation
scaling_matrix = [[1.1, 0.3], [0.3, 1.1]]
normalized_trace = sum(scaling_matrix[i][i] for i in range(2))  # Red herring

# Final output
print(f"Result: {thermal_capacity}")