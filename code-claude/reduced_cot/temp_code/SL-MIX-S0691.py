# Weather temperature analysis program

# Original temperature readings in Celsius for a week
temperatures = [22, -5, 18, 14, 32, 17, 8]

# Convert to Fahrenheit for reference
fahrenheit_temps = [round((c * 9/5) + 32) for c in temperatures]

# Find readings within comfortable range (10-25°C)
filtered_temps = [t for t in temperatures if 10 <= t <= 25]

# Calculate statistics
max_temp = max(temperatures)
min_temp = min(temperatures)

# Sum of temperatures in comfortable range
filtered_sum = sum(filtered_temps)

# Average of all temperatures
avg_temp = sum(temperatures) / len(temperatures)

print(f"Result: {filtered_sum}")