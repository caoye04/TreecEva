def analyze_sensor_data(raw_readings, threshold=0.75):
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in normalized if x > threshold]
    
    # Irrelevant preprocessing: frequency analysis (dead path)
    fft_peaks = []
    for i in range(len(normalized)):
        if i % 3 == 0 and normalized[i] > 0.5:
            fft_peaks.append(i * 0.1)

    # Distractor: unused transformation chain
    transformed = []
    scaling_factor = 1.8
    offset = -0.3
    for val in normalized:
        transformed.append(round(val * scaling_factor + offset, 2))

    # Actual relevant logic begins here
    segments = []
    current_seg = []
    for x in filtered:
        if x > threshold:
            current_seg.append(x)
        else:
            if len(current_seg) > 0:
                segments.append(current_seg)
                current_seg = []
    if current_seg:
        segments.append(current_seg)

    # Misleading intermediate: entropy-like calc (unused)
    import math
    shannon_entropy = 0.0
    for s in segments:
        prob = len(s) / len(filtered) if filtered else 0
        if prob > 0:
            shannon_entropy -= prob * math.log(prob)

    # Core data structure with cross-reference
    stats = {}
    for i, seg in enumerate(segments):
        stats[f'seg_{i}'] = {
            'length': len(seg),
            'avg': sum(seg) / len(seg),
            'peak': max(seg)
        }
    
    # Conditional expression usage (required feature)
    active_segments = [k for k, v in stats.items() if v['length'] > 1] if segments else []

    # Slice-based processing (required feature)
    time_window = raw_readings[::2]  # every other reading
    window_stats = sum(time_window) / len(time_window) if time_window else 0

    # Decoy metric with plausible name
    coherence_score = 0
    for i in range(1, len(filtered)):
        coherence_score += abs(filtered[i] - filtered[i-1])
    coherence_score = round(1 / (coherence_score + 1e-5), 3)

    # Critical computation path
    aggregate_metrics = []
    for key in sorted(stats.keys()):
        entry = stats[key]
        # Composite calculation: mix of arithmetic and logic
        metric = entry['avg'] * entry['length']
        if entry['peak'] > 0.9:
            metric *= 1.25
        aggregate_metrics.append(round(metric, 4))
    
    # Dead code: post-processing that isn't used
    if aggregate_metrics:
        smoothed = [aggregate_metrics[0]]
        for i in range(1, len(aggregate_metrics)):
            smoothed.append(0.7 * smoothed[-1] + 0.3 * aggregate_metrics[i])

    # Key statement - answer depends on this
    final_diagnostic = aggregate_metrics[-1] + len(active_segments)
    
    # Final red herring: alternate result based on irrelevant condition
    if len(raw_readings) % 7 == 0:
        final_diagnostic = int(sum(aggregate_metrics))

    print(f"Result: {final_diagnostic}")

# Simulate sensor input (deterministic)
data_stream = [120, 145, 160, 162, 148, 130, 175, 180, 165, 150, 190, 195, 188]
analyze_sensor_data(data_stream, threshold=0.77)