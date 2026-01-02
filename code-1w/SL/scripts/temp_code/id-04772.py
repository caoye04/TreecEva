def calculate_network_capacity():
    nodes = ['router_A', 'switch_B', 'hub_C', 'bridge_D']
    base_loads = [120, 85, 95, 110]
    efficiency_factors = [0.9, 1.1, 0.8, 1.0]

    # Apply efficiency corrections to base loads
    adjusted_loads = [base * eff for base, eff in zip(base_loads, efficiency_factors)]

    # Identify underutilized nodes
    threshold = 100
    underused_nodes = {name: load for name, load in zip(nodes, adjusted_loads) if load < threshold}

    # Simulate redistribution of excess load from overperforming nodes
    excess_pool = 0
    optimized_loads = []
    for load in adjusted_loads:
        if load > threshold:
            excess = load - threshold
            excess_pool += excess * 0.7  # 70% of excess is reallocated
        optimized_loads.append(min(load, threshold))

    # Reinject pooled capacity across underused nodes
    if underused_nodes:
        redistribution_share = excess_pool / len(underused_nodes)
        optimized_loads = [
            load + redistribution_share if name in underused_nodes else load
            for load, name in zip(optimized_loads, nodes)
        ]

    total_capacity = sum(optimized_loads)
    return total_capacity

result = calculate_network_capacity()
print(f"Result: {result}")