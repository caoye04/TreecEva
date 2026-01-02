def calculate_node_weight(node_id, load_factor):
    return (node_id * 3 + load_factor ** 2) % 17

def analyze_connection_density(edges):
    if len(edges) == 0:
        return 0
    max_node = max(max(edge) for edge in edges)
    density = len(edges) / (max_node * (max_node - 1) / 2) if max_node > 1 else 0
    return round(density, 3)

def calculate_system_capacity(nodes):
    total_weight = 0
    weight_map = {}
    
    # Simulate node initialization and weighting
    for i, node in enumerate(nodes):
        raw_weight = calculate_node_weight(node['id'], node['load'])
        adjusted_weight = raw_weight * (1 + node['priority'] * 0.1)
        weight_map[node['name']] = adjusted_weight
        total_weight += adjusted_weight
    
    # Distractor: unused structure processing
    temp_scores = [w * 0.95 for w in weight_map.values() if w > 10]
    avg_temp = sum(temp_scores) / len(temp_scores) if temp_scores else 0
    penalty = 0
    for score in temp_scores:
        if score > avg_temp:
            penalty += 1
    
    # Real logic continues: apply environmental stress factor
    stress_factor = 1.0
    if len(nodes) > 5:
        stress_factor *= 0.95
    if any(n['load'] > 80 for n in nodes):
        stress_factor *= 0.88
    
    # Use list comprehension to filter high-priority nodes
    hp_nodes = [n for n in nodes if n['priority'] >= 3]
    hp_contribution = sum([calculate_node_weight(n['id'], n['load']) for n in hp_nodes])
    
    # Distractor: irrelevant string manipulation
    labels = [n['name'].upper() for n in nodes]
    label_hash = sum([hash(l) % 100 for l in labels]) % 50
    
    # Distractor: dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print("Debug:", weight_map)
        redundant_calc = [x**2 for x in range(50)]

    # Main capacity formula
    base_capacity = total_weight * stress_factor * 100
    bonus = hp_contribution * 1.5 if len(hp_nodes) > 2 else 0
    
    # Final adjustment using dictionary aggregation
    stats_summary = {
        'count': len(nodes),
        'high_priority_count': len(hp_nodes),
        'total_weight': total_weight,
        'bonus_applied': bonus > 0
    }
    
    final_capacity = int(base_capacity + bonus)
    
    # This line is critical - output must match
    return final_capacity

# Define network configuration
network_nodes = [
    {'id': 12, 'name': 'alpha', 'load': 65, 'priority': 2},
    {'id': 7, 'name': 'beta', 'load': 45, 'priority': 3},
    {'id': 19, 'name': 'gamma', 'load': 88, 'priority': 4},
    {'id': 3, 'name': 'delta', 'load': 23, 'priority': 1},
    {'id': 14, 'name': 'epsilon', 'load': 77, 'priority': 3},
    {'id': 8, 'name': 'zeta', 'load': 54, 'priority': 3},
    {'id': 5, 'name': 'eta', 'load': 30, 'priority': 2}
]

# Calculate connection density as distractor
connections = [(12,7), (7,19), (19,3), (3,14), (14,8), (8,5), (5,12), (7,14)]
connection_density = analyze_connection_density(connections)

# Key execution point
final_capacity = calculate_system_capacity(network_nodes)
print(f"Result: {final_capacity}")