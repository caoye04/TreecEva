def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: reverse and pad data (distractor)
    padded_readings = [0] * 5 + raw_readings[::-1] + [0] * 3
    shifted_data = [x << 1 for x in padded_readings if x % 2 == 0]  # Bit manipulation red herring

    # Real processing begins: filter valid readings
    valid_readings = [x for x in raw_readings if 10 <= x <= 90]

    # Compute rolling average over triplets (only some used later)
    rolling_averages = []
    for i in range(len(valid_readings) - 2):
        avg = round((valid_readings[i] + valid_readings[i+1] + valid_readings[i+2]) / 3, 2)
        rolling_averages.append(avg)

    # Misleading statistical analysis (dead path)
    variance_proxy = 0
    if len(rolling_averages) > 5:
        mean_avg = sum(rolling_averages) / len(rolling_averages)
        variance_proxy = sum((x - mean_avg) ** 2 for x in rolling_averages) / len(rolling_averages)

    # Core logic: match calibration pattern using set operations
    calib_set = set(calibration_sequence)
    reading_set = set(valid_readings)
    matched_zones = calib_set & reading_set  # Intersection: relevant signal
    noise_floor = calib_set ^ reading_set   # Symmetric difference: distraction

    # Use enumerate and zip on aligned sequences (required Python idiom)
    time_series = list(enumerate(zip(valid_readings[:-1], valid_readings[1:])))
    spike_count = 0
    for idx, (prev_val, curr_val) in time_series:
        if curr_val > prev_val and (curr_val - prev_val) >= 15:
            spike_count += 1

    # Decoy recursive function (never called in critical path)
    def recursive_denoise(data, depth=0):
        if depth >= 3 or len(data) < 2:
            return data
        return recursive_denoise([data[i] for i in range(1, len(data), 2)], depth + 1)

    # Actual accumulation logic
    base_energy = sum(x * x for x in matched_zones if x % 3 == 0)  # Only multiples of 3 contribute
    aggregate_score = base_energy // max(len(matched_zones), 1)

    # Correction based on spike behavior
    if spike_count > 0:
        correction_factor = len(noise_floor) % 7
    else:
        correction_factor = -sum(noise_floor) % 5

    # Dead code: string-based diagnostics (irrelevant but plausible)
    status_log = "SensorOK,CalibMatch".split(',')
    flag_summary = ''.join(s[0] for s in status_log)
    debug_hash = sum(ord(c) for c in flag_summary)  # Unused

    # Key assignment statement
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

# Execute with fixed input
data_stream = [12, 45, 18, 22, 60, 11, 73, 36, 41, 88]
calibration_key = [45, 18, 60, 36, 99, 101]
analyze_sensor_data(data_stream, calibration_key)