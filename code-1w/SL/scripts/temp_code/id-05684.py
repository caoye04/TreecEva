from collections import defaultdict, Counter
import math

# Simulated network node diagnostic system with interference

def analyze_node_health(node_data, threshold):
    if not node_data['active']:
        return 'inactive'
    load_ratio = node_data['load'] / (node_data['capacity'] or 1)
    if load_ratio > threshold:
        return 'overloaded'
    elif load_ratio > 0.7:
        return 'stressed'
    elif load_ratio < 0.2:
        return 'underutilized'
    return 'stable'

def compute_entropy(values):
    # Irrelevant entropy calculation for distraction
    freq = Counter(values)
    total = len(values)
    return -sum((count/total) * math.log2(count/total) for count in freq.values())

def normalize_signal(data_stream):
    # Distractor function: signal processing red herring
    filtered = [x for x in data_stream if x > 0]
    norm = sum(x**2 for x in filtered) ** 0.5
    return [x/norm for x in filtered] if norm else []

def evaluate_redundancy(nodes):
    # Dead code path: never actually used in final computation
    backup_count = 0
    for node in nodes.values():
        if 'backup' in node.get('role', ''):
            backup_count += 1
    return backup_count

def detect_anomalies(log_entries):
    # Misleading intermediate analysis
    anomalies = []
    for entry in log_entries:
        if 'ERR' in entry['msg'] and entry['severity'] > 2:
            anomalies.append(entry['timestamp'])
    return anomalies

def aggregate_metrics(nodes, load_profile):
    # Core logic buried among distractions
    health_status = defaultdict(int)
    total_capacity = 0
    active_nodes = 0

    for nid, config in nodes.items():
        total_capacity += config['capacity']
        if config['active']:
            active_nodes += 1
            health = analyze_node_health(config, 0.85)
            health_status[health] += 1

    # Real computation hidden among irrelevant transforms
    baseline = len(load_profile) > 0 and sum(load_profile) / len(load_profile)
    adjusted_metric = (total_capacity * active_nodes) // (health_status['overloaded'] + 1)
    
    # Decoy intermediate values
    dummy_entropy = compute_entropy([len(str(v)) for v in nodes.keys()])
    signal_noise = normalize_signal([1, -2, 3, -4, 5])
    
    # Actual answer derivation
    diagnostic_score = 0
    diagnostic_score += adjusted_metric * 100
    diagnostic_score -= health_status['stressed'] * 500
    diagnostic_score += len(nodes) * 25
    
    # Final critical statement
    final_diagnostic = diagnostic_score + int(baseline * 10)

    # Unused variables to increase interference
    unused_snapshot = {'time': 12345, 'nodes_seen': 99, 'dummy_flag': True}
    temp_buffer = [0] * 2048
    debug_trace = eval("{'depth': 3, 'halted': False, 'reason': 'none'}")  # Avoid using eval in practice

    return final_diagnostic

# Simulation setup
network_nodes = {
    'N001': {'active': True, 'load': 780, 'capacity': 1000, 'role': 'primary'},
    'N002': {'active': True, 'load': 200, 'capacity': 800, 'role': 'primary'},
    'N003': {'active': False, 'load': 400, 'capacity': 800, 'role': 'backup'},
    'N004': {'active': True, 'load': 910, 'capacity': 1000, 'role': 'primary'},
    'N005': {'active': True, 'load': 100, 'capacity': 500, 'role': 'monitor'},
    'N006': {'active': True, 'load': 700, 'capacity': 1000, 'role': 'primary'},
    'N007': {'active': True, 'load': 880, 'capacity': 1000, 'role': 'primary'},
}

system_load = [0.1, 0.3, 0.5, 0.7, 0.9, 0.8, 0.6, 0.4]
system_logs = [
    {'timestamp': 1001, 'msg': 'OK: Service running', 'severity': 1},
    {'timestamp': 1005, 'msg': 'ERR: Timeout detected', 'severity': 3},
]

# Trigger decoy functions to mislead reasoning
_ = detect_anomalies(system_logs)
_ = evaluate_redundancy(network_nodes)

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Print result as required
print(f"Result: {final_diagnostic}")