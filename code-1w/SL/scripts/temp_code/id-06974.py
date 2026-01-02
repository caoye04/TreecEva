def analyze_stability(matrix):
    stability_score = 0
    for row in matrix:
        for val in row:
            stability_score += abs(val) % 3
    return stability_score


def calculate_thermal_output(grid, efficiency_map):
    base_power = 0
    adjustment_factor = 1.0
    temp_buffer = [0] * len(grid)
    
    # Irrelevant stability analysis (distractor)
    stability = analyze_stability(grid)
    if stability > 10:
        adjustment_factor *= 0.95

    # Real computation begins
    for i in range(len(grid)):
        row_slice = grid[i][1:-1]  # Use slicing
        for j, cell in enumerate(row_slice):
            coord_key = f'{i}_{j+1}'
            if coord_key in efficiency_map:
                raw_yield = cell * efficiency_map[coord_key]
                # Dead code path (misleading)
                if raw_yield < 0:
                    continue
                base_power += int(raw_yield)  # Only integer contributions

    # Additional irrelevant adjustments
    peak = max(max(row) for row in grid)
    if peak > 20:
        base_power -= 5  # Minor red herring

    # Final adjustment using modular arithmetic
    cycle_offset = len(grid) % 4
    thermal_capacity = base_power + (cycle_offset * 2)
    
    return thermal_capacity

# Setup input data
grid = [
    [5, 8, 3, 12],
    [9, 15, 7, 6],
    [2, 11, 14, 4],
    [10, 13, 8, 1]
]

efficiency_map = {
    '0_1': 1.2,
    '1_1': 0.9,
    '2_1': 1.1,
    '3_1': 1.0,
    '1_2': 1.3,
    '2_2': 0.8
}

# Misleading intermediate calculations
noise_level = sum(sum(row) for row in grid) / 16
reference_ratio = noise_level / 7.5

# Key statement
thermal_capacity = calculate_thermal_output(grid, efficiency_map)

# Print result
print(f"Result: {thermal_capacity}")