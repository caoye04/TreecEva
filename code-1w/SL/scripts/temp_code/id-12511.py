import math

def sensor_calibrate(raw_value, offset):
    # Irrelevant calibration function (dead code path)
    return (raw_value + offset) * 1.02

def compute_entropy(data_list):
    # Distractor: computes entropy but not used in main logic
    total = sum(data_list)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in data_list:
        p = x / total
        if p > 0:
            entropy -= p * math.log(p)
    return round(entropy, 6)

def detect_spike(value, history, sensitivity=0.1):
    # Misleading auxiliary function that looks important
    if len(history) < 3:
        return False
    avg = sum(history[-3:]) / 3
    return abs(value - avg) > avg * sensitivity

def preprocess_signal(signal_stream):
    # Adds noise and smoothing — irrelevant processing
    filtered = []
    for i, val in enumerate(signal_stream):
        if i > 0 and i % 4 == 0:
            val = (val + signal_stream[i-1]) / 2
        adjusted = val * 0.98 + 0.5
        filtered.append(round(adjusted, 3))
    return filtered

def decode_bitstream(bits):
    # Unused bit manipulation decoy
    result = 0
    for b in bits:
        result = (result << 1) | b
    return result ^ 0xFF

def analyze_readings(data, thresholds):
    # Core logic buried among distractions
    baseline = thresholds['base']
    mode_flag = thresholds['mode']
    accumulator = 0
    
    for entry in data:
        category = entry['type']
        reading = entry['value']
        
        if category == 'A':
            temp = int(reading // 2)
            if temp % 2 == 0:
                accumulator += temp
            else:
                accumulator -= (temp * 0.5)
        elif category == 'B':
            temp = math.floor(reading)
            if temp > baseline:
                accumulator += temp - baseline
        elif category == 'C':
            # This branch contributes to final answer
            temp = reading ** 2
            if temp < 50:
                accumulator += 11
            else:
                accumulator -= 7
    
    # Final transformation
    if mode_flag:
        accumulator = int(abs(accumulator) * 1.5)
    else:
        accumulator = int(accumulator + 10)
    
    return accumulator

# Simulated sensor readings (real input data)
signal_input = [2.1, 4.3, 5.6, 3.2, 7.8, 6.4]
raw_data = [
    {'id': 101, 'raw': 8.0, 'meta': [1,0,1]},
    {'id': 102, 'raw': 12.5, 'meta': [0,1,1]}
]

# Preprocessing chain with red herrings
smoothed_signal = preprocess_signal(signal_input)
entropy_metric = compute_entropy([4, 5, 3, 6])  # Computed but unused

# Constructing processed_data — only this matters
processed_data = [
    {'type': 'A', 'value': 8.0},
    {'type': 'B', 'value': 10.5},
    {'type': 'C', 'value': 6.0},  # 6^2 = 36 < 50 → +11
    {'type': 'C', 'value': 8.0},  # 8^2 = 64 >= 50 → -7
    {'type': 'A', 'value': 10.0}   # 10//2 = 5 → odd → -2.5
]

# Threshold configuration map (dictionary usage)
threshold_map = {
    'base': 9,
    'mode': True,
    'debug': entropy_metric,
    'spike_tol': 0.15
}

# Decoy operations — irrelevant bit stream
bit_sequence = [1, 0, 1, 1, 0]
decoded_int = decode_bitstream(bit_sequence)

# Real execution path
calibrated = [sensor_calibrate(x, 0.1) for x in [3.0, 4.5]]  # Unused list
spike_flags = [detect_spike(x, [3,4,5]) for x in [6.0, 10.0]]  # Dead computation

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")