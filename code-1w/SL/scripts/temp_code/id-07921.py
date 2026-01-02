from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed processing pipeline
task_load = [12, 15, 8, 20, 13, 17, 9, 14]
error_flags = [False, True, False, False, True, False, False, True]
execution_times = {f'task_{i}': (t ** 1.1) for i, t in enumerate(task_load)}
worker_nodes = ['alpha', 'beta', 'gamma', 'delta']
node_assignments = [worker_nodes[i % len(worker_nodes)] for i in range(len(task_load))]

# Irrelevant aggregation: distractor using Counter
flag_distribution = Counter(error_flags)
duplicate_tracker = Counter(node_assignments)

# Baseline thresholds (used later)
baseline = {
    'latency_cap': 18.5,
    'error_tolerance': 0.35,
    'throughput_floor': 12.0
}

# Distractor: unused function simulating dead code path
def analyze_health(metrics):
    score = 0
    for val in metrics:
        if val > 10:
            score += math.sqrt(val) * 0.1
    return round(score, 2)

# Distractor: misleading intermediate calculation with no impact
temp_adjustment_factor = 0.0
for idx, load in enumerate(task_load):
    if load > 10 and error_flags[idx]:
        temp_adjustment_factor += 0.05 * (load / 100)

temp_adjustment_factor = math.sin(temp_adjustment_factor) if temp_adjustment_factor else 0.0

# Real processing begins: build metric dictionary
metrics = defaultdict(float)
for i, load in enumerate(task_load):
    key = f'metric_{i+1}'
    time_val = execution_times[f'task_{i}']
    # Core signal: normalized effective performance
    if not error_flags[i]:
        metrics[key] = time_val * 0.9 if load < 15 else time_val * 1.1
    else:
        metrics[key] = max(0, time_val * 0.5)  # penalize errors

# Another red herring: complex but unused data structure
consistency_check = []
for node in worker_nodes:
    loads_on_node = [task_load[i] for i, n in enumerate(node_assignments) if n == node]
    avg_load = sum(loads_on_node) / len(loads_on_node)
    consistency_check.append({'node': node, 'deviation': abs(avg_load - 13.5)})

# Decoy transformation: bit manipulation with no downstream use
bit_encoded = 0
for i, flag in enumerate(error_flags):
    bit_encoded |= (1 << i) if flag else 0
bit_masked = bit_encoded ^ 0b11111111
masked_sum = bin(bit_masked).count('1')

# Key logic hidden among distractions
def calculate_efficiency(data):
    raw_values = list(data.values())
    mean_val = sum(raw_values) / len(raw_values)
    variance = sum((x - mean_val) ** 2 for x in raw_values) / len(raw_values)
    return mean_val / (math.sqrt(variance) + 1e-6)

# Secondary metric: count of high-throughput non-error tasks
high_perf_count = sum(
    1 for i, flag in enumerate(error_flags)
    if not flag and task_load[i] >= baseline['throughput_floor']
)

# Unused recursive red herring
def predict_stability(depth, factor):
    if depth <= 1:
        return factor
    return predict_stability(depth - 1, factor * 0.9) + predict_stability(depth - 1, factor * 0.1)

# Real evaluation function — only one that matters
def evaluate_performance(performance_data, base):
    efficiency = calculate_efficiency(performance_data)
    latency_ratio = sum(1 for v in performance_data.values() if v > base['latency_cap']) / len(performance_data)
    error_rate = error_flags.count(True) / len(error_flags)
    
    # Final scoring formula
    raw_score = efficiency * 100
    if latency_ratio <= base['error_tolerance'] and error_rate <= base['error_tolerance']:
        raw_score *= 1.25
    if high_perf_count >= 4:
        raw_score += 10
    
    return int(round(raw_score))

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output required format
print(f"Target result: {final_score}")