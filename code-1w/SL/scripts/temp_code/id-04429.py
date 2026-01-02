def calculate_network_capacity():
    nodes = ['router_A', 'switch_B', 'hub_C', 'bridge_D']
    bandwidths = [100, 200, 50, 150]
    utilization = [0.8, 0.75, 0.5, 0.9]

    # Calculate effective capacities using list comprehension
    capacities = [int(b * u) for b, u in zip(bandwidths, utilization)]
    
    # Irrelevant metadata (minimal distraction)
    node_count = len(nodes)
    avg_util = sum(utilization) / len(utilization)
    
    total_capacity = sum(capacities)
    
    # Print result as required
    print(f"Result: {total_capacity}")

    return total_capacity

result = calculate_network_capacity()