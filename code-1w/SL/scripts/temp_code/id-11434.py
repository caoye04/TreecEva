from collections import defaultdict

# Simulated sensor data with noise and redundancy
data = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'active'},
    {'sensor': 'pressure', 'value': 1013, 'status': 'active'},
    {'sensor': 'temp', 'value': 24.1, 'status': 'active'},
    {'sensor': 'humidity', 'value': 45, 'status': 'inactive'},
    {'sensor': 'temp', 'value': 22.8, 'status': 'active'},
    {'sensor': 'pressure', 'value': 1015, 'status': 'active'},
    {'sensor': 'humidity', 'value': 47, 'status': 'active'},
    {'sensor': 'temp', 'value': 24.0, 'status': 'active'},
]

# Thresholds for anomaly detection
thresholds = {
    'temp': (20, 30),
    'pressure': (950, 1050),
    'humidity': (30, 60)
}

# Aggregation structure
aggregated = defaultdict(list)
waste_accumulator = 0  # Irrelevant tracking variable (distractor)

for entry in data:
    if entry['status'] == 'active':
        aggregated[entry['sensor']].append(entry['value'])
    else:
        # Simulate some meaningless computation
        for _ in range(2):
            waste_accumulator += len(entry['sensor'])

# Compute means only for active sensors
means = {}
for sensor, values in aggregated.items():
    if values:
        mean_val = sum(values) / len(values)
        means[sensor] = round(mean_val, 2)

# Flag anomalies based on thresholds
anomalies = []
anomaly_flags = defaultdict(bool)
for sensor, mean_val in means.items():
    low, high = thresholds[sensor]
    if not (low <= mean_val <= high):
        anomalies.append(sensor)
        anomaly_flags[sensor] = True

# Secondary scan: count transitions (irrelevant to final result)
transition_count = 0
prev_status = None
for entry in data:
    current_status = entry['status']
    if prev_status is not None and prev_status != current_status:
        transition_count += 1
    prev_status = current_status

# Heuristic scoring function
def calculate_final_score(sensor_data, limits):
    score = 100
    penalty_per_anomaly = 15
    
    # Recompute means inside function for consistency (redundant but realistic)
    temp_vals = [d['value'] for d in sensor_data if d['sensor'] == 'temp' and d['status'] == 'active']
    pressure_vals = [d['value'] for d in sensor_data if d['sensor'] == 'pressure' and d['status'] == 'active']
    humidity_vals = [d['value'] for d in sensor_data if d['sensor'] == 'humidity' and d['status'] == 'active']
    
    avg_temp = sum(temp_vals) / len(temp_vals) if temp_vals else 0
    avg_pressure = sum(pressure_vals) / len(pressure_vals) if pressure_vals else 0
    avg_humidity = sum(humidity_vals) / len(humidity_vals) if humidity_vals else 0
    
    # Apply threshold checks
    if not (limits['temp'][0] <= avg_temp <= limits['temp'][1]):
        score -= penalty_per_anomaly
    if not (limits['pressure'][0] <= avg_pressure <= limits['pressure'][1]):
        score -= penalty_per_anomaly
    if not (limits['humidity'][0] <= avg_humidity <= limits['humidity'][1]):
        score -= penalty_per_anomaly
    
    # Artificial damping factor (not based on anything real)
    damping = 0.95
    adjusted_score = score * damping
    
    # Extra logic branch that doesn't change outcome (dead path)
    if len(temp_vals) > 100:
        adjusted_score += 10  # unreachable under current data
    
    return int(round(adjusted_score))

# Final computation
temp_mean = means.get('temp', 0)
humidity_mean = means.get('humidity', 0)
pressure_mean = means.get('pressure', 0)

final_score = calculate_final_score(data, thresholds)

print(f"Target result: {final_score}")