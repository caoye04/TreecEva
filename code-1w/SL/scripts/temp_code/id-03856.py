from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
data_stream = [
    ('temp', 23), ('temp', 23), ('humidity', 44), ('temp', 24), 
    ('pressure', 1013), ('humidity', 45), ('temp', 24), ('light', 300),
    ('pressure', 1013), ('humidity', 44), ('light', 305)
]

# Filter and normalize valid sensor types
valid_sensors = {'temp', 'humidity', 'pressure'}
filtered_readings = [item for item in data_stream if item[0] in valid_sensors]

# Count frequency of each reading for anomaly detection
reading_frequency = Counter(filtered_readings)
anomaly_threshold = 1
anomalies = {k: v for k, v in reading_frequency.items() if v <= anomaly_threshold}

# Aggregate data by sensor type
aggregated = defaultdict(list)
for sensor, value in filtered_readings:
    aggregated[sensor].append(value)

# Compute baseline statistics (some are distractions)
baseline_stats = {}
for sensor, values in aggregated.items():
    baseline_stats[sensor] = {
        'avg': sum(values) / len(values),
        'max_val': max(values),
        'min_val': min(values),
        'range_val': max(values) - min(values)
    }

# Extract primary metrics for evaluation
primary_metrics = {}
for s in ['temp', 'humidity', 'pressure']:
    if s in baseline_stats:
        primary_metrics[s] = round(baseline_stats[s]['avg'], 2)

# Simulate secondary validation chain (distractor logic)
duplicate_check = Counter([v for _, v in filtered_readings])
redundant_values = [v for v, cnt in duplicate_check.items() if cnt > 2]
consistency_score = len(redundant_values) * 1.5  # unused distraction

# Normalize metrics to a unified scale (0-100)
normalized = {}
scaling_map = {'temp': (20, 30), 'humidity': (30, 60), 'pressure': (1000, 1030)}
for sensor, val in primary_metrics.items():
    low, high = scaling_map[sensor]
    normalized[sensor] = 100 * (val - low) / (high - low) if high != low else 50

# Apply weighted importance (real computation path)
weights = {'temp': 0.4, 'humidity': 0.3, 'pressure': 0.3}
weighted_sum = sum(normalized[s] * weights[s] for s in normalized if s in weights)

# Additional state tracking (mostly irrelevant)
state_log = []
current_state = 'INIT'
for step in ['FILTER', 'AGGREGATE', 'NORMALIZE']:
    current_state = step
    state_log.append(f'{step}_OK')

# Final processing function
def calculate_final_score(data):
    base = weighted_sum  # capture outer scope value
    adjustment = 0
    
    # Conditional micro-adjustments (simulates calibration)
    if data['temp'] > 50:
        adjustment += 5
    elif data['temp'] < 30:
        adjustment -= 2
    
    if data['humidity'] > 70:
        adjustment -= 3
    
    # Apply adjustment (minimal effect in this case)
    result = base + adjustment
    
    # Dead code branch - never executed, adds interference
    if False:
        backup_system = [x for x in range(10)]
        result = sum(backup_system) / len(backup_system)
    
    return int(round(result))

# Execute main computation
processed_data = normalized
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")