import math

# Simulated system metrics from a distributed computing environment
task_completion_times = [1.2, 0.8, 2.1, 1.5, 0.9, 3.0, 2.4, 1.1]
node_efficiency_scores = {"n1": 0.92, "n2": 0.87, "n3": 0.95, "n4": 0.76, "n5": 0.88}
error_rates = {"n1": 0.01, "n2": 0.03, "n3": 0.005, "n4": 0.05, "n5": 0.02}

# Irrelevant auxiliary data (distractor)
benchmark_baseline = [1.0, 1.0, 1.0, 1.0, 1.0]
dummy_flags = [True, False, True, False, True]

# Decoy function that looks important but isn't used in final calculation
def compute_legacy_metric(data):
    return sum(x ** 0.5 for x in data if x > 1.0)

# Another decoy with misleading name
potential_outliers = [x for x in task_completion_times if x > 2.0]
outlier_count = len(potential_outliers)  # Distractor variable

# Real processing begins: normalize completion times
avg_time = sum(task_completion_times) / len(task_completion_times)
normalized_times = [(t - avg_time) ** 2 for t in task_completion_times]
time_variance = sum(normalized_times) / len(normalized_times)
score_component_1 = 100 * math.exp(-time_variance)

# Process node efficiency into weighted score
active_nodes = list(node_efficiency_scores.keys())
efficiency_values = [node_efficiency_scores[n] for n in active_nodes]
error_weights = [1 - error_rates[n] for n in active_nodes]

# Apply non-linear transformation via lambda (required feature)
transform = lambda x, w: 10 * (x ** 2) * w
weighted_efficiency_terms = [transform(efficiency_values[i], error_weights[i]) for i in range(len(efficiency_values))]
score_component_2 = sum(weighted_efficiency_terms)

# Dummy aggregation (unused)
raw_sum_efficiency = sum(efficiency_values)
penalty_factor = 0.9 if raw_sum_efficiency < 4.0 else 1.0  # Dead logic - always true but evaluated

# Construct metrics dictionary (required python feature: dict ops)
metrics = {
    "time_stability": score_component_1,
    "efficiency_bonus": score_component_2,
    "consistency_factor": 2.5,  # Fixed contribution
    "deprecated_flag": False       # Unused field
}

# Weights for final evaluation (some keys don't contribute)
weights = {
    "time_stability": 0.4,
    "efficiency_bonus": 0.5,
    "consistency_factor": 0.1
    # "deprecated_flag" has no weight — deliberate omission
}

# Red herring: unused recursive function (meant to distract)
def calculate_recursive_depth(n):
    if n <= 1:
        return 1
    return calculate_recursive_depth(n - 2) + calculate_recursive_depth(n - 1)

# Another distraction: sorting unrelated data
sorted_nodes = sorted(active_nodes, key=lambda x: node_efficiency_scores[x], reverse=True)
transition_penalty = 0
for i in range(len(sorted_nodes) - 1):
    if sorted_nodes[i][1] > sorted_nodes[i+1][1]:
        transition_penalty += 0.1

# Core evaluation logic
valid_keys = set(weights.keys()) & set(metrics.keys())
partial_scores = []
for k in valid_keys:
    partial_scores.append(metrics[k] * weights[k])

total_adjustment = sum(partial_scores)

# Final nonlinear calibration
final_score = int(total_adjustment + 5 * math.sin(math.pi * total_adjustment / 100))

# Print result as required
print(f"Result: {final_score}")