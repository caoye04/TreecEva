def calculate_network_capacity():
    nodes = ['router_A', 'router_B', 'switch_C', 'hub_D']
    base_speeds = [100, 200, 50, 10]
    utilization = [0.8, 0.75, 0.9, 0.3]

    # Calculate effective capacities
    capacity_map = {}
    for i, node in enumerate(nodes):
        capacity_map[node] = base_speeds[i] * (1 - utilization[i])

    # Minor irrelevant calculation (distractor)
    avg_util = sum(utilization) / len(utilization)
    temp_result = avg_util * 1000  # Unused variable

    total_capacity = sum(capacity_map.values())
    
    # Additional unrelated but harmless operation
    status_flags = {node: cap > 50 for node, cap in capacity_map.items()}
    active_count = sum(status_flags.values())  # Not used in main result

    print(f"Result: {total_capacity}")

calculate_network_capacity()