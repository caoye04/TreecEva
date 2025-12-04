# Weather station temperature analysis
temperatures = [23.5, 22.8, 25.1, 19.4, 26.7, 21.2, 24.3]

# Additional data from secondary sensors
secondary_readings = [22.9, 23.1, 24.0]

# Process the temperature data
all_temps = temperatures + secondary_readings

# Sort the temperatures for analysis
sorted_temps = all_temps[:]
sorted_temps.sort()

# Calculate the minimum and maximum temperature
min_temp = sorted_temps[0]
max_temp = sorted_temps[-1]
temp_range = max_temp - min_temp

# Find the median temperature
median_temperature = sorted_temps[len(sorted_temps)//2]

# Calculate average temperature
total = sum(sorted_temps)
average_temp = total / len(sorted_temps)

print(f"Result: {median_temperature}")