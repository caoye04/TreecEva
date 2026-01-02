from collections import defaultdict, Counter

# Simulated sensor data stream (temperature, pressure, vibration)
sensor_readings = [
    (23.5, 101.3, 0.08), (24.1, 102.0, 0.09), (22.7, 100.8, 0.07),
    (25.3, 103.1, 0.12), (26.0, 104.5, 0.15), (24.8, 102.9, 0.11),
    (35.2, 115.0, 0.30), (23.9, 101.7, 0.08), (27.1, 106.2, 0.18),
    (28.4, 108.0, 0.22)
]

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'normal_temp': 22.0,
    'calibration_offset': 0.5,
    'threshold_multiplier': 1.1
}

# Misleading anomaly detection with decoy logic
def is_anomaly_decoy(value, avg, std):
    return abs(value - avg) > 2 * std  # Not actually used in final logic

# Real-time normalization factors (unused path)
normalization_factors = defaultdict(float)
for i, (t, p, v) in enumerate(sensor_readings):
    normalization_factors['temp_norm'] += t * 0.1
    normalization_factors['press_norm'] += p * 0.05
    normalization_factors['vibe_norm'] += v * 0.2

# Fake transformation chain (dead code path)
transformed_readings = []
for reading in sensor_readings:
    temp_adj = reading[0] * 1.02 + 0.3
    press_adj = reading[1] * 0.99 - 0.7
    transformed_readings.append((temp_adj, press_adj, reading[2]))

# Actual processing begins here — key logic buried among distractions
valid_readings = []
for idx, (t, p, v) in enumerate(sensor_readings):
    if t < 30 and v < 0.25:  # Filter out extreme cases
        valid_readings.append((t, p, v))

# Compute averages only on filtered data
temp_avg = sum(r[0] for r in valid_readings) / len(valid_readings)
press_avg = sum(r[1] for r in valid_readings) / len(valid_readings)
vibe_avg = sum(r[2] for r in valid_readings) / len(valid_readings)

# Simulated health indicators per sensor type
health_scores = []
for t, p, v in valid_readings:
    t_score = 100 - abs(t - temp_avg) * 2
    p_score = 95 - abs(p - press_avg) * 0.5
    v_score = 110 - abs(v - vibe_avg) * 20
    avg_score = (t_score + p_score + v_score) / 3
    health_scores.append(avg_score)

# Aggregate using median to resist outliers
sorted_scores = sorted(health_scores)
mid = len(sorted_scores) // 2
if len(sorted_scores) % 2 == 0:
    aggregate_health_score = (sorted_scores[mid-1] + sorted_scores[mid]) / 2
else:
    aggregate_health_score = sorted_scores[mid]

# Bit manipulation red herring (looks important but unused)
bitmask = 0b101010
encoded_system_flag = bitmask ^ int(temp_avg) & 0b1111

# Decoy statistical analysis using zip and enumerate (irrelevant)
index_shifts = []
for i, (a, b) in enumerate(zip(health_scores, health_scores[1:])):
    index_shifts.append((i, abs(a - b)))

# Unused frequency counter (set operation distractor)
all_vibes_rounded = {round(v, 1) for _, _, v in sensor_readings}
frequency_map = Counter(round(v, 1) for _, _, v in sensor_readings)

# Case conversion decoy — mimics data sanitization
status_labels = ['OK', 'WARNING', 'CRITICAL']
label_lower = [label.lower() for label in status_labels]
label_upper = [label.upper() for label in label_lower]

# Critical system bias correction based on pressure trend
pressure_trend = 0
for i in range(1, len(valid_readings)):
    prev_p = valid_readings[i-1][1]
    curr_p = valid_readings[i][1]
    pressure_trend += (curr_p - prev_p)
system_bias_correction = -0.5 if pressure_trend > 5 else 0.5

# Key assignment — this is where the answer is determined
final_diagnostic = aggregate_health_score + system_bias_correction

print(f"Result: {final_diagnostic}")