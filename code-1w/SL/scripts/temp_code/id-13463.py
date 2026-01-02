def calculate_thermal_output(grid):
    base_factor = 1.5
    modifier = 0.8
    temp_grid = [row[1:4] for row in grid[1:4]]  # Slice central 3x3 region
    total_power = 0
    penalty = 0

    # Misleading computation: irrelevant frequency analysis
    frequency_map = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            val = grid[i][j]
            frequency_map[val] = frequency_map.get(val, 0) + 1
    dominant_value = max(frequency_map, key=frequency_map.get)
    anomaly_score = abs(dominant_value - 5) * 0.1  # Unused distraction

    # Relevant energy accumulation with conditional branching
    for i in range(len(temp_grid)):
        for j in range(len(temp_grid[i])):
            cell = temp_grid[i][j]
            if cell > 7:
                total_power += cell * base_factor
            elif cell > 4:
                total_power += cell * modifier
            else:
                penalty += 2  # Small penalty for low values

    # Simulated calibration offset (irrelevant)
    calibration_sequence = [i ** 2 for i in range(6) if i % 2 == 0]
    calibration_sum = sum(calibration_sequence)  # Dead code path

    # Final output influenced only by total_power and fixed adjustment
    raw_output = total_power - penalty
    efficiency_ratio = 0.91
    thermal_capacity = int(raw_output * efficiency_ratio)

    # Additional red herring: unused state tracking
    state_log = []
    for idx, row in enumerate(temp_grid):
        active_cells = sum(1 for x in row if x > 5)
        state_log.append((idx, active_cells))

    return thermal_capacity

# Initial system grid configuration
grid_state = [
    [3, 5, 7, 2, 8],
    [4, 6, 9, 1, 3],
    [7, 8, 6, 5, 4],
    [2, 9, 4, 7, 1],
    [5, 3, 8, 6, 9]
]

# Key execution point
thermal_capacity = calculate_thermal_output(grid_state)
print(f"Result: {thermal_capacity}")