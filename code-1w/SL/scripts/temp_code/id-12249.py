def calculate_efficiency(levels):
    total = 0
    for level in levels:
        if level > 0:
            total += level * 0.85
    return round(total, 3)

# Sensor readings from turbine array (irrelevant: timestamps)
timestamps = ['08:00', '08:05', '08:10', '08:15']
power_levels = [120, -1, 150, 0, 130]

# Data validation check (distraction)
valid_data = all(isinstance(x, int) for x in power_levels)

energy_output = calculate_efficiency(power_levels)
print(f'Result: {energy_output}')