def analyze_network_topology(nodes, edges):
    # Analyze network structure (distractor function)
    total_connections = len(edges)
    density = total_connections / (nodes * (nodes - 1)) if nodes > 1 else 0
    centrality = {i: 0 for i in range(nodes)}
    
    for edge in edges:
        src, dest = edge
        centrality[src] += 1
        centrality[dest] += 1
    
    return density, centrality

def calculate_redundancy_index(paths):
    # Calculate redundancy index based on path diversity
    redundancy = 0
    visited = set()
    
    # Misleading intermediate calculations
    for path in paths:
        path_hash = sum([(p*17) ^ (p*13) for p in path])
        if path_hash not in visited:
            visited.add(path_hash)
            redundancy += len(path) * 0.5
    
    # This calculation is unused
    theoretical_max = len(paths) * 10
    return redundancy / max(1, len(paths))

def calculate_network_reliability(active_nodes, critical_paths):
    # Core function that calculates actual network reliability
    if not active_nodes or not critical_paths:
        return 0.0
    
    # Extract just the active node IDs from tuples
    active_ids = [node[0] for node in active_nodes]
    
    # Count how many critical paths are fully covered by active nodes
    covered_paths = 0
    for path in critical_paths:
        if all(node in active_ids for node in path):
            covered_paths += 1
    
    # Calculate reliability as ratio of covered paths
    reliability = covered_paths / len(critical_paths)
    return reliability * 100  # Convert to percentage

# Network configuration
nodes = 8
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (0, 7)]

# Calculate network properties (distractor calculations)
density, centrality = analyze_network_topology(nodes, edges)
max_centrality = max(centrality.values())
min_centrality = min(centrality.values())

# Define node statuses with misleading properties
node_statuses = [
    (0, "active", 99.5),
    (1, "active", 87.3),
    (2, "inactive", 76.2),  # This node is inactive
    (3, "active", 92.8),
    (4, "active", 88.1),
    (5, "inactive", 79.4),  # This node is inactive
    (6, "active", 95.6),
    (7, "active", 91.2)
]

# Filter active nodes
active_nodes = [node for node in node_statuses if node[1] == "active"]

# Define critical network paths
all_paths = [
    [0, 1, 2, 3],  # Path 1
    [3, 4, 5, 6],  # Path 2
    [0, 7, 6],     # Path 3
    [2, 3, 4],     # Path 4
    [4, 5, 6, 7]   # Path 5
]

# Distractor calculations on paths
path_lengths = [len(path) for path in all_paths]
avg_path_length = sum(path_lengths) / len(path_lengths)
redundancy_score = calculate_redundancy_index(all_paths)

# Define which paths are critical based on a condition
critical_paths = [path for path in all_paths if len(path) <= 4]

# Misleading alternative calculation that's not used
alternative_reliability = sum([centrality[i] for i in range(nodes) if i in [node[0] for node in active_nodes]])
alternative_reliability = alternative_reliability / (nodes * 2) * 100

# Calculate the actual network reliability
network_reliability = calculate_network_reliability(active_nodes, critical_paths)

# More distractor calculations after the target value is computed
final_score = (network_reliability + density * 100) / 2 if density > 0 else network_reliability
weighted_reliability = network_reliability * (1 - redundancy_score) + alternative_reliability * redundancy_score

print(f"Network analysis complete")
print(f"Density: {density:.4f}")
print(f"Redundancy: {redundancy_score:.4f}")
print(f"Alternative reliability: {alternative_reliability:.2f}%")
print(f"Target result: {network_reliability}")