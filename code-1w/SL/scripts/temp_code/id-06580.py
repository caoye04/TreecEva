import itertools

# Simulated network node diagnostic system with interference

def analyze_node_health(status_code, load_factor):
    if status_code == 200:
        return load_factor < 0.75
    elif status_code == 503:
        return False
    else:
        return load_factor < 0.5

# Irrelevant helper (decoy)
def deprecated_normalization(x):
    return (x - min(x)) / (max(x) - min(x))

# Unused function (dead path)
def legacy_calibrate(nodes):
    total = 0
    for node in nodes:
        total += node.get('weight', 1) * 0.9
    return total

# Another red herring: historical data not used
historical_diagnostics = [
    {'timestamp': 1623456000, 'severity': 3, 'resolved': True},
    {'timestamp': 1623459600, 'severity': 5, 'resolved': False},
    {'timestamp': 1623463200, 'severity': 2, 'resolved': True}
]

# Key data structures
network_nodes = [
    {'id': 'N1', 'status': 200, 'load': 0.68, 'latency': 120, 'active': True},
    {'id': 'N2', 'status': 503, 'load': 0.45, 'latency': 800, 'active': False},
    {'id': 'N3', 'status': 200, 'load': 0.70, 'latency': 150, 'active': True},
    {'id': 'N4', 'status': 404, 'load': 0.30, 'latency': 300, 'active': True},
    {'id': 'N5', 'status': 200, 'load': 0.80, 'latency': 200, 'active': True}
]

system_load = [0.68, 0.45, 0.70, 0.30, 0.80]
system_status_codes = [node['status'] for node in network_nodes]

# Misleading intermediate calculation (unused)
avg_latency = sum(node['latency'] for node in network_nodes) / len(network_nodes)
high_latency_count = sum(1 for node in network_nodes if node['latency'] > 200)

# Distractor: complex but unused transformation
detailed_analysis = {
    node['id']: {
        'health': analyze_node_health(node['status'], node['load']),
        'risk': 'high' if node['load'] > 0.7 else 'low',
        'score': int((1 - node['load']) * 100)
    } for node in network_nodes
}

# Another decoy list comprehension with zip and enumerate (irrelevant)
redundant_pairs = []
for i, (node, load) in enumerate(zip(network_nodes, system_load)):
    if i % 2 == 0:
        transformed = (load * 100) + i
        redundant_pairs.append((node['id'], transformed))

# Core logic buried among distractions
def compute_stability_index(nodes):
    healthy_count = 0
    total_risk_score = 0
    for node in nodes:
        # Actual health logic used
        is_healthy = analyze_node_health(node['status'], node['load'])
        risk_level = 1 if node['load'] > 0.7 else 0
        total_risk_score += risk_level
        if is_healthy:
            healthy_count += 1
    return healthy_count - total_risk_score

# Aggregation function that combines multiple concepts
def aggregate_metrics(nodes, loads):
    stability = compute_stability_index(nodes)
    
    # Use of enumerate and zip (required python feature)
    weighted_sum = 0
    for idx, (node, load) in enumerate(itertools.zip_longest(nodes, loads)):
        if idx % 2 == 0 and load:
            weighted_sum += load * (idx + 1)
    
    # Real computation path
    base_metric = stability * 100
    adjustment = int(weighted_sum * 10)
    
    # Critical distraction: similar-looking but unused variable
    temp_diagnostic = base_metric + 50  # Never used
    
    # Actual answer computation
    final_value = base_metric + adjustment
    
    # Dictionary operation (required)
    summary = {'base': base_metric, 'adjustment': adjustment, 'final': final_value}
    return summary['final']

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes, system_load)
print(f"Target result: {final_diagnostic}")