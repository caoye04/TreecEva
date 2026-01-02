from itertools import combinations

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 150, 130, 160, 145, 135, 140, 155]
resource_usage = [0.65, 0.78, 0.62, 0.85, 0.73, 0.68, 0.71, 0.80]
completion_order = [i for i in range(8)]

# Irrelevant transformations (distractors)
distorted_durations = [d ** 0.5 * 1.2 for d in task_durations]
shifted_usage = [(u + 0.1) % 1.0 for u in resource_usage]
skewed_indices = [i * i + 2 * i + 1 for i in completion_order]

# Unused helper function (dead code path)
def analyze_trends(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1
    return trend_score

# Misleading intermediate metric
temporal_efficiency = sum([abs(task_durations[i] - task_durations[i-1]) for i in range(1, len(task_durations))]) / len(task_durations)

# Real processing begins: normalize durations
duration_normalized = [1 - (d - min(task_durations)) / (max(task_durations) - min(task_durations)) for d in task_durations]

# Weighted combination using zip and enumerate
weights = [0.4, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0]  # Only first four matter
metrics = []
for idx, (dur, res) in enumerate(zip(duration_normalized, resource_usage)):
    score_component = dur * 0.7 + res * 0.3
    adjustment = 0.05 * (idx % 2)  # Minor parity-based tweak
    metrics.append(score_component + adjustment)

# Spurious combinatorial analysis (red herring)
possible_pairs = list(combinations(metrics, 2))
coherence_sum = sum([abs(a - b) for a, b in possible_pairs]) / len(possible_pairs)

# Dummy transformation with slicing
slice_offset = len(metrics) // 2
mirrored_metrics = metrics[::-1]
blended = [(a + b) / 2 for a, b in zip(metrics[slice_offset:], mirrored_metrics[:slice_offset])]

# Core evaluation logic — depends only on first four metrics and weights
valid_metrics = metrics[:4]
valid_weights = weights[:4]

# Final aggregation
evaluate_performance = lambda m, w: sum([val * w[i] for i, val in enumerate(m)]) * 100
final_score = evaluate_performance(valid_metrics, valid_weights)

# Output result
print(f"Result: {final_score}")