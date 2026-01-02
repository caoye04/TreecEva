def calculate_thermal_output(phases):
    base_factor = 1.75
    adjustment = 0.92
    cumulative_stress = 0
    thermal_capacity = 0

    for phase in phases:
        duration = phase['duration']
        intensity = phase.get('intensity', 1)
        efficiency = phase.get('efficiency', 0.85)

        # Real computation branch
        stress_level = duration * intensity ** 0.5
        cumulative_stress += stress_level

        if intensity > 2:
            boosted_efficiency = efficiency * 1.3
        else:
            boosted_efficiency = efficiency * 1.05

        energy_delta = duration * intensity * boosted_efficiency
        thermal_capacity += energy_delta * base_factor

        # Distractor: irrelevant vibration metrics
        vibration_freq = phase.get('vibration', 0)
        harmonic_dampening = vibration_freq * 0.03 if vibration_freq > 50 else 0
        spectral_peak = harmonic_dampening ** 2  # Dead computation

    # Secondary adjustment based on cumulative stress
    stress_modifier = 1 + (cumulative_stress / 100) if cumulative_stress > 30 else 0.9
    thermal_capacity *= stress_modifier

    # More distractions: fake calibration sequence
    calibration_matrix = {'c1': 0.98, 'c2': 1.03, 'c3': 0.99}
    system_age = 5
    age_penalty = system_age * 0.012
    adjusted_calibration = calibration_matrix['c1'] * (1 - age_penalty)  # Unused

    return int(thermal_capacity)

# Simulated industrial process data
process_phases = [
    {'duration': 12, 'intensity': 3, 'efficiency': 0.88, 'vibration': 65},
    {'duration': 8, 'intensity': 1, 'efficiency': 0.92},
    {'duration': 15, 'intensity': 4, 'efficiency': 0.81, 'vibration': 78},
    {'duration': 5, 'intensity': 2, 'efficiency': 0.85}
]

initial_threshold = 25
threshold_met = any(p['duration'] > initial_threshold for p in process_phases)

# Dictionary-based mode routing (semi-relevant)
operation_mode = 'high_load' if sum(p['intensity'] for p in process_phases) > 8 else 'standard'
mode_multiplier = {'high_load': 1.1, 'standard': 1.0, 'economy': 0.9}

# Key execution point
thermal_capacity = calculate_thermal_output(process_phases)

# Apply mode only if threshold was met — which it isn't, so no effect
if threshold_met:
    thermal_capacity *= mode_multiplier[operation_mode]

# Final output
print(f"Result: {thermal_capacity}")