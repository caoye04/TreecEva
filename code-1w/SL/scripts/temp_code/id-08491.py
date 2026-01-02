def calculate_remaining_capacity(nodes, failed):
    active_nodes = nodes - failed
    redundancy_factor = 3
    base_capacity_per_node = 150
    total_capacity = len(active_nodes) * base_capacity_per_node
    usable_capacity = total_capacity // redundancy_factor
    
    # Irrelevant tracking variable (minor distraction)
    node_status_log = {node: 'active' for node in active_nodes}
    
    maintenance_overhead = 10
    final_capacity = usable_capacity - maintenance_overhead
    return final_capacity

# System configuration
all_nodes = {'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'}
failed_nodes_set = {'n3', 'n7'}

# Calculation entry point
final_capacity = calculate_remaining_capacity(all_nodes, failed_nodes_set)
print(f"Result: {final_capacity}")