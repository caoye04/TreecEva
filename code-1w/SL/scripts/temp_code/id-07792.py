def analyze_network_load(nodes, thresholds):
    load_profile = set()
    temp_buffer = 0
    for node in nodes:
        if node > thresholds['high']:
            load_profile.add('critical')
            temp_buffer += node * 0.1
        elif node > thresholds['medium']:
            load_profile.add('elevated')
            temp_buffer -= node * 0.05
        else:
            load_profile.add('normal')
    return load_profile, temp_buffer


def calculate_system_capacity(active_nodes, constraints):
    base_capacity = 1000
    efficiency_factor = 0.9
    penalty_rate = 0.15
    
    # Misleading intermediate calculation (not used in final result)
    dummy_analysis = [x ** 2 for x in range(len(active_nodes)) if x % 2 == 0]
    buffer_waste = sum(dummy_analysis) / (len(dummy_analysis) + 1) if dummy_analysis else 0
    
    # Real logic begins
    high_stress_count = 0
    total_utilization = 0
    
    for idx, node in enumerate(active_nodes):
        if node >= constraints['threshold']:
            high_stress_count += 1
            total_utilization += node * efficiency_factor
        else:
            total_utilization += node * (efficiency_factor - penalty_rate)
    
    # Simulate conditional branching effect
    adjustment = 0
    if high_stress_count > len(active_nodes) // 2:
        adjustment = -50
    elif high_stress_count == 0:
        adjustment = 30
    
    # Use of set operations to filter unique stress levels
    stress_levels = set()
    for node in active_nodes:
        if node > constraints['threshold']:
            stress_levels.add('overloaded')
        elif node > constraints['threshold'] * 0.7:
            stress_levels.add('stressed')
        else:
            stress_levels.add('stable')
    
    # Red herring: complex-looking but unused metric
    resilience_score = len(stress_levels) * 10 - buffer_waste
    
    # Final capacity depends only on total_utilization and adjustment
    final_capacity = int(base_capacity + total_utilization // 10 + adjustment)
    
    return final_capacity

# Main execution
node_metrics = [85, 92, 76, 88, 95]
config_limits = {'threshold': 80, 'high': 90, 'medium': 75}

# Initial analysis (side computation)
analysis_result, transient_load = analyze_network_load(node_metrics, config_limits)

# Key assignment
final_capacity = calculate_system_capacity(node_metrics, config_limits)

print(f"Result: {final_capacity}")