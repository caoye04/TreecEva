def analyze_sensor_node(node_data, config):
    readings = node_data.get('readings', [])
    metadata = node_data.get('meta', {})
    temp_offset = config.get('temp_offset', 0.0)
    calibration_map = config.get('calibration', {})
    
    # Irrelevant preprocessing: formatting timestamps (dead path)
    formatted_times = []
    for entry in readings:
        if isinstance(entry.get('timestamp'), str):
            cleaned = entry['timestamp'].replace('T', ' ').split('.')[0]
            formatted_times.append(cleaned)  # Unused
    
    # Distractor: complex string manipulation with no impact
    status_flag = metadata.get('status', 'OK').lower()
    encoded_flag = ''.join([chr(ord(c) + 3) for c in status_flag])
    masked_flag = ''.join([c for i, c in enumerate(encoded_flag) if i % 2 == 0])

    # Real logic begins: extract and adjust values
    raw_values = [r['value'] for r in readings if r.get('active', True)]
    adjusted_values = []
    for v in raw_values:
        key = str(int(v))[-1] if v != 0 else '0'
        adj = v + temp_offset + calibration_map.get(key, 0)
        adjusted_values.append(adj)
    
    # Distractor: bitwise decoy operation
    checksum = 0
    for val in raw_values:
        truncated = int(abs(val)) % 256
        checksum ^= (truncated << 1) ^ 0xAA
    final_checksum = checksum & 0xFF  # Unused

    # Filtering based on dynamic condition
    baseline = sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0
    variance = sum((x - baseline) ** 2 for x in adjusted_values) / len(adjusted_values) if adjusted_values else 0
    filtered_data = [x for x in adjusted_values if abs(x - baseline) <= 2 * (variance ** 0.5)]

    # Distractor: unused recursive function
    def recurse_noise(level, acc):
        if level <= 0:
            return acc
        return recurse_noise(level - 1, acc ^ (level * 0x5A))
    noise_pattern = recurse_noise(5, 0)  # Dead end

    # Real logic: prepare threshold map
    threshold_map = {}
    for i, val in enumerate(filtered_data):
        category = 'high' if val > baseline else 'low'
        code = chr(ord('X') + (i % 3))
        threshold_map[f'{category}_{code}'] = round(abs(val * 0.1), 4)

    # Critical call
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic


def process_readings(data, limits):
    if not data:
        return -999
    
    # Use enumerate and zip meaningfully
    indexed = list(enumerate(data))
    shifted = [data[(i + 1) % len(data)] for i in range(len(data))]
    pairs = list(zip(indexed, shifted))
    
    # Compute moving correlation-like metric
    total = 0.0
    for (i, val), next_val in pairs:
        if i % 2 == 0:
            diff = abs(val - next_val)
            adjustment = limits.get(f'{'high' if val > 0 else 'low'}_{'X' if i % 3 == 0 else 'Y' if i % 3 == 1 else 'Z'}', 0.0)
            total += diff - adjustment
        else:
            # Bitwise red herring
            combined = int(abs(val)) ^ int(abs(next_val))
            modulated = (combined & 0xF) * 0.05  # Not used in output
    
    # Final computation
    avg = sum(data) / len(data)
    penalty = sum(1 for x in data if x < 0) * 0.5
    result = round(avg * 100 - penalty + total, 4)
    
    # This is the actual answer
    return result

# Simulate execution
sensor_data = {
    'readings': [
        {'value': 12.5, 'timestamp': '2023-07-01T10:00:00.123Z', 'active': True},
        {'value': 13.1, 'timestamp': '2023-07-01T10:01:00.456Z', 'active': True},
        {'value': -8.7, 'timestamp': '2023-07-01T10:02:00.789Z', 'active': True},
        {'value': 12.9, 'timestamp': '2023-07-01T10:03:00.123Z', 'active': True},
        {'value': 14.2, 'timestamp': '2023-07-01T10:04:00.456Z', 'active': False},  # Inactive
        {'value': 11.8, 'timestamp': '2023-07-01T10:05:00.789Z', 'active': True}
    ],
    'meta': {
        'status': 'NORMAL',
        'node_id': 'SN-7XK-2023',
        'location': 'Sector G7'
    }
}

config_params = {
    'temp_offset': -0.3,
    'calibration': {'2': 0.1, '3': 0.2, '8': -0.4, '1': 0.05, '9': 0.15}
}

# Trigger the analysis
final_diagnostic = analyze_sensor_node(sensor_data, config_params)
print(f"Target result: {final_diagnostic}")