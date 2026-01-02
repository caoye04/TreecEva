def calculate_harmony(values, factors):
    total_harmony = 0
    for i, (val, fac) in enumerate(zip(values, factors)):
        adjusted = val * fac
        if i % 2 == 0:
            total_harmony += adjusted ** 0.5
        else:
            total_harmony -= adjusted / 2
    return total_harmony

# Environmental temperature readings in Celsius
temperatures = [16, 25, 36, 49]

# Seasonal weighting factors
weights = [0.5, 1.0, 0.8, 1.2]

# Irrelevant baseline measurement
baseline = 20.0

# Compute harmony index
total_harmony = calculate_harmony(temperatures, weights)

# Output result
print(f"Result: {total_harmony}")