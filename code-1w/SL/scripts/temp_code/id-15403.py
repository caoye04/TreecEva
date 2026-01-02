import itertools

# Simulated bio-reactor monitoring system with noise filtering and cycle analysis
def analyze_bioreactor_logs(log_series):
    base_threshold = 42
    noise_floor = 17
    peak_ceiling = 88
    correction_factor = 0.93

    # Irrelevant pre-processing: character frequency counting (distractor)
    log_str = ''.join(map(str, log_series))
    char_freq = {}
    for c in log_str:
        char_freq[c] = char_freq.get(c, 0) + 1
    dominant_char = max(char_freq, key=char_freq.get)

    # Misleading intermediate: entropy-like calculation (dead path)
    entropy = 0
    for freq in char_freq.values():
        if freq > 0:
            entropy -= (freq / len(log_str)) * (freq / len(log_str))

    # Real signal processing begins
    normalized = [x - noise_floor for x in log_series if x > noise_floor]
    adjusted = [x * 1.05 if x < peak_ceiling else x * 0.92 for x in normalized]

    # Generate sliding windows of cycles (key data structure)
    window_size = 4
    cycles = []
    for i in range(len(adjusted) - window_size + 1):
        window = adjusted[i:i+window_size]
        cycle_value = sum(window) / window_size
        cycles.append(cycle_value)

    # Bit manipulation red herring: simulate checksum (unused)
    checksum = 0
    for val in cycles:
        truncated = int(val) & 0xFF
        checksum ^= (truncated << 1 | truncated >> 7) & 0xFF

    # Set operations for outlier detection (relevant but indirect)
    high_outliers = {x for x in cycles if x > peak_ceiling * 0.75}
    low_outliers = {x for x in cycles if x < base_threshold * 0.6}
    all_outliers = high_outliers.union(low_outliers)

    # Critical filtering logic (target execution point)
    filtered_cycles = []
    for idx, val in enumerate(cycles):
        if val not in all_outliers and idx % 2 == 0:
            # Additional filter based on modular arithmetic pattern
            if (int(val) % 7) != (idx % 5):
                filtered_cycles.append(int(val))

    # Decoy statistical calculations (irrelevant)
    mean_filtered = sum(filtered_cycles) / len(filtered_cycles) if filtered_cycles else 0
    variance_proxy = sum((x - mean_filtered) ** 2 for x in filtered_cycles) / len(filtered_cycles) if filtered_cycles else 0

    # Key assignment statement - target of question
    filtration_score = sum(filtered_cycles) * correction_factor

    # Unused recursive function (heavy distractor)
    def recursive_denoise(arr, depth=0):
        if depth >= 3 or len(arr) < 2:
            return arr[0] if arr else 0
        split_idx = len(arr) // 2
        left = recursive_denoise(arr[:split_idx], depth + 1)
        right = recursive_denoise(arr[split_idx:], depth + 1)
        return (left + right) // 2 + depth

    # Dead code path with tuple unpacking decoy
    if len(filtered_cycles) > 100:
        head, *middle, tail = filtered_cycles
        backup_score = (head + tail) * 0.5

    # Linear search for rare pattern (never triggered in practice)
    rare_pattern_count = 0
    for i in range(len(log_series) - 2):
        if log_series[i] == dominant_char and log_series[i+1] == dominant_char:
            rare_pattern_count += 1

    # Final output (only this matters)
    print(f"Result: {filtration_score}")
    return filtration_score

# Generate deterministic input using itertools
base_pattern = [23, 45, 67, 89, 34, 56, 78, 91]
signal_extensions = list(itertools.chain.from_iterable([base_pattern, reversed(base_pattern)]))
expanded_log = [x + (i % 5) for i, x in enumerate(signal_extensions * 2)]

# Execute with realistic data
result = analyze_bioreactor_logs(expanded_log)