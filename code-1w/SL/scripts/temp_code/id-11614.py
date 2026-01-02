def analyze_distribution(hubs):
    total_nodes = sum(hub['nodes'] for hub in hubs)
    avg_load = total_nodes / len(hubs) if hubs else 0
    
    # Irrelevant statistical distraction
    variance = sum((hub['nodes'] - avg_load) ** 2 for hub in hubs) / len(hubs) if hubs else 0
    std_dev = variance ** 0.5
    normalized_score = (avg_load + std_dev) / (variance + 1)

    return total_nodes, avg_load, normalized_score


def filter_efficient_hubs(hubs):
    # Filter hubs that are above median node count
    node_counts = sorted([hub['nodes'] for hub in hubs])
    median = node_counts[len(node_counts)//2] if node_counts else 0
    
    efficient_hubs = [hub for hub in hubs if hub['nodes'] > median]
    redundant_hubs = [hub for hub in hubs if hub['nodes'] <= median]  # Unused path

    # Distractor: simulate load balancing that isn't used later
    balance_shift = 0
    for hub in redundant_hubs:
        balance_shift += hub['nodes'] // 2
    
    return efficient_hubs


def compute_overlap(hub_pairs):
    # Simulate interference between adjacent hubs using set operations
    overlap_count = 0
    for i in range(len(hub_pairs)):
        for j in range(i+1, len(hub_pairs)):
            set_a = set(range(hub_pairs[i]['start'], hub_pairs[i]['end']))
            set_b = set(range(hub_pairs[j]['start'], hub_pairs[j]['end']))
            intersection = set_a & set_b
            overlap_count += len(intersection)
    return overlap_count


def optimize_distribution(hubs, factor):
    base_total = sum(hub['nodes'] for hub in hubs)
    
    # Apply efficiency factor with decay over size
    penalty = 0
    for hub in hubs:
        if hub['nodes'] > 50:
            penalty += hub['nodes'] * 0.1
    
    adjusted = base_total - penalty
    boosted = adjusted * factor
    
    # Secondary adjustment based on combinatorial redundancy
    n = len(hubs)
    redundancy_factor = n * (n - 1) // 2 if n > 1 else 0  # Simple combinatorics
    final_value = boosted - redundancy_factor
    
    # Red herring calculation
    hypothetical_max = base_total * 1.5
    unused_buffer = hypothetical_max - final_value
    
    return int(final_value)

# Main execution
if __name__ == '__main__':
    network_hubs = [
        {'nodes': 30, 'region': 'A', 'start': 10, 'end': 40},
        {'nodes': 65, 'region': 'B', 'start': 25, 'end': 70},
        {'nodes': 45, 'region': 'C', 'start': 60, 'end': 90},
        {'nodes': 80, 'region': 'D', 'start': 85, 'end': 110},
        {'nodes': 55, 'region': 'E', 'start': 100, 'end': 130}
    ]

    # Step 1: Analyze full distribution (produces distractor stats)
    total, mean_load, score = analyze_distribution(network_hubs)

    # Step 2: Filter only efficient hubs above median
    processed_hubs = filter_efficient_hubs(network_hubs)

    # Step 3: Compute spatial overlap (used to justify logic but not directly affecting final result)
    overlap_regions = compute_overlap(processed_hubs)

    # Step 4: Determine efficiency factor based on modular pattern
    efficiency_factor = (len(processed_hubs) * 7) % 5 + 1.25  # e.g., 2.25 or 3.25

    # Step 5: Critical statement
    final_capacity = optimize_distribution(processed_hubs, efficiency_factor)

    print(f"Result: {final_capacity}")