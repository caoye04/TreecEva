from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed processing node
task_load = [12, 15, 10, 8, 20, 14, 16, 11]
error_rates = [0.01, 0.03, 0.02, 0.05, 0.04, 0.02, 0.01, 0.03]
response_times = [230, 190, 250, 300, 180, 210, 195, 240]
uptime_hours = 720
maintenance_windows = 4

# Irrelevant telemetry (distractor data)
gpu_temperatures = [67, 70, 72, 68, 71, 69, 73, 70]
disk_io_ops = [1200, 1150, 1300, 1400, 1250, 1180, 1320, 1270]

# Data aggregation with distraction
stats_summary = defaultdict(float)
for i, load in enumerate(task_load):
    stats_summary['total_load'] += load
    stats_summary['avg_response'] += response_times[i] / len(response_times)
    if error_rates[i] > 0.02:
        stats_summary['high_error_count'] += 1

# Unused transformation (dead code path)
reweighted_errors = []
for er in error_rates:
    transformed = math.log(er + 1) * 100
    reweighted_errors.append(round(transformed, 2))

# Decoy function that's defined but not used
def calculate_network_efficiency(packets, loss_rate):
    efficiency = (packets * (1 - loss_rate)) / packets if packets > 0 else 0
    penalty = 0
    for _ in range(3):
        penalty += efficiency * 0.1
    return efficiency - penalty

# Another red herring: memory usage pattern analysis (unused)
memory_usage_gb = [3.2, 3.8, 4.1, 3.5, 4.0, 3.7, 3.9, 3.6]
usage_counter = Counter(memory_usage_gb)
frequent_patterns = [val for val, cnt in usage_counter.items() if cnt > 1]

# Core evaluation logic buried among distractions
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

# Misleading intermediate calculation
theoretical_capacity = 25 * len(task_load)  # Max possible tasks
utilization_rate = stats_summary['total_load'] / theoretical_capacity

# Actual performance metric computation
raw_metrics = {
    'load_stability': 1 / (1 + abs(max(task_load) - min(task_load))),
    'error_rate_avg': sum(error_rates) / len(error_rates),
    'response_time_avg': sum(response_times) / len(response_times),
    'completion_ratio': stats_summary['total_load'] / theoretical_capacity
}

# Normalize metrics to [0,1] scale with manual bounds
norm_metrics = {}
for key, val in raw_metrics.items():
    if key == 'load_stability':
        norm_metrics[key] = normalize(val, 0, 1)
    elif key == 'error_rate_avg':
        norm_metrics[key] = 1 - normalize(val, 0, 0.1)  # Invert: lower error = better
    elif key == 'response_time_avg':
        norm_metrics[key] = 1 - normalize(val, 150, 350)  # Faster = better
    else:
        norm_metrics[key] = normalize(val, 0, 1)

# Weights applied to each normalized metric
weights = [0.3, 0.25, 0.25, 0.2]  # Stability, errors, speed, completion
metrics = [
    norm_metrics['load_stability'],
    norm_metrics['error_rate_avg'],
    norm_metrics['response_time_avg'],
    norm_metrics['completion_ratio']
]

# Final scoring using weighted average
final_score = weighted_average(metrics, weights)

# Spurious adjustment based on uptime (not actually used due to override below)
temp_score = final_score * (1 + min(uptime_hours / 8000, 0.1))

# Override with refined logic: apply logarithmic scaling for diminishing returns
final_score = 100 * (math.log(1 + final_score * 2))  # Scale to point-based system

# Print result as required
print(f"Result: {final_score}")