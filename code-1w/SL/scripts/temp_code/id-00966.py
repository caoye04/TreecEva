def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

# Simulated system metrics from a server cluster
temp_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.9]
cpu_loads = [78, 85, 65, 90, 88, 72, 80]
memory_usage = [12.3, 14.1, 11.8, 15.2, 13.9, 12.7, 14.5]  # in GB
network_latency = [45, 67, 52, 89, 55, 48, 73]  # ms

disk_io_ops = [1200, 1350, 1100, 1600, 1420, 1280, 1380]  # IOPS
dummy_calc_1 = sum([x ** 0.5 for x in disk_io_ops if x > 1200]) / len(disk_io_ops)

# Normalize all metrics to 0-1 scale
norm_temps = [normalize(t, 20.0, 30.0) for t in temp_readings]
norm_cpu = [normalize(c, 0, 100) for c in cpu_loads]
norm_memory = [normalize(m, 8.0, 16.0) for m in memory_usage]
norm_latency = [normalize(l, 10, 100) for l in network_latency]

# Weight assignment for performance evaluation
weights = {
    'efficiency': 0.3,
    'stability': 0.25,
    'responsiveness': 0.35,
    'capacity': 0.1
}

# Spurious computation - does not affect final result
temp_analysis = {i: (norm_temps[i] + norm_cpu[i]) / 2 for i in range(len(norm_temps))}
high_load_indices = [i for i, c in enumerate(cpu_loads) if c > 80]

# Aggregate metric scores
metrics = {
    'efficiency': sum(norm_memory) / len(norm_memory),
    'stability': 1 - (sum(norm_temps) / len(norm_temps)),  # Inverse relationship
    'responsiveness': 1 - (sum(norm_latency) / len(norm_latency)),
    'capacity': sum([1 for m in memory_usage if m < 14.0]) / len(memory_usage)
}

# Dead code path - never executed but looks relevant
if False:
    fallback_weights = {k: v * 0.9 for k, v in weights.items()}
    metrics = {k: v * 1.1 for k, v in metrics.items()}

# Misleading intermediate calculation
aggregate_health = 0
for key in metrics:
    aggregate_health += metrics[key] * weights[key] * 0.8  # Not used later

# Actual evaluation function
def evaluate_performance(perf_metrics, weight_map):
    score = 0.0
    for category in weight_map:
        if category == 'stability':
            # Apply quadratic penalty for low stability
            adjusted = perf_metrics[category] ** 2
        elif category == 'capacity':
            # Linear pass-through
            adjusted = perf_metrics[category]
        else:
            adjusted = perf_metrics[category]
        score += adjusted * weight_map[category]
    
    # Final nonlinear scaling
    if score > 0.7:
        score = 0.7 + (score - 0.7) * 0.5  # Diminishing returns
    return round(score * 100, 2)

# Execute evaluation
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")