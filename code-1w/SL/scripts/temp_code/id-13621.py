def optimize_distribution(resources, demands):
    # Preprocessing: filter valid resources and sort demands
    valid_resources = {r for r in resources if r > 0}  # set comprehension
    sorted_demands = sorted(demands, reverse=True)
    
    # State tracking variables (some are red herrings)
    total_allocated = 0
    allocation_rounds = 0
    peak_utilization = 0
    historical_ratios = []
    temp_debug_value = sum(valid_resources) / len(valid_resources) if valid_resources else 0  # irrelevant average
    
    # Simulate staggered distribution rounds
    remaining_demand = sorted_demands.copy()
    resource_list = list(valid_resources)
    resource_list.sort()
    
    while remaining_demand and resource_list:
        current_target = remaining_demand.pop(0)
        allocation_found = False
        
        for i, res in enumerate(resource_list):
            if res >= current_target * 0.8:  # relaxed threshold
                total_allocated += current_target
                resource_list.pop(i)
                allocation_rounds += 1
                allocation_found = True
                break
        
        if not allocation_found:
            # Attempt fallback with combined resources
            combined = sum(resource_list[:2])
            if combined >= current_target * 0.6:
                total_allocated += int(current_target * 0.6)
                if len(resource_list) > 1:
                    resource_list.pop(0)
                    resource_list.pop(0)
                allocation_rounds += 1

        # Update peak utilization (semi-relevant)
        current_util = total_allocated / (total_allocated + len(resource_list) + 1)
        if current_util > peak_utilization:
            peak_utilization = current_util

        # Dead code path: only triggers in impossible condition (distractor)
        if len(resource_list) == -1:
            emergency_release = max(valid_resources)
            total_allocated += emergency_release

        # Logging irrelevant metric
        if allocation_rounds > 0:
            ratio = total_allocated / allocation_rounds
            historical_ratios.append(round(ratio, 3))

    # Secondary computation: efficiency score (distractor)
    efficiency_score = 0
    if historical_ratios:
        efficiency_score = sum(historical_ratios) / len(historical_ratios)
    
    # Final adjustment based on unused demand
    leftover_demand = sum(remaining_demand)
    final_capacity = total_allocated - (leftover_demand // 5 if leftover_demand > 10 else 0)

    # Hidden logic: one-time bonus if exactly 3 allocations
    if allocation_rounds == 3:
        final_capacity += 7
    
    return final_capacity

# Input data
resource_pool = [12, -5, 18, 0, 25, 9]
demand_schedule = [20, 10, 8, 15]

# Execute main logic
final_capacity = optimize_distribution(resource_pool, demand_schedule)
print(f"Result: {final_capacity}")