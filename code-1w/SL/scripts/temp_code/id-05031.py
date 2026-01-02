temperatures_celsius = [23.5, 19.0, 25.8, 17.2, 30.1, 28.6, 21.3, 15.7]

# Convert to Fahrenheit using list comprehension
temperatures_fahrenheit = [(c * 9/5) + 32 for c in temperatures_celsius]

# Select only afternoon readings (index even)
afternoon_temps = [temp for i, temp in enumerate(temperatures_fahrenheit) if i % 2 == 0]

# Filter out values below freezing in Fahrenheit
filtered_temps = [temp for temp in afternoon_temps if temp > 32]

base_temp = 70
threshold_count = sum(1 for temp in filtered_temps if temp > base_temp)

Result: threshold_count