def optimize_distribution(inventories, matrix):
    # Simulate warehouse inventory redistribution efficiency
    total_items = sum(inventories)
    capacity_map = {i: val * 1.5 for i, val in enumerate(inventories)}
    
    # Irrelevant transformation: normalize values (not used in final logic)
    normalized = [x / max(inventories) for x in inventories if x > 0]
    temp_score = sum(normalized) * 0.7
    
    # Core logic: apply matrix weights and compute effective capacity
    weighted_load = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            weighted_load += matrix[i][j] * (i + j)

    # Secondary red herring: simulate unused threshold check
    threshold_exceeded = any(x > 500 for x in inventories)
    adjustment_factor = 1.1 if threshold_exceeded else 0.9
    
    # Real computation path
    base_capacity = sum(capacity_map.values())
    load_modifier = weighted_load / (len(matrix) ** 2 + 1)
    
    # Use conditional expression and set operation as required
    efficiency_bonus = 1.2 if load_modifier > 3 else 1.0
    unique_indices = set(range(len(inventories))) - {len(inventories) - 1}
    bonus_applied = efficiency_bonus if len(unique_indices) > 2 else 1.0
    
    # Final result calculation
    final_capacity = int(base_capacity * bonus_applied * 0.8)
    return final_capacity

# Input data
inventory_levels = [120, 180, 95, 210]
distribution_matrix = [
    [0.8, 1.2, 0.9],
    [1.1, 0.7, 1.3],
    [0.6, 1.4, 0.8],
    [1.0, 1.0, 1.0]
]

# Execution point
final_capacity = optimize_distribution(inventory_levels, distribution_matrix)
print(f"Result: {final_capacity}")