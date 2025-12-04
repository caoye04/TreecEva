# Data processing for sensor readings

temperature_readings = [22.5, 23.0, 22.5, 24.1, 23.8, 23.0, 22.9, 23.8, 24.1]

# Filter out readings below threshold
threshold = 23.0
filtered_data = [reading for reading in temperature_readings if reading >= threshold]

# Count readings above average
average = sum(temperature_readings) / len(temperature_readings)
high_readings = len([x for x in temperature_readings if x > average])

# Find unique elements in filtered data
unique_elements = len(set(filtered_data))

# Apply bitwise operations to encode data
encoded = lambda x: (x & 0x0F) | ((x << 4) & 0xF0)
check_value = encoded(unique_elements)

print(f"Result: {unique_elements}")