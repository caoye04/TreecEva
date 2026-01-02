from itertools import combinations

def calculate_network_efficiency(nodes):
    # Compute Euclidean distances between all node pairs
    distances = []
    for a, b in combinations(nodes, 2):
        dist = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
        distances.append(round(dist, 3))
    
    # Filter distances below threshold (efficient connections)
    threshold = 7.5
    filtered_distances = [d for d in distances if d < threshold]
    
    # Irrelevant auxiliary variable (minimal distraction)
    total_pairs = len(distances)
    efficiency_ratio = len(filtered_distances) / total_pairs if total_pairs else 0
    
    result = sum(filtered_distances)
    print(f"Result: {result}")
    return result

# Define network node coordinates
node_positions = [(0, 0), (3, 4), (6, 8), (1, 1), (7, 7)]
calculate_network_efficiency(node_positions)