from collections import defaultdict, Counter

# Simulated sensor data over time (timestamp -> readings)
sensor_readings = [
    {'temp': 72.5, 'pressure': 30.1, 'vibration': 0.45, 'humidity': 45},
    {'temp': 73.1, 'pressure': 29.9, 'vibration': 0.52, 'humidity': 47},
    {'temp': 71.8, 'pressure': 30.3, 'vibration': 0.49, 'humidity': 46},
    {'temp': 74.0, 'pressure': 29.8, 'vibration': 0.61, 'humidity': 48},
    {'temp': 72.9, 'pressure': 30.0, 'vibration': 0.54, 'humidity': 50}
]

# Irrelevant statistical counters (distractor)
decay_counter = defaultdict(int)
reading_stats = Counter()
for reading in sensor_readings:
    if reading['temp'] > 72:
        decay_counter['high_temp'] += 1
    if reading['vibration'] > 0.5:
        decay_counter['high_vibe'] += 1
    reading_stats['samples'] += 1

# Historical thresholds (unused legacy values - red herring)
historical_min = {'temp': 68.0, 'pressure': 29.5, 'vibration': 0.3}
historical_max = {'temp': 75.0, 'pressure': 30.5, 'vibration': 0.7}

# Data transformation pipeline
processed_metrics = []
anomaly_flags = []
baseline_offset = 0.0

for idx, r in enumerate(sensor_readings):
    metric = {}
    metric['t_norm'] = (r['temp'] - 70.0) / 10.0
    metric['p_norm'] = abs(r['pressure'] - 30.0)
    metric['v_norm'] = r['vibration'] ** 2
    metric['h_norm'] = max(0, r['humidity'] - 40) * 0.1
    processed_metrics.append(metric)
    
    # Flag anomalies (used later)
    if r['vibration'] > 0.55 or r['pressure'] < 29.9:
        anomaly_flags.append(idx)
    
    # Dead code path - never accessed due to logic
    if False:
        baseline_offset += metric['t_norm']

# Compute rolling averages (some unused)
avg_temp = sum(r['temp'] for r in sensor_readings) / len(sensor_readings)
avg_vibe = sum(r['vibration'] for r in sensor_readings) / len(sensor_readings)
avg_pressure = sum(r['pressure'] for r in sensor_readings) / len(sensor_readings)

# Secondary transformation: severity index per reading
severity_index = []
for m in processed_metrics:
    raw_score = m['t_norm'] + m['p_norm'] + m['v_norm'] + m['h_norm']
    adjusted = raw_score * 1.1 if m['v_norm'] > 0.25 else raw_score * 0.9
    severity_index.append(round(adjusted, 4))

# Misleading intermediate calculation (not used in final result)
extreme_count = sum(1 for s in severity_index if s > 0.8)
mode_analysis = Counter(severity_index)

# Core health metrics
base_health = 100.0
for s in severity_index:
    base_health -= s * 2.5

aggregate_health_score = round(base_health, 3)

# Anomaly penalty calculation
penalty_unit = 3.75
anomaly_penalty = len(anomaly_flags) * penalty_unit if anomaly_flags else 0.0

# Correction factor based on pattern analysis (key dependency)
correction_factor = 1.0
if len(anomaly_flags) >= 2:
    gaps = [anomaly_flags[i] - anomaly_flags[i-1] for i in range(1, len(anomaly_flags))]
    if all(g <= 2 for g in gaps):  # clustered anomalies
        correction_factor = 1.4
    else:
        correction_factor = 1.1
else:
    correction_factor = 0.9

# DEAD END: Predictive model stub (irrelevant)
def predict_failure_risk(log_data):
    return "low"  # never called

future_risk = None  # unused

# Final diagnostic score computation
final_diagnostic = aggregate_health_score + anomaly_penalty * correction_factor

# Print target result
print(f"Result: {final_diagnostic}")