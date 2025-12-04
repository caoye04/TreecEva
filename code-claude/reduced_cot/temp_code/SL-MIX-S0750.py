# Temperature data processing for weather analysis
# Processing daily temperature readings to find specific patterns

temperatures = [12, 15, 9, 22, 18, 24, 16, 10]
average_temp = sum(temperatures) / len(temperatures)

# Convert temperatures to Fahrenheit for international reporting
temp_in_fahrenheit = [round((t * 9/5) + 32) for t in temperatures]

# Track days with significant temperature changes
significant_changes = {i for i in range(1, len(temperatures)) if abs(temperatures[i] - temperatures[i-1]) > 5}

# Process numbers for specific analysis
numbers = [14, 7, 22, 16, 31, 8, 24, 10]
threshold = 10

# Calculate sum of even numbers above threshold
filtered_sum = sum(num for num in numbers if num % 2 == 0 and num > threshold)

# Check for days with both high temperature and significant changes
warm_days = len([t for t in temperatures if t > 20])

print(f"Result: {filtered_sum}")