# Temperature data processing for weather analysis
temperature_readings = [22.5, 19.8, 25.2, -999.0, 18.5, 23.7, -999.0, 20.1]

# Some utility functions
celsius_to_fahrenheit = lambda c: c * 9/5 + 32
is_valid = lambda x: x > -50 and x < 50

# Process the temperature data
valid_temps = []
for temp in temperature_readings:
    # Filter out error values (marked as -999.0)
    if temp != -999.0:
        valid_temps.append(temp)

# Extract a slice of the valid temperatures for analysis
temp_slice = valid_temps[1:4]

# Apply additional filtering criteria
filtered_temps = list(filter(is_valid, temp_slice))

# Calculate the average of filtered temperatures
filtered_avg = sum(filtered_temps) / len(filtered_temps)

# For verification, also calculate max temperature in fahrenheit
max_temp_f = celsius_to_fahrenheit(max(valid_temps))

print(f"Result: {filtered_avg}")