def calculate_network_capacity():
    nodes = ['router_A', 'router_B', 'switch_C', 'hub_D']
    base_speeds = [100, 200, 50, 10]
    utilization = [0.8, 0.9, 0.75, 0.3]

    # Irrelevant variable (minimal distraction)
    temp_buffer = [0] * len(nodes)

    # Create capacity map using dictionary comprehension
    capacity_map = {nodes[i]: base_speeds[i] * utilization[i] for i in range(len(nodes))}

    # Key computation point
    total_capacity = sum(capacity_map.values())

    # Additional unrelated but harmless operation
    max_node = max(capacity_map, key=capacity_map.get)

    print(f"Result: {total_capacity}")

    return total_capacity

# Execute function
calculate_network_capacity()