from collections import defaultdict

# Simulate system telemetry data from sensor array
technical_metrics = [
    {'cpu_load': 0.78, 'mem_usage': 0.64, 'disk_io': 0.33, 'net_latency': 46},
    {'cpu_load': 0.82, 'mem_usage': 0.71, 'disk_io': 0.41, 'net_latency': 52},
    {'cpu_load': 0.69, 'mem_usage': 0.58, 'disk_io': 0.29, 'net_latency': 41}
]

# Weight configuration for performance evaluation (higher = more important)
weights = {
    'efficiency': 0.4,
    'responsiveness': 0.35,
    'throughput': 0.25
}

# Auxiliary data — not all will be used
historical_baselines = defaultdict(float)
historical_baselines['avg_cpu'] = 0.75
historical_baselines['avg_mem'] = 0.65
historical_baselines['avg_disk'] = 0.35
historical_baselines['avg_net'] = 45

# Misleading intermediate calculations (distractors)
temp_offset = 0
correction_factor = 1.0
for i, record in enumerate(technical_metrics):
    temp_offset += record['net_latency'] * 0.01
    if record['cpu_load'] > 0.8:
        correction_factor *= 0.95

# Dead code path (never executed due to data)
anomaly_flags = []
for idx, metric in enumerate(technical_metrics):
    if metric['disk_io'] > 0.8:  # Never true
        anomaly_flags.append((idx, 'HIGH_DISK'))

# Data transformation with zip and enumerate
transformed = []
for i, (metric, baseline) in enumerate(zip(technical_metrics, [1.0, 1.1, 0.9])):  # baseline dummy scaling
    normalized = {
        'efficiency': (metric['cpu_load'] + metric['mem_usage']) / 2 * baseline,
        'responsiveness': max(1 - metric['net_latency'] / 100, 0),
        'throughput': 1 - metric['disk_io']
    }
    transformed.append(normalized)

# Secondary distraction: unused aggregation
dummy_aggregates = []
for t in transformed:
    avg_val = sum(t.values()) / len(t)
    dummy_aggregates.append(avg_val * correction_factor)

# Core logic: compute weighted score across metrics
def evaluate_performance(metrics_list, weight_dict):
    total_scores = defaultdict(float)
    
    for m in metrics_list:
        # Efficiency: balanced CPU and memory load
        total_scores['efficiency'] += (m['cpu_load'] + m['mem_usage']) / 2
        
        # Responsiveness: inverse of network latency
        total_scores['responsiveness'] += max(1 - m['net_latency'] / 100, 0)
        
        # Throughput: based on low disk I/O (more free capacity)
        total_scores['throughput'] += 1 - m['disk_io']
    
    # Average over samples
    for key in total_scores:
        total_scores[key] /= len(metrics_list)
    
    # Apply weights
    final = 0.0
    final += total_scores['efficiency'] * weight_dict['efficiency']
    final += total_scores['responsiveness'] * weight_dict['responsiveness']
    final += total_scores['throughput'] * weight_dict['throughput']
    
    return round(final * 100, 2)  # Scale to percentage-like score

# Critical execution point
final_score = evaluate_performance(technical_metrics, weights)

# Print result as required
print(f"Result: {final_score}")