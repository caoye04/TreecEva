import itertools

# Simulated sensor data processing with noise filtering and pattern analysis
def collect_sensor_readings():
    raw_readings = [127, 63, 191, 31, 223, 15, 255, 0, 111, 77]
    calibrated = [x ^ 128 for x in raw_readings]  # Invert high-bit bias
    filtered = [x for x in calibrated if x > 10]
    return filtered

# Irrelevant auxiliary function – dead code path (red herring)
def legacy_checksum(data):
    acc = 0
    for d in data:
        acc = (acc + d * 3) % 251
    return acc * 2  # Unused result

# Noise injection simulation – appears important but is not used in final logic
def generate_noise_profile(signal):
    base_freq = sum(signal) // len(signal)
    noise = []
    for i in range(len(signal)):
        noise.append((base_freq ^ i) % 100)
    return [n for n in noise if n % 3 == 0]

# Core transformation: extract bit patterns and classify
def transform_signal_sequence(signal):
    binary_profiles = []
    for val in signal:
        ones = bin(val).count('1')
        shifted = (val << 1) % 256
        combined = ones ^ shifted
        binary_profiles.append(combined)
    return binary_profiles

# Threshold engine – only certain pattern densities trigger diagnostic flags
def compute_adaptive_thresholds(data):
    avg = sum(data) / len(data)
    std_dev = (sum((x - avg) ** 2 for x in data) / len(data)) ** 0.5
    return {
        'low': avg - std_dev,
        'medium': avg,
        'high': avg + std_dev,
        'peak': avg + 2 * std_dev
    }

# Misleading statistical summary – looks critical but unused in decision path
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard measure, distractor
    return round(entropy, 4)

# Real-time anomaly flagger – used to pre-filter, but output partially ignored
def detect_anomalies(stream):
    flags = []
    for i, val in enumerate(stream):
        if val > 200 or (i > 0 and stream[i-1] == val):
            flags.append(i)
    return flags or [0]

# Central pattern analyzer – this is where final_diagnostic originates
def analyze_pattern(patterns, limits):
    count_high = sum(1 for p in patterns if p > limits['high'])
    count_mid = sum(1 for p in patterns if limits['medium'] <= p <= limits['high'])
    balance_score = count_mid - (count_high // 2)

    # Critical logic step: cross-reference with cyclic permutations
    cyclic_variants = list(itertools.permutations([patterns[0], patterns[2], patterns[4]], 3))
    valid_cycles = 0
    for cycle in cyclic_variants:
        if cycle[0] < cycle[1] > cycle[2]:  # Peak in middle
            valid_cycles += 1

    # Final computation – combines statistical and combinatorial signals
    base_result = balance_score * 17
    adjusted = base_result + (valid_cycles * 3)

    # Secondary adjustment using min/max spread (real dependency)
    spread = max(patterns) - min(patterns)
    if spread > limits['peak']:
        adjusted += 5

    return adjusted

# Orchestration function with multiple distraction paths
def main_pipeline():
    readings = collect_sensor_readings()           # Step 1: Get raw data
    anomalies = detect_anomalies(readings)         # Step 2: Flag anomalies (partially used)
    cleaned = [readings[i] for i in range(len(readings)) if i not in anomalies]  # Step 3: Filter
    transformed_data = transform_signal_sequence(cleaned)  # Step 4: Transform bits
    
    # Distractor computations (look relevant but aren't used in final answer)
    _ = compute_entropy(transformed_data)
    _ = generate_noise_profile(readings)
    _ = legacy_checksum(readings)
    
    thresholds = compute_adaptive_thresholds(transformed_data)  # Step 5: Compute thresholds
    final_diagnostic = analyze_pattern(transformed_data, thresholds)  # Step 6: Final analysis
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main_pipeline()