def preprocess_waveform(data, factor):
    return [x * factor for x in data if x > 0]


def evaluate_coherence(seq):
    paired = zip(seq, seq[1:])
    return sum(a & b for a, b in paired)

# Irrelevant helper (dead function - red herring)
def calculate_entropy(arr):
    from math import log
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    total = len(arr)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Unused transformation chain (distractor)
baseline_offset = 17
scaling_curve = [i**2 for i in range(8)]
filtered_readings = list(map(lambda x: x + baseline_offset, scaling_curve))

# Core signal components
pattern_buffer = [5, -3, 8, 2, -1, 7, 4]
reference_mask = {1, 2, 4, 8, 16}

# Misleading intermediate computation (no impact on final result)
temp_analysis = []
for idx, val in enumerate(pattern_buffer):
    if idx % 2 == 0 and val in reference_mask:
        temp_analysis.append(val)

# Threshold configuration (relevant)
threshold_map = {
    'low': 3,
    'high': 7,
    'critical': 10
}

# Auxiliary state tracker (partially relevant)
status_flags = []
for v in pattern_buffer:
    if v < threshold_map['low']:
        status_flags.append('L')
    elif v < threshold_map['high']:
        status_flags.append('M')
    else:
        status_flags.append('H')

# Complex conditional with distractors
aggregate_score = 0
if len(pattern_buffer) > 5:
    shifted = [x >> 1 for x in pattern_buffer]  # Bit manipulation (red herring)
    inverted = [~x for x in shifted]            # More distraction

    # Real logic begins here
    cleaned = preprocess_waveform(pattern_buffer, 1)
    coherence = evaluate_coherence(cleaned)

    # Secondary analysis path (some used, some not)
    magnitude_sum = sum(abs(x) for x in pattern_buffer)
    peak_count = sum(1 for x in pattern_buffer if x >= threshold_map['high'])

    # Another dead-end branch
    if magnitude_sum > 100:
        dummy = [x ** 0.5 for x in pattern_buffer]
        aggregate_score += len(dummy)

    # Actual key computation
    valid_highs = [v for v in pattern_buffer if v >= threshold_map['high']]
    adjusted_peaks = [v - threshold_map['low'] for v in valid_highs]

    # Cross-structure dependency
    flag_transitions = 0
    for i in range(len(status_flags) - 1):
        if status_flags[i] != status_flags[i+1]:
            flag_transitions += 1

    # Final diagnostic formula (uses multiple concepts)
    base_metric = len(adjusted_peaks) * coherence
    penalty = flag_transitions // 2
    bonus = 5 if len(valid_highs) >= 3 else 0

    # Critical assignment
    final_diagnostic = base_metric - penalty + bonus

# Extraneous post-processing (irrelevant)
if final_diagnostic > 20:
    normalized = final_diagnostic / 100.0
    classification = 'STABLE'
else:
    normalized = final_diagnostic / 50.0
    classification = 'MONITORING'

print(f"Result: {final_diagnostic}")