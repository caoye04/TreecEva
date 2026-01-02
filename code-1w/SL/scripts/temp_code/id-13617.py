def calculate_remaining_capacity(grid, excluded_areas):
    total_cells = len(grid) * len(grid[0])
    blocked = set()
    for zone in excluded_areas:
        for coord in zone:
            if coord[0] < len(grid) and coord[1] < len(grid[0]):
                blocked.add(coord)

    # Simulate sensor noise (irrelevant to final result)
    noise_accumulator = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            noise_accumulator += (i ^ j) & 3
    normalized_noise = noise_accumulator / total_cells

    # Real capacity calculation
    available = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in blocked:
                available.add((i, j))

    # Secondary validation pass (partially redundant)
    validated = set()
    for cell in available:
        i, j = cell
        neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        valid_neighbor = False
        for ni, nj in neighbors:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if (ni, nj) not in blocked:
                    valid_neighbor = True
        if valid_neighbor or (i, j) == (0, 0):  # Keep edge cells or origin
            validated.add(cell)

    # Distractor: unused diagnostic metric
    density_ratio = len(available) / total_cells if total_cells else 0
    fragmentation_score = 0
    for cell in validated:
        i, j = cell
        fragmentation_score += (i * j + 1) % 5

    # Final computation
    reserve_margin = len(validated) * 0.1
    base_capacity = len(validated)
    final_capacity = int(base_capacity - reserve_margin)

    # Debugging remnants (dead code)
    debug_log = []
    if len(validated) > 50:
        debug_log.append('High occupancy')
    elif len(validated) > 20:
        debug_log.append('Moderate load')

    return final_capacity

# System initialization
dimensions = (8, 8)
warehouse_grid = [[1 for _ in range(dimensions[1])] for _ in range(dimensions[0])]

# Define damaged zones (tuples of coordinates)
damaged_zones = [
    {(2, 2), (2, 3), (3, 2)},
    {(5, 6), (6, 6), (5, 7)},
    {(7, 0)}
]

# Execute main logic
final_capacity = calculate_remaining_capacity(warehouse_grid, damaged_zones)
print(f"Target result: {final_capacity}")