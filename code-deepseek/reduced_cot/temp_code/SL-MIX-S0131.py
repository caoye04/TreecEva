def process_network_data(nodes):
    active_nodes = [node for node in nodes if node['status'] == 'active']
    total_capacity = sum(node['capacity'] for node in active_nodes)
    
    # Distractor: Calculate average but don't use it
    avg_capacity = total_capacity / len(active_nodes) if active_nodes else 0
    
    # Semi-relevant: Check connectivity patterns
    connectivity_scores = list(map(lambda x: x['connections'] % 7, active_nodes))
    connectivity_sum = sum(connectivity_scores)
    
    # Key calculation using modular arithmetic
    processed_value = (total_capacity * 3) % 17
    processed_value += connectivity_sum if connectivity_sum % 2 == 0 else 0
    
    # Distractor: Create unused analysis dict
    analysis_dict = {
        'active_count': len(active_nodes),
        'total_capacity': total_capacity,
        'avg_capacity': avg_capacity,
        'connectivity': connectivity_sum
    }
    
    return processed_value

# Network configuration
network_nodes = [
    {'status': 'active', 'capacity': 25, 'connections': 8},
    {'status': 'inactive', 'capacity': 40, 'connections': 12},
    {'status': 'active', 'capacity': 18, 'connections': 5},
    {'status': 'active', 'capacity': 32, 'connections': 9},
    {'status': 'maintenance', 'capacity': 28, 'connections': 7}
]

# Main execution
final_analysis = process_network_data(network_nodes)
print(f"Result: {final_analysis}")