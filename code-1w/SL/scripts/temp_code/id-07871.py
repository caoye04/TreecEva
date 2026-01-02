import math

# Simulated sensor array diagnostics with interference
sensor_ids = ['S101', 'S102', 'S103', 'S104']
readings_raw = [1024, 768, 512, 256]
calibration_offsets = {'S101': 24, 'S102': -12, 'S103': 36, 'S104': 0}

# Irrelevant preprocessing: normalize to percentage (red herring)
normalized_readings = [r / max(readings_raw) * 100 for r in readings_raw]
percentile_map = {sid: norm for sid, norm in zip(sensor_ids, normalized_readings)}

# Distractor: unused signal smoothing function
def smooth_signal(data, factor=0.1):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * factor + data[i] * (1 - factor))
    return smoothed

# Real computation begins: apply calibration (relevant)
calibrated_readings = [
    r + calibration_offsets[sid] for r, sid in zip(readings_raw, sensor_ids)
]

# Bit manipulation for error detection code (misleading but looks important)
error_syndrome = 0
for val in calibrated_readings:
    error_syndrome ^= (val & 0xFF) ^ (val >> 8)

# Hidden checksum used later (decoy usage)
checksum = sum(calibrated_readings) & 0xFFFF

# Extract trend features using slicing and transformations (relevant)
trend_window = calibrated_readings[1:3]  # middle sensors only
trend_data = [abs(t - calibrated_readings[i+1]) for i, t in enumerate(trend_window)]
baseline = sum(calibrated_readings) / len(calibrated_readings)

# Spurious statistical analysis (dead path)
variance = sum((x - baseline) ** 2 for x in calibrated_readings) / len(calibrated_readings)
std_dev = math.sqrt(variance)
z_scores = [(x - baseline) / std_dev for x in calibrated_readings]
outliers = [z for z in z_scores if abs(z) > 2]

# Simulate fault pattern matching with enumeration (distractor)
fault_patterns = [(0, 10), (1, -5), (2, 0)]
matched_faults = []
for i, val in enumerate(calibrated_readings):
    for pos, effect in fault_patterns:
        if i == pos and val % 10 == abs(effect) % 10:
            matched_faults.append((i, effect))

# Unused recursive diagnostic (decoy function)
def recursive_diagnose(val, depth=0):
    if depth >= 3 or val < 10:
        return val
    return recursive_diagnose(val // 4, depth + 1)

# Anomaly detection via dictionary lookup and bit flags (partially relevant)
anomaly_flags = {i: (calibrated_readings[i] & (calibrated_readings[i]-1)) == 0 for i in range(len(calibrated_readings))}
anomaly_score = 0
for i, is_power_of_two in anomaly_flags.items():
    if is_power_of_two:
        anomaly_score += calibrated_readings[i] // 16

# Real metric aggregation function
def aggregate_metrics(metrics, reference):
    total = 0
    for i, m in enumerate(metrics):
        factor = 1 + (i * 0.5)
        total += m * factor
    adjustment = math.floor(reference / 100)
    return int(total - adjustment)

# Key statement: combines actual logic chain
final_diagnostic = aggregate_metrics(trend_data, baseline) + anomaly_score // 2

# Print result as required
print(f"Result: {final_diagnostic}")