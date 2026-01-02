from collections import defaultdict
from itertools import combinations

# Simulated IoT sensor stream for environmental monitoring
sensor_stream = [
    (1, 'temp', 23.5), (2, 'hum', 45.2), (3, 'temp', -19.1), (4, 'co2', 420),
    (5, 'temp', 24.8), (6, 'hum', 120.0), (7, 'co2', 380), (8, 'temp', 22.1),
    (9, 'hum', 47.3), (10, 'co2', 450), (11, 'temp', -25.0), (12, 'co2', 390)
]

# Thresholds for anomaly detection
thresholds = defaultdict(lambda: (float('-inf'), float('inf')))
thresholds['temp'] = (-20.0, 50.0)
thresholds['hum'] = (0.0, 100.0)
thresholds['co2'] = (300, 500)

# Tracking variables (some used, some not)
count_by_type = defaultdict(int)
anomaly_count = 0
rolling_window = []
temporal_gaps = []
summary_stats = {}
phantom_counter = 0  # Irrelevant distractor
useless_buffer = []   # Dead code path variable

for i in range(1, len(sensor_stream)):
    gap = sensor_stream[i][0] - sensor_stream[i-1][0]
    temporal_gaps.append(gap)
    phantom_counter += 1  # Distractor computation

# Filter anomalies based on thresholds
def filter_anomalies(stream):
    filtered = []
    global anomaly_count
    for reading in stream:
        sid, stype, value = reading
        min_val, max_val = thresholds[stype]
        count_by_type[stype] += 1
        if min_val <= value <= max_val:
            filtered.append(reading)
        else:
            anomaly_count += 1
    return filtered

# Process valid readings into diagnostic score
def process_readings(valid_readings):
    type_averages = defaultdict(list)
    for _, stype, value in valid_readings:
        type_averages[stype].append(value)
    
    averages = {}
    for t, vals in type_averages.items():
        averages[t] = sum(vals) / len(vals)
    
    # Diagnostic logic: deviation from ideal conditions
    ideal = {'temp': 22.0, 'hum': 50.0, 'co2': 400}
    deviations = []
    for t in ideal:
        if t in averages:
            dev = abs(averages[t] - ideal[t])
            deviations.append(dev)
    
    # Secondary check: presence of rare combinations
    temp_vals = type_averages.get('temp', [])
    co2_vals = type_averages.get('co2', [])
    rare_combo_detected = 0
    if temp_vals and co2_vals:
        for t, c in combinations([(t,c) for t in temp_vals for c in co2_vals], 1):
            if t[0] > 24 and c[1] > 440:
                rare_combo_detected = 10
                break

    # Final diagnostic score: weighted deviation with bonus penalty
    base_score = sum(deviations) * 10
    final_score = base_score + rare_combo_detected
    
    # Useless transformation chain (distractor)
    transformed = [x * 0.95 for x in type_averages.get('hum', [])]
    smoothed = [abs(x - 50) for x in transformed]
    useless_buffer.extend(smoothed)  # Dead-end buffer
    
    return int(round(final_score))

# Execution flow
filtered_data = filter_anomalies(sensor_stream)
final_diagnostic = process_readings(filtered_data)
print(f"Result: {final_diagnostic}")