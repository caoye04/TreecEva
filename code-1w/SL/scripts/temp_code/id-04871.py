def analyze_sensor_network(raw_logs, threshold=0.75):
    # Irrelevant preprocessing: log metadata parsing (distractor)
    log_headers = [log.split(':')[0] for log in raw_logs if ':' in log]
    sequence_ids = [int(header[-2:]) for header in log_headers if header.endswith(tuple('0123456789'))]

    # Real data extraction
    data_segments = [log.split('|')[1] for log in raw_logs if '|' in log]
    readings = []
    for segment in data_segments:
        try:
            values = [float(x) for x in segment.split(',')]
            readings.extend(values)
        except ValueError:
            continue

    # Dead code path: unused transformation (red herring)
    def transform_legacy(v):
        return (v * 1.07) + 0.3 if v < 50 else (v * 0.93) - 0.7

    legacy_mapped = [transform_legacy(r) for r in readings if r % 2 == 0]  # Unused

    # Relevant: filter by threshold percentile
    sorted_readings = sorted(readings)
    cutoff_index = int(len(sorted_readings) * threshold)
    filtered_data = sorted_readings[:cutoff_index]

    # Decoy statistical calculations (misleading intermediate results)
    mean_fake = sum(legacy_mapped) / len(legacy_mapped) if legacy_mapped else 0
    spike_count = sum(1 for r in readings if r > 2 * mean_fake)  # Distractor

    # Calibration map using dictionary operations (required feature)
    calibration_map = {i: (1 + 0.05 * i) for i in range(1, 11)}
    calibration_factor = calibration_map.get(len(filtered_data) % 10 + 1, 1.0)

    # Simulate checksum validation (irrelevant control flow)
    checksum = 0
    for i, val in enumerate(filtered_data):
        if i % 3 == 0:
            checksum ^= int(val) & 255
    expected_checksum = 127
    is_valid = (checksum == expected_checksum)  # Rarely true; dead logic branch

    if is_valid:
        # This block almost never executes (decoy)
        backup_result = sum(filtered_data) * 0.95
        return backup_result

    # Core processing function with nested logic
    def process_readings(data_list, factor):
        result = 0
        buffer = []
        for idx, value in enumerate(data_list):
            # Use enumerate and zip (required features) in a non-trivial way
            temp_record = list(zip([idx] * len(data_list), [value] * len(data_list)))
            if len(temp_record) > 0 and temp_record[0][1] > 10:
                buffer.append(value * 0.8)
            else:
                buffer.append(value)

        # Accumulate with conditional skips
        for j, val in enumerate(buffer):
            if j % 4 == 0:
                result += val * factor
            elif j % 4 == 2:
                result -= val * 0.1
        return result if result != 0 else 999  # Avoid zero default

    # Key statement
    final_diagnostic = process_readings(filtered_data, calibration_factor)

    # Redundant post-processing (distractor)
    normalized_diagnostics = [final_diagnostic / (i+1) for i in range(3)]
    smoothed = sum(normalized_diagnostics) / len(normalized_diagnostics)

    # Output the target variable as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input logs with embedded numeric data
logs = [
    "LOG:01|23.5,18.2,45.0,67.3",
    "META:Z9|12.1,8.5,53.7",
    "DATA:44|31.0,19.8,27.6,88.9,4.2",
    "INFO:M2|15.3,99.9,6.4",  
    "RECORD:77|5.5,11.1,33.3",
    "TRACE:C5|72.8,29.4,13.7,8.8,5.1"
]

# Execute function
analyze_sensor_network(logs)
