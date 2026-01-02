from itertools import compress

# Simulate sensor readings with some invalid (negative) values
temperature_readings = [23.5, -1, 26.0, -1, 24.8, 25.3, -1, 27.1, 26.9, -1]

# Mask for valid readings (non-negative)
valid_mask = [temp >= 0 for temp in temperature_readings]

# Extract only valid temperatures using compress
valid_temperatures = list(compress(temperature_readings, valid_mask))

# Calculate moving average of valid temperatures using slicing
smoothed_temps = [(valid_temperatures[i] + valid_temperatures[i+1]) / 2 
                     for i in range(len(valid_temperatures) - 1)]

# Select values above threshold
high_temps = [temp for temp in smoothed_temps if temp > 25.0]

# Dummy variable - irrelevant to final result
dummy_counter = len([x for x in temperature_readings if x == -1])

# Final computation: sum of high temperature segments
relevant_values = [val for val in high_temps if val < 27.5]
filtered_sum = sum(relevant_values)

print(f"Result: {filtered_sum}")