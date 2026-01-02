temperatures_celsius = [23, 19, 34, 44, 12, 47, 28]
humidity_levels = [45, 60, 30, 22, 65, 18, 50]

data_quality_flags = [True, False, True, True, False, True, True]

# Convert temperatures to Fahrenheit
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

# Identify valid readings: good quality and moderate humidity
valid_readings = []
for i, (temp, humidity, flag) in enumerate(zip(temperatures_fahrenheit, humidity_levels, data_quality_flags)):
    if flag and 20 <= humidity <= 60:
        valid_readings.append(temp)

# Filtered dataset based on criteria
valid_entries = [entry for entry in valid_readings if entry > 70]

# Final computation
filtered_sum = sum(valid_entries)
print(f"Result: {filtered_sum}")