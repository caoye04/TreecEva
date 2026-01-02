from itertools import combinations
from math import log

# Simulate environmental sensor readings over time
temperature_readings = [22, 25, 19, 24, 27, 30, 28]
humidity_readings = [45, 50, 60, 55, 40, 35, 50]
pressure_readings = [1013, 1015, 1010, 1008, 1012, 1016, 1014]

# Auxiliary data — some may not be directly used
wind_speed_avg = sum([12, 15, 10, 14, 16, 13, 11]) / 7
baseline_calibration = 0.98
drift_compensation = 0.02

# Pack sensor data into tuples for processing
sensor_data = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Misleading transformation — looks important but unused in final result
def transform_for_calibration(data):
    calibrated = []
    for t, h, p in data:
        adjusted_t = t * baseline_calibration
        adjusted_h = h + drift_compensation * 10
        adjusted_p = p * (1 + drift_compensation)
        calibrated.append((adjusted_t, adjusted_h, adjusted_p))
    return calibrated

# Red herring function: appears relevant but not called
def analyze_outliers(data):
    temp_vals = [t for t, _, _ in data]
    mean_temp = sum(temp_vals) / len(temp_vals)
    outliers = [t for t in temp_vals if abs(t - mean_temp) > 5]
    return outliers

# Real processing pipeline
lambda_filter = lambda x: x[0] >= 24 and x[1] <= 55  # High temp, moderate humidity
filtered_data = list(filter(lambda_filter, sensor_data))

# Generate all possible 3-element subsequences to simulate pattern search
subsequences = list(combinations(filtered_data, 3))
relevance_score = 0
for seq in subsequences:
    temps = [s[0] for s in seq]
    humids = [s[1] for s in seq]
    pressures = [s[2] for s in seq]
    # Arbitrary scoring to increase cognitive load
    score = (sum(temps) / 3) * (100 - sum(humids) / 3) / (max(pressures) - min(pressures) + 1)
    if score > relevance_score:
        relevance_score = score

# Unused intermediate calculation — distractor
dummy_aggregate = sum([log(p + 1) for _, _, p in sensor_data]) / len(sensor_data)

# Core logic: compute yield based on valid entries
valid_entries = 0
yield_accum = 0.0
for temp, humid, press in sensor_data:
    if temp >= 20 and humid <= 60:
        # Yield formula: temperature efficiency × pressure stability factor
        efficiency = (temp - 20) * 1.5
        stability_factor = press / 1010
        yield_contrib = efficiency * stability_factor
        yield_accum += yield_contrib
        valid_entries += 1

# Final computation using only core logic
if valid_entries > 0:
    average_yield_per_valid = yield_accum / valid_entries
    adjustment_factor = len(filtered_data) / len(sensor_data)
    final_yield = int(average_yield_per_valid * (1 + adjustment_factor))
else:
    final_yield = 0

# Irrelevant string manipulation — adds noise
status_log = "Sensor run complete"
parts = status_log.split(' ')
joined = '-'.join(parts)
ignored_flag = len(joined) > 10

print(f"Result: {final_yield}")