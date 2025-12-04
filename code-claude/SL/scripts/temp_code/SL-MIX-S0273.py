# Weather station data processing
raw_readings = [22.5, -999, 23.1, 21.8, -999, 24.0, 22.3, -999]

# -999 represents sensor errors that should be excluded
error_code = -999
sensor_count = len(raw_readings)
valid_count = 0

# Extract valid temperature readings using list comprehension
valid_readings = [reading for reading in raw_readings if reading != error_code]

# Calculate statistics
minimum_temp = min(valid_readings)
maximum_temp = max(valid_readings)

# Calculate the average temperature
average_temperature = sum(valid_readings) / len(valid_readings)

# Round to 1 decimal place for reporting
reported_average = round(average_temperature, 1)

print(f"Result: {average_temperature}")