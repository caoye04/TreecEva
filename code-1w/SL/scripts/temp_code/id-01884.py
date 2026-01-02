def analyze_sensor_data(raw_readings, config_params):
    # Irrelevant preprocessing: string cleaning (distractor)
    metadata = config_params.get('metadata', 'N/A').strip().lower()
    normalized_meta = metadata.replace('-', '').replace('_', '')
    if 'debug' in normalized_meta:
        print("Debug mode active")  # Dead code path

    # Core logic disguised among distractions
    base_offset = config_params.get('offset', 0)
    scaling_factor = config_params.get('scale', 1.0)
    readings = [x * scaling_factor + base_offset for x in raw_readings]

    # Decoy statistical computation (misleading intermediate)
    mean_val = sum(readings) / len(readings) if readings else 0
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings) if readings else 0
    std_dev = variance ** 0.5

    # Irrelevant character counting in a simulated ID (string method usage)
    device_id = config_params.get('device_id', 'DEV000')
    letter_count = sum(1 for c in device_id if c.isalpha())
    digit_count = sum(1 for c in device_id if c.isdigit())
    checksum = letter_count * 10 + digit_count

    # Conditional data filtering (relevant)
    threshold = config_params.get('threshold', 50)
    filtered_data = [x for x in readings if x > threshold - 10]

    # Unused sorting operation (dead code distractor)
    sorted_diagnostics = sorted([abs(x - mean_val) for x in readings])
    if std_dev > 10:
        sorted_diagnostics = [x for x in sorted_diagnostics if x < std_dev]

    # Simulated fault detection with early return red herring
    critical_faults = [x for x in readings if x > 100]
    if len(critical_faults) > 3:
        return -999  # Never reached due to logic flow

    # Actual key processing function
    def process_readings(data, limit):
        temp_result = 0
        for i, val in enumerate(data):
            if i % 2 == 0:
                temp_result += val * (i + 1)
            else:
                temp_result -= val // (i + 1) if (i + 1) != 0 else 0
        # Bit manipulation decoy
        bit_shifted = temp_result >> 2
        xor_mask = temp_result ^ 0xFF
        # Final adjustment based on control flow
        if temp_result > limit:
            return temp_result - limit
        else:
            return temp_result + limit

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold)

    # Redundant case conversion chain (irrelevant)
    status_flag = config_params.get('status', 'ACTIVE')
    inverted_status = status_flag.swapcase()
    coded_status = inverted_status[::-1]

    # Unused tuple unpacking (distractor)
    try:
        first, second, *rest = filtered_data
    except ValueError:
        first, second = 0, 0

    # Output the required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data and parameters
data_stream = [12, 45, 67, 89, 23, 55, 78, 91]
settings = {
    'offset': 5,
    'scale': 1.1,
    'threshold': 60,
    'metadata': 'SENSOR-LOG_v1',
    'device_id': 'SNSR9876',
    'status': 'active'
}

# Execute
analyze_sensor_data(data_stream, settings)