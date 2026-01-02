from itertools import combinations

# Simulate hourly network node load with interference
def analyze_network_load(nodes, hours):
    base_load = [len(node['name']) * 1.5 for node in nodes]
    temp_fluctuations = [abs(hash(node['type']) % 100) / 20.0 for node in nodes]
    
    # Irrelevant temperature simulation (distractor)
    heat_index = sum([t**1.2 for t in temp_fluctuations if t > 2]) / len(temp_fluctuations)
    heat_warnings = []
    for i, h in enumerate(temp_fluctuations):
        if h > 3:
            heat_warnings.append(f"Node {i} hot")

    # Generate usage per hour using complex pattern
    hourly_factors = [0.5 + (i % 4) * 0.25 for i in range(hours)]
    usage_matrix = []
    for i, node in enumerate(nodes):
        row = []
        for h in range(hours):
            load = base_load[i] * hourly_factors[h]
            if node['critical'] and h in [0, 23]:  # peak at start/end
                load *= 1.8
            row.append(round(load, 3))
        usage_matrix.append(row)

    # Flatten and compute usage levels with list comprehension
    all_usages = [val for row in usage_matrix for val in row]
    filtered_usages = [u for u in all_usages if u > 1.0]  # filter low usage

    # Dummy combinatorial analysis (dead code path - distractor)
    critical_nodes = [n for n in nodes if n['critical']]
    if len(critical_nodes) >= 2:
        pairs = list(combinations(critical_nodes, 2))
        pair_scores = [len(p[0]['name']) + len(p[1]['name']) for p in pairs]

    # Actual key computation
    avg_usage = sum(filtered_usages) / len(filtered_usages)
    usage_levels = [u / avg_usage * 100 for u in filtered_usages]  # normalize to percentage
    peak_capacity = max(usage_levels)

    # More distractions: unused statistical calculation
    variance = sum((x - avg_usage) ** 2 for x in filtered_usages) / len(filtered_usages)
    stability_ratio = (min(usage_levels) + 50) / (variance + 1)

    # Final result output
    print(f"Result: {peak_capacity}")

# Define input data
network_nodes = [
    {'name': 'router-alpha', 'type': 'core', 'critical': True},
    {'name': 'switch-bravo', 'type': 'edge', 'critical': False},
    {'name': 'firewall-gamma', 'type': 'security', 'critical': True},
    {'name': 'bridge-delta', 'type': 'lan', 'critical': False}
]

hours_in_day = 24

# Execute main function
analyze_network_load(network_nodes, hours_in_day)