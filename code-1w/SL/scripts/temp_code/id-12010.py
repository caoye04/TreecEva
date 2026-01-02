def analyze_routing_efficiency(edges, weights):
    efficiency_map = {}
    total_edges = len(edges)
    weight_sum = sum(weights)
    for i, (u, v) in enumerate(edges):
        efficiency_map[(u, v)] = (i + 1) * weights[i] / (total_edges or 1)
    return efficiency_map

node_pairs = [(1, 2), (2, 3), (3, 4), (4, 1)]
edge_weights = [5, 7, 3, 8]

# Irrelevant analysis - distractor
routing_efficiency = analyze_routing_efficiency(node_pairs, edge_weights)
spectral_factor = sum(routing_efficiency.values()) * 0.5

# Core data structures
link_bandwidths = [100, 200, 150, 300]
def calculate_network_capacity(bandwidths, node_importance):
    adjusted_caps = [bw * (imp % 4) for bw, imp in zip(bandwidths, node_importance)]
    
    # Intermediate transformation - partially relevant
    squared_norms = [x ** 2 for x in adjusted_caps if x > 100]
    norm_factor = sum(squared_norms) ** 0.5 or 1
    
    # Red herring: unused computation
    temp_analysis = [x / norm_factor for x in squared_norms]
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    # Actual capacity logic
    base_cap = sum(adjusted_caps)
    penalty = 0
    for cap in adjusted_caps:
        if cap > 200:
            penalty += cap * 0.1
    final = base_cap - penalty
    return int(final)

node_weights = [2.7, 3.2, 1.8, 4.0]
scaling_constants = [0.9, 1.1, 0.8, 1.2]  # Unused in final calc

# Misleading pre-computation
projected_loads = [bw * sc for bw, sc in zip(link_bandwidths, scaling_constants)]
avg_projected = sum(projected_loads) / len(projected_loads)

# Key assignment
final_capacity = calculate_network_capacity(link_bandwidths, node_weights)
print(f"Result: {final_capacity}")