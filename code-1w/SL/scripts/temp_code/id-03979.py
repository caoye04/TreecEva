from collections import defaultdict

# Simulated sensor readings over time for multiple sensors
timestamps = [100, 101, 102, 103, 104, 105]
sensor_ids = ['S1', 'S2', 'S3']
raw_readings = [
    [23.1, 45.0, 67.3],
    [24.5, 44.1, 68.0],
    [22.9, 46.2, 67.1],
    [25.0, 45.8, 69.4],
    [23.4, 44.0, 66.8],
    [24.1, 45.5, 68.2]
]

# Build structured sensor data using zip and enumerate
sensor_data = defaultdict(list)
for t_idx, ts in enumerate(timestamps):
    for s_idx, sid in enumerate(sensor_ids):
        sensor_data[sid].append((ts, raw_readings[t_idx][s_idx]))

# Thresholds for anomaly detection
thresholds = {
    'S1': (22.0, 25.0),  # normal range
    'S2': (44.0, 46.0),
    'S3': (66.0, 69.0)
}

# Tracking variables (some are just distractions)
anomaly_count = defaultdict(int)
stability_index = defaultdict(float)
drift_accumulator = 0.0
baseline_snapshot = {}
consistency_flags = []

# Compute per-sensor statistics
for sid, records in sensor_data.items():
    baseline_snapshot[sid] = records[0][1]  # first reading as baseline
    lower, upper = thresholds[sid]
    total_deviation = 0.0
    valid_readings = 0
    prev_val = None

    for ts, value in records:
        if lower <= value <= upper:
            consistency_flags.append(True)
            valid_readings += 1
            if prev_val is not None:
                drift_accumulator += abs(value - prev_val)  # accumulates across all sensors
            prev_val = value
        else:
            anomaly_count[sid] += 1
            consistency_flags.append(False)

        # Irrelevant intermediate calculation (distractor)
        temp_adjustment = (value * 0.98 + 1.5) / 1.02
        stability_index[sid] += temp_adjustment * 0.1  # misleading use

    stability_index[sid] /= len(records)  # normalization (not used later)

# Misleading global summary (dead-end computation)
global_stability = sum(stability_index.values()) / len(stability_index)
overall_consistency = sum(consistency_flags) / len(consistency_flags) if consistency_flags else 0

# Core logic: calculate final score based on anomalies and drift
anomaly_penalty = sum(anomaly_count.values()) * 10
drift_score = int(drift_accumulator)  # contributes to final result
base_performance = 100 - anomaly_penalty

# Secondary adjustment based on S1 and S3 behavior
s1_range = max([v for _, v in sensor_data['S1']]) - min([v for _, v in sensor_data['S1']])
s3_last = sensor_data['S3'][-1][1]

# Final score calculation
final_score = base_performance - drift_score
final_score += int(s1_range * 2)  # small correction
if s3_last > thresholds['S3'][1]:
    final_score -= 5
else:
    final_score += 3

# Output the target result
Result: {final_score}