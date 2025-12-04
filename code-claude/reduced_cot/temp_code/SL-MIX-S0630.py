def calculate_path(network, start, end):
    # Network analysis for optimal path calculation
    distances = {node: float('inf') for node in network}
    distances[start] = 0
    visited = set()
    
    # Priority factors for node evaluation
    priority_factors = {'A': 5, 'B': 3, 'C': 7, 'D': 2, 'E': 4}
    adjustment_values = {'A': 10, 'B': 15, 'C': 5, 'D': 20, 'E': 8}
    
    # Historical path data (unused but provides context)
    historical_paths = {
        ('A', 'B'): [12, 15, 18],
        ('B', 'C'): [9, 11, 14],
        ('C', 'D'): [22, 25],
        ('D', 'E'): [7, 8, 10],
        ('A', 'E'): [19, 21]
    }
    
    # Process nodes in order of their connections
    unprocessed = list(network.keys())
    
    while unprocessed:
        # Find node with minimum distance
        current = min(unprocessed, key=lambda x: distances[x])
        
        if current == end:
            break
            
        unprocessed.remove(current)
        visited.add(current)
        
        # Calculate alternative paths
        for neighbor, weight in network[current].items():
            if neighbor in visited:
                continue
                
            # Apply traffic conditions (not relevant to shortest path)
            traffic_factor = (ord(neighbor) % 3) + 1
            congestion_level = (ord(current) + ord(neighbor)) % 4
            
            # Calculate alternative distance
            alt_distance = distances[current] + weight
            
            # Update if shorter path found
            if alt_distance < distances[neighbor]:
                distances[neighbor] = alt_distance
    
    # Calculate weather impact (distracting calculation)
    weather_impact = sum([adjustment_values[node] for node in visited if node in adjustment_values])
    weather_factor = weather_impact % 10
    
    # Calculate path optimization metrics
    optimization_score = 100
    for node in visited:
        if node in priority_factors:
            optimization_score -= priority_factors[node]
    
    # Return the shortest path length
    return distances[end]

# Define network topology
network = {
    'A': {'B': 12, 'C': 14, 'E': 8},
    'B': {'A': 12, 'C': 9, 'D': 11},
    'C': {'A': 14, 'B': 9, 'D': 15, 'E': 20},
    'D': {'B': 11, 'C': 15, 'E': 7},
    'E': {'A': 8, 'C': 20, 'D': 7}
}

# Define nodes for analysis
starting_node = 'A'
intermediate_nodes = ['B', 'C']
target_node = 'D'

# Calculate alternative paths for comparison
alt_path1 = calculate_path(network, starting_node, intermediate_nodes[0])
alt_path2 = calculate_path(network, intermediate_nodes[1], target_node)

# These calculations aren't used in the final result
potential_savings = (alt_path1 * 0.8) + (alt_path2 * 0.6)
traffic_adjustment = sum([ord(n) for n in intermediate_nodes]) % 10

# Calculate direct path
optimal_path_length = calculate_path(network, starting_node, target_node)

# Calculate theoretical efficiency (unused)
efficiency = optimal_path_length / (alt_path1 + alt_path2) if (alt_path1 + alt_path2) > 0 else 0

# Additional metrics for report (not used in final answer)
network_density = len(network) / sum(len(connections) for connections in network.values())
path_complexity = optimal_path_length * network_density

print(f"Result: {optimal_path_length}")