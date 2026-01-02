def analyze_network_load(nodes, threshold=100):
    load_distribution = [len(node['connections']) * node['weight'] for node in nodes]
    high_load_nodes = [i for i, load in enumerate(load_distribution) if load > threshold]
    return set(high_load_nodes)


def calculate_node_efficiency(node_list):
    efficiency_scores = []
    total_links = 0
    
    for node in node_list:
        connections = len(node['connections'])
        weight = node['weight']
        score = (connections ** 0.5) * weight
        efficiency_scores.append(score)
        total_links += connections
    
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores) if efficiency_scores else 0
    return efficiency_scores, avg_efficiency, total_links


def calculate_system_capacity(selected_nodes):
    base_capacity = 0
    bonus_multiplier = 1.0
    
    for node in selected_nodes:
        base_capacity += len(node['connections']) * 2
        if node['type'] == 'core':
            bonus_multiplier += 0.1
        elif node['type'] == 'edge' and len(node['connections']) > 3:
            bonus_multiplier += 0.05
    
    # Misleading intermediate calculation (not directly used in final logic)
    theoretical_max = len(selected_nodes) * 50
    utilization_rate = base_capacity / theoretical_max if theoretical_max > 0 else 0
    
    adjusted_capacity = base_capacity * bonus_multiplier
    
    # Red herring: unused diagnostic variable
    diagnostic_trace = { 'nodes': len(selected_nodes), 'max_bonus': bonus_multiplier }
    
    return int(adjusted_capacity)

# System configuration data
network_nodes = [
    {'id': 'A', 'connections': ['B', 'C', 'D'], 'weight': 8, 'type': 'core'},
    {'id': 'B', 'connections': ['A', 'E'], 'weight': 5, 'type': 'relay'},
    {'id': 'C', 'connections': ['A', 'F', 'G', 'H'], 'weight': 6, 'type': 'edge'},
    {'id': 'D', 'connections': ['A', 'I', 'J'], 'weight': 9, 'type': 'core'},
    {'id': 'E', 'connections': ['B', 'K'], 'weight': 4, 'type': 'leaf'},
    {'id': 'F', 'connections': ['C'], 'weight': 3, 'type': 'leaf'},
    {'id': 'G', 'connections': ['C', 'L'], 'weight': 7, 'type': 'edge'},
    {'id': 'H', 'connections': ['C'], 'weight': 2, 'type': 'leaf'},
    {'id': 'I', 'connections': ['D'], 'weight': 5, 'type': 'leaf'},
    {'id': 'J', 'connections': ['D', 'M'], 'weight': 6, 'type': 'edge'},
    {'id': 'K', 'connections': ['E'], 'weight': 3, 'type': 'leaf'},
    {'id': 'L', 'connections': ['G'], 'weight': 4, 'type': 'leaf'},
    {'id': 'M', 'connections': ['J'], 'weight': 5, 'type': 'leaf'}
]

# Step 1: Identify high-load nodes (distractor path)
decision_set = analyze_network_load(network_nodes, threshold=15)

# Step 2: Compute efficiency metrics (semi-relevant)
efficiencies, avg_eff, total_edges = calculate_node_efficiency(network_nodes)

# Step 3: Determine optimal nodes based on combined criteria
optimal_nodes = []
for idx, node in enumerate(network_nodes):
    eff_score = efficiencies[idx] if idx < len(efficiencies) else 0
    is_high_load = idx in decision_set
    
    # Core logic for selection
    if node['weight'] >= 6 or (eff_score >= avg_eff and node['type'] in ['core', 'edge']):
        if not is_high_load or node['type'] == 'core':  # Prefer core even if overloaded
            optimal_nodes.append(node)

# Step 4: Calculate final system capacity (target computation)
final_capacity = calculate_system_capacity(optimal_nodes)

# Output result
print(f"Result: {final_capacity}")