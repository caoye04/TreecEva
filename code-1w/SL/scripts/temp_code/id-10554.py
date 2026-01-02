def analyze_risk_profile(data_stream, sensitivity_factor=0.87):
    # Irrelevant preprocessing (red herring)
    temp_buffer = [x ** 0.5 for x in data_stream if x > 5]
    debug_snapshot = list(enumerate(temp_buffer))

    # Core data transformation with distractors
    raw_metrics = [x * sensitivity_factor for x in data_stream]
    filtered_data = [x for x in raw_metrics if x > 10]

    # Unused but plausible dead-end function (decoy)
    def compute_shadow_index(seq):
        return sum(x % 3 for x in seq) * 0.1

    # Actual signal extraction
    signal_peaks = []
    for i, val in enumerate(filtered_data):
        if i == 0:
            continue
        if filtered_data[i] > filtered_data[i-1] * 1.1:
            signal_peaks.append(val)

    # Misleading intermediate calculation (distractor)
    average_peak = sum(signal_peaks) / len(signal_peaks) if signal_peaks else 0
    peak_variance = sum((x - average_peak)**2 for x in signal_peaks) if signal_peaks else 0

    # Key weights derived from combinatorics of positions
    indices = list(range(len(signal_peaks)))
    paired_offsets = list(zip(indices[:-1], indices[1:]))
    deltas = [b - a for a, b in paired_offsets]

    weight_map = {}
    for idx, delta in enumerate(deltas):
        if delta > 1:
            weight_map[idx] = delta * 1.5
        else:
            weight_map[idx] = delta * 0.75

    # Dummy dictionary for distraction (irrelevant)
    status_labels = {0: 'idle', 1: 'active', 2: 'pending', 3: 'archived'}
    metadata_log = {k: 'processed' for k in range(len(data_stream))}

    # Critical path: construct final weights using min/max logic and offset sums
    base_weights = [weight_map.get(i, 1.0) for i in range(len(deltas) + 1)]
    adjusted_weights = [w * (1 + sensitivity_factor) for w in base_weights]

    cumulative_shift = 0
    final_weights = []
    for w in adjusted_weights:
        cumulative_shift += w
        if cumulative_shift > 5:
            final_weights.append(cumulative_shift)
            cumulative_shift = 0  # Reset after threshold

    # Secondary reset logic to obscure control flow
    if len(final_weights) < 3:
        final_weights.extend([1.1, 2.2, 3.3])

    # Impact level determined by conditional nesting (key logic)
    impact_level = 0
    if len(signal_peaks) > 4:
        impact_level += 2
        if average_peak > 15:
            impact_level += 1
        if deltas.count(1) >= 2:
            impact_level += 1
    elif len(signal_peaks) > 2:
        impact_level += 1
        if sensitivity_factor > 0.8:
            impact_level += 1
    else:
        impact_level = 0

    # This line contains the key execution point
    threshold_balance = final_weights[impact_level]

    # Red herring print statements (never executed)
    # print(f'Debug: shadow_index={compute_shadow_index(raw_metrics)}')
    # print(f'Metadata entries: {len(metadata_log)}')

    # Correct output
    print(f'Result: {threshold_balance}')

# Input data
input_stream = [12, 15, 9, 23, 25, 27, 8, 31, 33, 14, 40]

# Execute
analyze_risk_profile(input_stream, sensitivity_factor=0.92)