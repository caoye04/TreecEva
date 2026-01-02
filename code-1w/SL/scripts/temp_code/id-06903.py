def analyze_sensor_data(raw_readings, threshold=100):
    # Irrelevant preprocessing: normalize signal (not used in final path)
    normalized = [x / max(raw_readings) * 100 for x in raw_readings]
    filtered = [x for x in raw_readings if x > threshold]

    # Distractor: complex frequency analysis (dead code path)
    def compute_harmonic_distortion(data):
        return sum(x ** 2 for x in data) / len(data) if data else 0

    freq_analysis = compute_harmonic_distortion(filtered)  # Unused
    spike_count = 0
    trend_segments = []

    # Real logic: detect rising trends above threshold
    for i, val in enumerate(filtered[:-2]):
        if filtered[i+1] > val and filtered[i+2] > filtered[i+1]:
            spike_count += 1
            trend_segments.append((i, filtered[i:i+3]))

    # Distractor: secondary metric with no impact
    avg_spike_rise = sum(filtered[i+2] - filtered[i] for i, _ in trend_segments) / spike_count if spike_count else 0

    # Core transformation: apply exponential decay to emphasize recent spikes
    decay_weights = [0.5 ** (len(trend_segments) - i) for i in range(len(trend_segments))]
    weighted_trend_sum = sum(len(segment[1]) * weight for segment, weight in zip(trend_segments, decay_weights))

    # Additional red herring: sort irrelevant permutations
    from itertools import permutations
    perm_sample = list(permutations([1, 2, 3]))[:1]  # Computationally wasteful

    # Simulate calibration offset (unused alternative)
    baseline_shift = sum(normalized[::3]) / len(normalized[::3]) if len(normalized) > 0 else 0

    # Critical data structure: multi-stage diagnostics
    diagnostics = []
    temp_buffer = []
    for idx, (pos, seg) in enumerate(trend_segments):
        # Embedded conditional with partial relevance
        if len(seg) == 3 and seg[2] > seg[0] * 1.5:
            temp_buffer.append(seg[2] - seg[0])
        if len(temp_buffer) >= 2:
            diagnostics.append(sum(temp_buffer) // len(temp_buffer))
            temp_buffer = []

    if temp_buffer:
        diagnostics.append(sum(temp_buffer))

    # Introduce decoy adjustment based on modular pattern
    decoy_adjustment = 0
    for d in diagnostics:
        if d % 7 == 0:
            decoy_adjustment += 5
        elif d % 4 == 0:
            decoy_adjustment -= 3

    # Actual correction factor derived from index patterns
    indices = [seg[0] for seg in trend_segments]
    index_gaps = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    correction_factor = sum(gap * (i+1) for i, gap in enumerate(index_gaps)) if index_gaps else 17

    # Final aggregation with distractor-influenced name
    aggregate_metrics = [sum(diagnostics), len(diagnostics) * 2, weighted_trend_sum, freq_analysis]
    
    # Key statement
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Output result as required
    print(f"Result: {final_diagnostic}")

# Execution entry point with realistic sensor data
sensor_input = [95, 102, 110, 108, 130, 145, 160, 112, 120, 128, 140, 155, 170, 185]
analyze_sensor_data(sensor_input)