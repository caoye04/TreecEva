import math

# System calibration parameters (irrelevant to final result)
calibration_sequence = [0.1, 0.3, 0.5, 0.7, 0.9]
baseline_offset = sum([math.sin(x * math.pi) for x in calibration_sequence])
reference_frame = {i: math.cos(i * 0.2) for i in range(8)}

# Sensor data input (simulated)
sensor_readings = [
    {'id': 'A7', 'values': [1.2, 3.4, -2.1, 5.6, 4.3, -1.0, 0.8, 2.2]},
    {'id': 'B3', 'values': [0.9, -3.1, 4.4, 2.7, -5.3, 1.8, 3.2, -2.2]},
    {'id': 'C9', 'values': [2.0, 1.1, -0.5, 3.3, 4.4, 2.1, -1.2, 0.9]}
]

# Irrelevant signal processing chain
def preprocess_signal(data):
    return [x * 1.05 for x in data if abs(x) > 0.5]

def apply_filter(signal, mode='lowpass'):
    if mode == 'lowpass':
        return [x for x in signal if x < 4.0]
    elif mode == 'highpass':
        return [x for x in signal if x > 0]
    else:
        return signal

# Unused but misleading transformation functions
def legacy_transform(x):
    return (x ** 2 + 2 * x + 1) if x >= 0 else (x ** 2 - 2 * x + 1)

def deprecated_normalize(vector):
    norm = sum([abs(v) for v in vector])
    return [v / norm for v in vector] if norm != 0 else vector

# Core logic — only this part matters for final answer
active_channels = set()
for reading in sensor_readings:
    channel_id = reading['id'][0]
    if channel_id in ['A', 'C']:
        active_channels.add(channel_id)

filtered_data = []
for reading in sensor_readings:
    processed = [x for x in reading['values'] if x > 1.0 and x < 5.0]
    filtered_data.extend(processed)

# Threshold map with red herring entries
threshold_map = {
    'A': 2.5,
    'B': 1.8,
    'C': 3.0,
    'X': 0.0,  # unused
    'Y': -1.0  # unused
}

# Distractor: complex but unused diagnostic routine
def compute_health_score(signal_chunk):
    if not signal_chunk:
        return 0
    mean_val = sum(signal_chunk) / len(signal_chunk)
    variance = sum((x - mean_val) ** 2 for x in signal_chunk) / len(signal_chunk)
    return int(math.sqrt(variance) * 10) if variance > 0 else 0

health_diagnostics = [
    compute_health_score(rd['values']) for rd in sensor_readings
]

# Actual analysis function contributing to answer
def analyze_signal(cleaned, thresholds):
    count_above = 0
    total_contrib = 0.0
    
    # Logical operations and conditional expressions
    primary_thresh = thresholds['A'] if 'A' in active_channels else thresholds['C']
    secondary_thresh = thresholds.get('C', 2.0)
    
    for val in cleaned:
        meets_primary = val > primary_thresh
        meets_secondary = val >= secondary_thresh
        
        # Bit manipulation red herring (unused)
        flag = (int(val) & 1) ^ 1  # flips LSB
        
        # Only this condition contributes to final result
        if meets_primary or (val > 2.0 and len(str(int(val))) == 1):
            count_above += 1
        
        if val < 4.5 and (val > 0):  # additional filter
            total_contrib += math.log(val + 1)
    
    # Linear search through reference (mostly irrelevant)
    matched_ref = None
    for k, v in reference_frame.items():
        if abs(v - total_contrib) < 0.1:
            matched_ref = k
            break
    
    # Final computation
    adjustment = len(active_channels) * 0.5
    raw_score = count_above * total_contrib
    return int(raw_score - adjustment) if raw_score > 5 else int(raw_score + adjustment)

# Dead code path — never called
def backup_analysis(seq):
    return sum([len(preprocess_signal(s['values'])) for s in seq])

# Key execution point
final_diagnostic = analyze_signal(filtered_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")