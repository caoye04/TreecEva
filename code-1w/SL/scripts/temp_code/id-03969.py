def calculate_thermal_output(efficiency, phase):
    base_output = 1500
    adjustment = 23 if phase > 0.5 else 17
    
    # Irrelevant signal processing computations (distractor)
    signal_strength = 89.4
    noise_floor = 12.7
    snr = signal_strength / noise_floor
    filtered_signal = [x * 0.87 for x in [signal_strength, noise_floor]]  # Unused list comprehension

    # Core thermal logic with conditional expression
    efficiency_factor = efficiency if efficiency > 0.7 else 0.7 + (efficiency * 0.1)
    power_modulator = 1.2 if efficiency_factor >= 0.85 else 0.9

    # Intermediate irrelevant state tracking
    status_codes = {'INIT': 100, 'RUN': 200, 'FAULT': 500}
    current_status = status_codes['RUN']
    heartbeat_interval = 500  # Dead code (not used later)

    # Main calculation chain
    raw_capacity = base_output * efficiency_factor * power_modulator
    phase_correction = 1 + (phase * 0.15) if phase > 0 else 0.95
    
    # Secondary distractor: unused sensor array simulation
    sensors = ['S1', 'S2', 'S3']
    calibration_offsets = {s: len(s) * 0.05 for s in sensors}  # Unused dict comprehension

    # Final output computation
    adjusted_capacity = raw_capacity * phase_correction
    damping_factor = 0.985
    thermal_capacity = int(adjusted_capacity * damping_factor)
    
    return thermal_capacity

# System initialization parameters
initial_efficiency = 0.82
system_phase = 0.68
monitoring_enabled = True
log_level = 'INFO'

# Spurious data structure (semi-relevant but not critical)
data_buffer = [{'timestamp': t, 'value': t*0.1} for t in range(10)]  # Not used

# Critical execution point
thermal_capacity = calculate_thermal_output(initial_efficiency, system_phase)

# Redundant validation check (does not alter flow)
if monitoring_enabled:
    if log_level == 'INFO':
        debug_msg = f"System active: {thermal_capacity} units"

print(f"Result: {thermal_capacity}")