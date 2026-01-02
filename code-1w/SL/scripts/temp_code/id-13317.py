from itertools import groupby

# Simulate sensor readings with some noise
temperature_readings = [20.1, 20.1, 22.5, 22.5, 22.5, 19.8, 19.8, 25.3, 27.4, 27.4, 27.4, 27.4]

# Remove consecutive duplicates using itertools.groupby
unique_readings = [key for key, _ in groupby(temperature_readings)]

# Apply correction factor to each reading using lambda
corrected_readings = list(map(lambda x: x + 0.5 if x < 20 else x - 0.3, unique_readings))

# Filter out readings below threshold
filtered_readings = [temp for temp in corrected_readings if temp >= 20.0]

# Final computation
processed_data = [round(val, 1) for val in filtered_readings]
filtered_sum = sum(processed_data)

print(f"Result: {filtered_sum}")