# Weather station temperature analysis
temperatures = [23.5, 19.7, 25.0, 21.8, 22.3]

# Convert readings from Celsius to Fahrenheit for analysis
fahrenheit_temps = []
for temp in temperatures:
    fahrenheit_temps.append(temp * 9/5 + 32)

# Sort the original temperature readings for median calculation
sorted_temps = sorted(temperatures)
mid_index = len(temperatures) // 2

# Calculate the median temperature
median_temperature = sorted_temps[mid_index] if len(temperatures) % 2 == 1 else (sorted_temps[mid_index-1] + sorted_temps[mid_index]) / 2

# Calculate average temperature (not needed for final result)
average_temp = sum(temperatures) / len(temperatures)

# Temperature range information
temp_range = max(temperatures) - min(temperatures)

print(f"Result: {median_temperature}")