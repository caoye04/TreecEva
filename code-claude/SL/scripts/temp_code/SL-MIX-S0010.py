import itertools

def calculate_network_priority(nodes):
    # Extract only active nodes with proper configuration
    valid_nodes = [n for n in nodes if n['active'] and n['config'] is not None]
    
    # This is the critical calculation
    if valid_nodes:
        return sum(n['weight'] * (n['priority'] % 10) for n in valid_nodes)
    return 0

def analyze_network_topology(connections):
    # Analyze network connections (not used in final calculation)
    paths = []
    for a, b in itertools.combinations(range(len(connections)), 2):
        if connections[a][b]:
            paths.append((a, b, connections[a][b]))
    
    # Misleading metrics calculation
    total_bandwidth = sum(p[2] for p in paths)
    avg_latency = total_bandwidth / len(paths) if paths else 0
    return {'paths': len(paths), 'bandwidth': total_bandwidth, 'latency': avg_latency}

# Network node definitions
nodes = [
    {'id': 1, 'name': 'router-1', 'active': True, 'priority': 23, 'weight': 5, 'config': {'ip': '10.0.0.1'}},
    {'id': 2, 'name': 'switch-1', 'active': True, 'priority': 17, 'weight': 3, 'config': {'ip': '10.0.0.2'}},
    {'id': 3, 'name': 'server-1', 'active': False, 'priority': 42, 'weight': 8, 'config': {'ip': '10.0.0.3'}},
    {'id': 4, 'name': 'router-2', 'active': True, 'priority': 19, 'weight': 4, 'config': None},
    {'id': 5, 'name': 'firewall-1', 'active': True, 'priority': 31, 'weight': 7, 'config': {'ip': '10.0.0.5'}}
]

# Connection matrix (adjacency matrix)
connections = [
    [0, 10, 5, 0, 8],
    [10, 0, 15, 12, 0],
    [5, 15, 0, 6, 9],
    [0, 12, 6, 0, 7],
    [8, 0, 9, 7, 0]
]

# Calculate security risk (misleading calculation)
def calculate_security_risk(nodes, connections):
    risk_factor = sum(n['priority'] for n in nodes if n['active']) / len(nodes)
    exposed_connections = sum(1 for row in connections for val in row if val > 10)
    return risk_factor * exposed_connections / 10

# Process data for different scenarios
scenario_weights = [0.3, 0.5, 0.2]
security_risk = calculate_security_risk(nodes, connections)
topology_metrics = analyze_network_topology(connections)

# Filter nodes based on complex conditions
filtered_nodes = []
for node in nodes:
    # Skip nodes with even IDs for test scenario (misleading condition)
    if security_risk > 20 and node['id'] % 2 == 0:
        continue
        
    # Include node if it meets certain criteria
    if node['active'] and (node['priority'] > 15 or node['name'].startswith('router')):
        # Deep copy to avoid modifying original
        node_copy = node.copy()
        
        # Adjust priority based on name (misleading calculation)
        if 'server' in node['name']:
            node_copy['priority'] += 10
        
        filtered_nodes.append(node_copy)

# Calculate composite metrics (misleading)
composite_score = topology_metrics['bandwidth'] * scenario_weights[0] + \
                  topology_metrics['latency'] * scenario_weights[1] + \
                  security_risk * scenario_weights[2]

# This is the key statement
final_priority = calculate_network_priority(filtered_nodes)

# Calculate alternative priority (misleading)
alt_priority = sum(n['priority'] for n in filtered_nodes if n['weight'] > 4)

print(f"Topology metrics: {topology_metrics}")
print(f"Security risk: {security_risk}")
print(f"Composite score: {composite_score}")
print(f"Alternative priority: {alt_priority}")
print(f"Result: {final_priority}")