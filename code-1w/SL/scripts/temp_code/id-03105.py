def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.1, 24.3, 18.7, 22.0, 25.6, 17.2, 26.8, 20.4, 21.9]

    # Calibration data from multiple sources (some irrelevant)
    calibration_offsets = [0.3, -0.2, 0.5, 0.0, -0.1]
    legacy_calibrations = [1.2, -0.8, 0.4, 0.9]  # Unused legacy values (distractor)
    temporal_weights = [0.9, 1.0, 1.1, 1.05, 0.95, 1.0, 0.99, 1.01, 0.98, 1.02]

    # System thresholds (some are decoys)
    warning_threshold = 24.0
    critical_threshold = 27.0
    deprecated_threshold = 15.0  # Not used (red herring)

    # Bitmask configuration for sensor validation (used later)
    sensor_status_flags = [0b1010, 0b1100, 0b1011, 0b0010, 0b1110, 0b1001, 0b0110, 0b1111, 0b1000, 0b0101]

    # Irrelevant preprocessing: historical average calculation (distraction)
    historical_avg = sum([22.1, 20.3, 23.4, 19.8, 21.7]) / 5
    projected_drift = 0.15  # Unused forecast parameter

    # Step 1: Filter out sensors with insufficient signal strength (bit 2 unset)
    valid_indices = []
    for i, flag in enumerate(sensor_status_flags):
        if flag & 0b100:  # Check if bit 2 is set (arbitrary selection criterion)
            valid_indices.append(i)

    # Step 2: Extract corresponding readings
    filtered_data = []
    for idx in valid_indices:
        filtered_data.append(raw_readings[idx])

    # Step 3: Apply dynamic weighting based on position (enumerate usage)
    weighted_readings = []
    for i, reading in enumerate(filtered_data):
        weight = temporal_weights[valid_indices[i]]
        weighted_readings.append(reading * weight)

    # Step 4: Compute calibration factor using XOR of index and offset (bitwise + modular)
    calibration_factor = 0.0
    for i, offset in enumerate(calibration_offsets):
        # Complex but deterministic calibration logic
        shift_amount = (i ^ 3) % 4  # XOR and mod for pseudo-randomness
        shifted = int((offset * 10) * (2 ** shift_amount))
        calibration_factor += shifted
    calibration_factor = (calibration_factor % 8) / 10.0  # Normalize to 0.0–0.7

    # Step 5: Process function with zip and complex control flow
    def process_readings(readings, calib):
        adjusted = []
        anomalies_detected = 0
        base_threshold = 20.5

        # Use zip to pair readings with alternating correction factors
        correction_cycle = [1.02, 0.98, 1.01, 0.99]
        for val, corr in zip(readings, correction_cycle * (len(readings)//4 + 1)):
            adjusted_val = val * corr + calib
            if abs(adjusted_val - base_threshold) > 5.0:
                anomalies_detected += 1
            adjusted.append(adjusted_val)

        # Secondary filtering: exclude highest and lowest (combinatorics)
        sorted_vals = sorted(adjusted)
        trimmed = sorted_vals[anomalies_detected:-anomalies_detected] if anomalies_detected < len(sorted_vals)//2 else sorted_vals

        # Final diagnostic computation
        if len(trimmed) == 0:
            return 0.0
        
        # Mean with floor bias
        mean_val = sum(trimmed) / len(trimmed)
        floor_bias = int(mean_val) % 3  # Additional interference
        final_score = mean_val - (floor_bias * 0.25)
        
        # Dead code branch (never reached due to prior logic)
        if len(trimmed) > 100:
            fallback = 0
            for x in legacy_calibrations:
                fallback ^= int(x * 10)
            return fallback / 100.0

        return final_score

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)

    # Redundant transformation (distractor)
    diagnostic_log = []
    for char in "Diagnostics Complete":
        diagnostic_log.append(ord(char) ^ 15)

    # Output result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute
analyze_sensor_network()