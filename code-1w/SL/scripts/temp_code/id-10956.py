import itertools

# Sensor readings from multiple environmental monitoring stations
temperature_readings = [23.4, 19.5, 27.8, 22.1, 30.3, 18.7, 25.6, 24.2]
humidity_readings = [45, 50, 60, 85, 30, 90, 70, 80]

# Identify anomalies: temperatures above 25.0 or humidity above 80 (potential sensor faults)
anomaly_flags = [(temp > 25.0 or humid > 80) for temp, humid in zip(temperature_readings, humidity_readings)]

# Generate all pairs of consecutive anomaly flags to detect sustained issues
consecutive_pairs = list(itertools.pairwise(anomaly_flags))
streak_count = sum(1 for a, b in consecutive_pairs if a and b)

# Filter temperature anomalies only where humidity was normal
filtered_temperatures = [temp for temp, humid in zip(temperature_readings, humidity_readings) if temp > 25.0 and humid <= 80]

# Simulate binary encoding of filtered indices for compact transmission
transmission_key = 0
for i, temp in enumerate(filtered_temperatures):
    if temp > 27.0:
        transmission_key |= (1 << i)

# Final filtration score: count of anomalies with normal humidity
filtered_anomalies = [1 for temp in filtered_temperatures if temp > 26.0]
filtration_score = sum(filtered_anomalies)

Result: filtration_score