import itertools

# Data represents daily temperature readings in Celsius
temperature_readings = [22, 24, 19, 21, 23, 20, 25]

# Filter out temperatures below threshold
threshold = 21
filtered_values = [temp for temp in temperature_readings if temp >= threshold]

# Calculate average of filtered temperatures
avg_temperature = sum(filtered_values) / len(filtered_values)
print(f"Average temperature: {avg_temperature:.2f}°C")

# Find the sum of products of all unique pairs
product_sum = sum(x * y for x, y in itertools.combinations(filtered_values, 2))

# Count number of pairs
pair_count = len(list(itertools.combinations(filtered_values, 2)))

# Display the results
print(f"Number of temperature pairs: {pair_count}")
print(f"Result: {product_sum}")