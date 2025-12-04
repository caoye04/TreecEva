# Analyzing overlapping data points from two temperature sensors
temperature_sensor1 = [23.5, 24.0, 22.8, 23.5, 25.1, 24.0, 22.8]
temperature_sensor2 = [22.8, 23.9, 25.1, 24.0, 23.5, 22.0]

# Extract data points present in both sensors
common_readings = set(temperature_sensor1).intersection(temperature_sensor2)

# Process the data
filtered_data = []
for i, temp in enumerate(temperature_sensor1):
    if i % 2 == 0 or temp in common_readings:
        filtered_data.append(round(temp))

# Calculate unique elements in the filtered data
unique_elements = len(set(filtered_data))

# Display the result
print(f"Result: {unique_elements}")