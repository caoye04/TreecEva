# Weather data analysis
temperatures = [22, 19, 24, 21, 18, 23, 20, 25, 17]
humidity = [65, 70, 55, 60, 75, 50, 65, 45, 80]

# Calculate average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Create filter function to find temperatures above average
filter_func = lambda temps: [t for t in temps if t > avg_temp]

# Get sum of temperatures above average
filtered_sum = sum(filter_func(temperatures))

# Get the temperature range
temp_range = max(temperatures) - min(temperatures)

# Get a slice of the highest temperatures
highest_temps = sorted(temperatures, reverse=True)[:3]

print(f"Result: {filtered_sum}")