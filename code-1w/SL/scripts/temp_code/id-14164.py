def calculate_equilibrium(matrix, temp):
    adjustment_factor = 0.87
    equilibrium_score = 0
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Irrelevant precomputation (distractor)
    max_val = float('-inf')
    for row in matrix:
        for val in row:
            if val > max_val:
                max_val = val

    # Semi-relevant normalization (not directly used later)
    normalized_temps = [t / sum(temp) for t in temp]

    # Core logic with slicing and zip
    for i, row in enumerate(matrix):
        shifted_row = row[1:] + [row[0]]  # Circular shift
        product_slice = [a * b for a, b in zip(row, shifted_row)]

        # Use of enumerate and slicing to compute weighted contributions
        for j, val in enumerate(product_slice):
            if i % 2 == 0:
                contribution = val * temp[i % len(temp)] * adjustment_factor
            else:
                contribution = val * (temp[(i + j) % len(temp)] ** 0.5)
            equilibrium_score += contribution

    # Dead code path (never executed under normal input)
    sentinel_flag = False
    if sentinel_flag:
        backup_data = [[x ** 2 for x in r] for r in matrix]
        equilibrium_score -= sum(sum(r) for r in backup_data)

    # Destructuring assignment (tuple unpacking) - partially relevant
    (primary_weight, _) = (0.9, 0.1)
    equilibrium_score *= primary_weight

    # Red herring dictionary operation
    metadata_log = {
        'max_observed': max_val,
        'iterations': rows * cols,
        'final_adjustment': adjustment_factor
    }
    metadata_log['score_snapshot'] = equilibrium_score * 0.5  # Not used

    return equilibrium_score

# Initialize system state
concentration_matrix = [
    [1.2, 3.4, 2.1, 0.8],
    [4.0, 1.1, 2.2, 3.3],
    [0.9, 1.8, 2.7, 3.6]
]
temperature_profile = [298.15, 305.6, 312.4]

# Dummy variables for distraction
placeholder_buffer = [0] * 10
tracking_index = 0
for _ in placeholder_buffer:
    tracking_index += 1

# Key execution point
equilibrium_score = calculate_equilibrium(concentration_matrix, temperature_profile)

# Output result as required
print(f"Result: {equilibrium_score}")