from collections import defaultdict

# Simulate warehouse storage grid and damage assessment

def analyze_storage_density(grid):
    density_map = defaultdict(int)
    total_cells = 0
    for row in grid:
        for cell in row:
            if cell > 0:
                density_map['active'] += 1
            elif cell == 0:
                density_map['empty'] += 1
            total_cells += 1
    density_map['total'] = total_cells
    return density_map

def detect_damaged_areas(sensors):
    alerts = []
    false_positives = 0
    for reading in sensors:
        if reading < 0.1:
            alerts.append(True)
        else:
            # Misleading: this tracking isn't used later
            false_positives += (1 if reading > 0.5 else 0)
    # Return only actual damage flags
    return [idx for idx, val in enumerate(alerts) if val]

def calculate_remaining_capacity(grid, excluded_regions):
    base_capacity = 0
    temp_buffer = 0  # Distractor: used for no real purpose
    
    # Simulate capacity loss due to structural stress in high-density rows
    stress_penalty = 0
    for i, row in enumerate(grid):
        row_sum = sum(row)
        if row_sum > 15:
            stress_penalty += 2  # Arbitrary penalty
        temp_buffer += row_sum * 0.1  # Dead computation

    # Actual usable capacity calculation
    for i, row in enumerate(grid):
        if i not in excluded_regions:
            for j, unit in enumerate(row):
                if unit > 0:
                    base_capacity += unit
    
    # Apply environmental degradation factor (constant)
    degradation_factor = 0.95
    final_capacity = int(base_capacity * degradation_factor - stress_penalty)
    
    # Unrelated logging
    log_entry = f"Processed {len(grid)} rows with {len(excluded_regions)} exclusions."
    return final_capacity

# Initialize warehouse layout (simulated sensor-derived grid)
warehouse_grid = [
    [4, 5, 0, 3],
    [6, 7, 8, 0],
    [0, 2, 1, 9],
    [5, 0, 6, 4]
]

# Sensor readings for structural integrity (one per row)
sensor_readings = [0.08, 0.35, 0.02, 0.45]

# Analyze layout (distractor call - not directly used)
density_analysis = analyze_storage_density(warehouse_grid)

# Detect damaged zones from sensor data
damaged_zones = detect_damaged_areas(sensor_readings)

# Compute final operational capacity
final_capacity = calculate_remaining_capacity(warehouse_grid, damaged_zones)

print(f"Result: {final_capacity}")