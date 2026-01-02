def optimize_distribution(resources, limits):
    # Initialize tracking variables
    allocated = 0
    overflow_buffer = 0
    temp_shadow = [0] * len(resources)

    # Preprocess: filter valid resources using set operations
    valid_indices = {i for i, r in enumerate(resources) if r > 0}
    restricted_set = {i for i in range(len(resources)) if limits[i]}
    active_indices = valid_indices & restricted_set  # Set intersection

    # Misleading secondary computation (dead-end path)
    phantom_load = sum(resources[i] ** 0.5 for i in valid_indices if i not in restricted_set)
    phantom_load = int(phantom_load % 97)

    # Primary logic with nested conditions and state updates
    priority_queue = []
    for i in active_indices:
        temp_shadow[i] = resources[i] * (2 if i % 3 == 0 else 1)
        if temp_shadow[i] > 50:
            overflow_buffer += temp_shadow[i] // 10

    # Simulate staged allocation with modular arithmetic
    step_factor = len(active_indices) % 4 or 1
    for _ in range(step_factor + 1):
        for i in sorted(active_indices):
            contribution = temp_shadow[i] % 17
            if contribution % 2 == 0:
                allocated += contribution // 2
            else:
                allocated += contribution * 2

    # Secondary distractor: complex but unused structure
    backup_snapshot = {
        'checksum': sum(temp_shadow) ^ 2024,
        'flags': [i for i in range(len(resources)) if resources[i] < 0],
        'meta': (len(valid_indices), len(restricted_set))
    }

    # Final adjustment based on aggregated state
    base_capacity = allocated // 3
    final_capacity = base_capacity - (overflow_buffer % 13)

    return final_capacity

# Setup input data
resource_pool = [12, -5, 67, 44, 0, 89, 23]
constraints = [True, True, False, True, False, True, True]

# Execute main logic
final_capacity = optimize_distribution(resource_pool, constraints)
print(f"Result: {final_capacity}")