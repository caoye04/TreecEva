from collections import defaultdict, Counter

# Simulated sensor network data with metadata
timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]
sensor_names = ['S1', 'S2', 'S3', 'S4']
raw_readings = [
    (1001, 'S1', 23.1), (1001, 'S2', 45.6), (1001, 'S3', 19.8), (1001, 'S4', 22.0),
    (1002, 'S1', 24.0), (1002, 'S2', 43.2), (1002, 'S3', 20.1), (1002, 'S4', 21.9),
    (1003, 'S1', 25.3), (1003, 'S2', 120.5), (1003, 'S3', 20.0), (1003, 'S4', 22.1),  # S2 anomaly
    (1004, 'S1', 24.9), (1004, 'S2', 44.1), (1004, 'S3', 19.9), (1004, 'S4', 22.2),
    (1005, 'S1', 23.0), (1005, 'S2', 42.8), (1005, 'S3', 180.9), (1005, 'S4', 22.0),  # S3 anomaly
    (1006, 'S1', 23.8), (1006, 'S2', 43.5), (1006, 'S3', 20.2), (1006, 'S4', 21.8),
    (1007, 'S1', 24.1), (1007, 'S2', 44.0), (1007, 'S3', 19.7), (1007, 'S4', 110.3),  # S4 anomaly
    (1008, 'S1', 23.9), (1008, 'S2', 43.7), (1008, 'S3', 20.3), (1008, 'S4', 22.4)
]

# Irrelevant auxiliary data (distraction)
location_grid = [[(x, y) for y in range(4)] for x in range(4)]
firmware_versions = {'S1': 'v2.1', 'S2': 'v2.3', 'S3': 'v1.9', 'S4': 'v2.0'}
maintenance_log = defaultdict(list)
maintenance_log['S1'].append('calibrated')

# Data aggregation structure (relevant)
sensor_data = defaultdict(list)
for ts, name, val in raw_readings:
    sensor_data[name].append(val)

# Decoy function: looks important but unused
def compute_health_score(data):
    return sum([abs(d - 50) for d in data]) / len(data)

# Another decoy: complex but irrelevant transformation
def encrypt_timestamps(ts_list):
    encrypted = 0
    for t in ts_list:
        encrypted ^= (t * 2654435761) % (2**32)
    return encrypted

# Misleading intermediate calculation (red herring)
total_encrypted = encrypt_timestamps(timestamps)  # Unused later

# Core logic: identify anomalies above threshold
def filter_anomalies(readings_per_sensor):
    anomalies = []
    for sensor, readings in readings_per_sensor.items():
        for value in readings:
            if value > 100:  # Threshold for anomaly
                anomalies.append((sensor, value))
    return anomalies

# Secondary processing: count per sensor (partially relevant)
def count_anomalies(anomaly_list):
    counts = Counter()
    for sensor, _ in anomaly_list:
        counts[sensor] += 1
    return counts

# Main processing chain
anomaly_events = filter_anomalies(sensor_data)
anomaly_counts = count_anomalies(anomaly_events)

# Complex conditional logic with distractors
alert_level = 0
if len(anomaly_events) > 2:
    alert_level = 3
elif len(anomaly_events) == 2:
    alert_level = 2
else:
    alert_level = 1

# Dead code path (never executed due to data, but plausible)
override_mode = False
calibration_factor = 1.0
if override_mode and calibration_factor > 1.5:
    adjusted_count = sum(anomaly_counts.values()) * calibration_factor
else:
    adjusted_count = sum(anomaly_counts.values())

# Simulate diagnostic weight adjustments based on pattern
pattern_weights = defaultdict(float)
for sensor, cnt in anomaly_counts.items():
    if cnt >= 2:
        pattern_weights[sensor] = 1.5
    elif cnt == 1:
        pattern_weights[sensor] = 0.8
    else:
        pattern_weights[sensor] = 0.1

# Additional distraction: unused statistical analysis
mean_readings = {s: sum(vals)/len(vals) for s, vals in sensor_data.items()}
variance_readings = {}
for s, vals in sensor_data.items():
    mean = mean_readings[s]
    variance_readings[s] = sum((v - mean)**2 for v in vals) / len(vals)

# Key transformation pipeline
def process_readings(anomalies):
    base_score = 100
    penalty = 0
    sensor_bonus = defaultdict(int)
    
    for sensor, value in anomalies:
        if value > 150:
            penalty += 15
            sensor_bonus[sensor] += 5
        elif value > 120:
            penalty += 10
            sensor_bonus[sensor] += 3
        else:
            penalty += 5
            sensor_bonus[sensor] += 1
    
    # Bonus only applies if no sensor exceeds twice
    bonus_applied = all(cnt <= 2 for cnt in Counter(s[0] for s in anomalies).values())
    total_bonus = sum(sensor_bonus.values()) if bonus_applied else 0
    
    return base_score - penalty + total_bonus

# Execution point of interest
final_diagnostic = process_readings(filter_anomalies(sensor_data))

# Print result as required
print(f"Target result: {final_diagnostic}")