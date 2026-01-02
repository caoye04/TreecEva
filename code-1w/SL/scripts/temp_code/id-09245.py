from collections import defaultdict, Counter

def network_traffic_analysis():
    # Simulated packet data: source, destination, size, priority
    packets = [
        ('node_a', 'node_b', 142, 'high'),
        ('node_b', 'node_c', 89, 'low'),
        ('node_a', 'node_c', 205, 'medium'),
        ('node_c', 'node_a', 76, 'high'),
        ('node_b', 'node_d', 134, 'medium'),
        ('node_d', 'node_a', 95, 'low'),
        ('node_c', 'node_d', 167, 'high')
    ]

    # Track total traffic per node (irrelevant for final result but adds cognitive load)
    node_traffic = defaultdict(int)
    priority_count = Counter(p[3] for p in packets)

    for src, dst, size, _ in packets:
        node_traffic[src] += size
        node_traffic[dst] += size

    # Misleading intermediate: average_packet_size_by_priority (not used later)
    total_by_priority = defaultdict(int)
    count_by_priority = defaultdict(int)
    for _, _, size, prio in packets:
        total_by_priority[prio] += size
        count_by_priority[prio] += 1
    
    avg_by_prio = {p: total_by_priority[p] / count_by_priority[p] 
                   for p in total_by_priority}

    # Extract high-priority flows for optimization
    high_priority_sizes = [size for src, dst, size, prio in packets if prio == 'high']
    sorted_sizes = sorted(high_priority_sizes, reverse=True)

    # Simulate bandwidth allocation with diminishing returns
    base_allocation = 0
    decay_factor = 0.8
    for i, size in enumerate(sorted_sizes):
        base_allocation += size * (decay_factor ** i)  # Larger packets get weighted more initially

    # Distractor: unused function that looks relevant
    def calculate_latency_reduction():
        return sum(size for size in high_priority_sizes) * 0.01

    # Distractor: dead-end logic path
    if len(packets) > 10:
        redundant_calc = sum(node_traffic.values()) / 100
    else:
        redundant_calc = None  # Not used

    # Core computation: optimize bandwidth using top-2 adjusted sizes
    adjustment_factor = 1.25
    if len(sorted_sizes) >= 2:
        # Weighted combination of largest and second-largest
        adjusted_sum = (sorted_sizes[0] * adjustment_factor) + (sorted_sizes[1] * 0.75)
        scaling_constant = 0.9
        final_bandwidth = int(adjusted_sum * scaling_constant)
    else:
        final_bandwidth = int(base_allocation)

    # Print result as required
    print(f"Result: {final_bandwidth}")

    return final_bandwidth

# Execute
network_traffic_analysis()