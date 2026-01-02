def calculate_thermal_output(region):
    base = sum(sum(row) for row in region)
    adjustment = len(region) * len(region[0])
    return base * 1.5 - adjustment

# Simulated geothermal grid sensor readings (arbitrary units)
sensor_grid = [
    [3, 1, 4, 2, 9],
    [6, 8, 5, 7, 1],
    [2, 9, 3, 6, 4],
    [8, 4, 7, 5, 3],
    [1, 6, 2, 8, 7]
]

# Irrelevant preprocessing: normalize each row (not used in final calculation)
normalized_grid = []
for row in sensor_grid:
    min_val, max_val = min(row), max(row)
    normalized_row = [(x - min_val) / (max_val - min_val + 1e-8) for x in row]
    normalized_grid.append(normalized_row)

# Secondary analysis: frequency of values (distractor)
frequency_map = {}
for row in sensor_grid:
    for val in row:
        frequency_map[val] = frequency_map.get(val, 0) + 1

top_values = sorted(frequency_map.items(), key=lambda x: -x[1])[:3]

# Data slicing based on geological zone of interest
zone_x, zone_y = 1, 1
width, height = 3, 3
grid_slice = [row[zone_y:zone_y+height] for row in sensor_grid[zone_x:zone_x+width]]

# Auxiliary computation: perimeter sum (semi-relevant but not used directly)
perimeter_sum = 0
for i in range(len(grid_slice)):
    for j in range(len(grid_slice[i])):
        if i == 0 or i == len(grid_slice)-1 or j == 0 or j == len(grid_slice[i])-1:
            perimeter_sum += grid_slice[i][j]

# Core thermal model integration
core_energy = 0
for i, row in enumerate(grid_slice):
    for j, val in enumerate(row):
        weight = 1 + (i + j) * 0.1
        core_energy += val * weight

# Final threshold check (does not alter outcome)
effective = core_energy > 50
status_flag = 'ACTIVE' if effective else 'STANDBY'

# Key statement that determines the answer
thermal_capacity = calculate_thermal_output(grid_slice)

# Additional irrelevant state tracking
current_mode = 'SCANNING'
scan_progress = 0
while scan_progress < 100:
    scan_progress += 25
    if scan_progress == 50:
        current_mode = 'ANALYZING'

print(f'Result: {thermal_capacity}')