def sensor_calibration(sequence):
    calibrated = []
    for val in sequence:
        if val < 0:
            val = abs(val) ^ 3
        temp = (val * 17 + 9) % 101
        calibrated.append(temp)
    return [x for x in calibrated if x % 2 == 1]

raw_readings = [42, -15, 8, 67, -23, 91, 14, 36]
depth_flags = {k: (k % 7) for k in range(10)}

# Irrelevant transformation chain (distractor)
def transform_sequence(data):
    result = []
    for d in data:
        d = d << 1
        d = d ^ 15
        d = d >> 1
        result.append(d)
    return result

transformed = transform_sequence(raw_readings)  # Dead path

# Actual preprocessing
processed_data = sensor_calibration(raw_readings)

# Misleading intermediate analysis (red herring)
def legacy_analysis(arr):
    score = 0
    for i in range(len(arr)):
        if arr[i] > 50:
            score += 2
        else:
            score += 1
    return score * 0.75

legacy_score = legacy_analysis(processed_data)  # Not used

# Threshold logic with tuple unpacking and lambda filtering
def dynamic_threshold(values):
    base = sum(values) / len(values)
    upper = base * 1.3
    lower = base * 0.7
    return (lower, upper)

threshold_bounds = dynamic_threshold(processed_data)
threshold_map = {
    'low': threshold_bounds[0],
    'high': threshold_bounds[1],
    'window': slice(1, len(processed_data)//2)
}

# Decoy function using string methods (irrelevant)
def format_diagnostics(code_list):
    labels = ['ERR', 'OK', 'WARN']
    codes = []
    for c in code_list:
        tag = labels[c % 3]
        codes.append(f'{tag}-{str(c).zfill(3)}')
    return ','.join(codes).replace('ERR', '***')

_ = format_diagnostics(processed_data)  # Unused result

# Core analysis with slicing and lambda
analyze_readings = lambda data, limits: \
    sum([\
        (data[i] ** 2) >> 2 \
        for i in limits['window'] \
        if limits['low'] < data[i] < limits['high']
    ]) + (limits['high'] - limits['low'])

# Key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result
print(f'Result: {final_diagnostic}')