# Temperature data analysis for weekly readings
temperature_readings = [22.5, 25.8, 27.1, 23.4, 19.6, 24.3, 26.5]
celsius_adjustment = 0.8
threshold = 24.0

# Process the temperature readings
processed_temperatures = [temp - celsius_adjustment for temp in temperature_readings]

# Calculate average temperature
average_temp = sum(processed_temperatures) / len(processed_temperatures)

# Find temperatures above threshold
high_temps = [temp for temp in processed_temperatures if temp > threshold]

# Calculate sum of temperatures above threshold
filtered_sum = sum([x for x in processed_temperatures if x > threshold])

# Count days with high temperatures
high_temp_days = len(high_temps)

print(f"Result: {filtered_sum}")