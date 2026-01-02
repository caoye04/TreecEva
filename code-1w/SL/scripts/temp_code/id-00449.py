def calculate_efficiency(load, factor):
    base_efficiency = 92.5
    adjustment = sum([int(x * factor) for x in load]) // len(load)
    return base_efficiency + adjustment

grid_load = [18, 24, 36, 42, 33]
capacity_factor = 0.87

# Irrelevant auxiliary variables (minimal distraction)
temperature_readings = [22.1, 23.5, 21.9]
uptime_hours = 98.7

energy_threshold = calculate_efficiency(grid_load, capacity_factor)
print(f"Result: {energy_threshold}")