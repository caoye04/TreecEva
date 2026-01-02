from collections import defaultdict

# Simulated sensor data over time (location -> list of temperature readings)
sensor_data = {
    'boiler': [78, 80, 82, 79],
    'radiator': [65, 67, 66, 68],
    'engine': [85, 83, 86, 84]
}

# Irrelevant distractor: unused variable for humidity (minimal interference)
humidity_levels = defaultdict(lambda: 0, {zone: 40 + i*2 for i, zone in enumerate(sensor_data.keys())})

# Compute average temperature across all sensors
total_readings = []
for location, temps in sensor_data.items():
    total_readings.extend(temps)

sum_temp = sum(total_readings)
count = len(total_readings)
avg_temp = sum_temp / count

# System state flag (based on pressure stability)
pressure_fluctuations = [0.1, 0.3, 0.2, 0.4]
stability_window = [p < 0.35 for p in pressure_fluctuations]
stable_conditions = stability_window.count(True) >= 3

critical_threshold = 75.0

# Key decision logic
final_temperature = max(avg_temp, critical_threshold) if stable_conditions else min(avg_temp, critical_threshold)

print(f"Result: {final_temperature}")