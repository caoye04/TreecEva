from itertools import combinations
from math import log, ceil

# Simulated system metrics and configuration
task_load = [120, 150, 95, 200, 175]
response_times = [0.45, 0.67, 0.33, 0.89, 0.54]
error_rates = [0.02, 0.05, 0.01, 0.07, 0.03]
throughput = [480, 390, 520, 320, 440]

# Irrelevant telemetry (distractor data)
telemetry_logs = [(1, 'OK'), (2, 'WARN'), (3, 'OK'), (4, 'ERROR')]
log_analysis = {code: msg for code, msg in telemetry_logs}
status_summary = [msg for code, msg in sorted(telemetry_logs)]

# Weighting schema for performance evaluation (real logic input)
weights = {'latency': 0.4, 'errors': 0.3, 'throughput': 0.2, 'load_balance': 0.1}

# Derived metrics (some are decoys)
avg_response = sum(response_times) / len(response_times)
max_error_rate = max(error_rates)
total_throughput = sum(throughput)
effective_load = sum(task_load) * 0.85

# Decoy transformations (dead computations)
log_data = [round(log(x + 1), 3) for x in task_load if x > 100]
squared_pairs = [(x**2, y**2) for x, y in zip(task_load[:3], response_times[:3])]
shifted_load = [x >> 2 for x in task_load]  # Bit manipulation red herring

# Real metric processing
normalized_latency = [1 / rt for rt in response_times]
scaled_errors = [1 - (er / 0.1) for er in error_rates]  # Inverted penalty
scaled_throughput = [tp / 600 for tp in throughput]

# Simulate load distribution score using bit counting (valid use)
load_bits = sum(bin(int(l)).count('1') for l in task_load)
load_balance_score = (load_bits / 20)  # Artificial normalization

# Build composite metrics
efficiency_metrics = []
for i in range(len(task_load)):
    score = (normalized_latency[i] * weights['latency'] +
             scaled_errors[i] * weights['errors'] +
             scaled_throughput[i] * weights['throughput'])
    efficiency_metrics.append(round(score, 4))

# Distractor: unused combination analysis
unused_combos = list(combinations(efficiency_metrics, 3))
combo_entropy = sum(ceil(sum(c)) for c in unused_combos) % 100  # Misleading complexity

# Secondary distractor: set operations with no impact
time_set = set(round(rt, 2) for rt in response_times)
error_set = set(er > 0.04 for er in error_rates)
overlap_flag = time_set.intersection({0.67, 0.89}) and not error_set.difference({True})

# Conditional decoy (never executed due to logic)
if len(task_load) < 4:
    fallback_score = sum(efficiency_metrics) / 2
else:
    dummy = [x * 0.1 for x in efficiency_metrics]  # Dead path

# Critical function: evaluates final score using average and balance term
def evaluate_performance(metrics, w):
    base_performance = sum(metrics) / len(metrics)
    
    # Hidden dependency on load balance (non-obvious linkage)
    adjustment_factor = w['load_balance'] * load_balance_score
    final = base_performance + adjustment_factor
    
    # Early return red herring (unreachable)
    if base_performance > 10:
        return round(base_performance, 3)
        
    return round(final, 4)

# Key statement — answer depends on correct tracing through distractions
final_score = evaluate_performance(efficiency_metrics, weights)

# Output result as required
print(f"Target result: {final_score}")