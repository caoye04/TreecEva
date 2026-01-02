def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.0, 25.3, 18.7, 30.1, 27.4, 22.0, 16.5, 24.8, 26.9, 20.3, 31.2, 28.6]

    # Irrelevant calibration constants for humidity (distractor)
    calibration_offsets = {'HUM': 0.87, 'CO2': 1.03, 'BARO': 0.94}
    scaling_factor = 1.05  # Unused scaling (red herring)

    # Critical temperature thresholds
    MIN_OPERATIONAL = 18.0
    MAX_OPERATIONAL = 28.5

    # Misleading secondary filter based on invalid assumption (dead logic path)
    def legacy_filter(x):
        return x > 17.5 and x < 30.0  # Not used in final logic

    # Actual dynamic threshold generator (used)
    def generate_threshold(delta):
        return lambda x: (x - MIN_OPERATIONAL) * delta

    adjustment_curve = generate_threshold(1.15)
    baseline_shift = adjustment_curve(20.0)  # Evaluates to 2.3, irrelevant to final result

    # Filter readings within operational range
    filtered_data = []
    outlier_count = 0
    for reading in raw_readings:
        if MIN_OPERATIONAL <= reading <= MAX_OPERATIONAL:
            filtered_data.append(round(reading, 1))
        else:
            outlier_count += 1  # Tracking but not used

    # Dead code branch - simulates alternate processing that never executes
    if False:  # Never taken
        filtered_data = [x * 0.98 for x in filtered_data]
        temp_offset = sum(calibration_offsets.values()) / len(calibration_offsets)

    # Auxiliary diagnostic function with red-herring computations
    def compute_stability_index(data):
        if len(data) == 0:
            return 0.0
        mean_val = sum(data) / len(data)
        variance = sum((x - mean_val) ** 2 for x in data) / len(data)
        fluctuation_score = sum(1 for i in range(1, len(data)) if abs(data[i] - data[i-1]) > 1.5)
        # Complex but unused metric
        coherence = (len(data) - fluctuation_score) / len(data) if data else 0
        return round(variance * 100, 2)  # Distractor return

    stability_metric = compute_stability_index(filtered_data)  # Computed but not used

    # Core processing function
    def process_readings(data, threshold_func):
        # Apply slicing to exclude first and last elements (edge noise removal)
        trimmed = data[1:-1] if len(data) > 2 else data

        # Use lambda to classify deviations
        deviation_check = list(map(lambda x: 1 if x > 24.0 else -1, trimmed))

        # Count positive deviations
        high_deviation_count = sum(1 for x in deviation_check if x == 1)
        low_deviation_count = sum(1 for x in deviation_check if x == -1)

        # Weighted impact score
        impact_score = 0
        weights = [0.8, 1.0, 1.2]  # Increasing sensitivity
        for i, val in enumerate(trimmed):
            weight = weights[i % len(weights)]
            if val > 24.0:
                impact_score += (val - 24.0) * weight
            else:
                impact_score -= (24.0 - val) * weight * 0.5

        # Final diagnostic combines multiple factors
        base_count_score = len(trimmed) * 10
        trend_bias = (high_deviation_count - low_deviation_count) * 5
        normalized_impact = int(round(abs(impact_score)))

        # Final computation
        final_score = base_count_score + trend_bias + normalized_impact

        # Decoy calculation (never used)
        phantom_diagnostic = (stability_metric + baseline_shift) * 2

        return final_score

    threshold_func = generate_threshold(1.15)
    final_diagnostic = process_readings(filtered_data, threshold_func)
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()