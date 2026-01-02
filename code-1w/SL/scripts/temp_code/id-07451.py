def analyze_sensor_stream(raw_input, config_params):
    # Irrelevant preprocessing: character frequency count (distractor)
    char_freq = {}
    for char in ''.join(raw_input):
        char_freq[char] = char_freq.get(char, 0) + 1

    # Misleading data transformation: base conversion with no use (red herring)
    temp_checksum = 0
    for i, val in enumerate(config_params['calibration_sequence']):
        temp_checksum += val * (2 ** (i % 8))
    scaled_checksum = bin(temp_checksum)[2:]

    # Actual relevant logic begins: parse and filter sensor readings
    readings = []
    for line in raw_input:
        parts = line.strip().split(',')
        if len(parts) < 3 or not parts[2].replace('.', '').lstrip('-').isdigit():
            continue
        try:
            sensor_id = int(parts[0])
            timestamp = float(parts[1])
            reading_val = float(parts[2])
            if config_params['valid_sensors'].get(sensor_id, False):
                readings.append((sensor_id, timestamp, reading_val))
        except (ValueError, IndexError):
            continue

    # Distractor: unused recursive function (dead code path)
    def calculate_entropy(data_list):
        if len(data_list) <= 1:
            return 0.0
        mid = len(data_list) // 2
        return 1 + max(calculate_entropy(data_list[:mid]),
                      calculate_entropy(data_list[mid:]))

    # Distractor: complex but irrelevant bit manipulation (misleading intermediate)
    magic_offset = 0
    for i in range(len(scaled_checksum)):
        if scaled_checksum[i] == '1':
            magic_offset ^= (i + 1) << (i % 5)

    # Relevant: filter by time window (conditional branch)
    t_min, t_max = config_params['time_window']
    recent_readings = [r for r in readings if t_min <= r[1] <= t_max]

    # Distractor: unused zip and enumerate on unrelated metadata
    labels = config_params['label_set']
    label_index_map = {idx: label for idx, label in enumerate(labels)}
    for idx, (sensor_id, _, _) in enumerate(recent_readings):
        _ = label_index_map.get(sensor_id % len(labels), 'unknown')  # No effect

    # Relevant: group readings by sensor using dictionary
    grouped = {}
    for sid, ts, val in recent_readings:
        if sid not in grouped:
            grouped[sid] = []
        grouped[sid].append(val)

    # Distractor: decoy statistical computation (not used in final result)
    outlier_flags = {}
    for sid, vals in grouped.items():
        mean_v = sum(vals) / len(vals)
        std_v = (sum((x - mean_v) ** 2 for x in vals) / len(vals)) ** 0.5
        outlier_flags[sid] = [abs(x - mean_v) > 2 * std_v for x in vals]

    # Relevant: apply dynamic thresholds from config
    threshold_map = {}
    for sensor_type, multiplier in config_params['threshold_multipliers'].items():
        base = config_params['base_thresholds'][sensor_type]
        env_factor = config_params['environment_factors'].get('humidity', 1.0)
        threshold_map[sensor_type] = base * multiplier * env_factor

    # Filter data based on type-specific thresholds (key filtering step)
    filtered_data = []
    for sid, vals in grouped.items():
        sensor_type = sid % 3
        thresh = threshold_map.get(sensor_type, 100.0)
        valid_vals = [v for v in vals if abs(v) <= thresh]
        if valid_vals:
            filtered_data.append((sid, sum(valid_vals) / len(valid_vals)))

    # Final processing function (critical execution point)
    def process_readings(data, thresholds):
        if not data:
            return -1
        weighted_sum = 0.0
        total_weight = 0
        for item in data:
            sensor_id = item[0]
            avg_val = item[1]
            weight = (sensor_id % 4) + 1
            # String-based condition as distractor (never triggers due to data constraints)
            trigger_str = "alert" if avg_val > 50 else "normal"
            if 'z' in trigger_str:  # Dead logic
                weight *= 2
            weighted_sum += avg_val * weight
            total_weight += weight
        return round(weighted_sum / total_weight, 6) if total_weight else 0.0

    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input setup
input_lines = [
    "1,10.5,15.2", "2,11.0,-8.4", "3,11.5,105.3", "1,12.0,17.1",
    "4,12.5,33.9", "2,13.0,9.7", "1,13.5,-22.4", "5,14.0,45.6",
    "3,14.5,110.0", "2,15.0,12.8"
]

params = {
    'calibration_sequence': [7, 3, 9, 1, 5],
    'valid_sensors': {1: True, 2: True, 3: True, 4: True},
    'time_window': (11.0, 15.0),
    'label_set': ['typeA', 'typeB', 'typeC'],
    'threshold_multipliers': {0: 1.2, 1: 0.9, 2: 1.5},
    'base_thresholds': {0: 20.0, 1: 15.0, 2: 100.0},
    'environment_factors': {'humidity': 1.1},
    'debug_mode': False
}

# Execute
analyze_sensor_stream(input_lines, params)