def analyze_sensor_data():
    # Simulated environmental sensor readings (temperature, pressure, humidity)
    raw_readings = [
        [23.4, 1013.25, 45.0],
        [24.1, 1012.80, 47.3],
        [19.8, 1014.10, 50.1],
        [22.0, 1013.50, 44.7],
        [20.5, 1013.90, 48.8]
    ]

    # Irrelevant baseline calibration offsets (distractor)
    calibration_offsets = [0.15, -0.22, 0.08]
    adjusted_offsets = [round(x * 1.07, 3) for x in calibration_offsets]

    # Extract temperature and pressure for processing
    temperatures = [row[0] for row in raw_readings]
    pressures = [row[1] for row in raw_readings]
    humidities = [row[2] for row in raw_readings]

    # Misleading normalization attempt (dead path)
    normalized_temps = []
    temp_min, temp_max = min(temperatures), max(temperatures)
    for t in temperatures:
        norm_val = (t - temp_min) / (temp_max - temp_min) if temp_max != temp_min else 0
        normalized_temps.append(round(norm_val, 4))

    # Compute rolling average of pressure with window size 2 (irrelevant)
    rolling_pressure_avg = []
    for i in range(1, len(pressures)):
        rolling_pressure_avg.append((pressures[i-1] + pressures[i]) / 2)

    # Primary analysis: detect anomalies in temperature
    anomaly_flags = []
    reference_temp = sum(temperatures) / len(temperatures)
    for i, temp in enumerate(temperatures):
        deviation = abs(temp - reference_temp)
        if deviation > 1.5:
            anomaly_flags.append((i, round(deviation, 3)))

    # Secondary: compute humidity trend (distractor)
    humidity_change_rate = []
    for i in range(1, len(humidities)):
        rate = humidities[i] - humidities[i-1]
        humidity_change_rate.append(rate)

    # Tertiary: cross-correlation attempt between temp and humidity (unused)
    temp_changes = [temperatures[i] - temperatures[i-1] for i in range(1, len(temperatures))]
    correlation_accum = 0
    for i in range(len(temp_changes)):
        if i < len(humidity_change_rate):
            correlation_accum += temp_changes[i] * humidity_change_rate[i]

    # Real processing begins: filter anomalous readings by index
    valid_indices = [i for i in range(len(temperatures)) if i not in [idx for idx, _ in anomaly_flags]]
    filtered_pressures = [pressures[i] for i in valid_indices]

    # Compute corrected mean pressure from clean data
    if filtered_pressures:
        corrected_mean_pressure = sum(filtered_pressures) / len(filtered_pressures)
    else:
        corrected_mean_pressure = 1013.25

    # Simulate diagnostic codepath with tuple unpacking and zip (required feature)
    diagnostics = [(i, round(abs(temperatures[i] - reference_temp), 3)) for i in range(len(temperatures))]
    indices, deviations = zip(*diagnostics) if diagnostics else ([], [])

    # Enumerate over deviations to compute quality score (required feature)
    quality_score = 0
    for idx, dev in enumerate(deviations):
        if dev < 2.0:
            quality_score += (2.0 - dev) * (idx + 1)

    # Complex but irrelevant transformation chain (red herring)
    entropy_proxy = 0
    sorted_devs = sorted(deviations)
    for i, d in enumerate(sorted_devs):
        if i > 0:
            entropy_proxy += abs(d - sorted_devs[i-1]) * (i ** 0.5)

    # Core metric calculation (hidden in noise)
    stability_metric = sum(temperatures) * 0.75 + corrected_mean_pressure * 0.25
    adjustment_log = [round(stability_metric / (i+1), 2) for i in range(3)]
    intermediate_diagnostic = stability_metric - adjustment_log[0]

    # Final aggregation with decoy variables
    scaling_constant = 0.987
    correction_factor = len(anomaly_flags) - len(humidity_change_rate)  # evaluates to -2
    temporal_weights = [0.1, 0.2, 0.4, 0.2, 0.1]
    weighted_temp_sum = sum(t * w for t, w in zip(temperatures, temporal_weights))

    # Actual answer computation buried in distractions
    aggregate_metrics = [reference_temp, corrected_mean_pressure, intermediate_diagnostic, quality_score]
    final_diagnostic = aggregate_metrics[-1] + correction_factor * scaling_constant

    # Decoy print statements (not required)
    debug_state = {
        'offsets': adjusted_offsets,
        'correlation': correlation_accum,
        'entropy': round(entropy_proxy, 4)
    }

    # Only this matters:
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()