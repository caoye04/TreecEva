def calculate_thermal_response(state_map):
    # Simulate thermal diffusion in a constrained grid
    rows, cols = len(state_map), len(state_map[0])
    temp_grid = [[state_map[i][j] for j in range(cols)] for i in range(rows)]
    
    # Irrelevant pre-processing: normalize unrelated metric
    total_flux = sum(sum(row) for row in state_map)
    normalization_factor = max(1, total_flux // 10)
    adjusted_flux = [row[:] for row in state_map]
    for i in range(rows):
        for j in range(cols):
            adjusted_flux[i][j] = (adjusted_flux[i][j] + 5) // normalization_factor

    # Real computation: count stable thermal zones using conditional logic and set ops
    stable_zones = 0
    visited = set()
    direction_offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(rows):
        for j in range(cols):
            if (i, j) in visited or temp_grid[i][j] < 20:
                continue
            
            # Flood-fill like expansion to find connected high-temp regions
            stack = [(i, j)]
            region_cells = set()
            while stack:
                x, y = stack.pop()
                if (x, y) in region_cells:
                    continue
                region_cells.add((x, y))
                
                for dx, dy in direction_offsets:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if temp_grid[nx][ny] >= 20 and (nx, ny) not in region_cells:
                            stack.append((nx, ny))
            
            # Only count as stable if region size >= 3 and has internal symmetry
            coords_x = [c[0] for c in region_cells]
            coords_y = [c[1] for c in region_cells]
            unique_x = set(coords_x)
            unique_y = set(coords_y)
            
            # Semi-relevant check: symmetry heuristic
            x_center = sum(coords_x) / len(coords_x)
            y_center = sum(coords_y) / len(coords_y)
            symmetric_x = all(abs(x - x_center) == abs(int(x_center)*2 - x - x_center) for x in coords_x)
            symmetric_y = all(abs(y - y_center) == abs(int(y_center)*2 - y - y_center) for y in coords_y)
            
            if len(region_cells) >= 3 and (symmetric_x or symmetric_y):
                stable_zones += 1
            
            # Update visited with current region
            visited.update(region_cells)

    # Distractor: unused transformation of grid
    transposed_grid = [[temp_grid[j][i] for j in range(rows)] for i in range(cols)]
    entropy_score = 0
    for row in transposed_grid:
        for val in row:
            if val > 0:
                entropy_score += val * (val.bit_length() or 1)
    
    # Final capacity depends on stable zones and base energy
    base_energy = sum(1 for row in state_map for cell in row if cell >= 20)
    thermal_capacity = base_energy * (stable_zones + 1) if stable_zones > 0 else base_energy
    
    # Dead code path: never executed due to condition above
    if False and base_energy == 0:
        backup_grid = [[max(0, cell-5) for cell in row] for row in state_map]
        thermal_capacity = sum(sum(row) for row in backup_grid)
    
    return thermal_capacity

# Initial grid state representing temperature readings (in °C)
global_grid = [
    [25, 22, 18, 30],
    [24, 21, 19, 28],
    [17, 23, 26, 27],
    [20, 16, 29, 31]
]

# Key execution point
thermal_capacity = calculate_thermal_response(global_grid)
print(f"Result: {thermal_capacity}")