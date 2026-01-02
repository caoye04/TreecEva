from itertools import combinations

# System parameters
temperature = 23.5
elevation = 150
humidity = 68

# Sensor readings (simulated)
sensor_data = [4, 7, 2, 9, 5, 8]

# Generate all unique pairs of sensor readings
pairs = list(combinations(sensor_data, 2))

# Calculate product for each pair
products = [a * b for a, b in pairs]

# Filter products greater than 30
filtered_products = [p for p in products if p > 30]

# Compute final result
result = sum(filtered_products)

print(f"Target result: {result}")