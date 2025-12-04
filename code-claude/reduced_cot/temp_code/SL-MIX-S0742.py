import itertools
from collections import defaultdict, Counter

def calculate_network_metrics(nodes, connections, traffic_patterns):
    # Initialize graph representation
    network = defaultdict(list)
    for src, dest, bandwidth in connections:
        network[src].append((dest, bandwidth))
        network[dest].append((src, bandwidth))  # Undirected graph
    
    # Calculate various network metrics
    centrality = {}
    for node in nodes:
        # Betweenness centrality approximation (not actually used)
        paths = list(itertools.permutations(nodes, 2))
        centrality[node] = len(paths) / len(nodes)
    
    # Traffic analysis
    congestion = Counter()
    for pattern in traffic_patterns:
        source, destination, volume = pattern
        # This is a distractor - doesn't affect the result
        congestion[source] += volume
        congestion[destination] += volume
    
    # Calculate routing efficiency
    hop_counts = []
    bandwidth_metrics = []
    
    # Process only relevant connections
    filtered_connections = [c for c in connections if c[0] in nodes and c[1] in nodes]
    
    # Main routing calculation
    routing_metrics = {}
    
    # Distractor calculations
    theoretical_max = sum(b for _, _, b in connections)
    adjusted_max = theoretical_max // 2  # Account for bidirectional
    
    # More distractors
    reliability_factor = len(nodes) / max(1, len(connections))
    scaling_coefficient = 2.5 if len(nodes) > 5 else 1.8
    
    # Extract bandwidth values for analysis
    bandwidths = [b for _, _, b in connections]
    bandwidth_stats = {
        "min": min(bandwidths) if bandwidths else 0,
        "max": max(bandwidths) if bandwidths else 0,
        "avg": sum(bandwidths) / len(bandwidths) if bandwidths else 0
    }
    
    # Intermediate calculation (distractor)
    partial_metric = bandwidth_stats["avg"] * reliability_factor
    
    # This section contains the key calculation
    node_degrees = {n: len(network[n]) for n in nodes}
    if sum(node_degrees.values()) > 0:
        connectivity_index = len(connections) / sum(node_degrees.values())
        # Critical calculation here
        essential_path_metric = int(42 * connectivity_index)
        
        # Store in metrics dictionary
        routing_metrics["connectivity"] = connectivity_index
        routing_metrics["essential"] = essential_path_metric
        routing_metrics["theoretical"] = theoretical_max
    else:
        # Fallback values
        routing_metrics["connectivity"] = 0
        routing_metrics["essential"] = 7
        routing_metrics["theoretical"] = 0
    
    # More distractor calculations that look important
    efficiency_score = 0
    for node, degree in node_degrees.items():
        if degree > 0 and node in congestion:
            efficiency_score += (congestion[node] / degree)
    
    # Final processing and normalizations
    normalized_efficiency = min(100, int(efficiency_score * scaling_coefficient))
    
    return routing_metrics, normalized_efficiency

# Network definition
nodes = ["A", "B", "C", "D", "E"]
connections = [
    ("A", "B", 10),
    ("B", "C", 15),
    ("C", "D", 20),
    ("D", "E", 25),
    ("E", "A", 30),
    ("B", "E", 35)
]
traffic_patterns = [
    ("A", "C", 5),
    ("B", "D", 8),
    ("E", "B", 12)
]

# Calculate metrics
metrics, efficiency = calculate_network_metrics(nodes, connections, traffic_patterns)

# Process results
if efficiency > 50:
    routing_metrics = {"essential": metrics["theoretical"] // 10}
else:
    # This is the branch that will be taken
    routing_metrics = {"essential": 21}

# Distractor calculations
possible_optimizations = {
    "path_shortening": efficiency * 0.8,
    "load_balancing": metrics["connectivity"] * 15
}

# Extract the answer
optimal_path_length = routing_metrics["essential"]

# More distractor calculations after the answer
final_score = optimal_path_length
if "path_shortening" in possible_optimizations:
    final_score += possible_optimizations["path_shortening"]

# Print the result
print(f"Result: {optimal_path_length}")