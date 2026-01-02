def calculate_network_capacity(bandwidths, nodes):
    base_threshold = 50
    scaling_factor = 1.75
    temp_load = [b * scaling_factor for b in bandwidths if b > base_threshold]
    
    # Irrelevant pre-processing: simulate latency adjustments (not used in final logic)
    latency_map = {i: (bandwidths[i] % 7) * 0.3 for i in range(len(bandwidths))}
    adjusted_latencies = [latency_map[k] for k in sorted(latency_map.keys()) if k % 2 == 0]

    # Core logic: count high-bandwidth links and apply node-based multiplier
    high_capacity_links = len(temp_load)
    node_coverage = sum(1 for n in nodes if n['active'] and n['priority'] > 1)
    
    # Simulate redundant transformation (distractor)
    coverage_stats = tuple((idx, val['priority']) for idx, val in enumerate(nodes) if val['active'])
    priority_set = {p for _, p in coverage_stats}
    max_priority = max(priority_set) if priority_set else 1

    # Actual computation path
    efficiency_ratio = 0.8 if node_coverage >= 3 else 0.6
    raw_capacity = sum(temp_load) * efficiency_ratio
    
    # Secondary adjustment based on set intersection of indices
    valid_indices = {i for i, b in enumerate(bandwidths) if b > 40}
    active_indices = {i for i, n in enumerate(nodes) if n['active']}
    overlap_count = len(valid_indices & active_indices)
    
    # Final capacity depends on overlapping resources
    final_capacity = int(raw_capacity + (overlap_count * max_priority * 10))
    return final_capacity

# Simulation setup
link_bandwidths = [30, 60, 80, 45, 90]
nodes = [
    {'active': True, 'priority': 2},
    {'active': False, 'priority': 3},
    {'active': True, 'priority': 4},
    {'active': True, 'priority': 1},
    {'active': True, 'priority': 5}
]

# Misleading intermediate calculation (dead-end)
cumulative_stress = 0
for bw in link_bandwidths:
    if bw < 70:
        cumulative_stress += bw * 0.1

# Key execution point
final_capacity = calculate_network_capacity(link_bandwidths, nodes)
print(f"Result: {final_capacity}")