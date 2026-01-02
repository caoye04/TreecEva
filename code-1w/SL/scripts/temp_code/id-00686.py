def calculate_remaining_capacity(grid, obstacles):
    total_cells = len(grid) * len(grid[0])
    reserved = set()
    temp_sum = 0
    
    # Simulate some irrelevant preprocessing
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            temp_sum += i * j + grid[i][j]
            if grid[i][j] > 5:
                reserved.add((i, j))

    # Actual logic: track available cells not blocked and not over capacity
    available = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in obstacles and grid[i][j] <= 10:
                available.add((i, j))
    
    # Simulate additional distraction with unused tracking
    overflow_zones = []
    for i, row in enumerate(grid):
        count_high = sum(1 for val in row if val > 8)
        if count_high > 2:
            overflow_zones.append(i)
    
    # Final calculation
    base_capacity = len(available)
    penalty = len(reserved.intersection(available))  # overlap adjustment
    final_capacity = base_capacity - penalty
    
    # Extra red herring: modify temp_sum based on overflow (not used later)
    adjustment_factor = len(overflow_zones) * 2
    temp_sum -= adjustment_factor
    
    return final_capacity

# Initialize warehouse grid (simulated storage levels)
warehouse_grid = [
    [3, 7, 2, 9, 4],
    [6, 1, 8, 5, 11],
    [4, 3, 7, 2, 6],
    [10, 12, 1, 3, 8]
]

# Blocked positions due to maintenance
blocked_positions = {(1, 4), (3, 1), (0, 3)}

# Compute result
final_capacity = calculate_remaining_capacity(warehouse_grid, blocked_positions)
print(f"Target result: {final_capacity}")