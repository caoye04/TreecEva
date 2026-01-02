def calculate_network_capacity():
    base_nodes = [12, 8, 15, 7, 11]
    expansion_factor = 1.5
    min_threshold = 10
    
    # Adjust node loads based on threshold and expansion
    adjusted_loads = []
    for i, load in enumerate(base_nodes):
        if load < min_threshold:
            adjusted_load = load * expansion_factor
        else:
            adjusted_load = load + 2
        adjusted_loads.append(int(adjusted_load))
    
    # Secondary computation (irrelevant to final result)
    avg_load = sum(base_nodes) / len(base_nodes)
    peak_index = 0
    for i, val in enumerate(base_nodes):
        if val > base_nodes[peak_index]:
            peak_index = i
    
    total_capacity = sum(adjusted_loads)
    return total_capacity

result = calculate_network_capacity()
print(f"Result: {result}")