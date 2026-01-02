import itertools

# Simulated sensor array diagnostics with interference from redundant and misleading metrics
sensor_readings = [0.88, 0.92, 0.76, 0.81, 0.94, 0.67, 0.85]
baseline_threshold = 0.8

critical_count = 0
minor_anomalies = 0
aggregate_score = 0.0

def compute_stability_index(readings):
    sorted_vals = sorted(readings)
    median_val = sorted_vals[len(sorted_vals) // 2]
    return sum((r - median_val) ** 2 for r in readings) / len(readings)

def legacy_compatibility_mode(flag=True):
    # Dead code path - never actually used in final logic
    if flag:
        return [x * 0.99 for x in range(50, 100)]
    else:
        return []

def deprecated_normalization(vector):
    # Unused function - red herring
    total = sum(vector)
    return [v / total for v in vector] if total != 0 else vector

# Begin primary diagnostic chain (relevant)
stability_index = compute_stability_index(sensor_readings)

for reading in sensor_readings:
    if reading < baseline_threshold - 0.1:
        critical_count += 1
    elif reading < baseline_threshold:
        minor_anomalies += 1

# Irrelevant transformation chain (distractor)
distorted_copy = [round(x**2 * 1.05, 3) for x in sensor_readings]
temp_shifted = list(itertools.accumulate(distorted_copy))
fake_trend = [t - temp_shifted[0] for t in temp_shifted]

# Decoy statistical analysis (misleading intermediate result)
mean_fake = sum(fake_trend) / len(fake_trend)
variance_fake = sum((x - mean_fake)**2 for x in fake_trend) / len(fake_trend)

# Real scoring logic buried among noise
valid_high_readings = [r for r in sensor_readings if r >= baseline_threshold]
if valid_high_readings:
    aggregate_score = sum(valid_high_readings) / len(valid_high_readings)
else:
    aggregate_score = 0.5

correction_factor = 0
if critical_count > 0:
    correction_factor = -50
elif minor_anomalies > 2:
    correction_factor = -20
else:
    correction_factor = 10

anomaly_weight = stability_index * 100  # Convert to integer-scale impact

# Secondary irrelevant processing (dead path)
expanded_grid = list(itertools.product([1, 2], sensor_readings[:3]))
grid_sum = sum(g[1] for g in expanded_grid if g[0] % 2 == 1)

# Unused data structure manipulation (decoy)
status_map = {i: 'OK' if val >= baseline_threshold else 'ERR' for i, val in enumerate(sensor_readings)}
error_states = [k for k, v in status_map.items() if v == 'ERR']

# Final computation buried in distractions
final_diagnostic = aggregate_score + correction_factor * anomaly_weight

# Fake calibration sequence (irrelevant)
def run_calibration_cycle():
    samples = [i * 0.1 for i in range(10)]
    calibrated = [s + 0.05 for s in samples]
    return sum(calibrated[::2])

# Another decoy function call
placeholder_result = run_calibration_cycle() * 0.77

# Output only the target variable
print(f"Result: {final_diagnostic}")