def analyze_signal_integrity(raw_samples, thresholds):
    base_offset = 17
    temp_buffer = []
    cumulative_power = 0
    spike_count = 0
    noise_floor = sum(raw_samples) / len(raw_samples) if raw_samples else 0
    adjustment_log = {}

    for idx, (sample, thresh) in enumerate(zip(raw_samples, thresholds)):
        adjusted_sample = abs(sample - noise_floor)
        if adjusted_sample > thresh * 1.5:
            spike_count += 1
            temp_buffer.append(adjusted_sample * 0.9)
        elif idx % 3 == 0:
            temp_buffer.append(adjusted_sample * 0.1)
        else:
            cumulative_power += adjusted_sample ** 0.5

    # Irrelevant transformation path (dead logic)
    if len(temp_buffer) > 10:
        transformed = [x * 1.1 for x in temp_buffer if x < 50]
        dummy_metric = sum(transformed) / len(transformed) if transformed else 0
    else:
        dummy_metric = 0
        shadow_accumulator = 0
        for x in temp_buffer:
            shadow_accumulator += x ^ 7  # Bitwise red herring

    # Actual signal metric computation (buried in noise)
    valid_signals = [x for x in temp_buffer if x > 2.0]
    signal_quality = len(valid_signals) / len(raw_samples) if raw_samples else 0
    aggregate_score = cumulative_power * signal_quality

    # Distractor block: unused conditional chain
    if aggregate_score > 100:
        status_flag = 'HIGH'
    elif aggregate_score > 50:
        status_flag = 'MEDIUM'
    else:
        status_flag = 'LOW'
        extra_penalty = 5 if spike_count > 3 else 0  # Unused

    # Core answer calculation — depends on multiple paths
    correction_factor = 0.85 if spike_count % 2 == 1 else 1.15
    offset_value = base_offset - (len(thresholds) % 7)
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Decoy output variables
    diagnostic_summary = {
        'baseline': noise_floor,
        'spikes': spike_count,
        'power': cumulative_power,
        'score': aggregate_score,
        'final': final_diagnostic,
        'dummy': dummy_metric  # Misleading intermediate
    }

    # Only this line matters
    print(f'Result: {final_diagnostic}')

# Input data (deterministic)
signal_data = [23, 15, -8, 44, 12, 67, 33, -12, 40, 29, 55]
thresh_levels = [10, 14, 12, 30, 11, 50, 25, 10, 20, 18, 40]

analyze_signal_integrity(signal_data, thresh_levels)