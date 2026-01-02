def analyze_sensor_network():
    # Simulated sensor IDs and raw data readings
    sensor_ids = [101, 102, 103, 104, 105, 106]
    raw_readings = [23.4, 19.8, 45.1, 33.2, 12.7, 55.6]
    calibration_offsets = {'101': 0.5, '102': -0.3, '103': 0.8, '104': 0.0, '105': 1.2, '106': -0.7}

    # Irrelevant backup mapping (distractor)
    backup_system_map = {k: f'BKP_{v}' for k, v in enumerate(reversed(sensor_ids))}

    # Apply calibration (meaningful transformation)
    calibrated_readings = []
    for i, val in enumerate(raw_readings):
        sid = str(sensor_ids[i])
        offset = calibration_offsets.get(sid, 0)
        calibrated_readings.append(round(val + offset, 2))

    # Define valid range and thresholds (used later)
    min_limit, max_limit = 20.0, 50.0
    safety_buffer = 2.5  # used in filtering logic

    # Decoy statistical calculation (dead path)
    avg_reading = sum(calibrated_readings) / len(calibrated_readings)
    variance_proxy = sum((x - avg_reading) ** 2 for x in calibrated_readings)
    std_dev_guess = variance_proxy ** 0.5

    # Identify anomalous sensors (unused but plausible)
    outlier_flags = [r < min_limit or r > max_limit for r in calibrated_readings]

    # Filter based on operational bounds (key preprocessing)
    filtered_data = []
    for i in range(len(calibrated_readings)):
        if min_limit <= calibrated_readings[i] <= max_limit:
            filtered_data.append(calibrated_readings[i])

    # Create threshold set using set operations (required Python feature)
    base_thresholds = {25.0, 30.0, 35.0, 40.0}
    dynamic_adjustments = {round(x - safety_buffer, 1) for x in base_thresholds}
    threshold_set = base_thresholds.union(dynamic_adjustments)
    extended_analysis_targets = threshold_set.intersection({x for x in calibrated_readings if x > 30})

    # String-based status tagging (required Python feature - string methods)
    status_log = []
    for reading in calibrated_readings:
        tag = "CRITICAL" if reading > max_limit else "NORMAL"
        padded_tag = f"[{tag}]".center(12, " ")
        formatted_entry = padded_tag.strip().lower().replace("c", "*")
        status_log.append(formatted_entry)

    # Unused recursive helper (distractor function)
    def compute_depth_factor(n):
        if n <= 1:
            return 1
        return n * compute_depth_factor(n - 2)  # skips every other

    depth_score = compute_depth_factor(5)

    # Key processing function (defined inside to increase nesting)
    def process_readings(data_list, thresholds):
        if not data_list:
            return -999.0

        total = 0.0
        count = 0
        applied_corrections = []

        for val in data_list:
            # Determine correction factor using threshold proximity
            near_threshold = any(abs(val - t) < 1.5 for t in thresholds)
            if near_threshold:
                adjustment = 0.75
            else:
                adjustment = 1.0

            # Accumulate corrected values
            corrected = val * adjustment
            applied_corrections.append((val, corrected))
            total += corrected
            count += 1

        # Final aggregation with integer division effect
        if count == 0:
            return 0
        average_corrected = total / count
        scaled_result = int(average_corrected * 100) // 10  # integer division and scaling
        return float(scaled_result)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_set)

    print(f"Result: {final_diagnostic}")

analyze_sensor_network()