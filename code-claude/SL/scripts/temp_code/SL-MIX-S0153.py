from collections import defaultdict, Counter

def process_network_data(raw_connections):
    # Process network connection data
    network_graph = defaultdict(list)
    signal_strengths = {}
    error_counts = Counter()
    
    for connection in raw_connections:
        source, target, strength = connection
        network_graph[source].append(target)
        signal_strengths[(source, target)] = strength
        
        # Track potential network errors (not used in main calculation)
        if strength < 10:
            error_counts[source] += 1
    
    return network_graph, signal_strengths, error_counts

def analyze_network_redundancy(graph):
    # Calculate network redundancy metrics (distractor function)
    redundancy_score = 0
    for node in graph:
        if len(graph[node]) > 1:
            redundancy_score += len(graph[node])
    
    reliability_factor = redundancy_score * 0.15
    return reliability_factor

def optimize_transmission(strengths):
    # Optimize transmission parameters (distractor function)
    transmission_values = list(strengths.values())
    if not transmission_values:
        return 0
    
    optimal_power = sum(transmission_values) / len(transmission_values)
    return optimal_power * 2

def calculate_optimal_route(graph, visited):
    # Calculate the optimal path length through the network
    # This is where we determine our answer
    nodes = [n for n in graph if n not in visited]
    
    # Base calculation using binary operations
    base_value = sum([len(graph[n]) for n in nodes])
    
    # Apply bit operations for path optimization
    path_metric = (base_value << 2) & 0b11111111
    
    # Apply network adjustment factors
    adjustment = len(visited) * 3
    if adjustment > 0:
        path_metric = (path_metric - adjustment) | 0b1100
    
    # Early return for empty networks
    if not nodes:
        return 42
    
    # Final calculation with XOR operation
    return path_metric ^ 0b10101010

# Network connection data: (source, target, signal_strength)
raw_connections = [
    ('A', 'B', 15),
    ('A', 'C', 22),
    ('B', 'D', 18),
    ('B', 'E', 9),  # Low signal strength
    ('C', 'F', 14),
    ('D', 'G', 11),
    ('E', 'G', 8),  # Low signal strength
    ('F', 'G', 20)
]

# Process the network data
network_graph, signal_strengths, error_counts = process_network_data(raw_connections)

# Calculate network metrics (distractors)
reliability = analyze_network_redundancy(network_graph)
optimal_power = optimize_transmission(signal_strengths)

# Track network performance (distractor)
network_performance = reliability * optimal_power / 10
if network_performance > 50:
    network_status = "optimal"
else:
    network_status = "suboptimal"

# Identify problematic nodes (distractor)
problematic_nodes = [node for node, count in error_counts.items() if count > 0]

# Initialize path tracking
visited_nodes = ['A', 'B', 'D']
target_node = 'G'

# Analyze alternative paths (distractor)
alternative_paths = []
for node in network_graph:
    if node not in visited_nodes and len(network_graph[node]) > 0:
        alternative_paths.append((node, len(network_graph[node])))

# Sort alternatives by connectivity (distractor)
alternative_paths.sort(key=lambda x: x[1], reverse=True)

# Calculate the optimal path length
optimal_path_length = calculate_optimal_route(network_graph, visited_nodes)

# Apply network status adjustment (distractor)
if network_status == "optimal":
    adjusted_length = optimal_path_length * 0.9
else:
    adjusted_length = optimal_path_length * 1.1

print(f"Result: {optimal_path_length}")