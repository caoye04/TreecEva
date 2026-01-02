import math

def sensor_calibrate(raw):
    return [(x * 1.05) + 2 for x in raw]

def filter_outliers(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= 2 * std_dev]

def transform_coordinates(values):
    # Irrelevant transformation
    return [int(v * math.cos(math.pi / 4)) for v in values]

def accumulate_series(nums):
    acc = 0
    series = []
    for n in nums:
        acc += n
        series.append(acc)
    return series  # Dead code path

def decode_flags(flag_list):
    result = 0
    for i, flag in enumerate(flag_list):
        result |= (flag << i)
    return result  # Unused bitwise aggregation

def analyze_readings(data_dict):
    readings = data_dict['readings']
    threshold = data_dict['threshold']
    
    # Real logic starts here
    valid_readings = [r for r in readings if r > threshold]
    adjustment_factor = len(valid_readings) / len(readings) if readings else 0
    
    temp_state = {
        'base': sum(valid_readings),
        'count': len(valid_readings),
        'factor': adjustment_factor
    }
    
    # Distractor: irrelevant stats
    stats_snapshot = {
        'max_val': max(readings) if readings else 0,
        'min_val': min(readings) if readings else 0,
        'range': 0,
        'median_guess': sorted(readings)[len(readings)//2] if readings else 0
    }
    stats_snapshot['range'] = stats_snapshot['max_val'] - stats_snapshot['min_val']
    
    # More distractions
    diagnostic_codes = [0x10, 0x20, 0x30]
    error_accumulator = 0
    for code in diagnostic_codes:
        if code & 0x10:
            error_accumulator += 1
    anomaly_flag = error_accumulator > 2
    
    # Critical path hidden among noise
    if temp_state['count'] > 0:
        base_score = temp_state['base'] * temp_state['factor']
        penalty = 0
        for r in readings:
            if r < 0:
                penalty += 10
        final_diagnostic = int(base_score - penalty)
    else:
        final_diagnostic = -1
        
    # Decoy assignment
    final_diagnostic = final_diagnostic ^ 0x00  # No-op XOR
    
    return final_diagnostic

# Simulated sensor input
raw_sensor_data = [12, -5, 34, 67, -3, 23, 66, 101, 45, 29]

# Irrelevant preprocessing chain
calibrated = sensor_calibrate(raw_sensor_data)
filtered = filter_outliers(calibrated)
coords = transform_coordinates(filtered)
accumulated = accumulate_series(filtered)

# Flag decoding with no effect
flags = [1, 0, 1, 1]
decoded_flag_value = decode_flags(flags)

# Build meaningful data structure
processed_data = {
    'readings': [int(x) for x in filtered],
    'source_count': len(raw_sensor_data),
    'origin': 'sensor_array_A7',
    'timestamp': '2023-10-05T12:00:00Z',
    'threshold': 20
}

# Actual target computation
final_diagnostic = analyze_readings(processed_data)
print(f"Result: {final_diagnostic}")