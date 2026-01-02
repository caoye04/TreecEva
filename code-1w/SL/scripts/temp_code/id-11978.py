def analyze_system_resources():
    # Simulate hardware resource profiling
    cpu_cores = [i for i in range(8)]
    memory_banks = {2, 4, 6, 8, 10}
    storage_units = set(range(5))

    # Auxiliary diagnostic checks (distractor computations)
    diagnostic_score = sum([x**2 for x in cpu_cores if x % 2 == 0])
    temp_threshold = diagnostic_score / len(cpu_cores) + 3.14

    # Identify functional units based on compatibility matrix
    functional_cores = {core for core in cpu_cores if core > 0 and core != 5}
    backup_units = {0, 2, 4, 6}

    # Determine overlapping configurations (semi-relevant)
    potential_configs = []
    for c in functional_cores:
        for s in storage_units:
            if (c + s) % 3 == 0:
                potential_configs.append((c, s))

    # Evaluate redundancy and fault tolerance
    redundant_pairs = 0
    for p1 in potential_configs:
        for p2 in potential_configs:
            if p1[0] < p2[0] and (p1[1] + p2[1]) % 2 == 0:
                redundant_pairs += 1

    # Core logic: find optimal configuration using set operations
    preferred_storage = storage_units - {0, 3}
    allowed_memory = memory_banks & {6, 8, 10, 12}

    optimal_config = set()
    for core in functional_cores:
        if core % 3 == 0:
            optimal_config.add(f'core_{core}')
        elif core % 4 == 0:
            optimal_config.add(f'backup_core_{core}')

    # Additional irrelevant state tracking
    system_health = 'STABLE'
    last_updated = '2023-11-05'
    audit_log = [f'Checked core {c}' for c in cpu_cores]

    # Critical execution point
    core_capacity = len(optimal_config)

    # More red herring calculations
    efficiency_ratio = redundant_pairs / (core_capacity + 1e-5)
    stress_test_result = efficiency_ratio ** 0.5

    # Final output
    print(f'Result: {core_capacity}')

analyze_system_resources()