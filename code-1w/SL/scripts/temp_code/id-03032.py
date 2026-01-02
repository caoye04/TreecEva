import itertools

# Simulated sensor data processing with noise filtering and performance evaluation
data_stream = [15, 23, 42, 17, 88, 34, 56, 27, 91, 13]
noise_floor = 10
signal_baseline = 20

# Irrelevant auxiliary variables (distractors)
placeholder_buffer = [0] * len(data_stream)
temp_cache = {i: val ** 2 for i, val in enumerate(data_stream)}
shadow_copy = data_stream[::-1]

# Filtered signal based on threshold (relevant path)
filtered_signal = [x for x in data_stream if x > noise_floor + signal_baseline]

# Decoy function: looks important but unused
def compute_entropy(sequence):
    from math import log
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Another decoy: complex-looking but irrelevant transformation
rolling_checksum = sum((data_stream[i] ^ data_stream[(i+1)%len(data_stream)]) for i in range(len(data_stream)))

# Real computation begins: group detection using itertools
consecutive_groups = []
for k, g in itertools.groupby(enumerate(filtered_signal), lambda ix: ix[0] - ix[1]):
    consecutive_groups.append([i for x, i in g])

group_lengths = [len(group) for group in consecutive_groups]

# Misleading intermediate metric (not used in final result)
avg_group_length = sum(group_lengths) / len(group_lengths) if group_lengths else 0

# Key derived metrics (only some are used)
metric_set = {
    'peak_count': len(filtered_signal),
    'max_value': max(filtered_signal) if filtered_signal else 0,
    'sum_of_pairs': sum(a + b for a, b in itertools.combinations(filtered_signal, 2)) if len(filtered_signal) > 1 else 0,
    'group_complexity': len(consecutive_groups)
}

# Dead code path: never executed but looks plausible
if False:
    for key in metric_set:
        metric_set[key] *= 2

# Unused helper (red herring)
def normalize_metrics(metrics):
    normed = {}
    for k, v in metrics.items():
        normed[k] = v / (v + 1e-6)
    return normed

# Core logic: actual evaluation function used
valid_keys = {'peak_count', 'max_value', 'group_complexity'}
weight_map = {'peak_count': 1.5, 'max_value': 0.01, 'group_complexity': 2.0}

# This function is critical and only uses subset of metric_set
def evaluate_performance(metrics):
    score = 0.0
    for key in valid_keys:
        if key in metrics:
            weight = weight_map[key]
            score += metrics[key] * weight
    # Artificial suppression factor based on data pattern
    if len(consecutive_groups) >= 2 and metric_set['max_value'] > 80:
        score *= 0.9
    return int(score)

# Final execution point
final_score = evaluate_performance(metric_set)

# Output the target result
print(f"Result: {final_score}")