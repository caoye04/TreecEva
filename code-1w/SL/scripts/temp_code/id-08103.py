import math

# Simulated sensor array data processing with diagnostic validation
def collect_sensor_readings():
    raw_values = [127, 255, 192, 64, 96]
    checksum = sum(raw_values) % 256
    if checksum != 120:
        return None
    return [v / 2 for v in raw_values]

def transform_frame(data):
    # Apply bit-shift normalization and phase shift
    normalized = [(d >> 2) ^ 15 for d in data]
    rotated = [int(bin(n)[2:][-2:] + bin(n)[2:][:-2], 2) if len(bin(n)) > 4 else n for n in normalized]
    return rotated

def validate_integrity(seq):
    # Checksum using XOR folding
    acc = 0
    for s in seq:
        acc ^= s
    return acc == 60

def extract_features(signal):
    # Extract statistical features with red herring transformations
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    peak = max(signal)
    
    # Distractor: irrelevant frequency sweep
    harmonics = []
    for i in range(5):
        harmonics.append(math.sin(i * 0.5) * peak)
    
    # Another red herring: unused convolution
    kernel = [0.25, 0.5, 0.25]
    smoothed = [signal[i-1]*kernel[0] + signal[i]*kernel[1] + signal[(i+1)%len(signal)]*kernel[2] 
               for i in range(len(signal))]
    
    # Only this feature is actually used later
    feature_vector = {
        'avg': int(mean_val),
        'var': int(variance),
        'peak_level': peak
    }
    return feature_vector

def route_by_priority(code_str):
    # String-based priority routing (only one path matters)
    if 'ERR' in code_str:
        return 1
    elif 'WRN' in code_str:
        return 2
    elif 'INFO' in code_str:
        return 3
    else:
        return 4

def generate_diagnostics(features):
    # Complex diagnostic logic with misleading branches
    base_score = 0
    if features['avg'] > 20:
        base_score += 15
    if features['var'] < 50:
        base_score += 25
    if features['peak_level'] >= 30:
        base_score += 10
    
    # Dead branch: never reached due to prior conditions
    temp_flag = False
    for i in range(100):
        if i == 50:
            temp_flag = True
            break
    if temp_flag and features['var'] > 100:
        base_score += 100  # unreachable
    
    # Irrelevant string manipulation chain
    status_msg = f"DIAG-{features['avg']:02d}-LEVEL"
    tokens = status_msg.split('-')
    extended_code = ''.join([t[::-1] for t in tokens])
    priority = route_by_priority(extended_code)  # always returns 4
    
    # Final adjustment based on priority (constant)
    final_score = base_score - (priority * 2)
    
    return final_score

def analyze_signal(dataset):
    # Main analysis pipeline
    processed = transform_frame(dataset)
    if not validate_integrity(processed):
        return -1
    features = extract_features(processed)
    result = generate_diagnostics(features)
    return result

# Execution flow
sensor_data = collect_sensor_readings()
if sensor_data is None:
    final_diagnostic = -999
else:
    # Linear search for anomalous readings (unused result)
    anomaly_index = -1
    for idx, val in enumerate(sensor_data):
        if val > 100:
            anomaly_index = idx
            break
    
    # Additional irrelevant transformation chain
    temp_buffer = []
    for x in sensor_data:
        temp_buffer.append(int(math.log2(x + 1)))
    
    processed_data = transform_frame(sensor_data)
    final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")