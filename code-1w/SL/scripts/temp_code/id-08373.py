import itertools

# Simulated system performance metrics across multiple tasks
task_data = [85, 90, 78, 92, 88, 76, 95, 87]
weights = [0.1, 0.15, 0.1, 0.2, 0.1, 0.15, 0.1, 0.1]

# Irrelevant baseline reference (distractor)
baseline_scores = [x * 0.9 for x in task_data]

# Normalize task data to 0-1 scale using min-max normalization
min_val, max_val = min(task_data), max(task_data)
normalized_metrics = [(x - min_val) / (max_val - min_val) for x in task_data]

# Extra transformation with no impact on final result (dead path)
stretched_metrics = [x ** 1.1 for x in normalized_metrics if x > 0.5]

# Simulate redundant weight expansion via itertools (moderate interference)
expanded_weights = list(itertools.repeat(weights[3], 4))
expanded_weights_sum = sum(expanded_weights)  # Unused variable (red herring)

# Apply smoothing filter (irrelevant computation)
smoothed_metrics = []
for i in range(len(normalized_metrics)):
    neighbors = normalized_metrics[max(0, i-1):i+2]
    smoothed_metrics.append(sum(neighbors) / len(neighbors))

# Weighted aggregation using original weights and normalized metrics
def aggregate_performance(w, m):
    total = 0.0
    for i in range(len(w)):
        total += w[i] * m[i]
    return round(total * 100, 2)

# Secondary metric: consistency check (not used in final score)
consistency_gap = max(normalized_metrics) - min(normalized_metrics)
penalty_factor = 0.95 if consistency_gap > 0.3 else 1.0  # Computed but unused

# Critical statement
final_score = aggregate_performance(weights, normalized_metrics)

# Print result as required
print(f"Result: {final_score}")