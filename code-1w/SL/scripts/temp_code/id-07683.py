from itertools import compress, count

# Domain-specific simulation: Sensor data validation and noise filtering
def analyze_sensor_readings(raw_readings, thresholds):
    # Irrelevant transformation: time stamps (distractor)
    base_time = 1609459200
    time_sequence = [base_time + i * 30 for i in range(len(raw_readings))]

    # Red herring: unused frequency analysis
    frequencies = {x: raw_readings.count(x) for x in set(raw_readings) if x > 0}
    avg_freq = sum(frequencies.values()) / len(frequencies) if frequencies else 0

    # Core logic: identify anomalous readings using dual threshold bands
    upper_band = thresholds['critical']
    lower_band = thresholds['warning']

    # Mask generation with complex conditions (some are irrelevant)
    is_high_anomaly = [x > upper_band for x in raw_readings]
    is_low_anomaly = [x < -upper_band for x in raw_readings]
    within_normal_range = [abs(x) <= lower_band for x in raw_readings]

    # Decoy logic: complex generator that's not used
    def generate_baseline():
        c = count(20, 0.7)
        for _ in range(100):
            yield round(next(c), 1)
    baseline = list(generate_baseline())[:10]  # Unused

    # Actual filter path: only moderate deviations are processed
    is_moderate_deviation = [lower_band < abs(x) <= upper_band for x in raw_readings]

    # Apply mask to extract values for correction
    moderate_values = list(compress(raw_readings, is_moderate_deviation))

    # Correction algorithm: apply decay function to moderate deviations
    corrected_values = []
    decay_factor = 0.85
    for val in moderate_values:
        sign = 1 if val >= 0 else -1
        corrected = sign * (abs(val) * decay_factor)
        corrected_values.append(round(corrected, 2))

    # Second-order anomaly detection on corrected set (distraction)
    recheck_threshold = thresholds['warning'] * 0.9
    needs_reprocessing = [abs(cv) > recheck_threshold for cv in corrected_values]
    reprocessed_count = sum(needs_reprocessing)

    # Final decision: use original moderate values, not corrected ones (misleading path)
    final_selection_mask = [not (x > upper_band * 1.1) for x in raw_readings]
    selected_raw = list(compress(raw_readings, final_selection_mask))

    # Key computation: filter only positive moderate deviations from original
    filtered_values = [x for x in selected_raw if lower_band < x <= upper_band]
    
    # Critical assignment point
    filtered_sum = sum(filtered_values)
    
    # Dead code path: unused accumulator with lambda
    aggregate_func = lambda a, b: a + b * 0.95
    rolling_total = 0
    for v in raw_readings:
        rolling_total = aggregate_func(rolling_total, v)

    return filtered_sum

# Input data (simulated sensor array output)
sensor_data = [12, -8, 15, 4, 23, -6, 9, 18, 3, 11, 27, -14, 7]
config = {
    'warning': 10,
    'critical': 20
}

# Execution
result = analyze_sensor_readings(sensor_data, config)

# Output target variable
print(f"Result: {result}")