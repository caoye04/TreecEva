temperatures = [23.5, 19.0, 27.3, 31.2, 18.8, 24.1, 29.5]
humidity_levels = [45, 60, 40, 30, 62, 50, 35]

# Pair temperature and humidity data using zip
temp_humidity_pairs = list(zip(temperatures, humidity_levels))

# Identify indices where temperature exceeds 25 and humidity is below 50
critical_indices = [i for i, (t, h) in enumerate(temp_humidity_pairs) if t > 25 and h < 50]

# Extract corresponding high-risk pairs
filtered_data = [temp_humidity_pairs[i] for i in critical_indices]

# Compute weighted impact score as product of temp and humidity
filtered_sum = sum(map(lambda x: x[0] * x[1], filtered_data))

# Print result for verification
print(f"Result: {filtered_sum}")