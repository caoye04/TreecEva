def calculate_system_capacity(resources, rules):
    # Initialize tracking variables
    active_nodes = set()
    reserved_units = {}
    total_utilization = 0
    overflow_count = 0

    # Precompute threshold based on average resource size (distractor)
    avg_size = sum(len(r) for r in resources.values()) / len(resources) if resources else 0
    size_threshold = int(avg_size * 1.5)

    # Process each node and its resource pool
    for node_id, resource_list in resources.items():
        if len(resource_list) >= size_threshold:
            active_nodes.add(node_id)

        # Track per-node reserved units (only some are used later)
        reserved = 0
        for res in resource_list:
            if res % 3 == 0:
                reserved += res // 4
            elif res % 5 == 0:
                reserved += res // 5  # Partially relevant
        reserved_units[node_id] = reserved

    # Apply allocation rules using modular arithmetic and set logic
    capacity_modifiers = []
    for rule_type, config in rules.items():
        base = config.get('base', 1)
        mod = config.get('modulus', 7)
        shift = config.get('shift', 0)

        # Complex but partially irrelevant transformation
        transformed = [(base * i + shift) % mod for i in range(1, 6)]
        filtered = [x for x in transformed if x in {1, 2, 4}]
        capacity_modifiers.extend(filtered)

    # Core logic: compute final capacity using only specific components
    base_capacity = len(active_nodes) * 100
    adjustment = sum(reserved_units[n] for n in active_nodes if n in reserved_units)  # Only this matters
    modifier_impact = sum(m for m in capacity_modifiers if m % 2 == 1)  # Only odd modifiers apply

    # Final computation
    final_capacity = base_capacity + adjustment * modifier_impact

    # Irrelevant debugging output (dead code)
    debug_snapshot = {
        'nodes': list(active_nodes),
        'checksum': sum(reserved_units.values()) % 97,
        'timestamp': 1678886400
    }

    return final_capacity


# System configuration data
resource_pool = {
    'node_alpha': [12, 15, 18, 20, 25],
    'node_beta': [8, 10, 14, 16],
    'node_gamma': [9, 12, 15, 21, 24, 30],
    'node_delta': [5, 7, 11]
}

allocation_rules = {
    'rule_A': {'base': 3, 'modulus': 5, 'shift': 2},
    'rule_B': {'base': 2, 'modulus': 8, 'shift': 1},
    'rule_C': {'base': 4, 'modulus': 6, 'shift': 0}
}

# Execute main calculation
final_capacity = calculate_system_capacity(resource_pool, allocation_rules)
print(f"Result: {final_capacity}")