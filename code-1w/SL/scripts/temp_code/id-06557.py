def calculate_system_load():
    base_loads = {'node_a': 12, 'node_b': 15, 'node_c': 10}
    adjustments = {'node_a': 3, 'node_b': -2, 'node_c': 5}
    
    system_loads = {}
    for node in base_loads:
        system_loads[node] = base_loads[node] + adjustments[node]
    
    peak_utilization = 0.9
    redundancy_offset = int(peak_utilization * 5)
    
    temp_correction = 2  # Irrelevant adjustment for sensor offset (distractor)
    final_load = max(system_loads.values()) + redundancy_offset
    
    return final_load

result = calculate_system_load()
print(f"Result: {result}")