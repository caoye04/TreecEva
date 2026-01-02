def optimize_allocation(resources, demands):
    # Precompute indices and pairs for optimization
    indexed_demand = list(enumerate(demands))
    capacity_pool = [r * 2 for r in resources if r > 0]
    
    temp_offset = sum([d for i, d in indexed_demand if i % 2 == 0])  # Irrelevant accumulation
    adjustment_factor = len(capacity_pool) - temp_offset % len(capacity_pool) if temp_offset > 0 else 1
    
    # Misleading transformation
    shadow_buffer = [d ** 0.5 for i, d in indexed_demand]
    normalized_shadow = [s / adjustment_factor for s in shadow_buffer]

    # Actual logic begins: pair resources with cyclic demand using zip
    cycle_demand = (d % 3 + 1 for d in demands)
    paired = list(zip(capacity_pool, cycle_demand))
    
    allocation_score = 0
    for i, (cap, dem) in enumerate(paired):
        if cap >= dem * 2:
            allocation_score += cap // dem
        elif cap >= dem:
            allocation_score += 1
    
    # Secondary filtering based on slicing pattern
    history_window = capacity_pool[-len(paired):]  # Slice window, partially redundant
    stability_check = sum(history_window) // len(history_window) if history_window else 0

    # Distractor: unused variables and dead path
    emergency_reserve = 0
    if False:  # Dead code branch
        emergency_reserve = max(resources) * 10
        for x in normalized_shadow:
            emergency_reserve -= x

    # Final computation using distractor-influenced but actually static factor
    scaling_hint = len(indexed_demand) % 4 or 1
    final_capacity = (allocation_score * stability_check) // scaling_hint
    
    return final_capacity

# Input data
resource_map = [8, -2, 5, 0, 12, 7]
demand_sequence = [3, 9, 1, 4, 2]

# Execution point
final_capacity = optimize_allocation(resource_map, demand_sequence)
print(f"Result: {final_capacity}")