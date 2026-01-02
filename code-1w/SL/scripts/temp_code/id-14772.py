def calculate_adjusted_efficiency(nodes, weights):
    total_efficiency = 0.0
    base_offset = len(nodes) % 7
    temp_buffer = [0] * len(nodes)
    debug_trace = []

    # Irrelevant precomputation (distractor)
    cumulative_xor = 0
    for idx in range(len(nodes)):
        cumulative_xor ^= idx * 2
    scaling_factor = (cumulative_xor % 9) + 1  # Not actually used later

    # Relevant processing with enumerate and zip
    node_ranks = sorted(enumerate(nodes), key=lambda x: x[1], reverse=True)
    weighted_pairs = list(zip(nodes, weights))

    efficiency_map = {}
    for rank, (orig_idx, node_val) in enumerate(node_ranks):
        weight = weights[orig_idx]
        raw_score = node_val * weight * (rank + 1)
        adjustment = 1.0 if node_val > 50 else 0.85
        adjusted_score = raw_score * adjustment
        efficiency_map[orig_idx] = adjusted_score

        # Dead code path (distractor)
        if rank == 3:
            temp_buffer[orig_idx] = raw_score / 2.5
            debug_trace.append(f"Checkpoint at rank {rank}")

    # Secondary loop with conditional branching and set operations
    active_indices = set()
    threshold = sum(weights) / len(weights)  # average weight

    for i, w in enumerate(weights):
        if w >= threshold:
            active_indices.add(i)

    contribution_sum = 0.0
    for idx in active_indices:
        contribution_sum += efficiency_map[idx]

    # Final computation with irrelevant intermediate steps
    outlier_count = 0
    for val in nodes:
        if val < 10 or val > 90:
            outlier_count += 1
    # This outlier count is computed but not used in final result

    stability_metric = len(active_indices) / len(nodes)
    final_score = contribution_sum * stability_metric

    return final_score

# Input data
network_nodes = [85, 42, 67, 91, 53, 74, 29]
weights = [0.9, 0.5, 0.7, 1.0, 0.6, 0.8, 0.4]

# Execution point of interest
final_score = calculate_adjusted_efficiency(network_nodes, weights)
print(f"Result: {final_score}")