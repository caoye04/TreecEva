def optimize_resources(resources, limit):
    # Simulate resource optimization under constraints
    used = set()
    overflow = set()
    temp_buffer = 0
    
    for val in resources:
        if val % 2 == 0:
            used.add(val)
        else:
            overflow.add(val)

    # Misleading intermediate calculation (not directly affecting final result)
    temp_buffer = sum([x * 2 for x in overflow if x > 5])
    temp_buffer -= len(overflow)  # Distractor operation

    base_score = len(used) * 3
    penalty = 0
    
    for val in used:
        if val > limit:
            penalty += (val // 2) - limit

    # Conditional expression usage
    adjustment = base_score - penalty if base_score > penalty else 0
    
    # Secondary distractor: unused loop with side-effect-free operations
    shadow_copy = [x + 1 for x in resources]
    for _ in range(2):
        shadow_copy = [x // 2 for x in shadow_copy if x > 3]

    # Key logic: capacity determined by adjusted score modulo constraint
    auxiliary_sum = sum(used) % 97
    final_capacity = (adjustment * 2) + (auxiliary_sum % 13)

    return final_capacity

# Input data
allocation_set = {12, 15, 18, 19, 22, 25, 26, 30}
threshold = 20

# Execution point
final_capacity = optimize_resources(allocation_set, threshold)
print(f"Result: {final_capacity}")