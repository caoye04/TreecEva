def analyze_workload():
    # Simulate a system monitoring workload across multiple servers
    server_loads = [12, 15, 10, 20, 18, 25, 17]
    thresholds = [14, 16, 11, 19, 21]
    maintenance_mode = False
    adjustment_factor = 0.9

    # Irrelevant transformation (distractor)
    adjusted_loads = [x * adjustment_factor for x in server_loads if x > 10]
    temp_sum = sum(adjusted_loads) / len(adjusted_loads) if adjusted_loads else 0

    # Real processing begins: track usage levels with time decay
    usage_levels = []
    decay_rate = 0.95
    base_offset = 5

    for i, load in enumerate(server_loads):
        # Simulate temporal decay effect on perceived load
        for j in range(i + 1):
            load = int(load * decay_rate)
        adjusted_entry = load + base_offset

        # Apply conditional scaling based on threshold zones
        matched_zone = False
        for t in thresholds:
            if abs(adjusted_entry - t) < 3:
                adjusted_entry *= 1.1
                matched_zone = True
                break
        
        if not matched_zone:
            adjusted_entry += 2

        usage_levels.append(int(adjusted_entry))

        # Dead code path - never executed due to logic above
        if maintenance_mode:
            usage_levels.clear()
            break

    # Redundant list transformation using zip and enumerate (semi-relevant but not critical)
    indexed_levels = list(enumerate(zip(usage_levels, [x**0.5 for x in usage_levels])))
    smoothing_correction = sum([idx * val[1] for idx, val in indexed_levels]) // len(indexed_levels) if indexed_levels else 0

    # Key computation point
    peak_capacity = max(usage_levels)
    peak_capacity += smoothing_correction // 10

    # Final diagnostic print
    print(f"Result: {peak_capacity}")

analyze_workload()