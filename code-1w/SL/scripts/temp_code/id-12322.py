def calculate_system_capacity():
    # System node configuration with nominal capacities
    node_specs = {
        'node_a': {'type': 'compute', 'base_power': 80, 'units': 3},
        'node_b': {'type': 'storage', 'base_power': 45, 'units': 6},
        'node_c': {'type': 'network', 'base_power': 20, 'units': 8}
    }

    # Derived capacity map based on unit count and base power
    capacity_map = {}
    for node_id, specs in node_specs.items():
        capacity_map[node_id] = specs['base_power'] * specs['units']

    # Efficiency factor due to thermal throttling and load balancing
    efficiency_factor = 0.88

    # Final aggregated system capacity
    total_capacity = sum(capacity_map.values()) * efficiency_factor

    # Irrelevant diagnostic metric (minimal distraction)
    avg_utilization = 76.4

    print(f"Result: {total_capacity}")

    return total_capacity

# Execute function
calculate_system_capacity()