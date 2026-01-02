def optimize_allocation(resources, demands):
    # Initialize tracking variables
    allocated = 0
    overflow_count = 0
    temp_buffer = []
    cumulative_shift = 0

    # Preprocess: filter valid resources and sort demands
    valid_resources = {r for r in resources if r > 0}  # Use set for uniqueness
    sorted_demands = sorted([d for d in demands if d > 0], reverse=True)  # List comprehension with filter

    # Misleading intermediate calculations (distraction)
    avg_resource = sum(valid_resources) / len(valid_resources) if valid_resources else 0
    peak_demand = max(sorted_demands) if sorted_demands else 0
    theoretical_max = avg_resource * len(valid_resources)  # Not used directly

    # Simulate allocation under priority rules
    for demand in sorted_demands:
        fulfilled = False
        while valid_resources:
            candidate = min(valid_resources, key=lambda x: abs(x - demand))
            if candidate >= demand:
                allocated += demand
                valid_resources.remove(candidate)
                temp_buffer.append(candidate - demand)
                fulfilled = True
                break
            else:
                # Resource too small, simulate degradation
                cumulative_shift += candidate >> 2
                valid_resources.remove(candidate)
                overflow_count += 1
        if not fulfilled:
            # Attempt partial fill from buffer (secondary pool)
            if temp_buffer:
                surplus = temp_buffer.pop()
                if surplus >= demand:
                    allocated += demand
                else:
                    allocated += surplus

    # Additional red herring computations
    efficiency_score = (allocated / sum(demands)) * 100 if demands else 0
    unused_surplus = sum(temp_buffer)
    final_capacity = allocated + unused_surplus  # Key result

    # Dead code path (never executed under current logic)
    if overflow_count > 100:
        final_capacity *= 0.95

    return final_capacity

# Input data
resource_pool = [12, 7, 15, 4, 4, 8, 0, -3, 10]
demand_schedule = [9, 6, 11, 5, 3, 7]

# Execute main logic
final_capacity = optimize_allocation(resource_pool, demand_schedule)
print(f"Result: {final_capacity}")