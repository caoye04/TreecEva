def analyze_system_stability():
    # Simulate a 2D grid of sensor readings (temperature variations)
    raw_readings = [i * (i + 3) % 17 for i in range(36)]
    grid = [raw_readings[i:i+6] for i in range(0, 36, 6)]

    # Irrelevant preprocessing: normalize values to [0,1] (not used in final calculation)
    normalized_grid = [[val / max(raw_readings) for val in row] for row in grid]

    # Misleading statistical summary
    mean_val = sum(sum(row) for row in grid) / len(grid)**2
    variance_proxy = sum((cell - mean_val)**2 for row in grid for cell in row) / len(grid)**2

    # Window size determined by conditional expression
    system_load = 8
    window_size = 3 if system_load > 5 else 2

    # Auxiliary function to compute stability index
    def calculate_stability_index(matrix, w):
        center_i, center_j = 2, 2  # Target region at center
        subgrid = [row[center_j:center_j+w] for row in matrix[center_i:center_i+w]]

        # Extract edge elements using slicing and flattening
        edges = []
        if w >= 3:
            edges += subgrid[0][:-1] + [subgrid[i][-1] for i in range(w-1)]
            edges += subgrid[w-1][::-1][:-1] + [subgrid[i][0] for i in range(w-1)][::-1]
            edges = list(dict.fromkeys(edges))  # Remove duplicates while preserving order

        # Dummy transformation on edges (irrelevant to core logic)
        transformed_edges = [e ^ 7 for e in edges if e % 2 == 1]  # XOR odd values

        # Core stability metric: sum of central 2x2 with modular adjustment
        core_sum = sum(subgrid[i][j] for i in range(1, min(w, 3)) for j in range(1, min(w, 3)))
        adjustment_factor = len(transformed_edges) % 4 if transformed_edges else 1

        # Final index includes redundant bitwise masking
        stability_index = (core_sum * adjustment_factor) & 0xFFFF

        return stability_index

    # Secondary unused computation path (distractor)
    backup_window = 2
    fallback_score = 0
    for i in range(0, 6, backup_window):
        for j in range(0, 6, backup_window):
            block = [grid[x][y] for x in range(i, i+backup_window) for y in range(j, j+backup_window)]
            fallback_score += max(block) - min(block)

    # Key execution point
    energy_threshold = calculate_stability_index(grid, window_size)

    # Print result as required
    print(f"Result: {energy_threshold}")

    return energy_threshold

# Execute and capture result
analyze_system_stability()