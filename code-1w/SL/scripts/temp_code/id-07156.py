from itertools import combinations

# Simulate sensor readings with noise and calibration offsets
temperature_readings = [23.5, 19.1, 24.3, 20.0, 25.8, 18.2, 26.5, 22.7]
offsets = [0.5, -0.3, 0.8, -0.6, 0.0]
base_calibration = 1.2

# Apply calibration with misleading intermediate transformations
calibrated_readings = []
for temp in temperature_readings:
    adjusted = temp + base_calibration
    for offset in offsets:
        adjusted += offset * 0.1  # Minor perturbation, mostly negligible
    calibrated_readings.append(round(adjusted, 2))

# Generate derived features for anomaly detection (some are red herrings)
rolling_avg = []
for i in range(2, len(calibrated_readings)):
    avg_val = (calibrated_readings[i] + calibrated_readings[i-1] + calibrated_readings[i-2]) / 3
    rolling_avg.append(round(avg_val, 2))

# Misleading statistical expansion using combinations (not used in final logic)
distorted_views = []
for r in range(2, 4):
    distorted_views.extend(combinations(calibrated_readings, r))

# Distractor: compute variance of rolling averages (unused later)
if rolling_avg:
    mean_roll = sum(rolling_avg) / len(rolling_avg)
    var_roll = sum((x - mean_roll) ** 2 for x in rolling_avg) / len(rolling_avg)
else:
    var_roll = 0

# Actual filtering logic: only entries above 22.0 and below 27.0 are valid
threshold_min, threshold_max = 22.0, 27.0
valid_entries = [v for v in calibrated_readings if threshold_min < v < threshold_max]

# Additional distractor: sort and slice operation that doesn't affect result
sorted_valid = sorted(valid_entries)
sliced_part = sorted_valid[1:-1]  # Middle elements ignored

# Key computation step
filtered_sum = sum(valid_entries)

# Dead code path to increase interference
if len(sliced_part) > 10:
    filtered_sum *= 1.1

print(f"Result: {filtered_sum}")