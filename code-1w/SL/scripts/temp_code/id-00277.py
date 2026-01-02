def main():
    # Sensor data from multiple environmental monitors
    raw_readings = [14.3, 15.8, 16.1, 14.9, 17.2, 18.0, 15.4, 16.6, 19.1, 20.3, 15.7]

    # Irrelevant backup buffer (distractor)
    backup_buffer = [x * 1.05 for x in raw_readings if x > 20]  # No elements qualify

    # Calibration offset from legacy system (unused)
    calibration_map = {i: val * 0.98 for i, val in enumerate(raw_readings)}

    # Current operational thresholds
    upper_limit = 18.5
    lower_limit = 14.5

    # Historical stats (distractor)
    historical_avg = sum([14.1, 15.6, 16.3, 15.2, 17.0]) / 5
    spike_count = len([x for x in raw_readings if x > upper_limit])

    # Filter valid readings within current operational bounds
    filtered_data = [x for x in raw_readings if lower_limit <= x <= upper_limit]

    # Bitwise status flags from hardware sensors (mixed relevance)
    sensor_flags = [0b1101, 0b1011, 0b1110, 0b0111, 0b1001, 0b1111, 0b1100, 0b1010]
    critical_flag = 0b1100
    flag_sum = sum(f & critical_flag for f in sensor_flags)  # Partially relevant

    # Lambda to determine dynamic threshold based on flag patterns
    threshold_func = lambda data, base: base + (flag_sum % 3) * 0.25

    # Dictionary of device statuses (some fields irrelevant)
    device_status = {
        'unit_01': {'state': 'active', 'priority': 1},
        'unit_02': {'state': 'standby', 'priority': 3},
        'unit_03': {'state': 'active', 'priority': 2}
    }

    # Helper function with dead code path
    def analyze_trend(data):
        if len(data) < 3:
            return 'unstable'
        trend = 'increasing' if data[-1] > data[0] else 'decreasing'
        # Dead code branch — never executed due to return above
        if len(data) == 100:
            return 'anomalous'
        return trend

    trend = analyze_trend(filtered_data)

    # Core processing function
    def process_readings(readings, threshold_gen):
        base_threshold = 15.5
        dynamic_threshold = threshold_gen(readings, base_threshold)

        # Count how many readings exceed dynamic threshold
        above_threshold = [r for r in readings if r > dynamic_threshold]

        # Apply slicing to simulate windowed analysis
        window = above_threshold[1:-1] if len(above_threshold) > 2 else above_threshold

        # Compute weighted impact score
        weights = [1.1, 1.3, 1.6][:len(window)] + [1.0] * max(0, len(window) - 3)
        weighted_impact = sum(w * v for w, v in zip(weights, window))

        # Diagnostic logic
        if trend == 'increasing':
            adjustment = 0.8
        else:
            adjustment = 1.2

        # Final diagnostic score
        diagnostic_score = len(above_threshold) * weighted_impact * adjustment

        # Unused derived metrics (distractors)
        avg_filtered = sum(readings) / len(readings) if readings else 0
        outlier_ratio = (len(raw_readings) - len(filtered_data)) / len(raw_readings)
        compression_factor = len(str(int(diagnostic_score)))  # Character counting distractor

        return int(diagnostic_score)  # Discretized result

    final_diagnostic = process_readings(filtered_data, threshold_func)
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()