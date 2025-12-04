# Weather monitoring system data processing
temperatures = [23, 18, 25, 16, 20, 22, 17]

# Calculate average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Find min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# Create list of temperature differences from average
temp_diffs = [abs(t - avg_temp) for t in temperatures]

# Calculate the sum of temperatures at even indices only
filtered_sum = sum(map(lambda x: x[1], filter(lambda item: item[0] % 2 == 0, enumerate(temperatures))))

# Process the data with zip for reporting
processed_data = list(zip(temperatures, temp_diffs))

# Display results
print(f"Average temperature: {avg_temp:.1f}")
print(f"Temperature range: {min_temp} to {max_temp}")
print(f"Result: {filtered_sum}")