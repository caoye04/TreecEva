def sensor_diagnostic_protocol():
    # Simulated environmental sensor readings (temperature, pressure, humidity)
    raw_readings = [
        (23.4, 101.3, 45.0), (22.9, 101.5, 47.2), (24.1, 100.9, 44.1),
        (25.6, 102.1, 42.3), (26.0, 101.8, 43.8), (23.8, 101.0, 46.0),
        (27.3, 103.4, 40.1), (26.8, 102.9, 41.5), (24.5, 101.2, 45.3)
    ]

    # Calibration coefficients for each sensor type
    temp_calib, pres_calib, hum_calib = 1.02, 0.98, 1.01  # Irrelevant after initial use

    # Apply calibration (only temperature used in final logic)
    calibrated_temps = [t * temp_calib for t, p, h in raw_readings]

    # Extract and slice relevant time window: middle 5 readings
    time_window = raw_readings[2:7]
    baseline_ref = raw_readings[0]  # Unused reference point (red herring)

    # Precompute various statistics (many are distractions)
    avg_temp = sum(t for t, p, h in time_window) / len(time_window)
    avg_pressure = sum(p for t, p, h in time_window) / len(time_window)
    max_humidity = max(h for t, p, h in time_window)
    temp_variance = sum((t - avg_temp)**2 for t, p, h in time_window) / len(time_window)

    # Noise filter simulation (unused)
    def apply_noise_reduction(data):
        return [x * 0.99 + 0.5 for x in data]  # Dead function

    # Process data: extract temperatures and apply conditional offset
    processed_temps = []
    for reading in time_window:
        temp, pressure, humidity = reading
        if temp > 25.0:
            temp += 0.5  # Overheat bias correction
        elif pressure < 101.0:
            temp -= 0.3  # Not triggered in this dataset
        processed_temps.append(round(temp, 2))

    # Assemble processed data with dummy metadata
    metadata_flags = {'source': 'primary', 'status': 'verified'}
    processed_data = (processed_temps, metadata_flags)

    # Threshold configuration map (critical)
    threshold_map = {
        'high_risk': 26.0,
        'warning': 24.5,
        'normal': 22.0
    }

    # Diagnostic counters (some are decoys)
    high_count = 0
    warn_count = 0
    stable_count = 0
    phantom_counter = 0  # Never updated (distractor)

    # Secondary unused diagnostic from different subsystem
    def legacy_diagnose(seq):
        total = 0
        for x in seq:
            total += x ^ 7  # Bitwise red herring
        return total % 100

    # Real analysis function
    def analyze_readings(data_with_meta, thresholds):
        temps = data_with_meta[0]
        above_warning = 0
        above_high = 0

        for t in temps:
            if t >= thresholds['warning']:
                above_warning += 1
                if t >= thresholds['high_risk']:
                    above_high += 1

        # Complex scoring logic
        if above_high >= 2:
            score = 85 + (above_high * 3)
        elif above_warning >= 3:
            score = 70 + (above_warning * 2)
        else:
            score = 50

        # Additional penalty for consecutive highs
        consecutive_highs = 0
        max_consecutive = 0
        for t in temps:
            if t >= thresholds['high_risk']:
                consecutive_highs += 1
            else:
                max_consecutive = max(max_consecutive, consecutive_highs)
                consecutive_highs = 0
        max_consecutive = max(max_consecutive, consecutive_highs)  # Final update

        if max_consecutive >= 2:
            score += 8  # Reward for detecting pattern

        # Data slicing to extract anomaly cluster
        sorted_temps = sorted(temps)
        mid_range = sorted_temps[1:-1]  # Remove outliers (slice usage)
        center_avg = sum(mid_range) / len(mid_range)

        # Final adjustment based on central tendency
        if center_avg > 25.0:
            score += 5

        # Spurious bitwise operation (never affects result)
        magic_key = 0b101010
        encrypted_flag = magic_key & 0xFF  # Distraction

        return int(score)

    # Trigger point: critical statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)

    # Irrelevant post-processing (dead code path)
    debug_snapshot = None
    if __debug__:
        debug_snapshot = {"raw": raw_readings[:], "temp_stats": (avg_temp, temp_variance)}

    print(f"Result: {final_diagnostic}")

sensor_diagnostic_protocol()