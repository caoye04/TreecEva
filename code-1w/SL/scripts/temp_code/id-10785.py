from itertools import combinations, chain

# Simulated system metrics from a distributed task scheduler
task_durations = [12, 15, 10, 8, 20, 14, 16, 9]
resource_usage = [0.65, 0.72, 0.54, 0.48, 0.81, 0.67, 0.77, 0.51]
completion_flags = [True, True, False, True, True, True, False, True]

# Irrelevant transformations (distractors)
distorted_durations = [d ** 0.5 for d in task_durations if d > 10]
scaled_usage = [(u * 100) // 1 for u in resource_usage]
flag_summary = sum(1 for f in completion_flags if f) / len(completion_flags)

# Unused helper function (dead code path)
def analyze_network_latency(packets):
    return sum(p % 7 for p in packets if p > 5)

# Decoy data structures
event_log = {
    'start': '2023-07-15T08:00:00',
    'nodes': ['A', 'B', 'C'],
    'checksum': 5831,
    'payload': [hex(i + 25)[2:] for i in range(8)]
}

# Simulated packet data for decoy function
packet_sequence = [3, 7, 12, 5, 9, 11]
latency_mock = analyze_network_latency(packet_sequence)  # unused result

# Core logic disguised among distractors
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Red herring transformation using itertools
all_pairs = list(combinations(task_durations[:4], 2))
pair_sums = [sum(pair) for pair in all_pairs]
filtered_combinations = [p for p in pair_sums if p > 25]

# Another distraction: character counting in node IDs
cumulative_chars = sum(len(node) for node in event_log['nodes'])

# Key processing pipeline
active_tasks = [t for t, c in zip(task_durations, completion_flags) if c]
normalized_duration = normalize([1 / t for t in active_tasks])  # efficiency score
normalized_resource = normalize(resource_usage)

# Bit manipulation red herring
bitwise_mask = 0
for val in task_durations:
    bitwise_mask ^= (val << 1) | 1

# Destructuring assignment with mixed relevance
primary_metric, *aux_metrics = normalized_duration + normalized_resource[:len(normalized_duration)]

# Linear search for threshold crossing (irrelevant but plausible)
threshold_index = -1
for i, nr in enumerate(normalized_resource):
    if nr > 0.7 and completion_flags[i]:
        threshold_index = i
        break

# Real computation path begins here
baseline = {
    'avg_duration': sum(active_tasks) / len(active_tasks),
    'efficiency_floor': 0.6,
    'weight_set': [0.4, 0.6]
}

metrics = {
    'duration_efficiency': sum(normalized_duration) / len(normalized_duration),
    'resource_stability': 1 - (max(resource_usage) - min(resource_usage)),
    'compliance_rate': flag_summary,
    'complexity_factor': len(list(chain.from_iterable(
        [combinations(active_tasks, 2)] + 
        [combinations(resource_usage[:len(active_tasks)], 2)]
    )))
}

# Core evaluation logic buried in abstraction
def evaluate_performance(perf_metrics, reference):
    w = reference['weight_set']
    d_e = perf_metrics['duration_efficiency']
    r_s = perf_metrics['resource_stability']
    c_f = perf_metrics['complexity_factor']
    
    # Actual answer computation
    base_score = (d_e * w[0] + r_s * w[1]) * 100
    penalty = (c_f / 100) * 15  # complexity penalty
    adjustment = (perf_metrics['compliance_rate'] - reference['efficiency_floor']) * 10
    return int(base_score - penalty + adjustment)

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output requirement
print(f"Result: {final_score}")