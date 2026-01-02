def analyze_system_performance(parameters):
    base_load = parameters.get('load', 100)
    stress_factor = parameters.get('stress', 1.5)
    decay_rate = 0.95

    # Simulate transient response over time steps
    transient_state = [base_load]
    for i in range(1, 8):
        updated_load = transient_state[i-1] * stress_factor + (i % 3)
        if updated_load > 200:
            updated_load *= decay_rate
        transient_state.append(updated_load)

    peak_response = max(transient_state)
    normalized_response = [x / peak_response for x in transient_state]

    adjustment_offset = 0
    for val in normalized_response:
        if val > 0.8:
            adjustment_offset += 0.05
        elif val > 0.5:
            adjustment_offset += 0.02

    return peak_response, adjustment_offset


def calculate_thermal_response(series, efficiency):
    raw_sum = sum(series)
    penalty = 0
    for i, val in enumerate(series):
        if i % 2 == 0 and val > 150:
            penalty += 10
    adjusted_sum = raw_sum - penalty

    # Irrelevant computation: signal harmonics (not used in final result)
    harmonic_component = 0
    for i in range(len(series)):
        harmonic_component += series[i] * (i + 1) % 7

    # Actual thermal model
    if efficiency > 1.2:
        efficiency = 1.2
    thermal_energy = adjusted_sum * efficiency

    # Secondary correction based on pattern density
    high_activity_periods = len([x for x in series if x > 140])
    correction_factor = 1 - (high_activity_periods * 0.05) if high_activity_periods < 10 else 0.5
    thermal_energy *= correction_factor

    return int(thermal_energy)

# Main execution block
config_params = {'load': 120, 'stress': 1.6}

peak_val, offset_correction = analyze_system_performance(config_params)

# Generate synthetic time-series data from peak response
base_sequence = [peak_val * (0.85 ** i) for i in range(6)]
time_series = [int(x + (i**2) % 10) for i, x in enumerate(base_sequence)]

# Add irrelevant transformations
noisy_signal = [t * 1.02 + 5 for t in time_series]
signal_baseline = sum(noisy_signal) / len(noisy_signal)

# Efficiency determined by conditional expression
system_age = 4
cooling_type = 'liquid'
efficiency_factor = 1.35 if system_age < 3 else (1.15 if cooling_type == 'liquid' else 0.9)

# Key computational step
thermal_capacity = calculate_thermal_response(time_series, efficiency_factor)

# Dead code path — never executed but adds distraction
if False:
    backup_capacity = 0
    for t in time_series:
        backup_capacity += t * 0.75
    thermal_capacity = int(backup_capacity)

# Print result as required
print(f"Result: {thermal_capacity}")