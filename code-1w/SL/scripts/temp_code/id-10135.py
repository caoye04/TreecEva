def calculate_efficiency(values):
    base_efficiency = 0.85
    adjustment_factor = 1.2
    adjusted = [v * base_efficiency for v in values]
    total = sum(adjusted)
    if total > 100:
        total *= 0.95
    return total

sensor_readings = [20, 25, 30, 15, 40]
offset = 5
transformed_readings = [v + offset for v in sensor_readings]
dummy_var = len(transformed_readings) * 2
energy_output = calculate_efficiency(transformed_readings)
print(f"Result: {energy_output}")