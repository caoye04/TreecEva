def calculate_safety_margin(loads, limit):
    filtered_loads = [load for load in loads if load > limit * 0.75]
    average_load = sum(filtered_loads) / len(filtered_loads) if filtered_loads else 0
    safety_factor = 1.35
    return average_load * safety_factor

# System parameters
critical_point = 82.4
thermal_loads = [67.2, 75.1, 88.3, 91.0, 79.8, 85.6]

# Irrelevant sensor offset (minimal distraction)
sensor_offset = 2.1
adjusted_loads = [x + sensor_offset for x in thermal_loads]  # unused

# Key computation
energy_threshold = calculate_safety_margin(thermal_loads, critical_point)

print(f"Result: {energy_threshold}")