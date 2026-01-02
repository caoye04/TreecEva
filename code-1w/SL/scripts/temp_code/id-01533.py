def calculate_harmony(values, factors):
    scaled = map(lambda x: x * 1.5, values)
    weighted = [a * b for a, b in zip(scaled, factors)]
    filtered = [val for val in weighted if val > 0]
    return sum(filtered) // len(filtered) if filtered else 0

# Environmental temperature readings in Celsius (simulated hourly data)
temperatures = [22, 19, 24, 27, 20]

# Sensor reliability weights (based on calibration history)
weights = [0.8, 0.95, 0.7, 0.6, 1.0]

# Secondary derived metric - average temp deviation (not used in final result)
avg_temp = sum(temperatures) / len(temperatures)
deviations = [abs(t - avg_temp) for t in temperatures]

# Core computation
total_harmony = calculate_harmony(temperatures, weights)

Result: {total_harmony}