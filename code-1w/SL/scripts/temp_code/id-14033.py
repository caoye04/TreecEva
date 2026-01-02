from collections import defaultdict
from itertools import cycle

# Simulate system performance metrics over time
time_intervals = [1, 2, 3, 4, 5]
raw_data_points = [88, 92, 75, 85, 95]

# Irrelevant auxiliary tracking (distractor)
heartbeat_log = defaultdict(int)
for t in time_intervals:
    heartbeat_log[t] = (t * 2 + 44) % 7

# Normalize data using min-max scaling
min_val, max_val = min(raw_data_points), max(raw_data_points)
normalized = [(x - min_val) / (max_val - min_val) for x in raw_data_points]

# Assign weights cyclically across dimensions (mixed relevance)
metrics = {f'metric_{i+1}': normalized[i] for i in range(len(normalized))}
weight_pattern = [0.1, 0.2, 0.3, 0.25, 0.15]
benchmark_weights = {k: weight_pattern[i % len(weight_pattern)] for i, k in enumerate(metrics)}

# Extra distraction: simulate a dead-end validation path
temp_diagnostic = []
for key in metrics:
    if '3' in key:
        temp_diagnostic.append(0.0)
    else:
        temp_diagnostic.append(-1.0)

# Core evaluation logic
weighted_sum = 0.0
total_weight = 0.0
for m in metrics:
    if m in benchmark_weights:
        weight = benchmark_weights[m]
        weighted_sum += metrics[m] * weight
        total_weight += weight

# Apply non-linear adjustment based on consistency
consistency_bonus = 1.0
if abs(metrics['metric_1'] - metrics['metric_5']) < 0.2:
    consistency_bonus = 1.1

# Final aggregation
final_score = weighted_sum / total_weight if total_weight > 0 else 0
final_score *= consistency_bonus

# Additional red herring: unused transformation chain
shifted_cycle = list(cycle([1.1, 0.9]))[:len(raw_data_points)]
adjusted_scores = [a * b for a, b in zip(normalized, shifted_cycle)]

print(f"Result: {final_score}")