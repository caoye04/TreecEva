def calculate_stability_index(state_grid):
    rows, cols = len(state_grid), len(state_grid[0])
    total_energy = 0
    edge_contributions = 0
    corner_multiplier = 1.5
    
    # Misleading initialization of irrelevant metrics
    debug_mode = True
    log_entries = []
    system_health = 100.0
    decay_rate = 0.05
    
    for i in range(rows):
        for j in range(cols):
            cell_value = state_grid[i][j]
            neighbors = 0
            
            # Valid energy accumulation from neighbors
            if i > 0:
                neighbors += state_grid[i-1][j]
            if j > 0:
                neighbors += state_grid[i][j-1]
            if i < rows - 1:
                neighbors += state_grid[i+1][j]
            if j < cols - 1:
                neighbors += state_grid[i][j+1]
            
            total_energy += abs(cell_value - neighbors / 4)

            # Irrelevant health tracking (distractor)
            if cell_value < 0:
                system_health -= decay_rate * 10
                log_entries.append(f"Anomaly at ({i},{j})")

    # Fake edge logic with partial use
    edge_cells = [state_grid[i][j] for i in range(rows) for j in range(cols) if i == 0 or j == 0 or i == rows-1 or j == cols-1]
    edge_contributions = sum(edge_cells) * 0.1

    # Actual core calculation (only total_energy matters)
    base_index = total_energy * 10
    
    # Dummy conditional that doesn't affect final result
    if system_health < 90:
        base_index *= 0.95
    
    return int(base_index)

# Simulated sensor grid (not related to sensors as a theme, just structured data)
grid_state = [
    [3, -1, 2],
    [1,  0, 4],
    [-2, 3, 1]
]

# Extraneous pre-processing (distractor)
processed_layers = [[x**2 for x in row] for row in grid_state]
consistency_check = sum(sum(row) for row in processed_layers)

# Key computation
energy_threshold = calculate_stability_index(grid_state)

# Output result
print(f"Result: {energy_threshold}")