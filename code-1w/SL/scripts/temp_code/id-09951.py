import math

# Simulated sensor array data from environmental monitoring system
def fetch_sensor_readings():
    raw_values = [127, 255, 193, 64, 88, 201, 142]
    noise_floor = 17
    adjusted = [val ^ noise_floor for val in raw_values]
    return adjusted

# Legacy function - unused but looks relevant
def legacy_calibrate(x):
    return (x >> 3) * 0.87

# Signal processing pipeline
def normalize(signal):
    max_val = max(signal)
    return [round(s / max_val * 255) for s in signal]

def detect_peaks(data, sensitivity=0.7):
    peaks = []
    avg = sum(data) / len(data)
    for i, val in enumerate(data):
        if val > avg * sensitivity:
            peaks.append(i)
    return peaks

def encode_metadata(peaks, version='v2'):
    # Encodes peak indices into a checksum
    base = 1
    checksum = 0
    for p in peaks:
        checksum += p * base
        base *= 3
    if version == 'v1':
        return checksum % 1000
    else:
        return checksum % 10000

# Irrelevant string transformation (distractor)
def scramble_id(device_id):
    rotated = device_id[3:] + device_id[:3]
    return rotated.upper().replace('A', 'X').strip()

device_code = "sensor42"
scrambled = scramble_id(device_code)  # Dead code path

# Data fusion and weighting logic
def fuse_channels(primary, secondary):
    fused = []
    weights = [0.7, 0.3]  # Emphasis on primary
    for i in range(len(primary)):
        fused.append(int(primary[i] * weights[0] + secondary[i] % 100 * weights[1]))
    return fused

# Unused fallback method
def simple_average(arr):
    return sum(arr) / len(arr)

# Core analysis functions
def classify_pattern(peaks):
    if len(peaks) == 0:
        return 1
    elif len(peaks) == 1:
        return 2
    elif peaks == sorted(peaks):  # Monotonic
        return 4
    else:
        return 8

threshold_map = {
    'low': 42,
    'mid': 85,
    'high': 128
}

# Complex multi-stage processing
def analyze_signal(data, limits):
    stage1 = [x for x in data if x > limits['low']]
    stage2 = [x for x in stage1 if x < limits['high']]
    
    # Apply non-linear transformation
    transformed = []
    for val in stage2:
        if val % 2 == 0:
            transformed.append(int(math.log(val, 2)))
        else:
            transformed.append(int(math.sqrt(val)))
    
    # Bit manipulation for anomaly detection
    bit_analysis = 0
    for t in transformed:
        bit_analysis ^= t << 1
        bit_analysis |= (t & 7)
    
    # Conditional adjustment based on size
    if len(transformed) >= 4:
        bit_analysis += 100
    else:
        bit_analysis -= 50
    
    # Final classification with embedded constant
    pattern_class = classify_pattern(stage2)
    score = bit_analysis * pattern_class
    
    # Red herring: floating point accumulation (unused)
    accumulator = 0.0
    for i in range(len(transformed)):
        accumulator += math.sin(i + 1) * transformed[i]
    normalized_acc = round(accumulator, 4)
    
    # Decoy operation: string-based key generation
    key_parts = [str(bit_analysis), 'XYZ', str(len(stage2))]
    signature = '-'.join(key_parts).lower().replace('x', '9')
    
    # Actual result
    final_diagnostic = score + len(signature)  # Main output depends on this
    return final_diagnostic

# Execution flow
raw_data = fetch_sensor_readings()
normalized_data = normalize(raw_data)
primary_channel = [x + 10 for x in normalized_data]
secondary_channel = [x * 2 for x in raw_data]
fused_signal = fuse_channels(primary_channel, secondary_channel)

# Extract peaks for metadata (part of distraction)
peak_indices = detect_peaks(fused_signal, sensitivity=0.65)
meta_checksum = encode_metadata(peak_indices, version='v2')

# Critical execution point
processed_data = [x - 20 for x in fused_signal if x > 40]
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")