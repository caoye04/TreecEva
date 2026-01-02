def analyze_sensor_network():
    # Simulated sensor readings (temperature in millidegrees)
    raw_readings = [23450, 25670, 22890, 27010, 24320, 26150, 23980, 25430]

    # Environmental interference factors (irrelevant for final result)
    wind_speeds = [12.5, 14.1, 11.8, 16.3, 13.0, 15.2, 12.9, 14.7]
    humidity_levels = [45, 52, 41, 58, 47, 54, 43, 50]

    # Calibration data from multiple sources (only one is used)
    calibration_source_a = 1.02
    calibration_source_b = 0.98  # unused
    calibration_source_c = 1.01  # unused
    calibration_factor = calibration_source_a

    # Thresholds and filters
    TEMP_MIN = 23000
    TEMP_MAX = 26500
    outlier_buffer = []  # collects values outside threshold (unused later)

    # Filter readings within operational range
    filtered_data = []
    for reading in raw_readings:
        if TEMP_MIN <= reading <= TEMP_MAX:
            filtered_data.append(reading)
        else:
            outlier_buffer.append(reading)  # distractor: collected but not used

    # Decoy transformation: string-based analysis of sensor IDs (completely irrelevant)
    sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
    id_analysis = set()
    for sid in sensor_ids:
        if sid.startswith('S'):
            id_analysis.add(sid[1:])
    hex_codes = {f'0x{int(n):X}' for n in id_analysis}  # set comprehension red herring

    # Bit manipulation decoy (no impact on result)
    security_checksum = 0
    for i in range(len(wind_speeds)):
        security_checksum ^= int(wind_speeds[i] * 10) & 0xFF
        if security_checksum > 200:
            security_checksum >>= 1

    # Unused recursive function (dead code path)
    def recursive_average(data, depth=0):
        if depth >= 3 or len(data) == 1:
            return data[0]
        mid = len(data) // 2
        left_avg = recursive_average(data[:mid], depth + 1)
        right_avg = recursive_average(data[mid:], depth + 1)
        return (left_avg + right_avg) / 2

    # Actual processing function
    def process_readings(data, calib):
        # Apply calibration
        calibrated = [int(x * calib) for x in data]
        
        # Compute moving average over 2-point window
        smoothed = []
        for i in range(len(calibrated) - 1):
            smoothed.append((calibrated[i] + calibrated[i + 1]) // 2)
        
        # Find anomalies (difference > 1000 millidegrees)
        anomalies = 0
        for i in range(len(smoothed) - 1):
            if abs(smoothed[i] - smoothed[i + 1]) > 1000:
                anomalies += 1
        
        # Final diagnostic score based on anomaly count and length
        base_score = len(smoothed) * 100
        penalty = anomalies * 250
        return base_score - penalty

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Distractor: tuple unpacking with irrelevant results
    try:
        first, *middle, last = filtered_data
        stability_check = (last - first) // len(middle)
    except:
        stability_check = 0

    # Additional noise: string formatting unrelated to logic
    report_header = f"Diagnostic Run: {len(raw_readings)} sensors"
    report_header = report_header.upper().replace(' ', '_')

    # Output the target result
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()