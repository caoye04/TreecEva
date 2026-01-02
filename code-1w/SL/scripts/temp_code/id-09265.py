import math

# System calibration constants (some are decoys)
calibration_offset = 17.3
timing_factor = 0.86
irrelevant_constant_A = 42.0
irrelevant_constant_B = 256.0
system_threshold = 91

# Signal processing setup
def generate_baseline(n):
    return [i * i % 19 for i in range(1, n+1)]

def filter_anomalies(signal_list, threshold):
    filtered = []
    anomalies_detected = 0
    for val in signal_list:
        if val > threshold:
            anomalies_detected += 1
        else:
            filtered.append(val)
    # Dead code path — never executed due to logic
    if anomalies_detected < 0:
        return [], 0
    return filtered, anomalies_detected

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Misleading auxiliary function — looks important but unused
def decrypt_sequence(seq, key):
    return [x ^ key for x in seq]

# Another red herring: checksum that is computed but not used
def calculate_legacy_checksum(arr):
    checksum = 0
    for i, x in enumerate(arr):
        checksum += (x + i) * 3 % 7
    return checksum * 2

# Core analysis with set operations and recursion
def detect_cycles(pattern):
    seen = set()
    cycle_count = 0
    start_idx = {}
    for idx, val in enumerate(pattern):
        if val in seen:
            if val in start_idx and idx - start_idx[val] > 1:
                cycle_count += 1
            else:
                start_idx[val] = idx
        else:
            seen.add(val)
    return cycle_count

def recursive_combinations(n, depth=0):
    if depth >= 3 or n <= 1:
        return 1
    return recursive_combinations(n-2, depth+1) + recursive_combinations(n//3, depth+1)

def analyze_pattern(signals, key):
    # Step 1: Use set difference to isolate unexpected signals
    base_template = set(generate_baseline(15))
    signal_set = set(signals)
    unexpected = signal_set - base_template
    expected_count = len(signal_set.intersection(base_template))

    # Step 2: Filter signals using threshold (with decoy variables)
    filtered_signals, anomaly_count = filter_anomalies(signals, system_threshold)
    temp_diagnostic = len(filtered_signals) * 3 + anomaly_count

    # Step 3: Compute entropy of filtered distribution
    entropy_score = compute_entropy(filtered_signals) if filtered_signals else 0.0

    # Step 4: Detect repeating patterns via cycles
    cycle_detection = detect_cycles(filtered_signals)

    # Step 5: Use recursive combinatorics (depends on key)
    combinatoric_load = recursive_combinations(key)

    # Step 6: Simulate legacy system check (dead computation - result unused)
    fake_checksum = calculate_legacy_checksum(filtered_signals)
    deprecated_flag = False
    if fake_checksum > 100:
        deprecated_flag = True  # Never actually affects anything

    # Step 7: Apply bit manipulation mask (distractor math)
    masked_entropy = int(entropy_score * 100) & 0xFF

    # Step 8: Combine multiple metrics into final diagnostic
    # Note: Only some components contribute meaningfully
    raw_score = (
        len(unexpected) * 1000 +
        expected_count * 100 +
        cycle_detection * 10 +
        combinatoric_load
    )

    # Final adjustment based on key and masked value (only this line matters)
    final_score = raw_score - masked_entropy

    return final_score

# Data initialization
raw_input_stream = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 17, 8, 5]
system_key = 7

# Irrelevant pre-processing steps
decoy_signal = [x ^ 3 for x in raw_input_stream if x % 4 == 0]
baseline_diagnostic = sum(decoy_signal) / len(decoy_signal) if decoy_signal else 0

# Actual relevant processing
collected_signals = [x for x in raw_input_stream if x < 150]  # Filter extreme values

# Key execution point
final_diagnostic = analyze_pattern(collected_signals, system_key)

print(f"Target result: {final_diagnostic}")