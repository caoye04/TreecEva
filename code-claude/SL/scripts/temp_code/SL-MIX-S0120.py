import itertools

# Weather monitoring system - calculating weighted temperature values
temperatures = [22, 24, 21, 23]
# Sensor weights (higher = more reliable sensor)
weights = [2, 3, 2]

# Some monitoring parameters (not directly relevant)
sample_interval = 15  # minutes
alarm_threshold = 30

# Weighted calculations
temperature_avg = sum(temperatures) / len(temperatures)
weight_total = sum(weights)

# Combine temperature and weight data
product_sum = sum(x * y for x, y in itertools.zip_longest(temperatures, weights, fillvalue=1))

# Calculate weighted average (not needed for this problem)
weighted_avg = product_sum / weight_total

print(f"Result: {product_sum}")