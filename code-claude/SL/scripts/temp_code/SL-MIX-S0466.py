from collections import defaultdict, Counter
import itertools

def calculate_network_stats(graph):
    # Calculate various network statistics (not relevant for main task)
    node_count = len(graph)
    edge_count = sum(len(connections) for connections in graph.values())
    density = edge_count / (node_count * (node_count - 1)) if node_count > 1 else 0
    
    # Calculate node degrees
    degrees = [len(connections) for connections in graph.values()]
    degree_distribution = Counter(degrees)
    
    # Calculate clustering coefficient (simplified version)
    clustering = sum(degrees) / node_count if node_count > 0 else 0
    
    return {
        'node_count': node_count,
        'edge_count': edge_count,
        'density': density,
        'degree_distribution': degree_distribution,
        'clustering': clustering
    }

def find_all_paths(graph, start, end, path=None, all_paths=None):
    # This function finds all possible paths between two nodes
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []
    
    path = path + [start]
    
    if start == end:
        return all_paths + [path]
    
    if start not in graph:
        return all_paths
    
    for node in graph[start]:
        if node not in path:  # Avoid cycles
            new_paths = find_all_paths(graph, node, end, path, all_paths)
            all_paths = new_paths
    
    return all_paths

def calculate_path_cost(graph, path):
    # Calculate cost of a path based on edge weights
    if len(path) <= 1:
        return 0
    
    total_cost = 0
    for i in range(len(path) - 1):
        current, next_node = path[i], path[i + 1]
        # Get weight for this edge
        weight = graph[current][next_node]
        total_cost += weight
    
    return total_cost

def analyze_traffic_flow(graph):
    # Simulates traffic flow in the network (not relevant for main task)
    flow_metrics = {}
    node_centrality = {}
    
    for node in graph:
        # Calculate a centrality measure
        connections = len(graph[node])
        weight_sum = sum(graph[node].values())
        node_centrality[node] = connections * weight_sum
        
        # Calculate flow capacity
        flow_capacity = connections * 2.5
        congestion_factor = min(1.0, connections / 5)
        
        flow_metrics[node] = {
            'capacity': flow_capacity,
            'congestion': congestion_factor
        }
    
    return flow_metrics, node_centrality

def calculate_optimal_path(graph, start, end):
    # This is the key function that calculates the optimal path length
    if start == end:
        return 0
    
    # Initialize distances with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Track processed nodes
    processed = set()
    
    # Process all nodes
    for _ in range(len(graph)):
        # Find node with minimum distance
        min_distance = float('infinity')
        min_node = None
        
        for node in graph:
            if node not in processed and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
        if min_node is None:
            break
        
        processed.add(min_node)
        
        # Update distances to neighbors
        for neighbor, weight in graph[min_node].items():
            # The actual path calculation - this is what matters
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    # The key result we want
    return distances[end]

# Create a network graph (directed with weights)
network_graph = {
    'A': {'B': 5, 'C': 3, 'E': 11},
    'B': {'A': 5, 'C': 1, 'D': 7},
    'C': {'A': 3, 'B': 1, 'D': 6, 'E': 8},
    'D': {'B': 7, 'C': 6, 'E': 4, 'F': 9},
    'E': {'A': 11, 'C': 8, 'D': 4, 'F': 2},
    'F': {'D': 9, 'E': 2}
}

# Calculate network statistics (not needed for main task)
network_stats = calculate_network_stats(network_graph)
print(f"Network has {network_stats['node_count']} nodes and {network_stats['edge_count']} edges")

# Analyze traffic flow (not needed for main task)
traffic_flow, centrality = analyze_traffic_flow(network_graph)

# These variables are misleading - not used for final answer
average_centrality = sum(centrality.values()) / len(centrality) if centrality else 0
max_congestion = max(node['congestion'] for node in traffic_flow.values()) if traffic_flow else 0

# Find paths between nodes
start_node = 'A'
end_node = 'F'

# This looks important but isn't used for final answer
all_possible_paths = find_all_paths(network_graph, start_node, end_node)
path_costs = [calculate_path_cost(network_graph, path) for path in all_possible_paths]

# Misleading calculations
if path_costs:
    min_cost_path = min(path_costs)
    max_cost_path = max(path_costs)
    average_path_cost = sum(path_costs) / len(path_costs)
else:
    min_cost_path = max_cost_path = average_path_cost = 0

# More misleading metrics
path_length_distribution = Counter([len(path) for path in all_possible_paths]) if all_possible_paths else Counter()
most_common_path_length = path_length_distribution.most_common(1)[0][0] if path_length_distribution else 0

# This is the key calculation that gives us our answer
optimal_path_length = calculate_optimal_path(network_graph, start_node, end_node)

# Some more irrelevant calculations to distract
potential_improvement = min_cost_path - optimal_path_length if path_costs else 0
efficiency_score = 100 * (1 - (optimal_path_length / max_cost_path if max_cost_path else 0))

# Process some alternative paths (not relevant)
alternative_routes = list(itertools.permutations(['B', 'C', 'D', 'E'], 2))
alternative_route_count = len([r for r in alternative_routes if r[0] in network_graph and r[1] in network_graph[r[0]]])

print(f"Result: {optimal_path_length}")