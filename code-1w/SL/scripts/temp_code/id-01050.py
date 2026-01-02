def analyze_node_health(health_scores):
    weighted_sum = 0
    total_weight = 0
    for i, score in enumerate(health_scores):
        weight = (i + 1) ** 0.5
        weighted_sum += score * weight
        total_weight += weight
    return weighted_sum / total_weight if total_weight != 0 else 0


def calculate_system_capacity(nodes, efficiency_map):
    base_capacity = 0
    adjustment_factor = 0.0
    temp_buffer = []
    
    for idx, node in enumerate(nodes):
        load = node['load']
        core_count = node['cores']
        frequency = node['frequency']
        
        # Relevant calculation
        capacity_contribution = core_count * frequency * (1 - load)
        base_capacity += capacity_contribution
        
        # Distractor: collecting unused intermediate values
        temp_buffer.append(load * core_count)
        adjustment_factor += len(temp_buffer) * 0.01  # Irrelevant accumulation

    # Real logic using dictionary operations
    efficiency_total = 0
    for name, factor in efficiency_map.items():
        if 'backup' not in name:
            efficiency_total += factor

    # Key computation step
    stabilized_capacity = base_capacity * (efficiency_total / len(efficiency_map))
    
    # Secondary distractor block: dead code path (never executed due to fixed condition)
    emergency_mode = False
    emergency_override = 0
    if emergency_mode and len(nodes) > 100:
        for n in nodes:
            emergency_override += n['cores'] // 2

    # Another distraction: unnecessary zip usage
    indices = list(range(len(nodes)))
    for i, n in zip(indices, nodes):
        adjustment_factor += (n['frequency'] - 2.0) * 0.001  # Minimal irrelevant effect

    final_capacity = int(stabilized_capacity - adjustment_factor * 100)
    
    return final_capacity

# Main execution
node_list = [
    {'load': 0.2, 'cores': 8, 'frequency': 3.2},
    {'load': 0.35, 'cores': 12, 'frequency': 2.8},
    {'load': 0.1, 'cores': 16, 'frequency': 3.5},
    {'load': 0.5, 'cores': 6, 'frequency': 2.5}
]

efficiency_factors = {
    'node_alpha': 0.95,
    'node_beta': 0.92,
    'backup_monitor': 0.3,  
    'node_gamma': 0.98
}

health_metrics = [88, 91, 79, 94]

# Trigger health analysis (distractor - result not used in final answer)
current_health_index = analyze_node_health(health_metrics)

# Key statement
final_capacity = calculate_system_capacity(node_list, efficiency_factors)

print(f"Result: {final_capacity}")