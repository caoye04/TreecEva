def calculate_efficiency(filter_func, readings):
    filtered = [r for r in readings if filter_func(r)]
    total_output = sum(filtered)
    count = len(filtered)
    return total_output // count if count > 0 else 0

# Sensor readings in megawatts
power_levels = [75, 82, 88, 79, 91, 83, 68]

# Irrelevant variable (minor distraction - intervention level 5)
current_mode = "eco"

# Key computation
energy_threshold = calculate_efficiency(lambda x: x > 80, power_levels)

print(f"Result: {energy_threshold}")