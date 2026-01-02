def calculate_thermal_response(grid, efficiency_map):
    base_factor = 1.0
    adjustment = 0.0
    temp_history = []
    cumulative_stress = 0
    
    for row in grid:
        row_sum = sum(row)
        if row_sum > 15:
            adjustment += 0.5
        else:
            adjustment -= 0.2

        for cell in row:
            if cell > 0:
                root_val = cell ** 0.5
                adjusted_val = root_val * (1 + adjustment)
                temp_history.append(adjusted_val)

    # Simulate sensor calibration (irrelevant to final result)
    calibration_offset = 0
    for i in range(3):
        calibration_offset += i * 0.1  # Dead computation
    
    # Efficiency processing
    efficiency_total = 0
    for key, value in efficiency_map.items():
        efficiency_total += value if value > 0.7 else 0
    
    # Main capacity calculation
    base_capacity = len(temp_history) * base_factor
    stress_ratio = cumulative_stress / (len(temp_history) or 1)
    
    # Final response calculation (only this matters)
    thermal_response = base_capacity + efficiency_total * 10
    
    # Extra state tracking (distraction)
    diagnostics = {"readings": len(temp_history), "calibration": calibration_offset}
    
    return int(thermal_response)

# Input data
grid = [
    [3, 5, 8],
    [2, 4, 9],
    [1, 6, 7]
]

efficiency_map = {
    "sensor_a": 0.85,
    "sensor_b": 0.65,
    "sensor_c": 0.92,
    "sensor_d": 0.77
}

# Execution
thermal_capacity = calculate_thermal_response(grid, efficiency_map)
print(f"Result: {thermal_capacity}")