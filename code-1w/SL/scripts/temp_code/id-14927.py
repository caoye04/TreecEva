from collections import defaultdict, Counter
import math

# Simulated system performance metrics over time
timestamped_metrics = [
    {'cpu': 78, 'memory': 65, 'latency': 23, 'throughput': 88},
    {'cpu': 82, 'memory': 70, 'latency': 21, 'throughput': 92},
    {'cpu': 90, 'memory': 75, 'latency': 25, 'throughput': 85},
    {'cpu': 88, 'memory': 78, 'latency': 20, 'throughput': 94},
    {'cpu': 85, 'memory': 72, 'latency': 19, 'throughput': 90}
]

# Irrelevant auxiliary function (decoy)
def analyze_network_traffic(data):
    total_packets = sum([len(str(val)) for entry in data for val in entry.values()])
    normalized = total_packets / (len(data) * 10)
    return round(normalized, 3)

# Unused variable block (red herring)
baseline_config = {
    'version': '2.1.0',
    'thresholds': {'critical': 95, 'warning': 80},
    'retries': 3,
    'timeout': 5000
}

current_state = defaultdict(lambda: 'active')
current_state['processor'] = 'optimal'
current_state['io_subsystem'] = 'degraded'

# Misleading intermediate calculation (dead path)
aggregated_load = 0
for metric in timestamped_metrics:
    load = metric['cpu'] * 0.6 + metric['memory'] * 0.4
    aggregated_load += load
aggregated_load = round(aggregated_load / len(timestamped_metrics), 2)

# Simulated anomaly detection (unused)
anomalies = []
for i, m in enumerate(timestamped_metrics):
    if m['latency'] > 22 and m['throughput'] < 89:
        anomalies.append(i)

# Core logic disguised among distractors
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def compute_stability_index(entries):
    cpu_vals = [e['cpu'] for e in entries]
    latency_vals = [e['latency'] for e in entries]
    throughput_vals = [e['throughput'] for e in entries]
    
    cpu_range = max(cpu_vals) - min(cpu_vals)
    latency_std = (sum((x - sum(latency_vals)/len(latency_vals))**2 for x in latency_vals) / len(latency_vals)) ** 0.5
    throughput_trend = sum(throughput_vals[i] < throughput_vals[i+1] for i in range(len(throughput_vals)-1))
    
    # Irrelevant transformation
    _ = [math.log(x + 1) for x in cpu_vals]
    
    stability = 100 - (cpu_range * 1.2) - (latency_std * 5) + (throughput_trend * 3)
    return round(stability, 2)

# Set operations with partial relevance
def filter_reliable_metrics(metrics):
    high_throughput = {i for i, m in enumerate(metrics) if m['throughput'] >= 90}
    low_latency = {i for i, m in enumerate(metrics) if m['latency'] <= 21}
    reliable_indices = high_throughput & low_latency  # Intersection
    return [metrics[i] for i in reliable_indices]

# Main evaluation function
def evaluate_performance(metrics_set, raw_data):
    # Distractor: unused counter
    metric_counter = Counter()
    for m in raw_data:
        for k, v in m.items():
            metric_counter[k] += 1
    
    # Actual relevant data path
    filtered_metrics = filter_reliable_metrics(metrics_set)
    
    if not filtered_metrics:
        return 0
    
    # Extract key dimensions
    cpu_scores = [m['cpu'] for m in filtered_metrics]
    memory_scores = [m['memory'] for m in filtered_metrics]
    
    # Normalize and weight
    avg_cpu = sum(cpu_scores) / len(cpu_scores)
    avg_memory = sum(memory_scores) / len(memory_scores)
    
    normalized_cpu = normalize(avg_cpu, 70, 100)
    normalized_memory = normalize(avg_memory, 50, 80)
    
    stability_bonus = compute_stability_index(filtered_metrics)
    
    # Final composite score
    base_score = (normalized_cpu * 60) + (normalized_memory * 20)
    final_score = base_score + (stability_bonus / 2)
    
    # Dead code branch (never reached due to logic)
    if len(filtered_metrics) > 10:
        adjustment = len(filtered_metrics) - 10
        final_score -= adjustment * 2
    
    return round(final_score, 4)

# Key execution point
metric_set = timestamped_metrics
benchmark_data = timestamped_metrics  # Redundant alias (distractor)

# Critical assignment
final_score = evaluate_performance(metric_set, benchmark_data)

# Output result
print(f"Result: {final_score}")