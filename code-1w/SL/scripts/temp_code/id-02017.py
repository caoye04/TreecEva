def optimize_distribution(inventory, constraints):
    # Simulate warehouse inventory reallocation under shipping limits
    adjustments = []
    temp_buffer = 0
    overflow_count = 0  # distractor: counts overflows but not used in final logic

    for i, (level, constraint) in enumerate(zip(inventory, constraints)):
        if level > constraint:
            delta = level - constraint
            adjustments.append(delta * 0.8)
            temp_buffer += delta * 0.2
            overflow_count += 1
        else:
            deficit = constraint - level
            filler = min(temp_buffer, deficit)
            adjustments.append(-filler)
            temp_buffer -= filler

    # Apply nonlinear correction using lambda
    corrector = lambda x: x ** 1.1 if x > 0 else x
    corrected = [corrector(adj) for adj in adjustments]

    # Secondary processing: aggregate relevant metrics
    total_readjustment = sum(abs(c) for c in corrected)
    average_shift = total_readjustment / len(corrected) if corrected else 0

    # Distractor variables
    simulated_cost = total_readjustment * 2.37  # unused in final result
    stability_index = len([c for c in corrected if c < 0])  # irrelevant metric

    # Core calculation: net usable capacity after optimization
    base_capacity = sum(inventory)
    penalty_factor = len([x for x in inventory if x < 50]) * 1.5
    final_capacity = int(base_capacity - total_readjustment + average_shift - penalty_factor)

    return final_capacity


# Input data
inventory_levels = [120, 85, 200, 45, 90, 150]
shipping_constraints = [100, 100, 180, 60, 95, 130]

# Execution point
final_capacity = optimize_distribution(inventory_levels, shipping_constraints)
print(f"Result: {final_capacity}")