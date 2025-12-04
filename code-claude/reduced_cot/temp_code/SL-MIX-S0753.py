# Environmental monitoring system data processing
# Process sensor readings to identify active sensors with readings above threshold

sensor_readings = [12.5, 8.3, 15.2, 9.7, 11.0, 7.8, 14.5]
sensor_status = [True, True, False, True, True, False, True]
threshold = 10.0

# Calculate average of all readings for reference
avg_reading = sum(sensor_readings) / len(sensor_readings)
print(f"Average reading: {avg_reading:.2f}")

# Count readings that are above average
above_avg = len([r for r in sensor_readings if r > avg_reading])

# Identify active sensors with readings above threshold
active_sensors = sum(1 for status, reading in zip(sensor_status, sensor_readings) if status and reading > threshold)

# Calculate potential energy savings
energy_savings = active_sensors * 2.5

print(f"Active sensors above threshold: {active_sensors}")
print(f"Potential energy savings: {energy_savings} kWh")