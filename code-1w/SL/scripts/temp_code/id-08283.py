from itertools import combinations

# Simulate a network load analysis across time windows and node clusters
def analyze_network_load(base_nodes, traffic_spikes, redundancy_factor):
    total_configs = 0
    usage_levels = []
    
    # Generate all possible node cluster configurations
    for r in range(2, len(base_nodes) + 1):
        for subset in combinations(base_nodes, r):
            total_configs += 1
            load_score = sum([hash(node) % 100 for node in subset])
            usage_levels.append(load_score)
    
    # Irrelevant: Calculate redundant combinatorial statistics
    comb_stats = [len(list(combinations(base_nodes, k))) for k in range(1, len(base_nodes))]
    avg_comb_size = sum(comb_stats) / len(comb_stats) if comb_stats else 0
    
    # Apply simulated traffic spikes to usage levels
    adjusted_levels = []
    for i, level in enumerate(usage_levels):
        spike = traffic_spikes[i % len(traffic_spikes)]
        adjusted = level * (1 + spike / 100.0)
        if adjusted > 150:
            adjusted -= redundancy_factor * 0.3
        adjusted_levels.append(round(adjusted))
    
    # Add misleading intermediate normalization
    normalized = [x / max(adjusted_levels) * 100 for x in adjusted_levels]
    filtered_peaks = [val for val in adjusted_levels if val >= 75]
    
    # Simulate fallback mechanism with no actual impact
    fallback_cap = 0
    for val in normalized:
        if val < 40:
            fallback_cap += 1
    fallback_cap *= 10
    
    # Key assignment point
    peak_capacity = max(usage_levels)
    
    # Print result as required
    print(f"Result: {peak_capacity}")
    return peak_capacity

# Inputs
nodes = ['router_A', 'switch_B', 'firewall_C', 'proxy_D', 'gateway_E']
spikes = [12, 18, 15, 20]
factor = 2

# Execute
result = analyze_network_load(nodes, spikes, factor)