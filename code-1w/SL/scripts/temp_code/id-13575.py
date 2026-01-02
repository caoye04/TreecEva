from collections import defaultdict

def calculate_harmony(values, importance):
    scaled = [v * w for v, w in zip(values, importance)]
    avg = sum(scaled) / len(scaled)
    variance = sum((x - avg) ** 2 for x in scaled) / len(scaled)
    return int(avg + variance ** 0.5)

# Environmental temperature readings in Celsius (fictional sensor data)
temperatures = [18, 21, 19, 23, 20]

# Sensor reliability weights (based on calibration history)
weights = [0.9, 1.1, 1.0, 1.2, 0.8]

# Secondary unrelated metric (distractor - not used in final result)
deviation_count = defaultdict(int)
for t in temperatures:
    deviation_count[abs(t - 20)] += 1

# Core computation
total_harmony = calculate_harmony(temperatures, weights)

Result: total_harmony