# Weather data analysis for a week
temperatures = [23.5, 18.2, 27.8, 22.1, 19.7, 30.4, 25.6]
humidity = [65, 72, 58, 61, 70, 55, 63]

# Find average temperature
avg_temp = sum(temperatures) / len(temperatures)

# Set threshold to be 80% of maximum temperature
max_temp = max(temperatures)
threshold = 0.8 * max_temp

# Get temperatures above threshold and calculate their sum
filtered_sum = sum([x for x in temperatures if x > threshold])

# Calculate number of comfortable days (temp between 20-26 and humidity < 70)
comfortable_days = len([i for i in range(len(temperatures)) if 20 <= temperatures[i] <= 26 and humidity[i] < 70])

print(f"Result: {filtered_sum}")