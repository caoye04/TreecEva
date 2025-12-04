# Processing environmental sensor data
sensor_readings = [18, 23, 7, 14, 32, 9, 27, 5]
base_threshold = 6

# Initial data analysis
total_readings = len(sensor_readings)
average_reading = sum(sensor_readings) / total_readings

# Apply bitwise filter to identify readings meeting criteria
filtered_count = len([s for s in sensor_readings if s & base_threshold > 0])

# Additional metrics calculation
max_reading = max(sensor_readings)
min_reading = min(sensor_readings)

print(f"Result: {filtered_count}")