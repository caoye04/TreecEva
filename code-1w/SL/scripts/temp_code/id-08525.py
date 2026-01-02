def calculate_thermal_response(grid, threshold):
    rows, cols = len(grid), len(grid[0])
    total_energy = 0
    peak_flux = float('-inf')
    stable_regions = 0
    transient_matrix = [[0] * cols for _ in range(rows)]

    # Simulate heat diffusion across grid layers
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] > threshold:
                total_energy += grid[i][j] * 1.75
                if grid[i][j] > peak_flux:
                    peak_flux = grid[i][j]

    # Identify thermally stable regions (not directly used)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            neighbors = [
                grid[i-1][j], grid[i+1][j],
                grid[i][j-1], grid[i][j+1]
            ]
            if all(abs(grid[i][j] - n) < 5 for n in neighbors):
                stable_regions += 1

    # Apply secondary compensation using list comprehension
    adjustment_factors = [grid[i][j] * 0.1 for i in range(rows) for j in range(cols) if grid[i][j] > threshold]
    compensation = sum(adjustment_factors) if adjustment_factors else 0.0

    # Compute final thermal capacity with adjusted energy
    base_capacity = total_energy + compensation
    efficiency_ratio = 1.0 / (1.0 + (peak_flux * 0.02))
    
    # Dead code path - never executed under current logic
    emergency_override = False
    if base_capacity < 0:
        emergency_override = True  # Unreachable due to positive inputs

    thermal_capacity = int(base_capacity * efficiency_ratio)

    # Irrelevant diagnostic trace
    debug_checksum = sum(sum(row) for row in transient_matrix)
    if debug_checksum > 1000:
        pass  # Placeholder for unused debugging

    return thermal_capacity

# Initialize experimental thermal grid from sensor array
data_grid = [
    [23, 45, 67, 89, 34],
    [12, 77, 91, 76, 21],
    [33, 88, 95, 85, 44],
    [55, 72, 89, 66, 53],
    [21, 44, 58, 77, 61]
]
threshold = 70

# Execute main calculation
thermal_capacity = calculate_thermal_response(data_grid, threshold)
print(f"Result: {thermal_capacity}")