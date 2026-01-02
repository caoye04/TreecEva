def calculate_distribution(inventory, routes):
    total_capacity = 0
    transfer_pool = []
    debug_trace = []

    for region, items in inventory.items():
        if len(region) % 2 == 0:
            capacity_hint = sum([len(item) for item in items])
        else:
            capacity_hint = len(items) * 2
        total_capacity += capacity_hint

        # Simulate regional prioritization (not used in final calc)
        priority_score = len(items) - (ord(region[0]) % 3)
        debug_trace.append(priority_score)

    # Misleading route analysis
    unused_analysis = {}
    for route_key in routes.keys():
        split_parts = route_key.split('_')
        unused_analysis[route_key] = len(split_parts[0]) + len(split_parts[-1])

    # Actual distribution logic
    base_factor = len(routes.get('primary', []))
    backup_count = len(routes.get('backup', []))
    adjustment = 1 if backup_count > 2 else 0.9

    temp_result = []
    for key in sorted(inventory.keys()):
        temp_result.extend(inventory[key][:2])

    # Core computation
    token_sum = 0
    seen_tokens = set()
    for item in temp_result:
        token_value = sum([ord(c) for c in item])
        if item not in seen_tokens:
            token_sum += token_value % 17
            seen_tokens.add(item)

    # Final load depends only on inventory structure and primary route
    final_load = (total_capacity + base_factor) * adjustment
    final_load -= len(seen_tokens)
    
    # Print required output
    print(f"Target result: {final_load}")
    return final_load

# Setup data
inventory_state = {
    'north': ['widget_a', 'gadget_x', 'part_m'],
    'south_east': ['widget_b', 'gadget_y'],
    'west': ['part_k', 'part_l', 'gadget_z', 'widget_c']
}

routing_map = {
    'primary': ['r1', 'r2', 'r3'],
    'backup': ['b1', 'b2'],
    'overflow': ['o1']
}

# Execution point
final_load = calculate_distribution(inventory_state, routing_map)