def calculate_stability_index(grid, limit):
    rows, cols = len(grid), len(grid[0])
    total_energy = 0
    edge_count = 0
    temp_buffer = []

    # Accumulate energy from stable zones (even indices)
    for i in range(0, rows, 2):
        for j in range(0, cols, 2):
            total_energy += grid[i][j]

    # Count active edges (irrelevant to final result but adds cognitive load)
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                edge_count += 1

    # Simulate transient fluctuations (distraction)
    for i in range(rows):
        fluctuation_row = [grid[i][j] ** 0.5 for j in range(cols) if grid[i][j] > 0]
        temp_buffer.extend(fluctuation_row)

    # Core logic: sum of diagonal elements modulated by threshold
    diag_sum = sum(grid[k][k] for k in range(min(rows, cols)))
    modulation_factor = abs(diag_sum) % limit if limit != 0 else 0

    # Secondary distraction: reverse slicing with no impact
    reversed_corners = grid[-1][::-1] + grid[0][::-1]
    corner_average = sum(reversed_corners) / len(reversed_corners) if reversed_corners else 0

    # Final computation: stability index based on diagonal and threshold
    stability_score = diag_sum + modulation_factor
    energy_threshold = stability_score * 2  # Key assignment point

    # Dead code path: never executed due to fixed condition
    if False:
        energy_threshold -= corner_average

    return energy_threshold

# Initialize 4x4 grid representing thermal readings in a reactor core
grid = [
    [3, 7, 2, 9],
    [1, 8, 4, 5],
    [6, 3, 7, 2],
    [9, 1, 8, 4]
]
threshold = 7

# Execute main calculation
energy_threshold = calculate_stability_index(grid, threshold)
print(f"Result: {energy_threshold}")