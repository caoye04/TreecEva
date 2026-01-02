def analyze_system_performance():
    base_nodes = 8
    expansion_factor = 1.5
    node_capacities = [base_nodes * (expansion_factor ** i) for i in range(6)]
    
    # Simulate load distribution across nodes
    raw_loads = [node_capacities[i] * (0.8 - 0.1 * i) for i in range(len(node_capacities))]
    
    # Normalize loads and filter out underutilized segments
    normalized_loads = [load / capacity for load, capacity in zip(raw_loads, node_capacities)]
    active_segments = [i for i, load in enumerate(normalized_loads) if load > 0.5]
    system_loads_filtered = [raw_loads[i] for i in active_segments]
    
    # Irrelevant tracking variable (minimal interference)
    total_segments_analyzed = len(raw_loads)
    
    peak_capacity = max(system_loads_filtered)
    return peak_capacity

result = analyze_system_performance()
print(f"Result: {result}")