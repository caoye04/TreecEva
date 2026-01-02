def calculate_network_capacity():
    nodes = ['router_A', 'switch_B', 'hub_C', 'bridge_D']
    base_speeds = [1000, 500, 100, 200]
    utilization = [0.85, 0.72, 0.45, 0.60]

    # Initialize capacity map using enumerate for index-aware pairing
    capacity_map = {}
    for i, node in enumerate(nodes):
        capacity_map[node] = int(base_speeds[i] * (1 - utilization[i]))

    # Update specific node using direct access (irrelevant adjustment)
    capacity_map['switch_B'] += 50

    # Add secondary metric (distractor: not used in final result)
    performance_scores = []
    for speed, util in zip(base_speeds, utilization):
        score = (speed / 10) * (1 - util)
        performance_scores.append(round(score, 2))

    # Final aggregation step
    total_capacity = sum(capacity_map.values())
    
    # Print result as required
    print(f"Result: {total_capacity}")

    # Additional irrelevant variable (minor interference)
    avg_performance = sum(performance_scores) / len(performance_scores) if performance_scores else 0

    return total_capacity

# Execute function
result = calculate_network_capacity()