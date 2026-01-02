import itertools

# Simulated sensor array data from a distributed monitoring system
def generate_sensor_readings():
    base_values = [127, 255, 89, 191, 64]
    readings = []
    for i, val in enumerate(base_values):
        shifted = (val + i * 17) % 256
        readings.append(shifted)
    return readings

# Irrelevant transformation: color space conversion (red herring)
def rgb_to_hsv(r, g, b):
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val
    if max_val == 0:
        hue = 0
    else:
        hue = (60 * ((g - b) / diff) + 360) % 360
    saturation = 0 if max_val == 0 else diff / max_val
    value = max_val / 255
    return (hue, saturation, value)

# Unused helper function — dead code path
def compute_entropy(data):
    from math import log2
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy

# Core processing with meaningful logic and distractors
def analyze_pattern(seq):
    # Bit manipulation for fault signature extraction
    fault_mask = 0x55  # 01010101
    filtered = [x ^ fault_mask for x in seq]

    # Decoy statistical analysis
    mean_val = sum(seq) / len(seq)
    variance_proxy = sum((x - mean_val) ** 2 for x in seq) / len(seq)

    # Real signal: detect repeating 4-bit pattern
    nibbles = [(x & 0xF) for x in filtered]
    pattern_cycle = list(itertools.cycle([1, 0, 1]))[:len(nibbles)]
    correlation = sum(1 for a, b in zip(nibbles, pattern_cycle) if a % 3 == b)

    # Distractor: unused complex structure
    diagnostics_log = {
        'raw_stats': {'mean': mean_val, 'variance': variance_proxy},
        'fft_approx': [abs(x - 128) for x in seq],
        'checksum': sum(seq) % 1024
    }

    # Actual key computation buried among noise
    adjusted_sum = sum(nibbles[i] * (i + 1) for i in range(len(nibbles)))
    return adjusted_sum

# Threshold calibration using conditional expression
base_threshold = lambda x: x // 4 if x > 100 else x * 2

# Misleading auxiliary map (not fully used)
auxiliary_map = {
    'level_a': lambda v: v ** 0.5,
    'level_b': lambda v: v % 128,
    'debug_mode': lambda v: v & 0x7F
}

# Main diagnostic processor
def process_metrics(signature, thresholds):
    # Unpack using destructuring
    core_signal, aux_signal = signature[:4], signature[4:]

    # Irrelevant unpacking and reassignment
    a, b, c, d = core_signal
    temp_vals = [d, c, b, a]  # shuffled order — unused

    # Conditional expression with red herring branch
    scaling_factor = 1.5 if sum(aux_signal) < 300 else 0.8

    # Real calculation: weighted XOR shift
    weighted = 0
    for i, val in enumerate(core_signal):
        weighted ^= (val * (i + 1)) << 1

    # Critical operation hidden in lambda chain
    transform = lambda x: thresholds['primary'](x)
    intermediate = transform(weighted % 256)

    # Final adjustment using average of specific indices
    adjustment = sum(aux_signal[i] for i in [0, 2]) // 2
    result = intermediate - adjustment

    # Decoy mutation of data structure
    decoy_list = [[i, val] for i, val in enumerate(signature)]
    for row in decoy_list:
        row.append(row[0] * row[1])

    return result

# Orchestration block with setup and execution
if __name__ == '__main__':
    # Generate real input data
    raw_readings = generate_sensor_readings()

    # Unused entropy computation (distraction)
    # entropy_score = compute_entropy(raw_readings)

    # Extract health signature via analyze_pattern
    health_signature = analyze_pattern(raw_readings)

    # Build threshold map — only 'primary' is used
    threshold_map = {
        'primary': base_threshold,
        'secondary': lambda x: x + 10,
        'diagnostic': lambda x: x & 0xFF
    }

    # Dead comparison with no effect
    if len(raw_readings) == 5:
        consistency_flag = True
        # Nested useless block
        if consistency_flag:
            normalized = [x / 255.0 for x in raw_readings]
            # This entire branch does nothing

    # Key assignment: final_diagnostic depends on prior logic
    final_diagnostic = process_metrics(health_signature, threshold_map)

    # Output the required result
    print(f"Result: {final_diagnostic}")