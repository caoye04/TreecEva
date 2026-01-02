def analyze_transmission_load(nodes, links):
    # Irrelevant computation: calculates average degree but not used in final result
    avg_degree = sum(len(node['connections']) for node in nodes) / len(nodes) if nodes else 0
    
    temp_utilization = [link['bandwidth'] * 0.85 for link in links]
    adjusted_load = sum(temp_utilization) + avg_degree  # Partially relevant but mostly distraction

    return adjusted_load


def calculate_node_influence(weights):
    # Some complex-looking transformation that isn't directly used
    squared_norm = sum(w ** 2 for w in weights)
    normalized = [w / (squared_norm ** 0.5) for w in weights]
    return [round(x * 100, 2) for x in normalized]

# System configuration
node_weights = [3, 7, 2, 8, 5]
link_bandwidths = [
    {'id': 'A', 'bandwidth': 12},
    {'id': 'B', 'bandwidth': 18},
    {'id': 'C', 'bandwidth': 9},
    {'id': 'D', 'bandwidth': 15}
]

# Simulate node metadata (distractor structure)
nodes = [
    {'id': 'N1', 'type': 'router', 'connections': ['N2', 'N3'], 'load': 0.6},
    {'id': 'N2', 'type': 'switch', 'connections': ['N1', 'N3', 'N4'], 'load': 0.4},
    {'id': 'N3', 'type': 'bridge', 'connections': ['N1', 'N2'], 'load': 0.7},
    {'id': 'N4', 'type': 'gateway', 'connections': ['N2'], 'load': 0.3}
]

# Distractor function call with side-effect-like structure but no real impact
_ = analyze_transmission_load(nodes, link_bandwidths)

# Core logic: compute weighted harmonic mean of bandwidths using node weights as coefficients
influence_scores = calculate_node_influence(node_weights)

# Actual key computation hidden among distractions
weighted_inv_sum = sum(
    (1.0 / link['bandwidth']) * (node_weights[i % len(node_weights)] / sum(node_weights))
    for i, link in enumerate(link_bandwidths)
)

# Compute effective network capacity using modular weighting and combinatorics-inspired factor
combination_factor = len(link_bandwidths) * (len(link_bandwidths) - 1) // 2 if len(link_bandwidths) > 1 else 1
base_capacity = 1.0 / weighted_inv_sum

scaling_factor = sum(
    (i + 1) * w for i, w in enumerate(node_weights)
) % 17  # Modular arithmetic twist

final_capacity = int(base_capacity * scaling_factor + combination_factor)

# Print result as required
Result: {final_capacity}