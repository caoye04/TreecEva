def calculate_optimal_distance(graph, source, target):
    # A function to find the shortest path in a network
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
    unvisited = set(graph.keys())
    
    # Initialize metrics tracking (not used in core algorithm)
    metrics = {
        'iterations': 0,
        'pruned_paths': 0,
        'potential_routes': len(graph) * (len(graph) - 1) // 2
    }
    
    # Temporary storage for alternative paths
    alternative_routes = []
    for i in range(5):
        alternative_routes.append((source, target, i * 10 + 5))
    
    while unvisited:
        # Find the node with minimum distance
        current = min(unvisited, key=lambda x: distances[x])
        
        # Early termination if target reached
        if current == target:
            break
            
        # Track iterations for performance analysis
        metrics['iterations'] += 1
        
        # Remove from unvisited set
        unvisited.remove(current)
        
        # Calculate path entropy (unused metric)
        path_entropy = sum([ord(c) for c in current]) % 17
        if path_entropy > 10:
            metrics['high_entropy_nodes'] = metrics.get('high_entropy_nodes', 0) + 1
        
        # Process neighbors
        for neighbor, weight in graph[current].items():
            if neighbor in unvisited:
                # Apply bitwise operations to weight for "optimization"
                optimized_weight = weight
                if weight & 1:  # If odd
                    optimized_weight = (weight << 2) >> 2  # No-op bitshift
                
                # Calculate potential new distance
                new_distance = distances[current] + optimized_weight
                
                # Record alternative route (not used)
                if len(alternative_routes) < 10 and new_distance > distances[current] * 1.5:
                    alternative_routes.append((current, neighbor, new_distance))
                    metrics['pruned_paths'] += 1
                
                # Update distance if shorter path found
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    # Calculate network density (unused metric)
    edge_count = sum(len(connections) for connections in graph.values())
    possible_edges = len(graph) * (len(graph) - 1)
    network_density = edge_count / possible_edges if possible_edges > 0 else 0
    
    # Generate report (not affecting result)
    report = {
        'source': source,
        'target': target,
        'path_count': len(alternative_routes),
        'density': network_density,
        'metrics': metrics
    }
    
    # Apply normalization factor based on graph size (not actually used)
    normalization = len(graph) / 10
    normalized_distance = distances[target] / normalization
    
    # Return the actual distance
    return distances[target]

# Define network graph with nodes and edge weights
network_graph = {
    'A': {'B': 5, 'C': 3, 'E': 11},
    'B': {'A': 5, 'D': 2, 'F': 7},
    'C': {'A': 3, 'D': 6, 'E': 5},
    'D': {'B': 2, 'C': 6, 'F': 4},
    'E': {'A': 11, 'C': 5, 'F': 8},
    'F': {'B': 7, 'D': 4, 'E': 8}
}

# Define unused alternative graph for comparison
alternative_graph = {
    'X': {'Y': 2, 'Z': 4},
    'Y': {'X': 2, 'Z': 1},
    'Z': {'X': 4, 'Y': 1}
}

# Set source and target nodes
source_node = 'A'
target_node = 'F'

# Calculate path statistics (not used in final result)
path_stats = {}
for node in network_graph:
    connections = len(network_graph[node])
    path_stats[node] = {
        'connections': connections,
        'centrality': connections / (len(network_graph) - 1),
        'avg_weight': sum(network_graph[node].values()) / connections
    }

# Create sets for network analysis (not used in core calculation)
visited_set = set()
unreachable = set()

# Perform string operations on node names (distraction)
node_chars = ''.join(sorted(network_graph.keys()))
char_frequency = {c: node_chars.count(c) for c in set(node_chars)}

# Generate node pairs for potential routes
node_pairs = []
for i, node1 in enumerate(sorted(network_graph.keys())):
    for node2 in list(sorted(network_graph.keys()))[i+1:]:
        node_pairs.append((node1, node2))

# Calculate zipped node information (distraction)
node_info = {}
for i, (node, stats) in enumerate(zip(network_graph.keys(), path_stats.values())):
    node_info[node] = (i, stats.get('connections', 0))

# Calculate the optimal path length
optimal_path_length = calculate_optimal_distance(network_graph, source_node, target_node)

# Apply unnecessary transformations (not affecting result)
if optimal_path_length > 0:
    transformed_length = optimal_path_length * 2 - optimal_path_length
else:
    transformed_length = 0

print(f"Result: {optimal_path_length}")