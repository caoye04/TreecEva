import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_readings):
    filtered = []
    for x in raw_readings:
        if abs(x - 512) < 200:  # valid range
            filtered.append(x * 0.98 + 12)
    return filtered[::2]  # slicing: every second element

# Irrelevant helper - looks useful but unused in critical path
def deprecated_normalize(arr):
    max_val = max(arr)
    return [a / max_val for a in arr]

# Data transformation pipeline
def encode_sequence(signal, key):
    encoded = []
    shift = sum(key) % 8
    for i, val in enumerate(signal):
        temp = int((val ^ (i * 3)) + (shift * 2))  # bitwise XOR and arithmetic
        encoded.append(temp % 1024)
    return encoded

# Red herring function: appears important but not used in final result
def compute_entropy(data):
    hist = {}
    for d in data:
        hist[d] = hist.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in hist.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

# Core pattern analyzer
def analyze_pattern(seq, cfg):
    window_size = cfg['window']
    threshold = cfg['thresh']
    score = 0
    
    # Multiple nested logic levels
    for i in range(len(seq) - window_size + 1):
        window = seq[i:i+window_size]  # slicing operation
        avg = sum(window) / len(window)
        deviation = sum(abs(w - avg) for w in window)
        
        # Complex conditional chain
        if avg > threshold:
            if deviation < 150:
                if window[0] % 2 == 0:
                    score += int(avg // 10)
                else:
                    score += int(avg // 15)
        elif avg < threshold - 50:
            score -= 1
    
    # Distractor computation (modifies score but ultimately irrelevant)
    backup_mode = cfg.get('backup', False)
    if backup_mode:
        score = abs(score) * 2  # dead branch: never executed
    
    # Final adjustment based on control flow history
    modifier = 1
    for j in range(2, 5):
        if all(seq[k] % j == 0 for k in range(0, min(6, len(seq)), 2)):
            modifier *= j
    
    return score * modifier

# Misleading intermediate variables
raw_sensor_data = [510, 520, 490, 600, 530, 515, 570, 505, 540, 560, 525, 535]
signal_baseline = sum(raw_sensor_data) / len(raw_sensor_data)
deprecated_index = [x - signal_baseline for x in raw_sensor_data]

# Actual execution path
processed = preprocess_signal(raw_sensor_data)

# Unused complex structure - red herring
lookup_table = {
    'modes': [1, 3, 5],
    'flags': {'f1': True, 'f2': False},
    'weights': [[i+j for j in range(3)] for i in range(3)]
}

config = {
    'window': 4,
    'thresh': 520,
    'version': '2.1'
}

key_mask = [3, 1, 4, 1, 5]
transformed_data = encode_sequence(processed, key_mask)

# Decoy usage of transformed_data
if len(transformed_data) > 10:
    transformed_data = transformed_data[:8]

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, config)

# Additional distractor: modifies state but not used
historical_logs = []
historical_logs.append({'timestamp': 12345, 'value': sum(transformed_data)})

# Output the target result
print(f"Target result: {final_diagnostic}")