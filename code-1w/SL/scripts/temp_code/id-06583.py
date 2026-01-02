def analyze_sensor_array(raw_input, config_params):
    # Irrelevant preprocessing stub
    temp_buffer = [x for x in raw_input if isinstance(x, int) and x > -1]
    metadata_log = ''.join(['E' if i % 3 == 0 else 'X' for i in range(len(temp_buffer))])
    
    # Distractor: complex-looking but unused transformation
    shifted_grid = []
    for i in range(len(temp_buffer)):
        shifted_val = (temp_buffer[i] << 2) ^ 0xFF
        if shifted_val < 100:
            shifted_grid.append(shifted_val)
    
    # Actual signal extraction
    valid_readings = []
    for val in raw_input:
        if type(val) == int and 10 <= val <= 99:
            tens_digit = val // 10
            ones_digit = val % 10
            if (tens_digit + ones_digit) % 2 == 0:
                valid_readings.append(val)

    # Dead code path - looks important but never reached due to condition
    outlier_report = []
    if len(valid_readings) > 100:
        for v in valid_readings:
            if v in [x*x for x in range(1,11)]:
                outlier_report.append(v)

    # Key filtering logic
    filtered_data = []
    for item in valid_readings:
        if item not in [11, 22, 33, 44, 55, 66, 77, 88, 99]:  # Remove repdigits
            digit_sum = sum(int(d) for d in str(item))
            if digit_sum in config_params['allowed_sums']:
                filtered_data.append(item * 2)  # Double relevant readings

    # Unused checksum calculation (distractor)
    checksum = 0
    mask_sequence = config_params.get('mask', [1,0,1])
    for idx, c in enumerate(str(sum(filtered_data))):
        checksum += int(c) * mask_sequence[idx % len(mask_sequence)]

    # Real threshold mapping based on environment mode
    threshold_map = {}
    mode = config_params.get('mode', 'standard')
    base_threshold = config_params.get('base_thresh', 40)
    
    for i in range(10, 100, 10):
        key = f'thresh_{i}'
        adj = 5 if i % 20 == 0 else 0
        calc_val = base_threshold + adj + (i // 10)
        threshold_map[i] = calc_val  # Only some are used later

    # Misleading early aggregation
    summary_stats = {
        'peak': max(filtered_data) if filtered_data else 0,
        'density': len([x for x in filtered_data if x > 50]),
        'flags': [False, True, False]
    }

    # Decoy function definition inside main flow
    def validate_integrity(data_slice):
        return sum(b & 1 for b in data_slice) % 2 == 0

    # Critical processing function defined inline
    def process_readings(data_list, limits):
        result = 0
        for num in data_list:
            decade = (num // 10) * 10
            limit_key = decade if decade in limits else 10
            if num < limits.get(limit_key, 99):
                result += num ^ (limit_key % 7)
            else:
                result -= num >> 1
        return abs(result)

    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Red herring: irrelevant string analysis
    debug_tag = "DGN" + str(len(metadata_log))
    if 'X' in debug_tag:
        debug_tag += '_ALT'
    
    # Final output
    print(f"Result: {final_diagnostic}")

# Simulate sensor input and configuration
sensor_input = [12, 13, 21, 22, 30, 34, 43, 44, 51, 55, 60, 67, 76, 77, 84, 88, 93, 99, 100, 'X', -5]
params = {
    'mode': 'enhanced',
    'base_thresh': 38,
    'allowed_sums': [3, 4, 6, 7],
    'mask': [2, 1]
}

# Execute
analyze_sensor_array(sensor_input, params)