from itertools import combinations

def analyze_connections(graph):
    connections = []
    for node in graph:
        for neighbor in graph[node]:
            if (neighbor, node) not in connections:
                connections.append((node, neighbor))
    return connections

def compute_density(edge_list, nodes):
    max_possible = len(nodes) * (len(nodes) - 1) / 2
    density = len(edge_list) / max_possible if max_possible > 0 else 0
    return round(density, 4)

def filter_relevant_paths(paths, threshold):
    filtered = []
    lengths = []
    for path in paths:
        length = len(path)
        lengths.append(length)
        if length >= threshold:
            filtered.append(path)
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    return filtered, avg_length

def calculate_final_score(data_dict):
    score = 0
    bonus = 0
    penalty = 0

    # Extract relevant components
    edges = data_dict['edges']
    nodes = data_dict['nodes']
    paths = data_dict['paths']

    # Core computation
    base_metric = len(edges) * 1.5
    if base_metric > 10:
        bonus += 8
    elif base_metric > 5:
        bonus += 3

    path_count = len(paths)
    if path_count > 0:
        longest_path = max(len(p) for p in paths)
        shortest_path = min(len(p) for p in paths)
        path_variability = longest_path - shortest_path
        score += path_variability * 2

    # Dummy analysis with no impact
    temp_analysis = set()
    for p in paths:
        temp_analysis.update(p)
    isolated_nodes = set(nodes) - temp_analysis

    # Misleading intermediate calculation
    phantom_score = 0
    for i, node in enumerate(nodes):
        phantom_score += hash(node) % (i + 1) if i % 3 == 0 else 0
    phantom_score = round(phantom_score / (len(nodes) + 1), 3)  # unused

    # Actual scoring branch
    density = compute_density(edges, nodes)
    if density > 0.5:
        score += 15
    else:
        penalty += 5

    cycle_detection = []
    for edge in edges:
        if edge[0] == edge[1]:
            cycle_detection.append(edge)
    if cycle_detection:
        penalty += len(cycle_detection) * 2

    # Final aggregation
    final_component = base_metric + score + bonus - penalty
    return int(round(final_component))

# Simulate data pipeline
raw_nodes = ['A', 'B', 'C', 'D', 'E']
raw_edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('B', 'D'), ('E', 'E')]

# Generate all simple paths between A and D
path_candidates = []
for r in range(2, 6):
    for seq in combinations(raw_nodes, r):
        if seq[0] == 'A' and seq[-1] == 'D':
            valid = True
            adj_set = set(raw_edges)
            for i in range(len(seq) - 1):
                if (seq[i], seq[i+1]) not in adj_set and (seq[i+1], seq[i]) not in adj_set:
                    valid = False
                    break
            if valid:
                path_candidates.append(seq)

processed_data = {
    'nodes': raw_nodes,
    'edges': raw_edges,
    'paths': path_candidates,
    'timestamp': 1712345678,
    'version': '2.1.0'
}

# Irrelevant precomputation
redundant_stats = {
    'node_combinations': list(combinations(raw_nodes, 2)),
    'edge_count_by_node': {n: sum(n in e for e in raw_edges) for n in raw_nodes}
}

# Unused helper
def validate_structure(data):
    required_keys = ['nodes', 'edges', 'paths']
    return all(k in data for k in required_keys)

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")