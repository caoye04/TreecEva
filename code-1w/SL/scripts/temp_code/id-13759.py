from collections import defaultdict

# Simulate sensor data with some noise and metadata
data_log = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'ok', 'timestamp': 1001},
    {'sensor': 'temp', 'value': 24.1, 'status': 'ok', 'timestamp': 1002},
    {'sensor': 'pressure', 'value': 1013, 'status': 'ok', 'timestamp': 1001},
    {'sensor': 'humidity', 'value': 45, 'status': 'ok', 'timestamp': 1001},
    {'sensor': 'temp', 'value': 22.9, 'status': 'ok', 'timestamp': 1003},
    {'sensor': 'pressure', 'value': 1015, 'status': 'ok', 'timestamp': 1003},
    {'sensor': 'humidity', 'value': 47, 'status': 'warning', 'timestamp': 1004},
    {'sensor': 'temp', 'value': 24.3, 'status': 'ok', 'timestamp': 1004}
]

# Weights for scoring model
weights = {'temp': 0.4, 'pressure': 0.35, 'humidity': 0.25}

# Track aggregate stats
sensor_stats = defaultdict(lambda: {'count': 0, 'total': 0.0})
duplicate_tracker = set()
status_counter = defaultdict(int)

# Preprocess and extract relevant values
processed_values = []
for entry in data_log:
    key = (entry['sensor'], entry['timestamp'])
    if key in duplicate_tracker:
        continue
    duplicate_tracker.add(key)
    
    # Irrelevant transformation (distractor)
    normalized_status = entry['status'].upper().replace('_', '')
    status_counter[normalized_status] += 1
    
    # Only process 'ok' status entries
    if entry['status'] == 'ok':
        sensor_stats[entry['sensor']]['count'] += 1
        sensor_stats[entry['sensor']]['total'] += entry['value']
        processed_values.append((entry['sensor'], entry['value']))

# Compute averages (used later)
averages = {}
for sensor, stats in sensor_stats.items():
    averages[sensor] = stats['total'] / stats['count']

# Dummy transformation on keys (irrelevant but adds complexity)
case_transformed_sensors = [k.upper().lower().title() for k in averages.keys()]
offset_correction = sum([len(s) for s in case_transformed_sensors]) * 0.01  # negligible effect

# Weight adjustment based on count distribution (distractor logic)
total_entries = sum(stats['count'] for stats in sensor_stats.values())
adjusted_weights = {}
for sensor in weights:
    raw_weight = weights[sensor]
    count_ratio = sensor_stats[sensor]['count'] / total_entries
    adjusted_weights[sensor] = raw_weight * (1 + abs(count_ratio - 0.33))  # slight perturbation

# Normalize adjusted weights to sum to 1.0
weight_sum = sum(adjusted_weights.values())
normalized_weights = {k: v / weight_sum for k, v in adjusted_weights.items()}

# Scoring function using average values and weights
def calculate_final_score(log, weight_dict):
    score_components = {}
    for sensor_type, avg in averages.items():
        if sensor_type == 'temp':
            # Apply nonlinear correction for temperature
            base_score = (avg ** 1.05) * normalized_weights[sensor_type]
        elif sensor_type == 'pressure':
            base_score = (avg / 10) * normalized_weights[sensor_type]
        elif sensor_type == 'humidity':
            base_score = (100 - abs(avg - 50)) * normalized_weights[sensor_type]
        else:
            base_score = avg * normalized_weights.get(sensor_type, 0)
        score_components[sensor_type] = base_score
    
    # Final aggregation
    total_score = sum(score_components.values())
    
    # Apply offset correction from earlier (minimal impact)
    total_score += offset_correction
    
    # Additional irrelevant check
    if len(status_counter) > 1 and 'OK' in status_counter:
        total_score *= (1 + 0.001 * status_counter['OK'])  # negligible boost
    
    return round(total_score, 4)

# Execute critical statement
final_score = calculate_final_score(data_log, weights)
print(f"Target result: {final_score}")