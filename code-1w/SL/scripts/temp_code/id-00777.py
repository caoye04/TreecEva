def optimize_allocation():
    # Network node capacity data (in Mbps)
    primary_nodes = {100, 200, 300, 400}
    backup_nodes = {150, 250, 300, 400, 500}

    # Redundant overlap in node capacities
    redundant_capacities = primary_nodes & backup_nodes

    # Simulate reallocation attempts
    attempted_reallocation = []
    fallback_threshold = 0
    for cap in sorted(redundant_capacities, reverse=True):
        if cap > 250:
            adjusted = cap * 0.9  # 10% efficiency loss
            attempted_reallocation.append(adjusted)
        else:
            fallback_threshold += cap

    # Irrelevant statistics (distractor variables)
    avg_redundant = sum(redundant_capacities) / len(redundant_capacities)
    peak_capacity = max(primary_nodes)
    unused_slots = len(backup_nodes) - len(primary_nodes)

    # Core logic: bandwidth optimization with conditional overrides
    base_allocation = 0
    override_triggered = False
    for val in attempted_reallocation:
        if val >= 300:
            base_allocation += val * 1.1  # Boost high-tier nodes
        elif val >= 200:
            base_allocation += val * 1.05
        else:
            override_triggered = True
            break

    # Secondary adjustment based on system load profile
    load_factor = 0.85
    stress_mode = False
    temp_buffer = []
    for i in range(3):
        temp_buffer.append(load_factor * base_allocation)
        load_factor += 0.05
        if load_factor > 0.9 and not stress_mode:
            stress_mode = True

    # Final computation with set-based validation
    valid_factors = {round(f, 2) for f in temp_buffer}
    if len(valid_factors) > 2:
        final_bandwidth = int(sum(valid_factors) / len(valid_factors))
    else:
        final_bandwidth = int(base_allocation)

    # Dead code path - never executed due to logic above
    if override_triggered and stress_mode and False:
        emergency_cap = min(redundant_capacities)
        final_bandwidth = emergency_cap // 2

    return final_bandwidth

# Execute and print result
target_result = optimize_allocation()
print(f"Target result: {target_result}")