def calculate_remaining_capacity(nodes):
    total_capacity = 0
    used_capacity = 0
    for node in nodes.values():
        total_capacity += node['max_storage']
        used_capacity += node['current_usage']
    
    # Irrelevant variable (minimal distraction)
    temp_warning_flag = False
    if used_capacity / total_capacity > 0.8:
        temp_warning_flag = True
    
    remaining = total_capacity - used_capacity
    return remaining

# Simulated distributed storage system node data
storage_nodes = {
    'node_01': {'max_storage': 1500, 'current_usage': 950},
    'node_02': {'max_storage': 2000, 'current_usage': 1400},
    'node_03': {'max_storage': 1800, 'current_usage': 1100},
    'node_04': {'max_storage': 1600, 'current_usage': 900}
}

# Additional irrelevant variable (low interference)
redundancy_factor = 1.2

final_capacity = calculate_remaining_capacity(storage_nodes)
print(f"Result: {final_capacity}")