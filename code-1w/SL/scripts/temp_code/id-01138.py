from collections import defaultdict

# Simulate sensor data aggregation in an industrial monitoring system
data_stream = ['85,72,90', '78,65,88', '92,70,95', '80,68,82']
temperature_readings = []
pressure_readings = []
humidity_readings = []

# Parse incoming data with extra processing for fault tolerance
for entry in data_stream:
    values = list(map(int, entry.split(',')))
    temperature_readings.append(values[0])
    pressure_readings.append(values[1])
    humidity_readings.append(values[2])

# Compute derived metrics with redundant intermediate steps
avg_temp = sum(temperature_readings) / len(temperature_readings)
median_pressure = sorted(pressure_readings)[len(pressure_readings)//2]
max_humidity = max(humidity_readings)

# Track historical trends (distractor: not used later)
history_log = defaultdict(int)
for val in temperature_readings:
    history_log[round(val, -1)] += 1

# Calculate stability index (semi-relevant)
stability_scores = []
for i in range(1, len(temperature_readings)):
    diff = abs(temperature_readings[i] - temperature_readings[i-1])
    normalized_diff = 1 - (diff / 100.0)
    stability_scores.append(normalized_diff)

average_stability = sum(stability_scores) / len(stability_scores) if stability_scores else 1.0

# Simulate calibration offset adjustment (dead code path - never triggered in this case)
calibration_factor = 1.0
sensor_status = "nominal"
if min(pressure_readings) < 60:
    calibration_factor = 0.95
    sensor_status = "adjusted"

calibrated_avg = avg_temp * calibration_factor  # Not actually used

# Primary evaluation logic
base_rating = avg_temp / 10  # Base efficiency from temperature

# Performance boost based on pressure consistency and humidity threshold
pressure_variance = sum((p - median_pressure) ** 2 for p in pressure_readings) / len(pressure_readings)
variance_penalty = pressure_variance / 100

humidity_compliance = 1 if max_humidity <= 90 else 0.8
performance_boost = (average_stability * humidity_compliance) - variance_penalty

# Key statement
efficiency_score = base_rating * (1 + performance_boost)

# Output result
print(f"Result: {efficiency_score}")