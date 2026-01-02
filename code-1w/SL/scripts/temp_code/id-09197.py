def calculate_stability_index(grid, limit):
    total = 0
    peak = 0
    temp_buffer = []
    for row in grid:
        row_sum = sum(row)
        temp_buffer.append(row_sum)
        if row_sum > peak:
            peak = row_sum
        total += row_sum
    
    # Misleading intermediate calculations
    average_row = total / len(grid) if grid else 0
    fluctuation_score = (peak - average_row) * 0.5
    normalization_factor = 1.0 if peak == 0 else peak
    
    # Actual key logic embedded here
    stable_count = 0
    for i, val in enumerate(temp_buffer):
        if val <= limit:
            stable_count += (i + 1)  # Weighted by position
    
    # Red herring: complex-looking but unused calculation
    entropy = 0
    for x in temp_buffer:
        if x > 0:
            entropy -= (x / total) * ((x / total) ** 0.5)
    
    return int(stable_count * normalization_factor) if normalization_factor else 0

# System configuration
system_active = True
safety_engaged = False
redundancy_level = 4

# Simulated sensor grid readings (3x3)
diagnostic_grid = [
    [12, 8, 15],
    [7, 5, 9],
    [10, 11, 6]
]

# Threshold for stability evaluation
critical_threshold = 10

# Auxiliary variables with no direct impact
diagnostic_mode = "verbose"
baseline_offset = 0.0034
iteration_log = []

# Key computation with conditional expression
energy_threshold = calculate_stability_index(diagnostic_grid, critical_threshold) if system_active else 0

# More distraction: unused scaling logic
scaling_profile = [redundancy_level ** 0.5 for _ in range(3)]
adjusted_energy = energy_threshold * (scaling_profile[0] if safety_engaged else 1)

# Final output
print(f"Result: {energy_threshold}")