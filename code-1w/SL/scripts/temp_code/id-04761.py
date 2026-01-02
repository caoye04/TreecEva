from itertools import compress

# Sensor data readings with some noise
temperature_readings = [23.5, 19.0, 25.3, 18.7, 30.2, 27.1, 22.0, 29.8]
threshold = 22.5

# Create a mask for temperatures above threshold
valid_readings_mask = [temp > threshold for temp in temperature_readings]

# Extract high-temperature readings using compress
filtered_values = list(compress(temperature_readings, valid_readings_mask))

# Sum the filtered values
filtered_sum = sum(filtered_values)

# Output result
print(f"Result: {filtered_sum}")