def optimize_distribution(resources, limit):
    # Initialize tracking variables
    total_capacity = 0
    peak_utilization = 0
    load_profile = []
    
    # Secondary computation - not directly used in final result
    shadow_buffer = [0] * len(resources)
    for i in range(len(resources)):
        shadow_buffer[i] = (resources[i][1] ** 2) % 7
    buffer_sum = sum(shadow_buffer)  # Distractor: computed but unused

    # Primary logic: process resource nodes above threshold
    active_nodes = 0
    temp_storage = []
    for res_id, capacity, priority in resources:
        if capacity > limit:
            adjusted_load = capacity * (priority + 1)
            if priority > 2:
                adjusted_load -= capacity * 0.1  # 10% reduction for high priority
            load_profile.append(adjusted_load)
            total_capacity += adjusted_load
            active_nodes += 1
            if adjusted_load > peak_utilization:
                peak_utilization = adjusted_load

    # Compute auxiliary metrics (distractors)
    avg_load = total_capacity / active_nodes if active_nodes else 0
    fluctuation_index = max(load_profile) - min(load_profile) if load_profile else 0

    # Simulate fallback calculation (dead path)
    if limit < 0:
        fallback = sum([c for _, c, _ in resources])
        total_capacity = fallback  # Never executed

    # Final transformation using list comprehension and filtering
    filtered_caps = [int(x) for x in load_profile if x > avg_load]
    bonus_allocation = len(filtered_caps) * 50

    # Critical assignment point
    final_load = int(total_capacity + bonus_allocation)

    # Extraneous state logging
    log_entry = f"Processed {active_nodes} nodes, peak={peak_utilization:.1f}"
    debug_flag = len(load_profile) > 3 and avg_load > 500
    
    return final_load

# Main execution context
resource_map = [
    ('R1', 120, 1),
    ('R2', 340, 3),
    ('R3', 180, 2),
    ('R4', 450, 4),
    ('R5', 90, 1),
    ('R6', 380, 3)
]
threshold = 100
baseline_offset = 77
scaling_factor = 1.0  # Unused in logic

# Irrelevant pre-computation
preliminary_check = any([cap > 400 for _, cap, _ in resource_map])
dummy_matrix = [[i*j for j in range(3)] for i in range(3)]  # Dead structure

final_load = optimize_distribution(resource_map, threshold)
print(f"Result: {final_load}")