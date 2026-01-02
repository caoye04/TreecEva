from itertools import compress

# Sensor data readings in millivolts
data_readings = [102, 115, 98, 124, 130, 119, 95, 108]

# Threshold filter: valid if above 100 mV
temperature_stable = [True, True, False, True, True, False, False, True]

# Apply filtering using compress to get only valid readings
filtered_data = list(compress(data_readings, temperature_stable))

# Calculate sum of filtered sensor readings
filtered_sum = sum(filtered_data)

# Print final result
print(f"Result: {filtered_sum}")