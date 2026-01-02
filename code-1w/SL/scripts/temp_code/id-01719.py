def calculate_remaining_capacity(grid, restrictions):
    total_cells = len(grid) * len(grid[0])
    blocked_set = set(restrictions)
    reserved_zones = set()
    temp_sum = 0

    # Simulate temperature zones (irrelevant to capacity but adds computation)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'TEMP_ZONE':
                temp_sum += (i + j) % 3

    # Identify reserved areas based on case-sensitive pattern
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cell_id = f'{i},{j}'
            if grid[i][j].lower() == 'reserved':
                reserved_zones.add(cell_id)

    # Count available cells
    available_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cell_key = f'{i},{j}'
            if cell_key not in blocked_set and cell_key not in reserved_zones:
                available_count += 1

    # Dummy linear search that doesn't affect result
    search_target = 'unused_search'
    found_index = -1
    for idx, row in enumerate(grid):
        if search_target in [cell.lower() for cell in row]:
            found_index = idx
            break

    # Final capacity calculation
    maintenance_margin = 5
    final_capacity = available_count - maintenance_margin

    # Print result as required
    print(f"Target result: {final_capacity}")
    return final_capacity

# Initialize warehouse layout
warehouse_grid = [
    ['normal', 'normal', 'RESERVED', 'normal'],
    ['normal', 'TEMP_ZONE', 'normal', 'normal'],
    ['normal', 'normal', 'normal', 'TEMP_ZONE'],
    ['RESERVED', 'normal', 'normal', 'normal']
]

# Define blocked sections (by coordinate)
blocked_sections = ['0,2', '3,0', '1,1']

# Call function to compute capacity
final_capacity = calculate_remaining_capacity(warehouse_grid, blocked_sections)