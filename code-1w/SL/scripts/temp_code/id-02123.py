sensor_values = [23.4, 24.1, 23.9, 24.0, 23.6]
stable_readings = True
for i in range(1, len(sensor_values)):
    if abs(sensor_values[i] - sensor_values[i-1]) > 0.8:
        stable_readings = False

baseline = sum(sensor_values) / len(sensor_values)
system_diagnostic = (max(sensor_values) - min(sensor_values)) / baseline
temperature_status = len(sensor_values) >= 4 and baseline > 23.5

# Key statement
threshold_flag = temperature_status if stable_readings else system_diagnostic > 0.5

# Additional irrelevant variable
irrelevant_count = sum(1 for v in sensor_values if v < 24.0)

print(f"Result: {threshold_flag}")