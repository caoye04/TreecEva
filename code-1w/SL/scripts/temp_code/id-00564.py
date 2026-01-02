from collections import defaultdict

# Simulated sensor readings over time
sensor_data = [
    ('temp', 23.5), ('pressure', 101.3), ('temp', 24.1), ('humidity', 45),
    ('pressure', 102.0), ('temp', 22.8), ('humidity', 47), ('pressure', 99.7),
    ('pressure', 100.8), ('temp', 23.0)
]

# Group readings by type
data_by_type = defaultdict(list)
for sensor, value in sensor_data:
    data_by_type[sensor].append(value)

# Extract pressure readings
pressure_readings = data_by_type['pressure']

# Calculate stability index as mean absolute deviation from median
median_pressure = sorted(pressure_readings)[len(pressure_readings) // 2]
deviations = [abs(p - median_pressure) for p in pressure_readings]

# Irrelevant: temperature average (minor distraction)
temp_readings = data_by_type['temp']
avg_temp = sum(temp_readings) / len(temp_readings)

# Stability metric based on pressure consistency
def calculate_stability(readings):
    if len(readings) < 2:
        return 0.0
    mean_deviation = sum(deviations) / len(deviations)
    return round(median_pressure - mean_deviation, 3)

# Compute final index
pressure_index = calculate_stability(pressure_readings)

print(f"Result: {pressure_index}")