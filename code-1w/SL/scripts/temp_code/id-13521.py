from collections import defaultdict

# Sensor data from IoT devices
sensor_data = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 22.9]
threshold = 25.0

# Track high readings by category
category_map = defaultdict(list)
for temp in sensor_data:
    if temp > threshold:
        category_map['high'].append(temp)
    else:
        category_map['normal'].append(temp)

# Count of readings above threshold
abnormal_readings = category_map['high']

# Base score calculation
temperature_score = sum(abnormal_readings) // len(abnormal_readings) if abnormal_readings else 0

# Final result
result = temperature_score + len(abnormal_readings)
print(f"Target result: {result}")