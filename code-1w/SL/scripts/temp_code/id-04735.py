def optimize_distribution(resources, limits):
    # Simulate resource optimization under capacity constraints using set operations and filtering
    allocated = set()
    overflow = set()
    temp_buffer = []
    threshold = sum(limits) // len(limits) if limits else 0

    for res in resources:
        if res < threshold:
            allocated.add(res)
        else:
            overflow.add(res)

    # Misleading intermediate computation - not used in final result
    unused_diagnostic = len(allocated) - len(overflow)
    dummy_shift = [x * 2 for x in resources if x % 2 == 0]

    # Conditional logic with red herring branch (never taken due to prior logic)
    if len(allocated) > 1000:
        recovery_mode = True
        temp_buffer.extend(dummy_shift)
    else:
        recovery_mode = False

    # Actual core logic: count how many high-value resources are within acceptable bounds
    filtered_high_tier = {r for r in overflow if r <= max(limits, default=1)}

    base_score = len(allocated) * 1.5
    bonus = 0

    # Recursive helper to simulate tiered evaluation (simple recursion)
    def calculate_bonus(tier_set, depth=0):
        if not tier_set or depth >= 3:
            return depth
        reduced = tier_set.copy()
        removed = reduced.pop() if reduced else 0
        return calculate_bonus(reduced, depth + (1 if removed % 2 == 0 else 0))

    bonus = calculate_bonus(filtered_high_tier)

    # Distractor: complex-looking but unused expression
    shadow_metric = sum([x ** 0.5 for x in resources if x > threshold]) if overflow else 0

    # Final capacity depends only on base_score and recursive bonus
    final_capacity = int(base_score + bonus)

    # Additional dead code path (unreachable under normal inputs)
    if recovery_mode and shadow_metric > 1e5:
        final_capacity *= 2

    return final_capacity


# Setup realistic input scenario
resource_pool = list(range(10, 125, 7))  # [10, 17, 24, ..., 116]
constraints = [50, 60, 55, 70, 45]

# Execute main logic
final_capacity = optimize_distribution(resource_pool, constraints)
print(f"Result: {final_capacity}")