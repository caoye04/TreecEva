from itertools import combinations

# Analyze network connection patterns
node_connections = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B'], 'D': ['B', 'E'], 'E': ['D']}

# Get all unique nodes and calculate possible combinations
all_nodes = list(node_connections.keys())
all_combinations = list(combinations(all_nodes, 2))

# Calculate unique connection pairs (undirected)
unique_pairs = set()
for node, neighbors in node_connections.items():
    for neighbor in neighbors:
        pair = tuple(sorted([node, neighbor]))
        unique_pairs.add(pair)

# Find missing potential connections
missing_pairs = []
for pair in all_combinations:
    if pair not in unique_pairs:
        missing_pairs.append(pair)

# Calculate metrics
unique_combinations = len(all_combinations)
actual_connections = len(unique_pairs)
missing_count = len(missing_pairs)

# Distractor calculations (not used in final result)
total_nodes = len(all_nodes)
max_possible = (total_nodes * (total_nodes - 1)) // 2
theoretical_density = actual_connections / max_possible

# Overlap calculation (used in final result)
overlap_count = 0
for pair in unique_pairs:
    if len(pair[0]) == len(pair[1]):
        overlap_count += 1

final_count = unique_combinations - overlap_count
print(f"Result: {final_count}")