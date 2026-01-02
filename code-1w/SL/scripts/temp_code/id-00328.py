def analyze_system_metrics(data_points):
    filtered_data = [x for x in data_points if x > 0]
    offset_correction = sum(filtered_data) // len(filtered_data) if filtered_data else 0
    adjusted_values = [x - offset_correction for x in data_points]
    return adjusted_values

energy_fluctuations = [12, -5, 23, 8, 16, -4, 7]
baseline_shift = 3

# Irrelevant transformation chain (distractor)
transformed_signal = [x * 2 + baseline_shift for x in energy_fluctuations]
signal_magnitude = max(transformed_signal) - min(transformed_signal)
scaled_envelope = [abs(x) ** 0.5 for x in transformed_signal]

# Dead code path - never used (distractor)
def deprecated_normalization(vec):
    norm_factor = sum(vec)
    return [v / norm_factor for v in vec]

# Simulate auxiliary sensor array (mostly irrelevant)
sensor_readings = {
    's1': 42,
    's2': 18,
    's3': 93
}
sensor_avg = sum(sensor_readings.values()) / len(sensor_readings)
sensor_variance = sum((v - sensor_avg) ** 2 for v in sensor_readings.values())

# Core processing with meaningful intermediate steps
def calculate_thermal_output(flux):
    raw_peaks = [x for x in flux if x > 10]
    peak_count = len(raw_peaks)
    
    # Apply conditional weighting based on parity pattern
    weight_map = {i: 2 if val % 2 == 0 else 1.5 for i, val in enumerate(flux)}
    weighted_flux = sum(flux[i] * weight_map[i] for i in range(len(flux)))
    
    # Set operation to filter redundant contributions
    unique_contributions = set(abs(x) for x in flux)
    contribution_adjustment = len(unique_contributions.intersection({8, 12, 16, 23}))
    
    # Misleading intermediate calculation (not final)
    nominal_output = weighted_flux * 0.75 + (peak_count * 5)
    
    # Final thermal model with correction factor
    correction_factor = 0.9 if len(flux) % 2 == 1 else 1.0
    thermal_index = sum(abs(x) for x in flux) * correction_factor
    
    # Critical integration step
    final_score = thermal_index - nominal_output * 0.3
    
    # Actual return value derived from complex logic
    return int(final_score + contribution_adjustment)

# Auxiliary state tracking (distractor)
current_state = 'ACTIVE'
state_log = []
if current_state == 'ACTIVE':
    state_log.append('initialized')
    state_log.append('validated')

# Key execution point
adjusted_energy = analyze_system_metrics(energy_fluctuations)
thermal_capacity = calculate_thermal_output(energy_fluctuations)

# Print result as required
print(f"Result: {thermal_capacity}")