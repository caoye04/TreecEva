import itertools

# Simulated sensor data processing with red herrings and complex flow
def preprocess_signal(raw):    
    offset = 42
    gain = 1.5
    filtered = [x for x in raw if x > 0]
    scaled = [gain * x + offset for x in filtered]
    return scaled

# Irrelevant transformation — looks important but unused in final result
def encrypt_sequence(data):
    key = 257
    return [(x ^ key) % 10000 for x in data]

# Decoy function — never called but distracts reasoning
def compute_entropy(seq):
    from math import log
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0.0
    total = len(seq)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Core logic: pattern analysis using recursion and bit manipulation
def detect_cycle(sequence, index=0, seen=None):
    if seen is None:
        seen = set()
    if index >= len(sequence):
        return False
    val = sequence[index] & 0xFF  # Use only lower byte
    if val in seen:
        return True
    seen.add(val)
    return detect_cycle(sequence, index + 1, seen)

# Data transformation with string operations (python idiom)
def transform_to_blocks(data):
    hex_strings = [hex(x)[2:].zfill(4) for x in data]
    joined = ''.join(hex_strings)
    blocks = [joined[i:i+8] for i in range(0, len(joined), 8)]
    # Use string method to filter
    valid = [b for b in blocks if b.count('a') + b.count('f') < 3]
    return [int(b, 16) for b in valid if len(b) == 8]

# Higher-order function with lambda — actual used component
def apply_correction(signal, mode='linear'):
    correct = {
        'linear': lambda x: x - 37,
        'quadratic': lambda x: x - (x * 0.02),
        'none': lambda x: x
    }[mode]
    
    # Apply correction and remove outliers
    corrected = [int(correct(x)) for x in signal]
    cleaned = [c for c in corrected if 10 <= abs(c) <= 5000]
    return list(map(lambda z: z + 1 if z < 0 else z, cleaned))

# Main analysis function — depends on prior steps
def analyze_pattern(dataset):
    # Step 1: Filter using min/max thresholds
    threshold_low = min(dataset) // 2
    threshold_high = max(dataset) * 2
    subset = [x for x in dataset if threshold_low < x < threshold_high]
    
    # Step 2: Compute average and derive control flag
    avg = sum(subset) / len(subset)
    flag = int(avg) & 0b1111  # Lower 4 bits
    
    # Step 3: Use itertools to generate rolling pairs
    paired = list(itertools.pairwise(subset))  # Python 3.10+ idiom
    differences = [abs(a - b) for a, b in paired]
    
    # Step 4: Logical filtering with nested conditionals
    significant = []
    for d in differences:
        if d > 100:
            if d % 2 == 0:
                significant.append(d // 2)
            else:
                significant.append(d + 50)
    
    # Step 5: Aggregate final metric
    base_metric = sum(significant) // len(significant) if significant else 0
    adjustment = flag * 3
    final_score = base_metric - adjustment
    
    # Dead code path — looks like it affects output but doesn't
    debug_mode = False
    if debug_mode:
        log_entry = f"Final: {final_score}, Flag: {flag}"
        print(log_entry)  # Never reached

    return final_score

# Entry point simulation
if __name__ == '__main__':
    # Initial data — realistic sensor readings
    raw_readings = [12, -5, 23, 45, 67, 89, 100, -15, 200, 250, 300, 350, 400]
    
    # Irrelevant variables — distract from real flow
    calibration_matrix = [[1, 0], [0, 1]]
    system_uptime = 98765
    firmware_hash = sum([ord(c) for c in 'v3.2.1'])
    
    # Real processing chain
    processed = preprocess_signal(raw_readings)
    corrected = apply_correction(processed, mode='linear')
    transformed_data = transform_to_blocks(corrected)
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Misleading intermediate
    encrypted = encrypt_sequence(transformed_data)  # Unused
    cycle_detected = detect_cycle(encrypted)  # Used nowhere
    
    # Output required variable
    print(f"Result: {final_diagnostic}")