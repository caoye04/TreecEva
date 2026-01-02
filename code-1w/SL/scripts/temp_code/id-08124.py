def analyze_signal_pattern(raw_data, threshold=0.75):
    # Irrelevant preprocessing: character frequency analysis (dead end)
    char_freq = {}
    for c in 'synthetic_monitoring_frame':
        char_freq[c] = char_freq.get(c, 0) + 1
    entropy_approx = sum([v * v for v in char_freq.values()]) / len(char_freq)

    # Real computation begins: transform raw signal
    filtered = [x for x in raw_data if x > threshold]
    indices = [i for i, x in enumerate(raw_data) if x > threshold]
    paired_metrics = list(zip(filtered, indices))

    # Misleading intermediate: complex but unused transformation
    def decoy_transform(seq):
        return [seq[i] ** 2 - seq[i-1] for i in range(1, len(seq))] + [seq[0]]
    
    transformed = decoy_transform(raw_data)  # Computed but not used

    # Actual relevant logic: counting valid segments
    segment_count = 0
    segment_values = []
    i = 0
    while i < len(raw_data):
        if raw_data[i] > threshold:
            segment_count += 1
            accumulation = 0
            while i < len(raw_data) and raw_data[i] > threshold:
                accumulation += raw_data[i]
                i += 1
            segment_values.append(accumulation)
        i += 1

    # Secondary red herring: unused min/max tree
    max_tree = [max(segment_values[i:i+2]) if i+1 < len(segment_values) else segment_values[i] 
                for i in range(0, len(segment_values), 2)]
    min_tree = [min(segment_values[i:i+2]) if i+1 < len(segment_values) else segment_values[i]
                for i in range(0, len(segment_values), 2)]

    # Core calculation chain
    base_magnitude = sum(segment_values)
    peak_response = max(segment_values) if segment_values else 0
    avg_per_segment = base_magnitude / segment_count if segment_count else 0

    # Conditional expression determining correction factor
    status_flag = 'critical' if len(segment_values) > 3 else 'normal'
    correction_factor = -17.3 if status_flag == 'critical' else 9.4

    # Additional distraction: bitwise manipulation with no impact
    mask = 0b1101
    masked_segments = [s ^ mask & 0b1010 for s in segment_values]
    checksum = sum([(s >> 2) & 0b111 for s in masked_segments])

    # Destructuring assignment (relevant only for syntax diversity)
    first_seg, *middle_segs, last_seg = segment_values if len(segment_values) > 2 else (segment_values[0],) if segment_values else (0,)

    # Key aggregation
    stability_index = (last_seg - first_seg) / peak_response if peak_response else 0
    volatility_score = sum([abs(a - b) for a, b in zip(segment_values, segment_values[1:])])

    # Final determination path
    if segment_count >= 2:
        trend_bias = sum(middle_segs) / len(middle_segs) if middle_segs else 0
        aggregate_score = base_magnitude + trend_bias * 1.5
    else:
        aggregate_score = base_magnitude

    # Critical statement: answer depends on this
    final_diagnostic = aggregate_score + correction_factor

    # Output requirement
    print(f"Result: {final_diagnostic}")

    # Unused trailing logic (dead path)
    if False:
        fallback = 0
        for idx, val in enumerate(zip(max_tree, min_tree)):
            fallback += val[0] - val[1] + idx
        return fallback

    return final_diagnostic

# Input data
input_stream = [0.81, 0.69, 0.92, 0.88, 0.71, 0.95, 0.93, 0.87, 0.76, 0.91]

# Execution
result = analyze_signal_pattern(input_stream)