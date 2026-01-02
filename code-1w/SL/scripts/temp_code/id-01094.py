def analyze_sensor_network():
    # Simulated sensor data with noise and redundant metrics
    raw_readings = [14.2, 18.5, 22.1, 9.7, 31.3, 25.6, 11.0, 44.8, 19.9, 8.3]
    calibration_offsets = [0.5, -0.3, 0.8, -0.1, 0.0, 0.2, -0.4, 0.6, -0.2, 0.1]
    sensor_ids = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10']

    # Irrelevant pre-processing: mapping IDs to arbitrary groups
    id_groups = {sid: int(sid[1:]) % 3 for sid in sensor_ids}
    group_weights = {0: 1.1, 1: 0.9, 2: 1.05}
    weighted_groups = {k: v * group_weights[id_groups[k]] for k, v in zip(sensor_ids, raw_readings)}

    # Noise injection (distractor computation)
    noise_profile = [abs((x * 0.02) * ((i + 1) % 7)) for i, x in enumerate(raw_readings)]
    perturbed_readings = [raw_readings[i] + noise_profile[i] for i in range(len(raw_readings))]

    # Apply real calibration (relevant)
    calibrated_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]

    # Threshold logic with set operations
    high_threshold = 20.0
    medium_threshold = 15.0
    alert_set = {i for i, val in enumerate(calibrated_readings) if val > high_threshold}
    warn_set = {i for i, val in enumerate(calibrated_readings) if medium_threshold < val <= high_threshold}
    threshold_set = {"high": alert_set, "warn": warn_set, "low": set(range(10)) - alert_set - warn_set}

    # Filtering based on valid diagnostic range (key step)
    filtered_data = [calibrated_readings[i] for i in range(len(calibrated_readings)) if i not in threshold_set['low']]

    # Dummy transformation chain (distractors)
    reshaped_data = [[filtered_data[i], filtered_data[i+1]] for i in range(0, len(filtered_data)-1, 2)] if len(filtered_data) > 1 else [[0, 0]]
    transposed = list(zip(*reshaped_data)) if reshaped_data else [(0,), (0,)]
    averaged_slices = [sum(transposed[0])/len(transposed[0]), sum(transposed[1])/len(transposed[1])] if transposed else [0, 0]

    # Unused statistical decoy
    mean_reading = sum(calibrated_readings) / len(calibrated_readings)
    variance = sum((x - mean_reading)**2 for x in calibrated_readings) / len(calibrated_readings)
    outlier_indices = {i for i, x in enumerate(calibrated_readings) if abs(x - mean_reading) > 1.5 * variance**0.5}

    # Real processing function
    def process_readings(data, thresholds):
        # Nested conditional logic with slicing
        if len(data) == 0:
            return 0
        sorted_vals = sorted(data)
        mid_slice = sorted_vals[len(sorted_vals)//4 : len(sorted_vals)*3//4]  # IQR-like slice

        # Bit manipulation red herring
        magic_key = 0
        for val in [2, 3, 5]:
            magic_key ^= int(sum(mid_slice)) % val

        # Actual computation path
        base_score = sum(mid_slice)
        adjustment = 0
        if len(thresholds['high']) > 2:
            adjustment += 10
        if len(thresholds['warn']) % 2 == 0:
            adjustment -= 3

        # Final logic with logical operations
        multiplier = 2 if (len(thresholds['high']) >= 3 and adjustment > 0) else 1.5
        final_value = (base_score + adjustment) * multiplier

        # Early return distraction
        if final_value < 0:
            return -1  # unreachable due to data

        return final_value

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_set)

    # Dead code path (never executed)
    def legacy_diagnostic(seq):
        return max(seq) - min(seq) if seq else 0

    # Print result as required
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()