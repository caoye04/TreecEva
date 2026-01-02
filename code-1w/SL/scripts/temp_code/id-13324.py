def calculate_efficiency(load_profile):
    base_capacity = 120
    peak_multiplier = 1.25
    adjustment_factor = 0.88

    # Simulate dynamic load scaling
    scaled_load = [load * peak_multiplier for load in load_profile]
    average_load = sum(scaled_load) / len(scaled_load)

    # Efficiency calculation with rounding to nearest integer
    raw_efficiency = (average_load / base_capacity) * 100
    rounded_efficiency = round(raw_efficiency)

    # Secondary adjustment using fixed factor
    final_efficiency = rounded_efficiency * adjustment_factor

    return int(final_efficiency)

# System grid data (in MW)
grid_load = [95, 102, 110, 98, 105]

# Irrelevant sensor status (distractor variables)
sensor_a_status = True
sensor_b_status = False
data_latency_ms = 12

# Key computation
energy_threshold = calculate_efficiency(grid_load)

# Output result
print(f"Result: {energy_threshold}")