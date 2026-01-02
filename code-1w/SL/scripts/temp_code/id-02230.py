def analyze_network_load():
    node_loads = [12, 7, 15, 3, 9, 18, 4, 6]
    threshold = 10
    high_load_nodes = {node for node in node_loads if node > threshold}
    low_load_nodes = {node for node in node_loads if node <= threshold}
    
    # Perform set difference to identify nodes that are only in high load
    isolated_high = high_load_nodes - low_load_nodes
    
    # List of active nodes above dynamic criterion
    filtered_nodes = [node for node in node_loads if node in isolated_high]
    
    base_multiplier = 2.5
    adjustment = 0.2
    scaling_factor = base_multiplier * (1 + adjustment)
    
    active_threshold = len(filtered_nodes) * scaling_factor
    
    # Irrelevant tracking variable (minor distraction)
    total_iterations = 0
    for i in range(len(node_loads)):
        total_iterations += 1
    
    print(f"Result: {active_threshold}")

analyze_network_load()