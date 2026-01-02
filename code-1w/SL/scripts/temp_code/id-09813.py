from collections import defaultdict

# Simulate a distributed system node load analysis
def analyze_node_efficiency(node):
    base = node['load'] * 0.9
    overhead = len(node['services']) * 0.1
    return base - overhead if base > overhead else 0.5

def balance_workload(nodes):
    total_load = 0
    efficiency_map = {}
    temp_adjustments = []

    # Real computation: calculate adjusted load
    for node_id, node in nodes.items():
        raw_load = node['load']
        service_count = len(node['services'])
        
        # Distractor: irrelevant transformation
        normalized_name = ''.join(ch.lower() for ch in node['name'] if ch.isalnum())
        
        efficiency = analyze_node_efficiency(node)
        efficiency_map[node_id] = efficiency
        
        # Core logic contribution
        adjusted_load = raw_load * efficiency
        if service_count > 2:
            adjusted_load *= 0.95  # minor optimization
        
        # Red herring: collected but not used in final sum
        temp_adjustments.append(adjusted_load * 0.1)
        
        total_load += adjusted_load

    # Secondary processing with filtering
    high_load_nodes = []
    for nid in efficiency_map:
        if nodes[nid]['load'] > 40:
            high_load_nodes.append(nid)
    
    # Fake correction factor (unused)
    correction_factor = len(high_load_nodes) * 1.5 if total_load > 100 else 0
    
    # Final adjustment based on system-wide thresholds
    if total_load > 150:
        total_load *= 0.9
    elif total_load < 50:
        total_load *= 1.1
    
    # Final balancing step
    avg_service_count = sum(len(n['services']) for n in nodes.values()) / len(nodes)
    if avg_service_count > 2.0:
        total_load -= 5
    
    return int(total_load)

# Initialize system nodes
nodes = {
    'N1': {'name': 'Gateway-A', 'load': 45, 'services': ['auth', 'route', 'monitor']},
    'N2': {'name': 'Storage-B', 'load': 30, 'services': ['disk', 'backup']},
    'N3': {'name': 'Compute-C', 'load': 60, 'services': ['worker', 'queue', 'dns', 'api']},
    'N4': {'name': 'Edge-D', 'load': 25, 'services': ['proxy']}
}

# Track auxiliary metrics (distractor)
cpu_utilization = defaultdict(float)
for k, v in nodes.items():
    cpu_utilization[k] = v['load'] * 0.01

# Irrelevant precomputation
service_set = set()
for node in nodes.values():
    service_set.update(node['services'])
service_hash = sum(hash(s) % 100 for s in service_set)

# Key execution point
final_load = balance_workload(nodes)

# Output result
print(f"Result: {final_load}")