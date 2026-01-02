sensor_readings = [105, 210, 198, 97, 230, 142, 117, 201]
threshold = 100

# Classify sensors based on dynamic thresholds
responsive_sensors = {val for val in sensor_readings if val > threshold}
efficient_sensors = {val for val in sensor_readings if val % 3 == 0}
stable_sensors = {val for val in sensor_readings if val < 200}

# Determine overlap between efficient and stable performance
dynamic_range = max(sensor_readings) - min(sensor_readings)
baseline = sum(sensor_readings) / len(sensor_readings)

filtration_score = len(efficient_sensors & stable_sensors)

# Output result
print(f"Result: {filtration_score}")