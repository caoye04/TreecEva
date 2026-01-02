from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.78, 'errors': 3, 'ping': 45},
    {'node': 'B', 'load': 0.82, 'errors': 1, 'ping': 52},
    {'node': 'A', 'load': 0.65, 'errors': 0, 'ping': 47},
    {'node': 'C', 'load': 0.91, 'errors': 7, 'ping': 110},
    {'node': 'B', 'load': 0.79, 'errors': 2, 'ping': 54},
    {'node': 'C', 'load': 0.88, 'errors': 5, 'ping': 98},
    {'node': 'A', 'load': 0.83, 'errors': 4, 'ping': 50},
    {'node': 'D', 'load': 0.67, 'errors': 0, 'ping': 44}
]

# Irrelevant baseline configuration (distractor)
default_configs = {
    'timeout': 30,
    'retries': 3,
    'protocol': 'http',
    'buffer_size': 1024
}

# System health thresholds
system_thresholds = {
    'max_load': 0.80,
    'max_errors': 2,
    'max_latency': 100
}

# Aggregation map for node metrics (used later)
node_metrics = defaultdict(lambda: {'load_sum': 0, 'error_count': 0, 'response_times': [], 'samples': 0})

# Process raw stream into aggregated node statistics
for entry in telemetry_stream:
    node = entry['node']
    node_metrics[node]['load_sum'] += entry['load']
    node_metrics[node]['error_count'] += entry['errors']
    node_metrics[node]['response_times'].append(entry['ping'])
    node_metrics[node]['samples'] += 1

# Compute averages and flag anomalies (some results are distractions)
anomaly_flags = {}
performance_score = {}
for node, data in node_metrics.items():
    avg_load = data['load_sum'] / data['samples']
    avg_response = sum(data['response_times']) / len(data['response_times'])
    
    # Distractor computation: performance score (not used in final result)
    performance_score[node] = round(100 * (1 - avg_load) * (1 - min(data['error_count'], 10)/10), 2)
    
    # Actual anomaly logic
    over_load = avg_load > system_thresholds['max_load']
    excessive_errors = data['error_count'] > system_thresholds['max_errors']
    high_latency = avg_response > system_thresholds['max_latency']
    
    anomaly_flags[node] = [over_load, excessive_errors, high_latency]

# Decoy function - looks important but unused
def compute_network_diameter(adjacency_map):
    return max(len(path) for path in adjacency_map.values()) if adjacency_map else 0

# Another distractor: historical trend analysis (dead code path)
historical_trends = []
for i in range(1, len(telemetry_stream)):
    prev, curr = telemetry_stream[i-1], telemetry_stream[i]
    if prev['node'] == curr['node']:
        load_change = round(abs(curr['load'] - prev['load']), 2)
        if load_change > 0.1:
            historical_trends.append((curr['node'], load_change))

# Real processing function
log_data = []
for entry in telemetry_stream:
    if entry['errors'] > 0:
        log_data.append(f"ERR-{entry['node']}-{entry['errors']}")

# Secondary aggregation using list comprehension and set operations
distinct_error_nodes = set([record.split('-')[1] for record in log_data])
error_logs_per_node = {node: len([r for r in log_data if node in r]) for node in distinct_error_nodes}

# Bit manipulation red herring (irrelevant to outcome)
network_segment_id = 0b110101
mask = 0b1111
shifted_key = (network_segment_id << 3) & 0xFF

# Core diagnostic logic
active_nodes = set(node_metrics.keys())
critical_nodes = set()
for node, flags in anomaly_flags.items():
    # Only consider nodes exceeding load AND errors
    if flags[0] and flags[1]:  # high load and too many errors
        critical_nodes.add(node)

# Tertiary filtering with unnecessary complexity
quarantined_set = critical_nodes.copy()
for node in list(quarantined_set):
    # Extra check that doesn't change outcome due to data
    if node_metrics[node]['samples'] < 2:
        quarantined_set.remove(node)

# Final metric calculation
baseline_penalty = 5
size_factor = len(quarantined_set)

# Distractor: unused complex formula involving bit results
theoretical_capacity = (shifted_key % 50) * (len(active_nodes) or 1)

# Relevant transformation chain
raw_counts = [node_metrics[n]['error_count'] for n in quarantined_set]
effective_risk = sum(raw_counts) * 10 if raw_counts else 0

# Final diagnostic score incorporating multiple factors
final_diagnostic = baseline_penalty + size_factor * 15 + effective_risk

# Print result as required
print(f"Result: {final_diagnostic}")