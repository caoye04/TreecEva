def optimize_allocation(resources, limits):
    temp_score = 0
    adjusted = [r * 1.5 for r in resources if r > 10]
    scaling_factor = sum(adjusted) / len(adjusted) if adjusted else 1.0

    # Irrelevant transformation on backup data
    backup_data = [x ** 0.5 for x in resources]
    avg_backup = sum(backup_data) / len(backup_data)
    temp_score += avg_backup * 0.1  # Minor influence, ultimately unused

    # Core logic with conditional expression and dictionary usage
    status_map = {i: 'active' if val >= limits['threshold'] else 'inactive' for i, val in enumerate(resources)}
    active_count = list(status_map.values()).count('active')

    # Simulate load distribution using lambda
    distribute_load = lambda x: x * scaling_factor if x > limits['min_alloc'] else x * 0.8
    processed = [distribute_load(r) for r in resources]

    # Misleading cumulative calculation (not used in final result)
    cumulative_waste = 0
    for p in processed:
        if p < limits['optimal_range'][0]:
            cumulative_waste += limits['optimal_range'][0] - p

    # Key computation path
    base_total = sum(processed)
    efficiency_bonus = 1.2 if active_count >= limits['efficiency_trigger'] else 1.0
    penalty = 0.9 if len([p for p in processed if p < limits['min_alloc']]) > 2 else 1.0

    # Final bandwidth determined here
    final_bandwidth = (base_total * efficiency_bonus * penalty) // 1  # Integer result

    # Dead code branch (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {temp_score}, {cumulative_waste}')

    return final_bandwidth

# Input setup
resource_pool = [12, 15, 8, 23, 5, 19, 14]
constraints = {
    'threshold': 10,
    'min_alloc': 12,
    'optimal_range': (15, 25),
    'efficiency_trigger': 4
}

# Execution
final_bandwidth = optimize_allocation(resource_pool, constraints)
print(f"Result: {final_bandwidth}")