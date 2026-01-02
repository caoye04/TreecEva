from itertools import combinations, cycle

# Simulated system metrics from a distributed task scheduler
task_durations = [120, 85, 93, 142, 78, 110, 95]
resource_usage = [0.65, 0.72, 0.54, 0.83, 0.49, 0.77, 0.61]
completion_flags = [True, True, False, True, True, False, True]

# Irrelevant auxiliary data (distractor)
heartbeat_intervals = [1.0, 1.5, 1.2, 1.8, 1.0, 1.1, 1.05]
system_nodes = ['node_alpha', 'node_beta', 'node_gamma', 'node_delta']
node_cycle = list(cycle(system_nodes))[:7]

# Misleading intermediate calculations (dead computations)
avg_heartbeat = sum(heartbeat_intervals) / len(heartbeat_intervals)
node_performance_proxy = {node: 0 for node in system_nodes}
for i, node in enumerate(node_cycle):
    node_performance_proxy[node] += resource_usage[i] * (1 + i % 3)

# Real processing begins here
filtered_indices = [
    i for i, flag in enumerate(completion_flags) if flag
]

dynamic_weights = {}
for i in filtered_indices:
    base_weight = 1.0 + (task_durations[i] / 100)
    adjustment = 0.5 if resource_usage[i] > 0.7 else 0.2
    dynamic_weights[i] = round(base_weight + adjustment, 3)

# Red herring: unused weight mapping
inverse_duration_map = {
    i: round(1 / task_durations[i], 4) for i in range(len(task_durations))
}

# Core metric computation
metric_weights = []
for i in sorted(dynamic_weights.keys()):
    weight = dynamic_weights[i]
    if i % 2 == 0:
        weight *= 1.1
    else:
        weight *= 0.95
    metric_weights.append(round(weight, 3))

raw_outcomes = []
for i in filtered_indices:
    score = task_durations[i] * resource_usage[i]
    penalty = 10 if task_durations[i] > 100 else 0
    raw_outcomes.append(score - penalty)

# Decoy function that is never called
def calculate_thermal_load(seq):
    total = 0
    for x in seq:
        if x > 100:
            total += x * 0.1
    return total // 7

# Unused combinatorial analysis (distractor)
combo_risk = []
for combo in combinations(filtered_indices, 2):
    diff = abs(task_durations[combo[0]] - task_durations[combo[1]])
    if diff > 40:
        combo_risk.append((combo, 'HIGH'))
    else:
        combo_risk.append((combo, 'LOW'))

# Actual evaluation logic
aggregated = 0.0
for w, val in zip(metric_weights, raw_outcomes):
    aggregated += w * val

normalization_factor = len(metric_weights) * 0.85
if len(filtered_indices) > 5:
    normalization_factor *= 1.2
else:
    normalization_factor *= 0.95

adjusted_aggregate = aggregated / normalization_factor

scaling_lookup = {i: (1 + i*0.05) for i in range(1, 6)}
scale = scaling_lookup.get(len(filtered_indices), 1.2)

intermediate_result = adjusted_aggregate * scale

# Final transformation with conditional offset
offset = 0
if sum(1 for x in resource_usage if x > 0.7) >= 3:
    offset = 15
elif sum(task_durations) > 600:
    offset = 7
else:
    offset = -3

final_score = int(intermediate_result) + offset

print(f"Result: {final_score}")