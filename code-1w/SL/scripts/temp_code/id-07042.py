def optimize_allocation(resources, demands):
    # Initialize tracking variables
    allocated = {}
    overflow_log = []
    deficit_count = 0
    scaling_factor = 1.25
    base_threshold = sum(demands) * 0.1

    # Preprocess: categorize resources by type
    resource_types = {'A': [], 'B': [], 'C': []}
    for key in resources.keys():
        if 'type_a' in key:
            resource_types['A'].append(resources[key])
        elif 'type_b' in key:
            resource_types['B'].append(resources[key])
        else:
            resource_types['C'].append(resources[key])

    total_A = sum(resource_types['A'])
    total_B = sum(resource_types['B'])
    total_C = sum(resource_types['C'])

    # Misleading intermediate calculation (not used in final result)
    phantom_load = (total_A * 0.3) + (total_B * 0.7) - (total_C * 0.1)
    if phantom_load > 100:
        deficit_count += 1

    # Actual allocation logic
    cumulative_demand = 0
    for day, demand in enumerate(demands):
        cumulative_demand += demand
        if day % 7 == 6:  # Weekly reset
            weekly_buffer = cumulative_demand * 0.05
            cumulative_demand += weekly_buffer

    # Simulate adaptive scaling
    adjusted_capacity = cumulative_demand * scaling_factor

    # Destructuring irrelevant data
    temp_data = [(1, 2), (3, 4), (5, 6)]
    for x, y in temp_data:
        overflow_log.append(x * y)

    # Final decision logic based on thresholds
    if adjusted_capacity > base_threshold * 5:
        final_capacity = int(adjusted_capacity * 0.8)
    else:
        final_capacity = int(adjusted_capacity * 0.6)

    # Red herring: unused set operation
    unused_set = {1, 2, 3, 4}
    unused_set.discard(2)
    unused_set.add(sum(overflow_log))

    return final_capacity

# Main execution
resource_pool = {
    'node_alpha_type_a': 20,
    'node_beta_type_a': 30,
    'node_gamma_type_b': 50,
    'node_delta_type_b': 10,
    'node_epsilon_type_c': 5,
    'node_zeta_type_c': 15
}

demand_schedule = [8, 12, 14, 10, 18, 22, 26, 9, 13, 17]

final_capacity = optimize_allocation(resource_pool, demand_schedule)
print(f"Result: {final_capacity}")