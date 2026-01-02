def analyze_sequence(data):
    # Irrelevant transformation: character frequency count (distractor)
    freq = {}
    for char in ''.join(map(str, data)):
        freq[char] = freq.get(char, 0) + 1

    # Dead code path: never executed due to condition (red herring)
    if len(freq) > 100:
        return sum(int(k) * v for k, v in freq.items() if k.isdigit())

    # Real but obscured logic: extract every third element and square them
    processed = [x ** 2 for i, x in enumerate(data) if (i + 1) % 3 == 0]

    # Misleading accumulation with no effect (distractor)
    temp_sum = 0
    for val in processed:
        temp_sum += val * 0.1  # Scaled down, unused later

    return processed


def filter_outliers(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5

    # Useless filtered list (decoy result)
    _ = [x for x in values if abs(x - mean_val) <= 2 * std_dev]

    # Actual output: return sorted unique values above median
    sorted_vals = sorted(set(values))
    median = sorted_vals[len(sorted_vals) // 2]
    return [x for x in sorted_vals if x > median]


def compute_weighted_segments(arr, config):
    # Complex slicing and zipping without immediate purpose (distraction)
    slices = [arr[i:i+4] for i in range(0, len(arr), 4)]
    labels = [f'seg_{j}' for j in range(len(slices))]
    labeled_slices = list(zip(labels, slices))

    # Decoy dictionary construction
    stats = {label: {'sum': sum(sl), 'max': max(sl), 'min': min(sl)} for label, sl in labeled_slices}

    # Real logic hidden among distractions: take last segment, reverse, and scale by config factor
    last_segment = slices[-1]
    reversed_scaled = [config['scale'] * x for x in reversed(last_segment)]

    # Extra computation that looks important but isn't used
    normalized = [round((x - min(reversed_scaled)) / (max(reversed_scaled) - min(reversed_scaled) + 1e-8), 3)
                  for x in reversed_scaled]

    return reversed_scaled


def evaluate_performance(metrics, weights):
    # Initialize multiple irrelevant accumulators (distractors)
    total_impact = 0
    penalty_score = 0
    bonus_tracker = []

    # Fake normalization chain
    normalized_metrics = [(m - min(metrics)) / (max(metrics) - min(metrics) + 1e-6) for m in metrics]
    scaled_fake = [nm * 100 for nm in normalized_metrics]

    # Real scoring logic buried here: dot product with weights, but only on transformed subset
    adjusted_metrics = [m ** 0.5 for m in metrics[::2]]  # Only even-indexed, square-rooted
    weight_slice = weights[:len(adjusted_metrics)]

    # Heavily nested conditional that evaluates to False (misleading branch)
    if len(metrics) > 5 and sum(m > 10 for m in metrics) < 3:
        for i, w in enumerate(weight_slice):
            bonus_tracker.append(adjusted_metrics[i] * w * 0.05)
        total_impact += sum(bonus_tracker)
    else:
        # Actual contribution
        total_impact = sum(a * w for a, w in zip(adjusted_metrics, weight_slice))

    # Final red herring: complex string-based check that doesn’t affect result
    status_flags = ['high' if m > 20 else 'low' for m in metrics]
    flag_summary = ''.join(f[0] for f in status_flags).upper()
    if 'H' in flag_summary:
        temp_flag_score = sum(ord(c) for c in flag_summary) % 7
        penalty_score += temp_flag_score  # But never used!

    return round(total_impact, 6)

# Main execution block
raw_data = [4, 9, 16, 25, 36, 49, 64]
data_analysis = analyze_sequence(raw_data)
filtered_results = filter_outliers(data_analysis)

config_params = {'scale': 0.5, 'offset': 2, 'mode': 'relaxed'}
segment_output = compute_weighted_segments(filtered_results, config_params)

performance_weights = [1.2, 0.8, 1.5, 2.0, 0.7, 1.1, 1.3]
final_metrics = [x + 10 for x in segment_output]  # Augment before evaluation

# Key statement
final_score = evaluate_performance(final_metrics, performance_weights)

print(f"Target result: {final_score}")