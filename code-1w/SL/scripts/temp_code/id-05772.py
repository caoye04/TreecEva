def calculate_thermal_output(load_profile, efficiency_curve):
    base_heat = 0
    peak_modulator = 1.78
    thermal_capacity = 0

    # Irrelevant signal smoothing block (distractor)
    smoothed_signal = [load_profile[i] + 0.1 * (i % 3) for i in range(len(load_profile))]
    normalization_factor = sum(smoothed_signal) / len(smoothed_signal) if smoothed_signal else 1

    # Real processing begins
    for idx, load in enumerate(load_profile):
        if load > 75:
            stage_boost = 2
        elif load > 50:
            stage_boost = 1
        else:
            stage_boost = 0

        # Efficiency lookup with dictionary (required feature)
        current_efficiency = efficiency_curve.get(f'level_{idx % 4}', 0.85)

        # Heat contribution calculation
        heat_contribution = load * current_efficiency * (1 + stage_boost * 0.5)
        base_heat += heat_contribution

        # Dead code path - never affects final result
        if normalization_factor > 10:
            base_heat -= 5  # unreachable due to data scale

    # Secondary irrelevant transformation
    temp_array = [base_heat / (i + 1) for i in range(1, 4)]
    filtered_temps = list(filter(lambda x: x > 50, temp_array))
    average_temp = sum(filtered_temps) / len(filtered_temps) if filtered_temps else 0

    # Final computation unrelated to distractors
    thermal_capacity = int(base_heat // 10)  # Integer division and rounding

    # Linear search through hypothetical sensor array (semi-relevant)
    sensor_readings = [98, 99, 101, 102, 105]
    target_idx = -1
    for i in range(len(sensor_readings)):
        if sensor_readings[i] >= thermal_capacity:
            target_idx = i
            break

    return thermal_capacity

# Main execution context
processor_load = [68, 76, 82, 45, 91, 53]
efficiency_map = {
    'level_0': 0.88,
    'level_1': 0.91,
    'level_2': 0.85,
    'level_3': 0.93
}

thermal_capacity = 0
thermal_capacity = calculate_thermal_output(processor_load, efficiency_map)
print(f"Result: {thermal_capacity}")