def analyze_system_load(readings):
    avg_load = sum(readings) / len(readings)
    peak = max(readings)
    normalized = [x / peak for x in readings]
    return sum(normalized) / len(normalized)


def calculate_efficiency(runs):
    total_ops = 0
    overhead = 0
    for ops, time_spent in runs:
        if time_spent > 0:
            efficiency = ops / time_spent
            if efficiency > 100:
                overhead += 1
            total_ops += efficiency
    return total_ops if total_ops > 0 else 1

# Irrelevant helper (decoy)
def predict_failure(temps):
    risk = 0
    for t in temps:
        if t > 75:
            risk += (t - 75) * 1.5
    return risk  # Unused

# Misleading intermediate calculation
temp_history = [68, 72, 79, 65, 81, 77]
failure_risk = predict_failure(temp_history)
baseline_shift = sum([x - 70 for x in temp_history]) / len(temp_history)

# Core data
metrics_log = {
    'latency': [120, 140, 95, 160],
    'throughput': [850, 900, 800, 950],
    'errors': [3, 1, 4, 2],
    'memory_usage': [70, 75, 80, 72]
}

# Distractor: unused transformation
normalized_latency = [1000/x for x in metrics_log['latency']]
scaled_throughput = [t/10 for t in metrics_log['throughput']]

weights = {
    'latency': 0.4,
    'throughput': 0.5,
    'error_penalty': 0.3,
    'memory_penalty': 0.2
}

# Fake aggregation path (dead code)
aggregated = 0
for key in ['latency', 'throughput']:
    aggregated += sum(metrics_log[key]) // len(metrics_log[key])

# Real evaluation logic
def evaluate_performance(log, w):
    base_latency = sum(log['latency']) / len(log['latency'])
    base_throughput = sum(log['throughput']) / len(log['throughput'])
    error_rate = sum(log['errors']) / len(log['errors'])
    avg_memory = sum(log['memory_usage']) / len(log['memory_usage'])

    # Compute score components using weighted contributions
    latency_score = (100 - (base_latency / 2)) * w['latency']
    throughput_score = (base_throughput / 10) * w['throughput']
    error_score = 10 - (error_rate * w['error_penalty'] * 10)
    memory_score = 10 - ((avg_memory - 60) * w['memory_penalty'])

    # Hidden dependency: system load factor from auxiliary function
    load_factor = analyze_system_load(log['latency'])
    efficiency_run_data = [(1000, 1.2), (800, 0.9), (1200, 1.5)]
    efficiency_bonus = calculate_efficiency(efficiency_run_data) / 100

    # Final computation chain
    raw_score = latency_score + throughput_score + error_score + memory_score
    adjusted_score = raw_score * (1 + (load_factor - 1) * 0.1)
    final_normalized = adjusted_score + efficiency_bonus

    # Critical assignment point
    final_score = int(round(final_normalized * 10))

    # Dead-end distraction
    audit_trace = []
    for i in range(len(log['errors'])):
        audit_trace.append(f"E{i}:{log['errors'][i]}")

    return final_score

# Execution point of interest
final_score = evaluate_performance(metrics_log, weights)
print(f"Result: {final_score}")