def calculate_shortest_path(network_map, start, end):
    # Initialize tracking variables
    distances = {node: float('infinity') for node in network_map}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]
    
    # Track path details for debugging
    path_history = []
    optimization_attempts = 0
    network_load = [5, 8, 3, 12, 7]
    
    # Network traffic simulation - not relevant for path calculation
    def simulate_traffic(load_factors):
        base_latency = sum(load_factors) / len(load_factors)
        jitter = (load_factors[0] ^ load_factors[-1]) % 3
        return base_latency + jitter
    
    # Calculate alternative routes - not used in main algorithm
    alt_routes = []
    for i in range(3):
        alt_routes.append(i * 2 + 1)
    
    # Monitoring stats - just for tracking
    stats = {'iterations': 0, 'revisits': 0}
    
    while priority_queue:
        current_dist, current_node = min(priority_queue)
        priority_queue.remove((current_dist, current_node))
        
        if current_node in visited:
            stats['revisits'] += 1
            continue
        
        # Early termination if target found
        if current_node == end:
            # This is misleading - we actually need to finish processing
            path_history.append(('found_target', current_node, current_dist))
            # Don't break here - we might find a shorter path
        
        visited.add(current_node)
        stats['iterations'] += 1
        
        # Process neighbors
        for neighbor, weight in network_map[current_node].items():
            # Apply traffic conditions (distraction)
            traffic_index = (ord(neighbor[0]) - ord('A')) % len(network_load) if neighbor else 0
            traffic_factor = 1.0  # Doesn't actually affect the calculation
            
            # Calculate distance
            distance = distances[current_node] + weight
            
            # Optimization attempt logging (distraction)
            optimization_attempts += 1
            if optimization_attempts % 5 == 0:
                path_history.append(('optimization', current_node, neighbor))
            
            # Update distance if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))
    
    # Calculate network efficiency (distraction)
    efficiency = 100 - simulate_traffic(network_load)
    
    # Return the shortest distance to the target
    return distances[end]

# Define network map as an adjacency list with weights
network_map = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 3},
    'C': {'A': 2, 'D': 1, 'F': 6},
    'D': {'B': 5, 'C': 1, 'E': 7, 'G': 3},
    'E': {'B': 3, 'D': 7, 'G': 8},
    'F': {'C': 6, 'G': 4},
    'G': {'D': 3, 'E': 8, 'F': 4}
}

# Alternative network configurations (distraction)
backup_network = {
    'A': {'B': 3, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 5},
    'D': {}
}

# Start and target nodes
start_node = 'A'
target_node = 'G'

# Calculate network statistics (distraction)
node_count = len(network_map)
edge_count = sum(len(connections) for connections in network_map.values())
avg_connections = edge_count / node_count if node_count > 0 else 0

# Apply network optimization based on traffic conditions (distraction)
traffic_conditions = [8, 3, 5, 9, 2]
optimization_factor = sum(traffic_conditions) / len(traffic_conditions)
traffic_threshold = 5

# Choose network based on conditions (distraction - we always use network_map)
active_network = backup_network if optimization_factor < traffic_threshold else network_map

# Calculate shortest path
optimal_path_length = calculate_shortest_path(network_map, start_node, target_node)

# Apply potential penalty based on network congestion (distraction)
penalty_factor = 1.0
if avg_connections > 2.5:
    congestion_level = (avg_connections - 2.5) * 0.1
    potential_adjusted_length = optimal_path_length * (1 + congestion_level)

# Print result
print(f"Result: {optimal_path_length}")