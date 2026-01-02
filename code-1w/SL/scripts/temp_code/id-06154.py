def calculate_overlap(region_a, region_b):
    return len(set(region_a) & set(region_b))

# Simulate resource regions and allocations
region_x = list(range(10, 23))
region_y = list(range(18, 30))
overlap_size = calculate_overlap(region_x, region_y)

resource_map = {
    'A': 45,
    'B': 32,
    'C': 27,
    'D': 51
}

allocation_list = ['A', 'B', 'A', 'C', 'D', 'B', 'A']

# Misleading capacity transformation (not used in final logic)
temp_capacities = [val ** 0.5 for val in resource_map.values()]
avg_temp = sum(temp_capacities) / len(temp_capacities)
adjusted_avg = int(avg_temp * 2) if avg_temp > 5 else int(avg_temp * 3)

# State tracking with red herring counters
counter_log = {}
for res in allocation_list:
    counter_log[res] = counter_log.get(res, 0) + 1

# Actual processing: weighted decay model on original map
working_map = resource_map.copy()
decay_factor = 0.1

for resource in allocation_list:
    if resource in working_map:
        reduction = int(working_map[resource] * decay_factor)
        working_map[resource] -= reduction

# Secondary adjustment based on overlap influence
scaling_modifier = (overlap_size + 1) / 10.0
for k in working_map:
    working_map[k] = int(working_map[k] * scaling_modifier)

# Final aggregation using dictionary operations and conditional expression
base_total = sum(working_map.values())
penalty = 10 if len(allocation_list) > 5 else 5
final_capacity = base_total - penalty

# Distractor: unused intermediate calculation
theoretical_max = max(resource_map.values()) * scaling_modifier
expected_utilization = base_total / (sum(resource_map.values()) * scaling_modifier)

print(f"Result: {final_capacity}")