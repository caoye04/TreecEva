import itertools

def analyze_frequency(stream):
    freq_map = {}
    for item in stream:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

def compute_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 6)

def filter_outliers(seq):
    mean_val = sum(seq) / len(seq)
    deviances = [(x - mean_val) ** 2 for x in seq]
    variance = sum(deviances) / len(deviances)
    std_dev = variance ** 0.5
    return [x for x in seq if abs(x - mean_val) <= 2 * std_dev]

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def shift_cipher(text, key):
    # Irrelevant distraction: string cipher function not used in main logic
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c
    return result

def accumulate_pairs(iterable):
    # Unused helper – red herring
    acc = 0
    pairs = []
    for i, val in enumerate(iterable):
        acc += val
        if i % 2 == 1:
            pairs.append((iterable[i-1], val, acc))
    return pairs

def calculate_final_score(raw_data):
    # Step 1: Transform data using zip and enumerate
    indexed = list(enumerate(raw_data))
    shifted = [x[1] + (x[0] * 0.1) for x in indexed]

    # Step 2: Use itertools to group consecutive similar-magnitude values
    grouped = []
    for k, g in itertools.groupby(shifted, key=lambda x: x // 10):
        group = list(g)
        grouped.append(group)

    # Step 3: Extract sizes and compute frequency distribution
    sizes = [len(g) for g in grouped]
    freq_analysis = analyze_frequency(sizes)

    # Step 4: Compute entropy of group sizes (important)
    entropy_metric = compute_entropy(freq_analysis.values())

    # Step 5: Filter groups with size > 1 (distraction)
    large_groups = [g for g in grouped if len(g) > 1]
    flattened_large = [item for sublist in large_groups for item in sublist]

    # Step 6: Find peaks in flattened large groups (misleading path)
    peak_values = extract_peaks(flattened_large)

    # Step 7: Apply outlier filtering on original transformed data (partially relevant)
    cleaned = filter_outliers(shifted)

    # Step 8: Calculate weighted sum using position (key step)
    weighted_sum = 0
    for idx, value in enumerate(cleaned):
        weight = 1 + (idx * 0.05)
        weighted_sum += value * weight

    # Step 9: Combine with entropy metric (crucial)
    composite = weighted_sum * entropy_metric

    # Step 10: Apply arbitrary scaling based on length parity (subtle but deterministic)
    scale_factor = 1.5 if len(cleaned) % 2 == 0 else 0.8

    # Step 11: Add bonus if any group has exactly 3 elements (distractor check)
    bonus = 100 if any(len(g) == 3 for g in grouped) else 0  # Triggered

    # Step 12: Final score calculation
    final_score = (composite * scale_factor) + bonus

    # Decoy assignments (dead code)
    debug_trace = {"steps": 12, "peak_count": len(peak_values), "cipher_test": shift_cipher("hello", 3)}
    temp_result = accumulate_pairs([1, 2, 3, 4])

    return int(round(final_score))

# Main execution
if __name__ == '__main__':
    # Simulated sensor data stream (realistic domain: IoT telemetry)
    data_stream = [12, 15, 23, 23, 23, 45, 67, 67, 34, 34, 34, 34, 89, 90, 91, 100, 100]

    # Key statement
    final_score = calculate_final_score(data_stream)

    print(f"Target result: {final_score}")