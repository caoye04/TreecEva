def analyze_sensor_network():
    # Simulated sensor grid readings (temperature in Celsius)
    raw_readings = [23.5, 19.1, 27.3, 30.0, 18.2, 24.7, 26.8, 21.4, 29.6, 22.0, 25.3, 28.9]

    # Irrelevant calibration constants (distractor)
    calib_a, calib_b, calib_c = 1.02, -0.5, 3.14159
    adjusted_offsets = [calib_a * x + calib_b for x in range(5)]  # Unused path

    # Threshold policy per zone (real logic)
    threshold_map = {
        'low': 20.0,
        'optimal': 25.0,
        'high': 28.0
    }

    # Historical baselines (mostly irrelevant)
    historical_avg = {
        'Q1': 21.3, 'Q2': 23.7, 'Q3': 26.1, 'Q4': 24.8
    }
    seasonal_delta = sum(historical_avg.values()) / len(historical_avg) - 22.0  # Distractor calc

    # Filter valid sensors: only those with index in [1, 3, 4, 6, 7, 9, 10, 11]
    sensor_indices = list(range(len(raw_readings)))
    active_mask = [i % 2 == 1 or i > 8 for i in sensor_indices]  # Complex but clear filter
    filtered_data = [raw_readings[i] for i in range(len(raw_readings)) if active_mask[i]]

    # Decoy transformation: character counting on fake labels (red herring)
    zone_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    char_count = sum(len(label) for label in zone_labels)  # Always 6, unused

    # Spurious sorting and slicing (intermediate distractor)
    sorted_readings = sorted(raw_readings, reverse=True)
    mid_range_slice = sorted_readings[3:9]  # Looks important, not used later

    # Real processing function (nested logic)
    def process_readings(data, thresholds):
        count_low = count_optimal = count_high = 0
        temp_stats = {'sum': 0.0, 'count': 0}

        for val in data:
            temp_stats['sum'] += val
            temp_stats['count'] += 1

            if val < thresholds['low']:
                count_low += 1
            elif val <= thresholds['optimal']:
                count_optimal += 1
            elif val <= thresholds['high']:
                count_high += 1
            else:
                # Above high threshold
                pass  # Implicit increment not needed

        # Compute weighted diagnostic score
        weights = {'low': -1.5, 'optimal': 2.0, 'high': -0.5, 'critical': -3.0}
        base_score = (weights['low'] * count_low + 
                     weights['optimal'] * count_optimal + 
                     weights['high'] * count_high)

        # Add bonus if average is in optimal band
        avg_temp = temp_stats['sum'] / temp_stats['count']
        if threshold_map['low'] < avg_temp <= threshold_map['optimal']:
            base_score += 5.0  # Bonus for good average

        # Irrelevant bitwise manipulation (distractor)
        magic_flag = (0xABC ^ 0x123) & 0xFF  # Computes 0x1EF, unused

        # Final non-linear transformation
        diagnostic_value = int((base_score ** 2) - (avg_temp * 1.3))

        return diagnostic_value

    # Dead code path: complex dictionary transformation (never called)
    def generate_report(snapshot):
        report_dict = {}
        for i, val in enumerate(snapshot):
            key = f"sensor_{i % 4}"
            if key not in report_dict:
                report_dict[key] = []
            report_dict[key].append(val * 1.1)
        return {k: sum(v)/len(v) for k, v in report_dict.items()}

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output required result
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()