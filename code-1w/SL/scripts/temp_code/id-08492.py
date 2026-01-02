temperatures_celsius = [23.5, 19.0, 27.3, 32.1, 18.8, 25.6, 30.4, 20.2]

# Convert to Fahrenheit and filter out extreme values
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
fahrenheit_readings = [celsius_to_fahrenheit(temp) for temp in temperatures_celsius]

# Identify readings in moderate range using set operations
valid_range_f = set(range(60, 90))
fahrenheit_set = set(fahrenheit_readings)
filtered_readings = fahrenheit_set.intersection(valid_range_f)

# Use enumerate to log index-positioned valid readings (for system logging, not used in result)
indexed_valid = [(i, val) for i, val in enumerate(sorted(filtered_readings))]

# Determine final reported temperature
final_temperature = max(filtered_readings)

print(f"Result: {final_temperature}")