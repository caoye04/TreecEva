def analyze_segments(signal, threshold=0.5):
    segments = []
    start = None
    for i, val in enumerate(signal):
        if val > threshold and start is None:
            start = i
        elif val <= threshold and start is not None:
            segments.append((start, i))
            start = None
    if start is not None:
        segments.append((start, len(signal)))
    return segments


def filter_noise(data, window=3):
    smoothed = [0] * len(data)
    for i in range(len(data)):
        lower = max(0, i - window // 2)
        upper = min(len(data), i + window // 2 + 1)
        smoothed[i] = sum(data[lower:upper]) / (upper - lower)
    return smoothed


def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)


def calculate_final_score(data):
    # Misleading pre-processing steps
    temp_state = [x ** 0.5 for x in data if x > 0]
    offset_correction = sum(temp_state) / len(temp_state) if temp_state else 0
    adjusted = [x + offset_correction for x in data]

    # Real processing begins
    binary_flags = [1 if x > 0.8 else 0 for x in adjusted]
    transitions = 0
    for i in range(1, len(binary_flags)):
        if binary_flags[i] != binary_flags[i-1]:
            transitions += 1

    # Use of slicing and zip to correlate with shifted version
    paired = list(zip(binary_flags[:-1], binary_flags[1:]))
    change_pairs = [(a, b) for a, b in paired if a != b]
    
    # Additional irrelevant computation
    dummy_matrix = [[i * j for j in range(3)] for i in range(3)]
    trace_sum = sum(dummy_matrix[i][i] for i in range(3))  # Not used later

    # Core logic: score based on modular patterns and transition density
    pattern_cycle = [binary_flags[i % len(binary_flags)] for i in range(len(binary_flags) * 2)]
    mod_counts = [0] * 5
    for idx, val in enumerate(pattern_cycle):
        if val == 1:
            mod_counts[idx % 5] += 1

    peak_mod_group = max(mod_counts) % 4  # Distraction

    # Actual contribution to final score
    base_score = transitions * 17
    entropy_proxy = len(change_pairs) * 3.1416
    noise_mask = [x for x in adjusted if x < 1.0]
    suppression_factor = len(noise_mask) % 7

    # Final computation
    final_score = base_score - suppression_factor + peak_mod_group
    return int(final_score)

# Simulated sensor signal data
raw_signal = [0.1, 0.9, 0.85, 0.2, 0.3, 0.95, 0.75, 0.1, 0.05, 0.88, 0.92]

# Irrelevant preprocessing chain
filtered_signal = filter_noise(raw_signal, window=3)
denoised_log = [round(x, 2) for x in filtered_signal if x > 0.4]

# Segment detection (partially relevant)
segments = analyze_segments(filtered_signal, threshold=0.4)
segment_lengths = [end - start for start, end in segments]

# Main data used in calculation
processed_data = [round(x, 2) for x in filtered_signal]

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")