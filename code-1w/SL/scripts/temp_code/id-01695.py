from itertools import combinations, cycle
import math

# System health monitoring simulation with diagnostic filtering

# Real-time sensor inputs (simulated)
sensor_readings = [14, 28, 19, 35, 22, 47, 31, 29]

# Irrelevant backup buffer (distractor)
backup_cache = [x ** 2 for x in sensor_readings if x < 30]

# Baseline calibration curve (unused red herring)
calibration_curve = list(map(lambda x: round(math.sin(x / 10), 4), range(1, len(sensor_readings) + 1)))

# Historical anomaly thresholds (misleading context)
thresh_critical = 45
thresh_warning = 30

# Simulated event log tags (dead code path)
event_tags = []
for val in sensor_readings:
    if val > thresh_critical:
        event_tags.append('CRITICAL')
    elif val > thresh_warning:
        event_tags.append('WARNING')
    else:
        event_tags.append('NORMAL')

# Active processing: filter anomalies above warning level but below critical
candidate_anomalies = [x for x in sensor_readings if thresh_warning < x < thresh_critical]

# Secondary validation: must appear in top quartile of rolling pairs
rolling_pairs = list(combinations(sensor_readings, 2))
pair_averages = [round((a + b) / 2, 2) for a, b in rolling_pairs]
valid_pair_set = {val for pair in rolling_pairs for val in pair if sum(pair) / 2 > 32.0}

# Refine candidates: only those participating in high-average pairs
candidate_anomalies = [x for x in candidate_anomalies if x in valid_pair_set]

# Diagnostic weight assignment per anomaly
weight_map = {}
for idx, val in enumerate(candidate_anomalies):
    # Complex weighting with decay factor and position penalty
    base_weight = val * 0.85
    position_decay = 0.95 ** idx
    jitter_comp = math.cos(val % 3)  # Irrelevant stabilization term
    weight_map[val] = base_weight * position_decay * jitter_comp  # Jitter has no real effect due to small magnitude

# Decoy transformation chain (never used)
transform_cycle = cycle([2, -1, 3])
decoy_sequence = []
for i, w in enumerate(weight_map.values()):
    decoy_sequence.append(w * next(transform_cycle))

# True aggregation logic begins
baseline_offset = sum([x for x in sensor_readings if x % 2 == 0]) // len(sensor_readings)

# Processing chain: apply logarithmic scaling only to weights above median
temp_weights = sorted(weight_map.values())
median_weight = temp_weights[len(temp_weights) // 2] if temp_weights else 0
scaled_weights = []
for w in weight_map.values():
    if w >= median_weight:
        scaled_weights.append(math.log(w * 1.5 + 1e-5))  # Prevent log(0)
    else:
        scaled_weights.append(w + 0.1)

# Apply exponential smoothing in processing chain
alpha = 0.7
smoothed = []
if scaled_weights:
    smoothed.append(scaled_weights[0])
    for i in range(1, len(scaled_weights)):
        smoothed.append(alpha * scaled_weights[i] + (1 - alpha) * smoothed[i-1])

processing_chain = [round(x, 4) for x in smoothed]

# Final diagnostic computed from smoothed values and baseline offset
final_diagnostic = aggregate_metrics = lambda chain, offset: int(sum(chain) * offset)
final_diagnostic = aggregate_metrics(processing_chain, baseline_offset)

# Output result
print(f"Result: {final_diagnostic}")