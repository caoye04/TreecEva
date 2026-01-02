def calculate_zone_capacity(zone):
    total = 0
    for row in zone:
        for cell in row:
            if cell > 0:
                total += cell ** 2
    return total

# Simulate warehouse storage grid (rows represent shelves, values represent item capacity)
warehouse_grid = [
    [3, -1, 4, 2],
    [5, 0, 1, -1],
    [2, 3, 3, 1],
    [-1, 2, 4, 3]
]

# Faulty sensor readings (irrelevant to final logic but used in distraction)
sensor_noise = [0.1, -0.3, 0.0, 0.5]
distorted_readings = [abs(x) * 100 for x in sensor_noise]

# Identify sections with damaged cells (marked as -1)
faulty_positions = set()
for i, row in enumerate(warehouse_grid):
    for j, cell in enumerate(row):
        if cell == -1:
            faulty_positions.add((i, j))

# Extra unused helper function (dead code path)
def validate_sensor_integrity(noise_levels):
    return all(abs(x) < 0.5 for x in noise_levels)

# Track repaired sections (not actually used in final calculation)
repaired_sections = set()
temporary_fix_log = []
for pos in faulty_positions:
    repaired_sections.add(pos)
    temporary_fix_log.append(f"Fixed {pos}")

# Calculate base capacity ignoring faults
raw_capacity = 0
for row in warehouse_grid:
    for val in row:
        if val > 0:
            raw_capacity += val

# Simulate partial recalibration (distractor computation)
recalibration_factor = len(distorted_readings) / (len(sensor_noise) + 1) if sensor_noise else 0
adjusted_capacity_estimate = raw_capacity * (1 + recalibration_factor)

# Actual core logic: compute capacity using squared contributions and subtract overlap
primary_zone = [row[:] for row in warehouse_grid if any(x > 0 for x in row)]
overlap_correction = 0
for i in range(len(primary_zone) - 1):
    shared_cells = 0
    for j in range(len(primary_zone[i])):
        if primary_zone[i][j] > 0 and primary_zone[i+1][j] > 0:
            shared_cells += 1
    overlap_correction += shared_cells * 0.5

# Introduce auxiliary structure (semi-relevant)
capacity_map = {}
for idx, row in enumerate(primary_zone):
    capacity_map[idx] = sum(x for x in row if x > 0)

# Core function that computes final usable capacity
def calculate_remaining_capacity(grid, excluded):
    effective_total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val > 0 and (i, j) not in excluded:
                effective_total += val ** 2  # Higher weight for functional high-capacity cells
    # Additional filtering based on neighborhood
    bonus = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in excluded and grid[i][j] > 2:
                neighbors = 0
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]):
                        if (ni, nj) not in excluded and grid[ni][nj] > 0:
                            neighbors += 1
                if neighbors >= 3:
                    bonus += 1
    return int(effective_total - overlap_correction + bonus)

# Final computation step
final_capacity = calculate_remaining_capacity(warehouse_grid, faulty_positions)
print(f"Result: {final_capacity}")