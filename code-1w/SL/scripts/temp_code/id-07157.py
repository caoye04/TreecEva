def calculate_thermal_response(data):
    # Irrelevant preprocessing: normalize unrelated sensor weights
    sensor_weights = [0.1 * (i + 1) for i in range(len(data))]
    weighted_sum = sum([w * 1.5 for w in sensor_weights])
    adjustment_factor = weighted_sum / (len(sensor_weights) or 1)

    # Distractor: simulate pressure drift (not used in final calculation)
    pressure_drift = 0
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if i % 2 == 0:
                pressure_drift += (val ** 0.5) * (j + 1)
            else:
                pressure_drift -= (val // (j + 1)) if j > 0 else 0

    # Relevant: extract edge temperatures using slicing
    edge_temps = []
    for row in data:
        if len(row) >= 3:
            edge_temps.extend(row[:2] + row[-1:])

    # Use enumerate and zip to pair indices with edge values
    indexed_edges = list(enumerate(edge_temps))
    paired_deltas = [abs(a - b) for a, b in zip(edge_temps, edge_temps[1:])]

    # Secondary distractor: unused dynamic threshold array
    thresholds = [0.8 * delta + adjustment_factor for delta in paired_deltas]
    valid_deltas = [d for d in paired_deltas if d > 0.5]

    # Core logic: compute thermal capacity from mean of valid deltas
    base_response = sum(valid_deltas) / (len(valid_deltas) or 1)
    thermal_growth = 1.0
    for _ in range(3):
        thermal_growth *= 1.1  # Simulate exponential stabilization

    final_capacity = base_response * thermal_growth
    return int(final_capacity)

# Simulated grid data from thermal sensors
grid_data = [
    [4, 8, 6, 3],
    [2, 5, 9, 7],
    [1, 4, 3, 2],
    [8, 6, 5, 9]
]

# Key computation point
thermal_capacity = calculate_thermal_response(grid_data)
print(f"Result: {thermal_capacity}")