from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
data_stream = [
    (1, 'temp', 23.5), (2, 'temp', 24.1), (3, 'pressure', 1013),
    (4, 'temp', 23.9), (5, 'humidity', 45), (6, 'pressure', 1012),
    (7, 'temp', 24.0), (8, 'humidity', 47), (9, 'pressure', 1015),
    (10, 'temp', 24.2)
]

# Misleading variables - not used in final computation
dummy_counter = 0
redundant_sum = 0.0
noise_floor = 0.5

# Extract and group by type
data_by_type = defaultdict(list)
for seq_id, sensor_type, reading in data_stream:
    data_by_type[sensor_type].append(reading)
    dummy_counter += 1  # Distractor: counts all entries but unused

# Process temperature with smoothing and outlier filtering
raw_temps = data_by_type['temp']
avg_temp = sum(raw_temps) / len(raw_temps)
temp_std_dev = (sum((t - avg_temp) ** 2 for t in raw_temps) / len(raw_temps)) ** 0.5
filtered_temps = [t for t in raw_temps if abs(t - avg_temp) <= 2 * temp_std_dev]
smoothed_temp = sum(filtered_temps) / len(filtered_temps)

# Pressure trend analysis using modular arithmetic for cyclic behavior
pressure_readings = data_by_type['pressure']
pressure_deltas = [(pressure_readings[i+1] - pressure_readings[i]) % 5 for i in range(len(pressure_readings)-1)]
net_pressure_trend = sum(pressure_deltas)

# Humidity mode detection using Counter
humidity_readings = data_by_type.get('humidity', [])
humidity_mode = Counter(humidity_readings).most_common(1)
humidity_consistency = humidity_mode[0][1] if humidity_mode else 1

# Auxiliary function with nested logic
def calculate_stability_metrics(values, weight=1.0):
    if len(values) < 2:
        return 0.0
    diffs = [abs(values[i+1] - values[i]) for i in range(len(values)-1)]
    return weight * (1 / (1 + sum(diffs)))

# Compute intermediate stability scores
temp_stability = calculate_stability_metrics(filtered_temps, weight=1.2)
pressure_stability = calculate_stability_metrics(pressure_readings, weight=0.8)

# Combine metrics into processed data structure
processed_data = {
    'base': smoothed_temp * 10,
    'trend': net_pressure_trend * 5,
    'stability': (temp_stability + pressure_stability) * 20,
    'consistency': humidity_consistency * 15
}

# Red herring computation - dead-end path
aggregate_variance = 0.0
for key, value in processed_data.items():
    aggregate_variance += (value - 50) ** 2  # Arbitrary center, unused later

# Final scoring logic
def calculate_final_score(data):
    score = 0
    score += data['base']
    score += data['trend']
    if data['stability'] > 10:
        score += data['stability'] * 0.7
    else:
        score += data['stability'] * 0.3
    score += data['consistency']
    
    # Extra distraction: complex conditional that doesn't trigger
    if len(raw_temps) > 100:  # Never true
        score -= 50
    elif any(x < 0 for x in [data['base'], data['trend']]):
        score *= 0.9
    
    return int(round(score))

# Execute main computation
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")