def calculate_efficiency(readings):
    avg = sum(readings) / len(readings)
    adjusted = [r * 1.2 for r in readings if r < avg]
    return round(sum(adjusted) / len(readings), 3)

sensor_readings = [15, 23, 18, 32, 27, 14, 20]
valid_sensors = [s for s in sensor_readings if s >= 14]
filtered_readings = list(filter(lambda x: x % 2 == 0, valid_sensors))
baseline = 18
energy_threshold = 0

if len(filtered_readings) > 3:
    energy_threshold = max(filtered_readings) * 0.9
else:
    energy_threshold = calculate_efficiency(filtered_readings)

Result: energy_threshold