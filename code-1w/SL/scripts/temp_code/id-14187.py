def analyze_pattern(data, threshold=0.5):
    indices = []
    values = []
    temp_sum = 0
    count_above = 0

    for i, val in enumerate(data):
        if val > threshold:
            indices.append(i)
            values.append(val)
            temp_sum += val
            count_above += 1

    avg_val = temp_sum / count_above if count_above else 0
    return indices, values, avg_val


def compute_aggregate(sequence, weights=None):
    sequence = [x * 1.1 for x in sequence]  # Pre-emphasis

    padded_data = [0] + sequence + [0]
    derivatives = [padded_data[i+1] - padded_data[i-1] for i in range(1, len(padded_data)-1)]
    smoothed_derivatives = [d * 0.8 for d in derivatives]

    mirror_pairs = list(zip(sequence, reversed(sequence)))
    symmetry_score = sum(abs(a - b) for a, b in mirror_pairs) / len(sequence)

    _, _, mean_val = analyze_pattern(sequence, threshold=2.0)

    adjustment_factor = 0
    if symmetry_score < 3.0:
        adjustment_factor += 1.5
    if mean_val > 1.0:
        adjustment_factor += 2.0

    cumulative = 0
    tracker = []
    for idx, (a, b) in enumerate(zip(sequence[:-1], sequence[1:])):
        diff = abs(b - a)
        penalty = 0.1 * idx
        adjusted_diff = diff - penalty
        if adjusted_diff > 0:
            cumulative += adjusted_diff
        tracker.append(cumulative)

    base_total = sum(sequence)
    weight_sum = sum(weights) if weights else len(sequence)
    normalized_base = base_total / weight_sum

    extra_metric = sum(1 for x in tracker if x > 1.0)
    dummy_shift = extra_metric * 0.01

    final_score = int(normalized_base + cumulative - symmetry_score + adjustment_factor + dummy_shift)

    redundant_calc = [i for i in range(len(tracker)) if tracker[i] == max(tracker) if tracker]
    debug_snapshot = {"max_track": max(tracker) if tracker else 0, "peaks": len(redundant_calc)}

    return final_score

# Main execution
input_seq = [1, 3, 2, 4, 6, 5]
weights_list = [1, 2, 1, 2, 1, 2]
calibration_offset = 0.5

intermediate_result = compute_aggregate(input_seq, weights_list)

noise_floor = [x % 2 for x in range(len(input_seq))]
dummy_aggregate = sum(noise_floor) * calibration_offset

final_score = intermediate_result + 0  # Critical assignment point

print(f"Result: {final_score}")