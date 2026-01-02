def analyze_node_health(node_data, threshold=0.75):
    return sum(1 for metric in node_data['metrics'] if metric > threshold) / len(node_data['metrics'])


def compute_entropy(data_stream):
    from math import log2
    frequency = {}
    for bit in data_stream:
        frequency[bit] = frequency.get(bit, 0) + 1
    entropy = 0
    total = len(data_stream)
    for count in frequency.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)


def detect_anomalies(log_entries):
    anomalies = []
    for entry in log_entries:
        if 'ERROR' in entry['level'] or 'CRITICAL' in entry['status']:
            anomalies.append(entry['timestamp'])
    return set(anomalies)

# Irrelevant helper (distractor)
def predictive_cache_optimization(size):
    if size < 100:
        return size * 1.5
    else:
        return size * 0.8

# Unused function (dead code path)
def legacy_compatibility_check(version_string):
    parts = version_string.split('.')
    major = int(parts[0])
    minor = int(parts[1])
    patch = int(parts[2]) if len(parts) > 2 else 0
    return (major * 1000) + (minor * 100) + patch

# Misleading intermediate transformation
temp_calibration_factor = 1.037
offset_correction_table = {i: i * 0.021 for i in range(1, 50)}

# Simulated network node data
network_nodes = [
    {
        'id': 'N001',
        'type': 'router',
        'metrics': [0.82, 0.76, 0.91, 0.64, 0.79],
        'status': 'active',
        'bandwidth': 987
    },
    {
        'id': 'N002',
        'type': 'switch',
        'metrics': [0.63, 0.55, 0.67, 0.59, 0.61],
        'status': 'degraded',
        'bandwidth': 423
    },
    {
        'id': 'N003',
        'type': 'gateway',
        'metrics': [0.93, 0.88, 0.95, 0.91, 0.87],
        'status': 'active',
        'bandwidth': 1024
    }
]

# System event log with noise
system_log = [
    {'timestamp': 1001, 'level': 'INFO', 'status': 'OK', 'source': 'N001'},
    {'timestamp': 1002, 'level': 'WARNING', 'status': 'OK', 'source': 'N002'},
    {'timestamp': 1003, 'level': 'ERROR', 'status': 'RECOVERED', 'source': 'N002'},
    {'timestamp': 1004, 'level': 'INFO', 'status': 'OK', 'source': 'N003'},
    {'timestamp': 1005, 'level': 'DEBUG', 'status': 'OK', 'source': 'N001'},
    {'timestamp': 1006, 'level': 'CRITICAL', 'status': 'CRITICAL', 'source': 'N002'}
]

# Extraneous data structure
redundant_index_map = {
    'N001': [0, 1],
    'N002': [1, 2],
    'N003': [0, 2]
}

# Fake accumulator (red herring)
cumulative_interference_score = 0
for node in network_nodes:
    if node['bandwidth'] > 500:
        cumulative_interference_score += 17
    else:
        cumulative_interference_score += 9

# Bitmask simulation (distractor)
flag_register = 0b10101100
enabled_features = flag_register & 0b1111
active_modules = (flag_register >> 4) & 0b1111

# Data stream for entropy (irrelevant to final result)
data_transmission_buffer = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]

# Unused statistical summary
mean_bandwidth = sum(node['bandwidth'] for node in network_nodes) / len(network_nodes)
median_bandwidth = sorted(node['bandwidth'] for node in network_nodes)[1]

# Core logic disguised among distractions
def aggregate_metrics(nodes, log):
    healthy_count = 0
    total_priority_weight = 0
    
    # Step 1: Evaluate health based on metrics
    for node in nodes:
        health_ratio = analyze_node_health(node)
        if health_ratio > 0.7:
            healthy_count += 1
            if node['type'] == 'gateway':
                total_priority_weight += 3
            elif node['type'] == 'router':
                total_priority_weight += 2
            else:
                total_priority_weight += 1
    
    # Step 2: Count critical failures
    critical_failures = 0
    for entry in log:
        if entry['level'] == 'CRITICAL' and entry['status'] == 'CRITICAL':
            critical_failures += 1
    
    # Step 3: Use set operation to identify unique impacted nodes
    error_timestamps = detect_anomalies(log)
    affected_node_ids = set()
    for entry in log:
        if entry['timestamp'] in error_timestamps:
            affected_node_ids.add(entry['source'])
    
    # Step 4: Combine metrics with penalty
    base_score = healthy_count * 100 + total_priority_weight * 10
    penalty = len(affected_node_ids) * 25 + critical_failures * 50
    
    # Step 5: Final diagnostic calculation
    result = base_score - penalty
    
    # Additional irrelevant adjustment (not actually used due to order)
    calibrated_result = result * temp_calibration_factor
    
    return int(result)  # Final value determined here

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_log)

# Print result as required
print(f"Target result: {final_diagnostic}")