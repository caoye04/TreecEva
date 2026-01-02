def analyze_pattern(sequence, threshold):
    count = 0
    for i, val in enumerate(sequence):
        if val > threshold:
            count += 1
            temp_adjust = (i * 2) + val // 4
    return count


def transform_values(data_list):
    transformed = []
    offset = len(data_list) // 2
    for idx, item in enumerate(data_list):
        if idx % 2 == 0:
            transformed.append(item * 3 + offset)
        else:
            transformed.append(item - offset)
    return transformed


def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return round(entropy, 6)


def filter_and_shift(dataset, limit):
    filtered = [x for x in dataset if x < limit]
    shifted = [(x << 1) ^ 3 for x in filtered]
    return shifted


def evaluate_performance(metrics, base):
    adjusted = [m - base for m in metrics]
    positive_count = sum(1 for x in adjusted if x > 0)
    negative_count = sum(1 for x in adjusted if x < 0)
    net_bias = positive_count - negative_count

    if net_bias >= 0:
        scale_factor = 1.5
    else:
        scale_factor = 0.8

    raw_score = sum(adjusted) * scale_factor

    # Distractor: complex transformation with no impact
    dummy_data = [i**2 for i in range(len(metrics))]
    _ = transform_values(dummy_data)
    _ = analyze_pattern(dummy_data, 10)

    # Real computation path
    magnitude = abs(raw_score)
    if magnitude > 100:
        magnitude = 95 + (magnitude % 7)

    penalty = 0
    for i, m in enumerate(metrics):
        if m < base * 0.5:
            penalty += 2

    final_value = int(magnitude - penalty)

    # More distractions
    decoy_entropy = compute_entropy([1, 2, 3, 4])
    _ = filter_and_shift([5, 8, 12, 14], 13)
    unrelated_set_op = set(range(5)) | set(range(3, 8))

    return final_value

# Irrelevant initialization block
initial_buffer = [0] * 10
for k in range(len(initial_buffer)):
    initial_buffer[k] = k * k + 2

snapshot_data = [12, 15, 10, 20, 8, 16]
baseline_ref = 13

# Key distractor: looks important but unused later
aggregated_stats = []
for index, value in enumerate(snapshot_data):
    deviation = abs(value - baseline_ref)
    status_flag = 'HIGH' if deviation > 3 else 'LOW'
    aggregated_stats.append((index, deviation, status_flag))

# Another red herring function call
_ = analyze_pattern(snapshot_data, 11)

metric_data = [14, 16, 11, 19, 9, 17]

# Critical execution point
final_score = evaluate_performance(metric_data, baseline_ref)

# Output result
print(f"Result: {final_score}")