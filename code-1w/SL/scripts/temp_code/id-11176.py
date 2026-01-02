from collections import defaultdict

# Simulate a distributed network load balancing scenario

def preprocess_nodes(node_list, threshold=10):
    valid_nodes = []
    temp_weights = []
    for node in node_list:
        load = node['load']
        weight = node['weight']
        if load < threshold * 2:
            valid_nodes.append(node)
        temp_weights.append(weight)  # Not used later, distractor
    return valid_nodes


def generate_traffic_matrix(nodes, base_factor=0.5):
    matrix = defaultdict(float)
    total_capacity = 0
    for node in nodes:
        cap = node['load'] * base_factor
        total_capacity += cap
    
    # Create pairwise distribution keys (irrelevant for final result)
    for i, node in enumerate(nodes):
        key = f"node_{i}_traffic"
        matrix[key] = node['load'] * base_factor / (total_capacity + 1e-9)
    
    matrix['normalization'] = total_capacity  # Red herring
    return matrix


def optimize_routing(nodes):
    ranked = sorted(nodes, key=lambda x: x['load'])
    selected = []
    cumulative_load = 0
    for node in ranked:
        if cumulative_load < 50 and len(selected) < 5:
            selected.append(node)
            cumulative_load += node['load']
    return selected


def calculate_distribution(nodes, traffic_map):
    score_map = defaultdict(int)
    adjustment = len(nodes) * 0.1
    
    for idx, node in enumerate(nodes):
        normalized_score = (node['load'] + idx) / (node['weight'] + 1)
        score_map[node['id']] = int(normalized_score)
    
    total_score = sum(score_map.values())
    
    # Irrelevant aggregation
    avg_score = total_score / len(score_map) if score_map else 0
    penalty = 0
    for k, v in score_map.items():
        if v > avg_score:
            penalty += 1  # Unused distraction
    
    # Core calculation (depends only on total_score and adjustment)
    result = total_score * adjustment
    return int(result)

# Main execution
if __name__ == "__main__":
    network_nodes = [
        {'id': 'A', 'load': 8, 'weight': 2},
        {'id': 'B', 'load': 12, 'weight': 3},
        {'id': 'C', 'load': 5, 'weight': 1},
        {'id': 'D', 'load': 15, 'weight': 4},
        {'id': 'E', 'load': 7, 'weight': 2}
    ]

    # Step 1: Filter nodes below critical threshold
    filtered_nodes = preprocess_nodes(network_nodes, threshold=10)

    # Step 2: Generate traffic distribution matrix (contains unused data)
    traffic_matrix = generate_traffic_matrix(filtered_nodes)

    # Step 3: Optimize node selection based on load ranking
    optimized_nodes = optimize_routing(filtered_nodes)

    # Step 4: Calculate final distribution load
    final_load = calculate_distribution(optimized_nodes, traffic_matrix)

    # Output target result
    print(f"Target result: {final_load}")