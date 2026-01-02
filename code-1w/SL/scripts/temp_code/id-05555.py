import math

# Simulated sensor data from environmental monitoring stations
data_stream = [32.4, 35.1, -999, 33.8, -999, 36.2, 37.5, -999, 38.0, 34.9, 33.0, 36.5]

# Placeholder for calibration coefficients (irrelevant to final result)
calibration_map = {i: round(math.sin(i * 0.1), 4) for i in range(15)}

# Decoy function – appears useful but unused in critical path
def normalize readings(readings):
    max_val = max(readings)
    return [x / max_val for x in readings]

# Data cleaning: remove invalid readings marked as -999
valid_readings = [x for x in data_stream if x != -999]

# Additional irrelevant transformation (distractor)
shifted_readings = [round(x + 0.5, 2) for x in valid_readings]

# Historical baselines (unused red herring)
historical_avg = 34.2
seasonal_offset = 1.3
projected_trend = historical_avg + seasonal_offset  # Irrelevant calculation

# Filter readings above dynamic threshold
threshold_limit = sum(valid_readings) / len(valid_readings) + 1.5

# Lambda-based dynamic threshold function (used later)
threshold_func = lambda x: x > threshold_limit

# Another decoy structure: mapping with no downstream use
deviation_report = {
    f'hour_{i}': round(abs(val - historical_avg), 3)
    for i, val in enumerate(valid_readings)
}

# Filtered high-value readings
filtered_data = list(filter(threshold_func, valid_readings))

# Set operations to identify anomalies (core concept)
baseline_set = set(round(x, 0) for x in valid_readings)
anomaly_set = set(round(x, 0) for x in filtered_data)
unique_anomalies = anomaly_set - baseline_set  # Always empty – misleading!

# Recursive depth counter (distractor with apparent complexity)
def recursion_probe(n, depth=0):
    if n <= 1:
        return depth
    return recursion_probe(n // 2, depth + 1)

probe_result = recursion_probe(len(valid_readings))  # Unused result

# Core analysis logic using lambda and set concepts
analyze_readings = lambda readings, func: \
    len([r for r in readings if func(r)]) * \
    (int(math.log2(len(set(int(r) for r in readings)) + {0}) + 1) if readings else 1)

# Critical execution point
final_diagnostic = analyze_readings(filtered_data, threshold_func)

# Extraneous post-processing (dead code path)
optimized_output = []
for val in filtered_data:
    if val > 37.0:
        optimized_output.append({'level': 'high', 'value': val})

# Print target result
print(f"Target result: {final_diagnostic}")