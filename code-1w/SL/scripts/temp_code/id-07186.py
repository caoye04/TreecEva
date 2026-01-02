def analyze_node_health(node_data):
    healthy_count = 0
    temp_threshold = 75.0
    for node_id, metrics in node_data.items():
        temperature = metrics['temp']
        uptime = metrics['uptime']
        status = metrics['status']
        
        # Irrelevant health check (distractor)
        if uptime > 1000 and status == 'active':
            baseline_score = 85
        else:
            baseline_score = 60
            
        # Actual relevance: only temperature affects capacity
        if temperature < temp_threshold:
            healthy_count += 1

    return healthy_count


def calculate_system_capacity(nodes, efficiency_map):
    total_weight = 0.0
    base_multiplier = 1.0
    adjustment_factor = 0.05
    
    # Real computation begins
    active_nodes = [nid for nid, props in nodes.items() if props['status'] == 'active']
    idle_nodes = [nid for nid, props in nodes.items() if props['status'] == 'idle']
    
    # Dummy tracking variables (distractors)
    max_uptime = max(nodes[nid]['uptime'] for nid in nodes)
    avg_temp = sum(nodes[nid]['temp'] for nid in nodes) / len(nodes)
    
    for idx, node_id in enumerate(active_nodes):
        weight = nodes[node_id]['weight']
        efficiency_key = f"node_{node_id % 3}"
        
        # Conditional expression with zip and enumerate (required features)
        efficiency_bonus = efficiency_map[efficiency_key] if efficiency_key in efficiency_map else 0.1
        
        # Core calculation
        contribution = weight * (1 + efficiency_bonus)
        
        # Use of string method (required feature)
        label = str(node_id).zfill(3)
        if label.startswith('0'):
            contribution *= 1.02  # minor boost for formatting?

        total_weight += contribution

    # Another distractor: combinatorics-like count that isn't used
    possible_pairs = 0
    for i in range(len(idle_nodes)):
        for j in range(i + 1, len(idle_nodes)):
            possible_pairs += 1
    
    # Final capacity depends only on total_weight and base multiplier
    final_capacity = int(total_weight * base_multiplier)
    
    # This print is required
    print(f"Result: {final_capacity}")
    return final_capacity

# Setup data
node_info = {
    1: {'temp': 70, 'uptime': 1200, 'status': 'active', 'weight': 10},
    2: {'temp': 80, 'uptime': 500, 'status': 'active', 'weight': 15},
    3: {'temp': 68, 'uptime': 2000, 'status': 'idle', 'weight': 12},
    4: {'temp': 72, 'uptime': 800, 'status': 'active', 'weight': 20},
    5: {'temp': 78, 'uptime': 300, 'status': 'idle', 'weight': 8}
}

efficiency_factors = {
    'node_0': 0.15,
    'node_1': 0.20,
    'node_2': 0.10
}

# Execute
final_capacity = calculate_system_capacity(node_info, efficiency_factors)