import itertools

def calculate_thermal_response(grid, thresh):
    temp_log = []
    surge_count = 0
    suppression_factor = 1.0
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell > thresh:
                surge_count += 1
                temp_log.append(cell * 0.85)
            else:
                temp_log.append(cell * 0.1)
    
    # Irrelevant smoothing pass (distractor)
    smoothed = [sum(temp_log[i:i+3]) / 3 for i in range(len(temp_log) - 2)] if len(temp_log) > 2 else temp_log
    
    # Dummy conditional that never triggers (dead code path)
    if len(smoothed) > 1000:
        suppression_factor = 0.5
    
    # Actual relevant computation
    active_cells = list(itertools.compress(temp_log, (x > 5 for x in temp_log)))
    
    # Secondary filtering with zip and enumerate
    filtered_pairs = [(i, val) for i, val in enumerate(active_cells) if i % 2 == 0]
    correction_offset = sum(i * 0.01 for i, _ in filtered_pairs)
    
    base_response = sum(active_cells)
    thermal_response = base_response - correction_offset
    
    # Additional red herring: unused transformation
    inverted_grid = [[1 / (1 + abs(cell)) for cell in row] for row in grid]
    entropy_proxy = sum(itertools.chain(*inverted_grid))
    
    return int(thermal_response)

# Simulated sensor grid data (real input)
grid_state = [
    [3, 12, 7, 15],
    [9, 4, 18, 6],
    [11, 8, 5, 13],
    [2, 10, 14, 1]
]
threshold = 8

# Key assignment statement
thermal_capacity = calculate_thermal_response(grid_state, threshold)

# Print final result as required
print(f"Result: {thermal_capacity}")