from itertools import combinations

# System parameters for sensor array calibration
temperature_readings = [23.4, 25.1, 24.8, 26.7, 22.9, 27.3, 26.1]
base_offsets = [1.2, 0.9, 1.5, 0.7, 1.3]

efficiency_scores = []

# Simulate dynamic response under varying conditions
for i in range(len(temperature_readings) - 2):
    window_avg = sum(temperature_readings[i:i+3]) / 3
    adjusted_avg = window_avg - base_offsets[i % len(base_offsets)]
    efficiency_scores.append(round(adjusted_avg * 1.75, 2))

# Evaluate combinatorial stability across triplets
diagnostic_checks = []
for combo in combinations([10, 20, 30, 40], 3):
    diagnostic_checks.append(combo[0] + combo[1] + combo[2])

# Final capacity assessment
peak_capacity = max(efficiency_scores)

Result: peak_capacity