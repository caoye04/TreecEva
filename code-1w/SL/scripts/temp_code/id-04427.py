import math

# Simulated sensor data from environmental monitoring array
def acquire_sensor_readings():
    raw_samples = [14, 17, 23, 34, 25, 18, 14, 11, 9, 12, 15, 22, 29, 31]
    noise_floor = 8
    return [x - noise_floor for x in raw_samples]

# Legacy function – unused but looks relevant (red herring)
def deprecated_filter(signal):
    return [x for x in signal if x > 5 and x % 2 == 1]

# Apply moving average smoothing
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        segment = data[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

# Transform readings into categorized bands
def categorize_magnitude(value):
    if value < 5:
        return 'LOW'
    elif value < 10:
        return 'MODERATE'
    else:
        return 'HIGH'

# Unused diagnostic – misleading intermediate result
unused_peak_analysis = {
    'max_reading': 22,
    'anomaly_count': 3,
    'risk_level': 'MODERATE'
}

# Simulate time-series metadata alignment
timestamps = [f't{str(i)}' for i in range(14)]
readings = acquire_sensor_readings()
indexed_data = list(zip(timestamps, readings))

# Extract only values for processing
extracted_values = [val for _, val in indexed_data]

# Smooth the extracted signal
smoothed_readings = smooth_signal(extracted_values)

# Apply logarithmic compression for dynamic range adjustment (relevant)
compressed_signal = [math.log(x + 1) for x in smoothed_readings]

# Generate threshold map using bitwise pattern (distractor with real usage)
baseline_thresholds = []
for i in range(14):
    # Complex-looking but deterministic threshold generation
    temp_val = (i ^ 7) & 12  # Bitwise red herring
    scaled = round((temp_val + 3.5) / 2.1, 2)
    baseline_thresholds.append(scaled)

# Unused alternate method (dead code path)
def evaluate_spike_risk(seq):
    risk_score = 0
    for val in seq:
        if val > 10:
            risk_score += val // 4
    return risk_score

# Real processing begins: prepare data structure
processed_data = {
    'metrics': [],
    'flags': []
}

for idx, val in enumerate(compressed_signal):
    category = categorize_magnitude(val)
    flag_state = (idx % 4 == 0) or (val > 2.8)
    processed_data['metrics'].append({
        'index': idx,
        'value': round(val, 3),
        'band': category
    })
    processed_data['flags'].append(flag_state)

# Threshold map used in final analysis
threshold_map = {ts: th for ts, th in zip(timestamps, baseline_thresholds)}

# Decoy statistical summary (irrelevant computation)
phantom_trend = sum(baseline_thresholds[i] * 0.9 for i in range(0, len(baseline_thresholds), 2))

# Core analysis function with conditional logic and recursion
def analyze_signal(data, thresholds, index=0):
    if index >= len(data['metrics']):
        return 0
    
    metric = data['metrics'][index]
    ts_key = f't{index}'
    thresh = thresholds[ts_key]
    value = metric['value']
    flag = data['flags'][index]
    
    base_score = 0
    if value > thresh:
        base_score += int(value * 2)
    elif flag:
        base_score += 5
    
    # Recursive accumulation with conditional branching
    recursive_offset = analyze_signal(data, thresholds, index + 1)
    
    # Conditional transformation based on band
    if metric['band'] == 'HIGH':
        base_score = int(base_score * 1.2) if recursive_offset > 10 else base_score + 3
    elif metric['band'] == 'MODERATE':
        base_score = max(base_score, recursive_offset // 2)
    
    return base_score + recursive_offset // 3

# Execute main analysis
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Irrelevant post-processing (distractor)
adjusted_diagnostics = [final_diagnostic + i for i in range(3)]
scaled_report = {"level": final_diagnostic / 7, "status": "OK"}

# Output the target result
print(f"Result: {final_diagnostic}")