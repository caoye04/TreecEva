def analyze_pattern(sequence, threshold=0.75):
    # Irrelevant statistical analysis (dead path)
    mean_val = sum(sequence) / len(sequence)
    variance = sum((x - mean_val) ** 2 for x in sequence) / len(sequence)
    stdev = variance ** 0.5
    normalized = [(x - mean_val) / stdev for x in sequence]

    # Distractor: unused transformation
    inverted = [round(1 / (1 + x), 3) for x in sequence if x > 0]

    # Real logic begins: detect rising patterns above threshold
    signal_peaks = []
    for i in range(1, len(sequence) - 1):
        if sequence[i] > threshold and sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
            signal_peaks.append(i)

    # Secondary distractor: entropy calculation (unused)
    from math import log2
    counts = {}
    for x in sequence:
        rounded = int(x * 10)
        counts[rounded] = counts.get(rounded, 0) + 1
    entropy = -sum((count / len(sequence)) * log2(count / len(sequence)) for count in counts.values())

    # Real logic: compute weighted position score only on peaks
    weights = {i: sequence[i] * (i + 1) for i in signal_peaks}
    if not weights:
        return 0

    # Use dictionary and slicing to derive intermediate result
    sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
    top_slice = sorted_weights[:len(sorted_weights)//2 + 1]  # Take top half

    # Extract indices and apply XOR folding
    indices = [index for index, _ in top_slice]
    folded_index = 0
    for idx in indices:
        folded_index ^= idx  # Bitwise XOR accumulation

    # Compute harmonic adjustment using string-based precision control
    precision_tag = "harm_adj_4"
    decimal_places = int(precision_tag[-1])  # Extract '4' from string
    harmonic_sum = sum(1 / (i + 1) for i in range(folded_index) if i < folded_index)
    adjusted = round(harmonic_sum, decimal_places)

    # Final aggregation with min/max guardrails
    raw_magnitude = max(adjusted, 0.1) * min(len(signal_peaks) * 100, 500)
    return int(raw_magnitude)


def compute_aggregate(data_stream):
    # Distractor: complex unpacking with irrelevant components
    header, *payload, footer = data_stream
    meta_tags = {'init': header, 'term': footer}
    processed_tags = {k: v % 7 for k, v in meta_tags.items() if isinstance(v, int)}

    # Real processing: filter valid signal segments
    segments = []
    temp_segment = []
    for val in payload:
        if val < 0:
            if len(temp_segment) >= 3:
                segments.append(temp_segment)
            temp_segment = []
        else:
            temp_segment.append(val / 100.0)
    if temp_segment and len(temp_segment) >= 3:
        segments.append(temp_segment)

    # Distractor: unused segment compression via string join/split
    compressed = [''.join(f'{int(x*100):02d}' for x in seg) for seg in segments]
    recovered = [[int(s[i:i+2]) / 100 for i in range(0, len(s), 2)] for s in compressed]

    # Real logic: score each segment and combine
    scores = []
    for seg in segments:
        score = analyze_pattern(seg, threshold=0.5)
        scores.append(score)

    # Aggregate final score using bitwise and arithmetic combo
    base_total = sum(scores)
    modifier = len(scores) & 7  # Bitwise mask
    enhanced_total = base_total + (modifier * 17)

    # Apply final bounds and rounding down
    clamped = min(max(enhanced_total, 10), 9999)
    return clamped

# Main execution with decoy inputs and red herring variables
raw_input_stream = [15, 23, 88, 91, 45, -1, 76, 82, 95, 67, 54, -1, 33, 41, 50, 60, 70, -1, 12]
decoy_matrix = [[i * j for j in range(5)] for i in range(4)]  # Unused matrix computation
auxiliary_map = {x: x ** 2 for x in range(10) if x % 3 == 0}  # Dead dictionary

# Key statement
final_score = compute_aggregate(raw_input_stream)
Result: {final_score}