def analyze_sequence(data, config):
    # Irrelevant transformation chain
    temp_a = [x ** 2 for x in data if x % 3 == 0]
    temp_b = [x for x in data if x > config.get('limit', 50)]
    unused_shadow = sum(temp_a) - len(temp_b)

    # Distractor: complex but unused calculation
    decoy_score = 0
    for i, val in enumerate(temp_b):
        if i % 2 == 0:
            decoy_score += val >> 2
    decoy_score = max(decoy_score, 100) if decoy_score > 0 else 0

    # Relevant path begins: extract critical timestamps
    timestamps = [x for x in data if x < 0]
    abs_timestamps = [abs(t) for t in timestamps]
    normalized = [t % 100 for t in abs_timestamps]

    # Misleading intermediate with similar name
    diagnostic_sum = sum(normalized) * config.get('multiplier', 1)

    # Real computation hidden among noise
    valid_markers = [n for n in normalized if n in config['markers']]
    marker_indices = [i for i, n in enumerate(valid_markers)]
    index_map = dict(zip(marker_indices, valid_markers))

    # Core logic disguised as post-processing
    if len(index_map) >= 2:
        sorted_pairs = sorted(index_map.items())
        diffs = [sorted_pairs[i+1][1] - sorted_pairs[i][1] for i in range(len(sorted_pairs)-1)]
        avg_diff = sum(diffs) / len(diffs) if diffs else 0
        final_diagnostic = int(avg_diff * 1000)
    else:
        final_diagnostic = diagnostic_sum  # Dead end branch

    return final_diagnostic


def process_metrics(entries, thresholds):
    # Unused preprocessing red herring
    filtered = []
    for e in entries:
        if 'error' in e and e['error'] > thresholds['err_cap']:
            continue
        filtered.append(e)

    # Decoy aggregation
    error_total = sum(e.get('error', 0) for e in filtered)
    weight_seq = [e['value'] * e['weight'] for e in filtered]
    weighted_avg = sum(weight_seq) / len(weight_seq) if weight_seq else 0

    # Hidden relevant data extraction
    raw_values = [e['value'] for e in entries if e['active']]
    capped_values = [min(v, thresholds['cap']) for v in raw_values]
    adjusted = [v + thresholds['bias'] for v in capped_values]

    # Critical distractor: looks important but unused
    stats_snapshot = {
        'max': max(adjusted),
        'min': min(adjusted),
        'range': max(adjusted) - min(adjusted)
    }

    # Real signal buried in list operations
    paired = list(zip(capped_values, adjusted))
    deltas = [a - c for c, a in paired]
    net_drift = sum(deltas) / len(deltas) if deltas else 0

    # Final decision obscured by conditional
    if net_drift > thresholds['tolerance']:
        result_code = int(net_drift * 100)
    else:
        result_code = len([d for d in deltas if d > 0]) * 100  # Used path

    return result_code

# Main execution block
if __name__ == '__main__':
    log_entries = [
        {'value': 15, 'weight': 2.0, 'error': 3, 'active': True},
        {'value': 25, 'weight': 1.5, 'error': 8, 'active': True},
        {'value': 40, 'weight': 1.0, 'error': 1, 'active': False},
        {'value': 35, 'weight': 2.5, 'error': 12, 'active': True},
        {'value': 10, 'weight': 1.8, 'error': 5, 'active': True}
    ]

    system_thresholds = {
        'cap': 30,
        'bias': 5,
        'tolerance': 7.5,
        'err_cap': 10,
        'markers': [10, 15, 20, 25]
    }

    # Unused legacy variables (distractors)
    baseline_ref = 987
    calibration_offset = -42
    temporal_weighting = [0.1, 0.3, 0.6]

    # Key call that produces the answer
    final_diagnostic = process_metrics(log_entries, system_thresholds)

    # Print required output
    print(f"Result: {final_diagnostic}")