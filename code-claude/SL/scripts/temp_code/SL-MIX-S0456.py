def process_sensor_readings(readings):
    # Process temperature readings from multiple sensors
    # Filter out invalid readings and calculate the sum of valid readings
    valid_readings = [r for r in readings if 10 <= r <= 40]
    return valid_readings

# Sensor data from different locations (in Celsius)
sensor_data = [12.5, 8.3, 22.1, 45.6, 32.8, 19.7, 5.2, 37.4]

# Some additional data that might be useful later
location_ids = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8']

# Process the sensor readings
filtered_values = process_sensor_readings(sensor_data)

# Calculate statistics
min_temp = min(filtered_values) if filtered_values else 0
max_temp = max(filtered_values) if filtered_values else 0

# Calculate the sum of valid temperature readings
filtered_total = sum(filtered_values)

# Display the results
print(f"Valid readings: {filtered_values}")
print(f"Temperature range: {min_temp} to {max_temp}")
print(f"Result: {filtered_total}")