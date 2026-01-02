def calculate_efficiency(readings, limit):
    above_limit = list(filter(lambda x: x > limit, readings))
    return len(above_limit) / len(readings) if readings else 0

# Sensor data from thermal array
temperature_readings = [23.5, 32.1, 45.6, 27.8, 51.3, 39.4, 41.2]
baseline_offset = 2.0
threshold = 35.0
scaling_factor = 100.0

# Compute effective thermal capacity based on efficiency
thermal_efficiency = calculate_efficiency(temperature_readings, threshold)
thermal_capacity = calculate_efficiency(temperature_readings, threshold) * scaling_factor

# Additional sensor metrics (irrelevant to main computation)
avg_temp = sum(temperature_readings) / len(temperature_readings)
max_deviation = max(abs(t - avg_temp) for t in temperature_readings)

Result: thermal_capacity