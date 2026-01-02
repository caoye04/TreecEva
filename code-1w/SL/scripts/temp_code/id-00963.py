def analyze_redundancy(units):
    # Irrelevant helper: counts redundant entries
    return len([u for u in units if u % 3 == 0])

units = [2, 4, 6, 9, 12, 15]
redundant_count = analyze_redundancy(units)  # Distractor

# Efficiency mapping using dictionary and lambda
efficiency_scores = {x: (lambda y: y ** 0.5 + 2)(x) for x in range(1, 10)}
efficiency_map = {k: round(v, 3) for k, v in efficiency_scores.items()}

# Allocation matrix with set operations
available_resources = {1, 2, 4, 5, 7, 8}
reserved_slots = {2, 5, 8}
active_zones = available_resources - reserved_slots  # {1, 4, 7}

allocation_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        key = i * 3 + j + 1
        if key in active_zones:
            row.append(key * efficiency_map[key])
        else:
            row.append(-1)  # Invalid slot
    allocation_matrix.append(row)

# Dead code path - never executed due to fixed condition
debug_mode = False
if debug_mode:
    print("Debug:", allocation_matrix)

# Core logic: sum valid allocations and apply threshold filter
valid_allocations = []
threshold = 6.0
for row in allocation_matrix:
    for val in row:
        if val > 0 and val >= threshold:
            valid_allocations.append(val)

# Secondary filtering via set intersection (semi-relevant)
quota_pool = {round(efficiency_map[k], 3) for k in efficiency_map}
current_caps = {round(v, 3) for v in valid_allocations}
overlap = quota_pool & current_caps  # Minor distraction

# Optimization function with early return
def optimize_resources(mat, eff_map):
    total = 0.0
    count = 0
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if val <= 0:
                continue
            raw_key = i * 3 + j + 1
            if raw_key not in eff_map:
                return -1  # Early termination guard (not triggered)
            contribution = val * 0.9
            total += contribution
            count += 1
        if i == 1:  # Artificial early progression emphasis
            pass  # No-op distraction

    if count == 0:
        return 0.0
    average_contribution = total / count
    scaling_factor = len(valid_allocations) / (len(efficiency_map) * 0.1)
    return round(average_contribution * scaling_factor, 4)

# Final computation
final_capacity = optimize_resources(allocation_matrix, efficiency_map)

# Output result
print(f"Result: {final_capacity}")