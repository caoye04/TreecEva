from collections import defaultdict, Counter

# Simulated sensor data over time with noise and redundant readings
timestamped_readings = [
    (100, [3.2, 3.5, None, 3.4, 3.6]),
    (101, [4.1, None, 4.3, 4.2, 4.2]),
    (102, [2.9, 3.1, 3.0, None, 3.2]),
    (103, [5.0, 5.1, 5.0, 5.2, None]),
    (104, [3.8, 3.7, 3.9, 3.8, 3.7])
]

# Irrelevant auxiliary mapping (distractor)
status_interpretation = {
    'normal': 0,
    'warning': 1,
    'critical': 2,
    'unknown': -1
}

# Dead code path - never called (distractor)
def legacy_calibrate(x):
    return x * 0.98 + 0.1

# Unused transformation function (red herring)
def smooth_signal(readings):
    cleaned = [r for r in readings if r is not None]
    return sum(cleaned) / len(cleaned) if cleaned else 0.0

# Misleading intermediate accumulator (looks important but unused later)
shadow_accumulator = 0.0
for ts, vals in timestamped_readings:
    valid = [v for v in vals if v is not None]
    if valid:
        avg = sum(valid) / len(valid)
        shadow_accumulator += avg ** 0.5

# Core processing begins here
sensor_metrics = defaultdict(list)
for ts, readings in timestamped_readings:
    filtered = [r for r in readings if r is not None]  # Remove nulls
    if filtered:
        mean_val = sum(filtered) / len(filtered)
        rounded_val = round(mean_val, 1)
        sensor_metrics[ts].append(rounded_val)

# Extract sequence of processed values
processed_sequence = []
for key in sorted(sensor_metrics.keys()):
    processed_sequence.extend(sensor_metrics[key])

# Bitmask simulation for system cycle
system_ticks = 104 - 100
cycle_phase = (system_ticks << 2) & 15  # Should yield 8

# Anomaly detection via simple threshold and pattern counting
trend_counter = Counter()
for i in range(1, len(processed_sequence)):
    if processed_sequence[i] > processed_sequence[i-1]:
        trend_counter['up'] += 1
    elif processed_sequence[i] < processed_sequence[i-1]:
        trend_counter['down'] += 1
    else:
        trend_counter['stable'] += 1

# Compute base health score from trends
base_health = trend_counter['up'] * 2 - trend_counter['down'] * 3

# Secondary scoring from raw magnitude analysis
magnitude_score = 0
for val in processed_sequence:
    if val >= 4.0:
        magnitude_score += 2
    elif val >= 3.0:
        magnitude_score += 1
    else:
        magnitude_score -= 1

# Combine into aggregate (this is used)
aggregate_health_score = base_health + magnitude_score

# Spurious independent calculation (distractor)
temporal_variance = 0
prev = processed_sequence[0]
for curr in processed_sequence[1:]:
    temporal_variance += abs(curr - prev)
    prev = curr
temporal_variance = round(temporal_variance, 2)

# Unused recursive helper (dead code, red herring)
def count_patterns(seq, idx=0, count=0):
    if idx >= len(seq) - 1:
        return count
    delta = seq[idx+1] - seq[idx]
    if delta > 0.5:
        return count_patterns(seq, idx + 1, count + 1)
    return count_patterns(seq, idx + 1, count)

# Anomaly bitmask based on trend imbalance
anomaly_mask = 0
if trend_counter['down'] > trend_counter['up']:
    anomaly_mask |= 4
if magnitude_score < 5:
    anomaly_mask |= 2
if processed_sequence[-1] < 3.5:
    anomaly_mask |= 1  # Set bit 0

# Key statement — this determines the answer
final_diagnostic = aggregate_health_score + (cycle_phase ^ anomaly_mask)

# Additional irrelevant final computation (distractor)
consistency_ratio = len(processed_sequence) / (len(timestamped_readings) * 1.0)
adjusted_diagnostic = final_diagnostic * (0.9 + 0.2 * consistency_ratio) if consistency_ratio > 1 else final_diagnostic

print(f"Result: {final_diagnostic}")