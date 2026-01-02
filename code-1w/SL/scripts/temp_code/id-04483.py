import math

# Simulated telemetry data structure for a distributed system
node_metrics = {
    'latency_ms': [120, 150, 95, 200, 300, 170, 250],
    'packet_loss': [0.01, 0.03, 0.02, 0.05, 0.07, 0.04, 0.06],
    'cpu_load': [0.65, 0.72, 0.58, 0.81, 0.89, 0.75, 0.83]
}

# Irrelevant historical stats (distractor)
historical_averages = {
    'latency_ms': 180,
    'packet_loss': 0.045,
    'cpu_load': 0.74
}

# Decoy function - looks relevant but unused in critical path
def compute_health_score_v1(metrics):
    score = 100
    score -= metrics.get('latency_ms', 0) * 0.1
    score -= metrics.get('error_rate', 0) * 50
    return max(score, 0)

# Core analysis function with recursion and lambda usage
def detect_anomalies(data_list, threshold, index=0, accumulator=None):
    if accumulator is None:
        accumulator = []
    
    # Base case
    if index >= len(data_list):
        return accumulator
    
    current_value = data_list[index]
    # Anomaly: value exceeds threshold by dynamic factor
    if current_value > threshold * (1 + 0.1 * len(accumulator)):
        accumulator.append(current_value)
    
    # Recursive call
    return detect_anomalies(data_list, threshold, index + 1, accumulator)

# Unused helper (dead code path)
def normalize_values(raw_data):
    total = sum(raw_data)
    return [x / total for x in raw_data] if total > 0 else raw_data

# Set operation to filter critical nodes
active_nodes = set(range(1, 8))
degraded_nodes = set()

for i, latency in enumerate(node_metrics['latency_ms']):
    if latency > 200:
        degraded_nodes.add(i + 1)

# Critical node intersections (irrelevant to final result)
critical_intersection = active_nodes.intersection(degraded_nodes)

# Real-time event queue (unused distractor)
event_queue = [{'type': 'heartbeat', 'seq': i} for i in range(10)]

# Fault correlation engine using lambda and dictionary mapping
correlation_engine = {
    'latency_spike': lambda x: x > 250,
    'loss_spike': lambda x: x > 0.06,
    'load_warning': lambda x: x > 0.8
}

# Apply anomaly detection on multiple metrics
telemetry_log = {}
fault_counts = {}

for metric_name, values in node_metrics.items():
    base_threshold = {'latency_ms': 220, 'packet_loss': 0.055, 'cpu_load': 0.8}.get(metric_name, 0)
    anomalies = detect_anomalies(values, base_threshold)
    telemetry_log[metric_name] = anomalies
    fault_counts[metric_name] = len(anomalies)

# Misleading intermediate calculation (looks important)
average_faults = sum(fault_counts.values()) / len(fault_counts) if fault_counts else 0
projected_downtime = average_faults * 1.5  # Not used later

# Secondary diagnostic chain with red herring
consensus_flags = []
for node_id in range(len(node_metrics['latency_ms'])):
    high_latency = node_metrics['latency_ms'][node_id] > 190
    high_loss = node_metrics['packet_loss'][node_id] > 0.045
    high_cpu = node_metrics['cpu_load'][node_id] > 0.7
    if high_latency and high_loss and high_cpu:
        consensus_flags.append(node_id * 0.1)  # Looks diagnostic, not used

# Core recursive summation with conditional filtering
def recursive_sum(data, idx=0, total=0):
    if idx >= len(data):
        return total
    value = data[idx]
    if value < 300:  # Filter extreme outliers
        total += int(value // 10)  # Scale down contribution
    return recursive_sum(data, idx + 1, total)

# Weighted aggregation function (used in final step)
weights = {'latency_ms': 1.2, 'packet_loss': 2.5, 'cpu_load': 0.8}

weighted_total = 0
for key, count in fault_counts.items():
    weighted_total += weights.get(key, 1.0) * count * 10

# Final diagnostic computation
baseline_score = 500
adjustment_factor = math.log(weighted_total + 1) if weighted_total > 0 else 0

# This variable is actually irrelevant
diagnostic_shadow = baseline_score - adjustment_factor * 10

# Real answer depends on recursive sum of specific anomaly pattern
spike_magnitudes = telemetry_log['latency_ms'] + [x * 100 for x in telemetry_log['packet_loss']]
raw_impact = recursive_sum(spike_magnitudes)

# Final computation
final_diagnostic = baseline_score + raw_impact - int(weighted_total)

# Print result as required
print(f"Result: {final_diagnostic}")