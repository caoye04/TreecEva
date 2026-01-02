from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_durations = [2.3, 1.8, 4.5, 3.1, 2.9, 5.2, 3.7, 4.0, 2.5, 3.3]
node_loads = [0.67, 0.82, 0.45, 0.91, 0.53, 0.74, 0.68, 0.88]
completion_flags = [True, True, False, True, True, False, True, True, True, True]

# Irrelevant statistical distraction
mean_duration = sum(task_durations) / len(task_durations)
std_dev = (sum((x - mean_duration) ** 2 for x in task_durations) / len(task_durations)) ** 0.5
normalized = [(x - mean_duration) / std_dev for x in task_durations]

# Decoy scoring using unused method
decoy_weights = {'latency': 0.3, 'load': 0.5, 'retries': 0.2}
decoy_scores = defaultdict(float)
for i, dur in enumerate(task_durations):
    decoy_scores[f'task_{i}'] = dur * 0.7 + (node_loads[i % len(node_loads)] * 100)

# Red herring: complex bit manipulation with no impact
temp_bit = 0
for flag in completion_flags:
    temp_bit ^= int(flag) << 2
    temp_bit += temp_bit & 7

# Unused transformation chain
transformed_loads = list(map(lambda x: round(1 / (1 + math.exp(-10 * (x - 0.7))), 3), node_loads))
filtered_nodes = [load for load in node_loads if load > 0.75]

# Core data structures involved in actual computation
raw_outcomes = {
    'throughput': 8740,
    'error_rate': 0.023,
    'retry_count': 6,
    'concurrency': 32
}

metric_weights = defaultdict(float)
metric_weights['throughput'] = 0.4
metric_weights['error_rate'] = -0.3  # Negative weight
metric_weights['retry_count'] = -0.2
metric_weights['concurrency'] = 0.1

# Distractor: fake normalization queue
norm_queue = []
for k, v in raw_outcomes.items():
    if k == 'error_rate':
        norm_queue.append((k, round(v * 100, 1)))
    else:
        norm_queue.append((k, min(v, 100)))

# Fake aggregation path (dead code)
aggregation_key = ''
if len(completion_flags) > 8:
    aggregation_key = 'high_volume'
elif len([x for x in node_loads if x > 0.8]) > 3:
    aggregation_key = 'overloaded'
else:
    aggregation_key = 'standard'

# Unused recursive helper
def calculate_depth(n):
    if n <= 1:
        return 1
    return n * 0.9 + calculate_depth(n - 2)

# Real evaluation logic buried in distractions
effective_throughput = raw_outcomes['throughput'] * (1 - raw_outcomes['error_rate'])
effective_retries = max(0, raw_outcomes['retry_count'] - 2)  # First two retries forgiven

# Primary scoring function
scaled_metrics = {}
scaled_metrics['throughput'] = effective_throughput / 100  # Scale down
scaled_metrics['error_rate'] = (1 - raw_outcomes['error_rate']) * 100  # Invert and scale
scaled_metrics['retry_count'] = 10 - min(effective_retries, 10)  # Cap at 10
scaled_metrics['concurrency'] = raw_outcomes['concurrency']

# Final performance evaluation (key statement)
final_score = 0
for metric, weight in metric_weights.items():
    if metric in scaled_metrics:
        final_score += scaled_metrics[metric] * weight

# Additional irrelevant set operations
duplicate_flags = set(completion_flags)
flag_summary = set([1 if f else 0 for f in completion_flags])
combined_status = duplicate_flags.union({True}).difference({False})

# Another decoy calculation
length_score = len(task_durations) * 10 if len(task_durations) % 2 == 0 else len(task_durations) * 5

# Print target result
print(f"Result: {final_score}")