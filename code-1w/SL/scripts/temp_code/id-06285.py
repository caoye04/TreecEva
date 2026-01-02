from collections import defaultdict, Counter

# Simulate sensor data with timestamps and readings
data_log = [
    {'time': 1, 'sensor': 'A', 'value': 10, 'status': 'active'},
    {'time': 2, 'sensor': 'B', 'value': 15, 'status': 'active'},
    {'time': 3, 'sensor': 'A', 'value': 8, 'status': 'noisy'},
    {'time': 4, 'sensor': 'C', 'value': 20, 'status': 'active'},
    {'time': 5, 'sensor': 'B', 'value': 12, 'status': 'active'},
    {'time': 6, 'sensor': 'A', 'value': 11, 'status': 'active'},
    {'time': 7, 'sensor': 'C', 'value': 18, 'status': 'noisy'},
    {'time': 8, 'sensor': 'B', 'value': 14, 'status': 'active'}
]

# Weight mapping for sensors
weights = {'A': 1.2, 'B': 1.5, 'C': 1.8}

# Precompute auxiliary stats (some are distractions)
total_entries = len(data_log)
sensor_count = Counter(entry['sensor'] for entry in data_log)
status_breakdown = defaultdict(int)
for entry in data_log:
    status_breakdown[entry['status']] += 1

# Dummy transformation: invert status counts (not used later)
inverted_status = {k: 1/(v + 1) for k, v in status_breakdown.items()}

# Filter only active status readings
active_data = [e for e in data_log if e['status'] == 'active']

# Group values by sensor
sensor_values = defaultdict(list)
for entry in active_data:
    sensor_values[entry['sensor']].append(entry['value'])

# Compute average per sensor
sensor_averages = {}
for sensor, values in sensor_values.items():
    avg = sum(values) / len(values)
    sensor_averages[sensor] = round(avg, 2)

# Calculate weighted contribution
weighted_contributions = {}
dummy_tracker = []
for sensor, avg in sensor_averages.items():
    weight = weights.get(sensor, 1.0)
    contribution = avg * weight
    weighted_contributions[sensor] = contribution
    
    # Distractor: track intermediate states unnecessarily
    dummy_tracker.append({
        'sensor': sensor,
        'avg': avg,
        'weight': weight,
        'contrib': contribution,
        'flag': True if contribution > 15 else False
    })

# Compute composite baseline (unused)
baseline_avg = sum(sensor_averages.values()) / len(sensor_averages) if sensor_averages else 0
offset_correction = abs(baseline_avg - 10) * 0.1  # red herring

# Final score calculation
def calculate_final_score(data, w_map):
    clean_data = [d for d in data if d['status'] == 'active']
    total_weighted = 0
    total_weight_factor = 0
    
    temp_aggr = defaultdict(float)  # unused accumulator (distraction)
    
    for record in clean_data:
        s = record['sensor']
        v = record['value']
        wt = w_map[s]
        total_weighted += v * wt
        total_weight_factor += wt
        temp_aggr[s] += v  # tracked but not used
    
    if total_weight_factor == 0:
        return 0.0
    
    # Apply artificial damping based on number of entries (moderate effect)
    entry_count_factor = len(clean_data) / (total_entries + 1)
    raw_score = total_weighted / total_weight_factor
    final = raw_score * (1 + entry_count_factor)  # boosting factor
    
    # Extra processing to mislead: case conversion on string version (dead path)
    str_score = str(final)
    if str_score.lower() != str_score.upper():
        str_score = str_score.replace('.', 'x')
    
    return round(final, 4)

# Execute main logic
intermediate_sum = sum(v for v in sensor_count.values() if v > 1) * 0.5  # distraction

final_score = calculate_final_score(data_log, weights)

# Print result as required
print(f"Result: {final_score}")