def calculate_stability_index(temps, depths):
    stability_sum = 0
    temp_changes = []
    depth_intervals = []
    
    for i in range(len(temps) - 1):
        delta_temp = temps[i + 1] - temps[i]
        delta_depth = depths[i + 1] - depths[i]
        if delta_depth != 0:
            gradient = delta_temp / delta_depth
            temp_changes.append(abs(gradient))
            depth_intervals.append(delta_depth)
    
    # Distractor: Compute average depth (not used in final result)
    avg_depth = sum(depths) / len(depths)
    max_gradient = max(temp_changes) if temp_changes else 0
    
    # Simulate correction factor based on pressure layers (semi-relevant)
    pressure_weights = [d ** 0.5 for d in depths if d > 0]
    weighted_stability = 0
    for val in temp_changes:
        weighted_stability += val * 0.8
    
    # Key logic: stability index derived from normalized max gradient
    raw_index = max_gradient * 10
    
    # Red herring: entropy-like computation with no impact
    entropy_proxy = 0
    for t in temps:
        if t != 0:
            entropy_proxy += t * (-t / 100) 
    
    # Final index adjusted by fixed heuristic
    stability_score = int(raw_index) + 5
    return stability_score

# Experimental dataset from oceanic thermal profiling
base_temperature = 20
altitude_effect = -0.01
humidity_factor = 3.2

# Real input data
depth_layers = [0, 100, 200, 300, 400]
temperature_profile = [base_temperature + i * altitude_effect * 10 for i in range(len(depth_layers))]

# Add noise correction (unused branch - dead code path)
correction_matrix = []
for z in enumerate(temperature_profile):
    if z[0] % 2 == 0:
        correction_matrix.append(z[1] * 0.95)

# Sensor calibration offset (irrelevant variable)
sensor_bias = sum(humidity_factor / (i + 1) for i in range(5))

# Primary computation
thermal_gradient = calculate_stability_index(temperature_profile, depth_layers)

# Output result as required
print(f"Result: {thermal_gradient}")