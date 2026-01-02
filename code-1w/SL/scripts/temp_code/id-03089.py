from collections import defaultdict

# Simulate warehouse storage grid with inventory counts
def generate_warehouse_grid():
    grid = defaultdict(int)
    positions = [
        (0,0), (0,1), (0,3),
        (1,0), (1,2), (1,3),
        (2,1), (2,2), (2,3)
    ]
    for i, (x, y) in enumerate(positions):
        grid[(x, y)] = (i * 3 + 7) % 11  # Non-uniform inventory distribution
    return grid

def detect_blocked_zones():
    # These zones are under maintenance
    return {(0,1), (1,2), (2,3)}

def analyze_access_paths(grid):
    # Irrelevant analysis for routing - distractor
    rows = defaultdict(set)
    cols = defaultdict(set)
    for (x, y) in grid.keys():
        rows[x].add(y)
        cols[y].add(x)
    connectivity = 0
    for r in rows:
        if len(rows[r]) > 1:
            connectivity += 1
    return connectivity  # Not used later

def calculate_density_profile(grid):
    # Another distractor: analyzes density but not used in final calculation
    density = defaultdict(float)
    for x in range(3):
        total = sum(grid[(x, y)] for y in range(4))
        if total > 0:
            density[x] = round(total / 4.0, 3)
    return dict(density)

def calculate_remaining_capacity(grid, blocked):
    total_capacity = 0
    max_per_cell = 10
    for x in range(3):
        for y in range(4):
            if (x, y) not in blocked:
                current = grid[(x, y)]
                available = max_per_cell - current
                total_capacity += available
    # Apply efficiency factor based on layout continuity (semi-relevant)
    occupied = {pos for pos in grid if grid[pos] > 0}
    adjacent_free = 0
    for (i, j) in occupied:
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (i+dx, j+dy)
            if neighbor not in blocked and neighbor not in grid and 0 <= neighbor[0] < 3 and 0 <= neighbor[1] < 4:
                adjacent_free += 1
    efficiency_bonus = min(adjacent_free // 3, 5)  # Max bonus of 5
    total_capacity += efficiency_bonus
    return total_capacity

# Main execution
warehouse_grid = generate_warehouse_grid()
blocked_zones = detect_blocked_zones()
connectivity_score = analyze_access_paths(warehouse_grid)  # Dead computation
density_map = calculate_density_profile(warehouse_grid)      # Dead computation
final_capacity = calculate_remaining_capacity(warehouse_grid, blocked_zones)
print(f"Result: {final_capacity}")