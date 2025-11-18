import itertools
from collections import defaultdict

def compute_variance(values):
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / (len(values) - 1)

temperature_readings = [
    [23.5, 24.1, 22.8, 25.0, 23.9],
    [21.0, 22.5, 20.9, 23.3],
    [19.8, 20.1, 19.9, 20.2, 20.0, 19.7]
]

variance_threshold = 2.0
sensor_stability_flags = []

for readings in temperature_readings:
    var = compute_variance(readings)
    is_stable = var <= variance_threshold
    sensor_stability_flags.append(is_stable)

stability_counter = defaultdict(int)
for flag in sensor_stability_flags:
    stability_counter[flag] += 1

active_sensor_combinations = list(itertools.combinations(range(len(temperature_readings)), 2))
valid_combination_count = 0

for i, j in active_sensor_combinations:
    if sensor_stability_flags[i] and sensor_stability_flags[j]:
        valid_combination_count += 1
    if valid_combination_count > 3:
        break

combined_variance = 0.0
if valid_combination_count > 0:
    all_valid_readings = []
    for idx, is_stable in enumerate(sensor_stability_flags):
        if is_stable:
            all_valid_readings.extend(temperature_readings[idx])
    combined_variance = compute_variance(all_valid_readings)

final_stability_index = round(valid_combination_count * combined_variance, 2) if combined_variance > 0 else 0.0
print(f"Result: {final_stability_index}")