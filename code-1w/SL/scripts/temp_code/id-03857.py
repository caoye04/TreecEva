def analyze_network_topology(nodes):
    # Irrelevant preprocessing step (distractor)
    signal_strengths = {node['id']: len(node['connections']) * node.get('weight', 1) for node in nodes}
    total_bandwidth = sum(s ** 0.5 for s in signal_strengths.values() if s > 5)
    
    # Relevant transformation: extract high-throughput nodes
    processed_nodes = set()
    for node in nodes:
        throughput = len(node['connections']) * node.get('efficiency', 1.0)
        if throughput >= 2:
            processed_nodes.add(node['id'])
    
    return processed_nodes


def compute_base_metrics(data_points):
    # Dead function - not used in final computation (distractor)
    avg = sum(data_points) / len(data_points)
    variance = sum((x - avg) ** 2 for x in data_points) / len(data_points)
    return {'average': avg, 'variance': variance}


def collect_capacity_segments(zones):
    # Semi-relevant: builds initial pool but only part is used
    capacity_pool = set()
    temp_tracker = []
    
    for zone in zones:
        base_cap = zone['nodes'] * 10
        offset = zone.get('redundancy', 1) - 1
        adjusted = base_cap - (offset * 5)
        
        # Only even capacities are added to final pool
        if adjusted % 2 == 0:
            capacity_pool.add(adjusted)
        else:
            temp_tracker.append(adjusted)  # unused tracker (distractor)
    
    # Additional irrelevant logic
    if len(temp_tracker) > 2:
        capacity_pool.add(sum(temp_tracker) // len(temp_tracker))
    
    return capacity_pool


def optimize_distribution(active_nodes, available_caps):
    # Core logic: find optimal match between node count and capacity
    node_count = len(active_nodes)
    sorted_caps = sorted(available_caps)
    
    # Find first capacity that can support all nodes with headroom
    target = None
    for cap in sorted_caps:
        if cap >= node_count * 3:
            target = cap
            break
    
    # Secondary fallback logic (not triggered in this case)
    if target is None:
        backup_set = {c + node_count for c in available_caps}
        target = min(backup_set)
    
    # Final adjustment based on parity alignment
    if (target + node_count) % 2 == 0:
        final_capacity = target + 2
    else:
        final_capacity = target - 1
    
    return final_capacity

# Main execution flow
network_nodes = [
    {'id': 'N1', 'connections': [2, 3], 'weight': 3, 'efficiency': 1.2},
    {'id': 'N2', 'connections': [1, 4, 5], 'weight': 2},
    {'id': 'N3', 'connections': [1], 'weight': 4, 'efficiency': 0.8},
    {'id': 'N4', 'connections': [2, 5], 'weight': 1, 'efficiency': 1.5},
    {'id': 'N5', 'connections': [2, 4], 'weight': 5}
]

zone_configurations = [
    {'nodes': 4, 'redundancy': 1},
    {'nodes': 6, 'redundancy': 3},
    {'nodes': 3, 'redundancy': 2},
    {'nodes': 8, 'redundancy': 1}
]

# Step 1: Process active network nodes
processed_nodes = analyze_network_topology(network_nodes)

# Step 2: Collect and filter capacity segments
capacity_pool = collect_capacity_segments(zone_configurations)

# Step 3: Compute irrelevant metrics (distractor)
data_metrics = compute_base_metrics([4, 7, 2, 9, 5])
intermediate_score = data_metrics['average'] * 2  # unused downstream

# Step 4: Optimize final distribution
final_capacity = optimize_distribution(processed_nodes, capacity_pool)

print(f"Target result: {final_capacity}")