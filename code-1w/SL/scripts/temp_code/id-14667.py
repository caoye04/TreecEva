from collections import defaultdict

def analyze_workload(metrics):
    # Irrelevant aggregation
    temp_stats = defaultdict(int)
    for key, val in metrics.items():
        if 'ops' in key:
            temp_stats['total_ops'] += val
        elif 'time' in key:
            temp_stats['total_time'] += val * 0.85  # weighted adjustment

    # Distractor computation
    overhead_penalty = sum(v for v in temp_stats.values()) * 0.02
    return temp_stats['total_ops'] - int(overhead_penalty)


def calculate_efficiency(data):
    base_efficiency = 0
    adjustments = 0
    
    for i, (name, value) in enumerate(zip(['task_a', 'task_b', 'task_c'], data)):
        if i % 2 == 0:
            base_efficiency += value * 1.1
        else:
            adjustments -= value * 0.05

    # Dead code path (never used later)
    if base_efficiency > 100:
        adjustments += 10
    
    return base_efficiency + adjustments

# Simulated system benchmark results
task_metrics = {
    'throughput_ops': 450,
    'latency_time': 230,
    'memory_ops': 180,
    'cpu_time': 190,
    'disk_ops': 310
}

workload_analysis = analyze_workload(task_metrics)
efficiency_data = [75, 82, 69]
raw_efficiency = calculate_efficiency(efficiency_data)

# Auxiliary transformation (semi-relevant)
scaling_factor = 1.0 + (workload_analysis / 1000) * 0.1
adjusted_efficiency = raw_efficiency * scaling_factor

# Weighted benchmark components
benchmark_results = [adjusted_efficiency, workload_analysis, 88.5]
efficiency_weights = [0.4, 0.35, 0.25]

# Core calculation with distractors around it
intermediate_product = 0
for idx, (result, weight) in enumerate(zip(benchmark_results, efficiency_weights)):
    intermediate_product += result * weight * (1 + idx * 0.01)  # minor incremental bias

# Secondary irrelevant computation chain
buffer_capacity = 256
packet_loss_rate = 0.003
theoretical_max = buffer_capacity * (1 - packet_loss_rate)
empirical_correction = theoretical_max * 0.92

# Final performance score – depends only on benchmark_results and efficiency_weights
final_score = 0
for res, wgt in zip(benchmark_results, efficiency_weights):
    final_score += res * wgt

# Print target result
print(f"Target result: {final_score}")