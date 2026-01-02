import math

# Simulated sensor data processing with red herrings and complex flow
def preprocess_signal(raw_input):
    offset = 17
    scale = 2.3
    filtered = []
    temp_cache = {}
    accumulator = 0

    for i in range(len(raw_input)):
        val = raw_input[i] + offset
        if i % 3 == 0:
            val = int(val * scale) % 127
        elif i % 5 == 0:
            val = (val ^ 64) & 127
        else:
            val = max(0, val - 32)
        filtered.append(val)
        
        # Irrelevant caching logic (dead path)
        key = f'entry_{i % 11}'
        if key not in temp_cache:
            temp_cache[key] = []
        temp_cache[key].append(val * 19)

    return filtered

# Decoy transformation - never actually used in final result
def spectral_shift(data, factor=3):
    shifted = []
    for x in data:
        shifted.append((x << 2) | (x >> 6))
    return shifted[::-1]

# Real transformation function used in computation
def time_warp_sequence(seq, warp_factor=0.8):
    warped = []
    for i, x in enumerate(seq):
        adjusted = int(x * warp_factor) + (i % 7)
        warped.append(adjusted)
    return warped[::2] + warped[-1::-2][:len(warped)//2]  # slicing mix

# Bit manipulation misdirection
def entropy_score(arr):
    score = 0
    for x in arr:
        bits = bin(x).count('1')
        score += bits * (x % 9)
    return score // len(arr) if arr else 0

# Core analysis logic
def build_threshold_map(config_code):
    base_map = {}
    for i in range(25):
        code_val = (config_code * i) % 19
        limit = int(math.sin(code_val / 10) * 100) + 50
        base_map[f'node_{i}'] = abs(limit)
    
    # Unused nested structure (distractor)
    base_map['debug_meta'] = {
        'version': '2.1-alpha',
        'checksum': sum([hash(k) % 1000 for k in base_map.keys()]) % 97,
        'flags': [True, False, True]
    }
    
    return {k: v for k, v in base_map.items() if 'node_' in k}  # dictionary comprehension

# Set operation decoy
def validate_integrity(data):
    expected_range = set(range(256))
    actual_set = set(data)
    missing = expected_range - actual_set
    extras = actual_set - expected_range
    return len(missing) == 0 and len(extras) < 10

# Main pattern analyzer (used in final answer)
def analyze_pattern(dataset, limits):
    count = 0
    history = []
    node_keys = sorted(limits.keys(), key=lambda x: int(x.split('_')[1]))
    
    for i, value in enumerate(dataset):
        node_idx = i % len(node_keys)
        threshold = limits[node_keys[node_idx]]
        
        # Conditional branching with multiple concepts
        if value > threshold:
            count += 1
            if value % 2 == 0:
                history.append(value // 3)
            else:
                history.append(value // 4)
        elif value == threshold:
            history.append(-1)
        else:
            history.append(value // 5)
    
    # Final aggregation uses history slicing and bit ops
    focus_window = history[len(history)//4 : len(history)//2]
    aggregate = 0
    for h in focus_window:
        aggregate ^= (h + 5) & 255  # XOR accumulation
    
    return aggregate

# Entry point with distractions
if __name__ == '__main__':
    # Real input data
    sensor_readings = [88, 102, 45, 131, 73, 66, 92, 110, 54, 81, 77, 120, 68]
    
    # Irrelevant dataset (red herring)
    dummy_logs = [
        {'id': 'A7', 'status': 200, 'size': 144},
        {'id': 'B2', 'status': 404, 'size': 89},
        {'id': 'C9', 'status': 500, 'size': 201}
    ]
    
    # Chained real transformations
    calibrated = preprocess_signal(sensor_readings)
    transformed_data = time_warp_sequence(calibrated, 0.85)
    
    # Dead code path: unused but plausible
    if len(transformed_data) > 20:
        transformed_data = spectral_shift(transformed_data, 4)
    
    # Actual threshold map used in analysis
    threshold_map = build_threshold_map(13)
    
    # Misleading validation call (does nothing to result)
    is_valid = validate_integrity(calibrated)
    score_entropy = entropy_score(calibrated)
    
    # --- KEY STATEMENT ---
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")