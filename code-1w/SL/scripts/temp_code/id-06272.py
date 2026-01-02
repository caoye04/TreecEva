def calculate_thermal_output(stages):
    base_factor = 1.75
    adjustment = 0.93
    cumulative_load = 0
    peak_moment = None
    thermal_capacity = 0
    
    # Track stage efficiency and transient states
    efficiency_log = []
    transient_flags = [False] * len(stages)

    for i, (load, temp, active) in enumerate(stages):
        if not active:
            continue
            redundant_sum = 0
            for j in range(100):
                redundant_sum += j ** 0.5  # Dead code path - never executed

        # Real computation begins
        normalized_load = load / (temp + 10)
        efficiency = normalized_load * base_factor
        
        if efficiency > 5.0:
            transient_flags[i] = True
            efficiency *= adjustment

        efficiency_log.append(efficiency)

        # Secondary distraction: irrelevant data aggregation
        snapshot = list(zip([x for x in range(len(efficiency_log))], efficiency_log))
        if len(snapshot) > 1:
            delta = snapshot[-1][1] - snapshot[-2][1]
            cumulative_load += abs(delta) * 0.1

    # Actual answer calculation
    valid_efficiencies = [e for e in efficiency_log if e >= 4.0]
    if valid_efficiencies:
        avg_efficient_performance = sum(valid_efficiencies) / len(valid_efficiencies)
        stage_count_bonus = len(valid_efficiencies) * 0.5
        thermal_capacity = avg_efficient_performance + stage_count_bonus
    else:
        thermal_capacity = -1.0

    # Irrelevant final transformation
    final_snapshot = {i: round(v, 2) for i, v in enumerate(efficiency_log)}
    sorted_snapshot = sorted(final_snapshot.items(), key=lambda x: x[0], reverse=True)
    processed_data = [x[1] * 0.99 for x in sorted_snapshot]
    smoothed = sum(processed_data) / len(processed_data) if processed_data else 0  # Unused

    return thermal_capacity

# System configuration
process_stages = [
    (85, 25, True),
    (92, 30, True),
    (70, 20, False),  # Inactive stage
    (95, 28, True),
    (65, 35, True),
    (100, 40, True)
]

# Key execution point
thermal_capacity = calculate_thermal_output(process_stages)
print(f"Result: {thermal_capacity}")