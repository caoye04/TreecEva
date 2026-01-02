import itertools

def preprocess_signal(samples):
    # Irrelevant preprocessing function (dead path)
    return [s * 0.95 for s in samples if s > 0]

def compute_entropy(data):
    # Misleading computation: looks important but unused
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

def detect_anomalies(stream, threshold=0.75):
    # Distractor: complex logic that doesn't affect final result
    anomalies = []
    for i, val in enumerate(stream):
        if i > 0 and abs(val - stream[i-1]) > threshold:
            anomalies.append((i, val))
    return anomalies

def extract_signatures(patterns):
    # Unused transformation with slicing red herring
    sigs = []
    for p in patterns:
        chunk = p[::2]  # Every second element — looks meaningful
        sigs.append(sum(chunk) % 7)
    return sigs

def validate_checksum(sequence):
    # Bit manipulation decoy
    checksum = 0
    for num in sequence:
        checksum ^= (num << 1) | (num >> 2)
        checksum %= 1000
    return checksum == 42  # Always false in practice here

def aggregate_metrics(sensor_log, keyframe):
    # Core logic embedded in noise
    accumulator = 0
    pivot_index = 0
    
    # Real logic starts here — nested and obscured
    for idx, reading in enumerate(sensor_log):
        if idx % 3 == 0:
            temp_val = reading ^ keyframe[idx % len(keyframe)]  # XOR operation
            if temp_val % 2 == 0:
                accumulator += temp_val * 2
            else:
                accumulator -= temp_val // 3
        elif idx % 5 == 0:
            # Secondary branch with modular arithmetic
            mod_shift = (reading + idx) % 8
            accumulator += mod_shift ** 2
    
    # Data transformation using zip and enumerate
    paired = list(zip(sensor_log[1::2], keyframe))
    for i, (a, b) in enumerate(paired):
        if i in {2, 3}:
            accumulator += (a & b) * i  # Bitwise AND used selectively
    
    # Final adjustment using itertools.cycle
    cyclic_adjust = 0
    for a, b in itertools.islice(itertools.zip_longest(sensor_log, keyframe), 7):
        if b is not None:
            cyclic_adjust += (a - b) % 4
    
    accumulator -= cyclic_adjust
    
    # Critical assignment point
    final_diagnostic = accumulator * 3 + 17
    
    # Dead code below
    outlier_map = detect_anomalies(sensor_log)
    entropy_score = compute_entropy(keyframe)
    valid = validate_checksum(sensor_log)
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input data with domain-specific meaning
    turbine_data = [127, 89, 211, 64, 193, 77, 144, 202, 58, 131, 95]
    calibration_sequence = [17, 23, 19, 29, 31]
    
    # Irrelevant variables (distractors)
    baseline_ref = preprocess_signal(turbine_data)
    signature_list = extract_signatures([turbine_data[:5], calibration_sequence])
    status_flags = [0] * len(turbine_data)
    
    # Key execution point
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")