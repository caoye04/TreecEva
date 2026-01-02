def compute_harmony(values, factors):
    if not values:
        return 0
    weighted_sum = 0
    norm_factor = sum(abs(f) for f in factors)
    for i, (val, fac) in enumerate(zip(values, factors)):
        adjustment = val * (fac / norm_factor)
        weighted_sum += adjustment
    return weighted_sum

# Environmental temperature readings in Celsius
temperatures = [23.5, 19.0, 27.3, 16.8, 22.1]

# Sensor reliability weights
weights = [0.8, 1.2, 0.9, 1.1, 1.0]

# Irrelevant auxiliary variable (minimal distraction)
sensor_count = len(temperatures)

# Core computation
normalized_total = sum(temperatures) / len(temperatures)
total_harmony = compute_harmony(temperatures, weights)

print(f"Result: {total_harmony}")