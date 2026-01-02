def preprocess_readings(raw_data):
    processed = []
    for val in raw_data:
        if val < 0:
            val = abs(val) * 2
        processed.append(val + 10)
    return processed

raw_sensor_data = [3, -5, 7, -2]
filtered_data = preprocess_readings(raw_sensor_data)

# Irrelevant transformation chain (distractor)
baseline_offset = 45
adjusted_readings = [x - baseline_offset for x in filtered_data]
scaled_readings = [int(x * 1.5) for x in adjusted_readings if x > 5]
aggregated_total = sum(scaled_readings) // 2 if scaled_readings else 0

# Energy matrix from sensors (relevant data structure)
energy_matrix = [
    [12, 8, 15],
    [6, 11, 9],
    [14, 7, 10]
]

# Efficiency mapping per zone (dictionary operation - relevant)
efficiency_map = {
    'zone_A': 0.85,
    'zone_B': 0.92,
    'zone_C': 0.78
}

# Dead code path (misleading function)
def deprecated_calc(x):
    return (x ** 2) % 7

# Unused helper with bit manipulation red herring
bitmask = 0b1010
flag_check = bitmask & 4

# Conditional expression used idiomatically (required feature)
mode = 'turbo' if aggregated_total > 100 else 'normal'

# Simulated time-series drift correction (irrelevant)
drift_accumulator = 0.0
for i in range(len(filtered_data)):
    drift_accumulator += filtered_data[i] * 0.01

corrected_level = int(filtered_data[0] - drift_accumulator)

# Core calculation logic (relevant)
def calculate_thermal_output(matrix, efficiencies):
    total_energy = 0
    weights = list(efficiencies.values())
    
    # Accumulate weighted row sums using efficiency values
    for idx, row in enumerate(matrix):
        row_sum = sum(row)
        weight = weights[idx % len(weights)]
        total_energy += row_sum * weight
    
    # Apply conditional adjustment based on mode (conditional expression)
    modifier = 1.25 if mode == 'turbo' else 0.9
    
    # Bitwise check that looks important but is actually irrelevant
    debug_flag = (total_energy ^ 255) & 1
    
    # Final capacity with rounding
    capacity = int(total_energy * modifier)
    
    # Dead branch (never executed due to mode)
    if mode == 'debug':
        capacity = capacity ^ 10
        capacity += 500  # Misleading large offset
    
    return capacity

# Key statement
thermal_capacity = calculate_thermal_output(energy_matrix, efficiency_map)

# Print result as required
print(f"Result: {thermal_capacity}")