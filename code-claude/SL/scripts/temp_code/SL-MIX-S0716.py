# Weather data analysis
# Analyzing temperature readings to find sum of above-freezing temperatures

freezing_point = 32  # Temperature in Fahrenheit
temperatures = [28, 35, 42, 31, 37, 22, 45, 33, 30, 40]

# Count of all readings
total_readings = len(temperatures)

# Find minimum and maximum temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# Calculate the sum of temperatures above freezing point
filtered_sum = sum([x for x in temperatures if x > freezing_point])

# Calculate average of all temperatures
average_temp = sum(temperatures) / total_readings

print(f"Result: {filtered_sum}")