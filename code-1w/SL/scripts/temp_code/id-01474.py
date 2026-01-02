from collections import defaultdict

# Simulate sensor data aggregation and performance evaluation
sensor_readings = [
    ('temp', 23.5), ('pressure', 101.3), ('temp', 24.1), ('humidity', 45.2),
    ('pressure', 102.0), ('temp', 22.8), ('humidity', 47.8), ('pressure', 100.9)
]

# Aggregating raw data by type
raw_aggregation = defaultdict(list)
for sensor_type, value in sensor_readings:
    raw_aggregation[sensor_type].append(value)

# Compute averages (used later)
average_metrics = {}
for stype, values in raw_aggregation.items():
    average_metrics[stype] = sum(values) / len(values)

# Irrelevant computation: normalize readings to arbitrary scale (not used in final logic)
normalized = {}
total_sum = sum(sum(v) for v in raw_aggregation.values())
for stype, values in raw_aggregation.items():
    normalized[stype] = [v / total_sum for v in values]

# Misleading state tracking: counts fluctuations above threshold (distractor)
fluctuation_count = 0
base_threshold = 23.0
for val in raw_aggregation.get('temp', []):
    if abs(val - base_threshold) > 1.0:
        fluctuation_count += 1  # distractor variable

# Secondary distraction: simulate calibration offset
calibration_map = {'temp': -0.2, 'pressure': 0.5, 'humidity': 1.0}
adjusted_averages = {}
for k, v in average_metrics.items():
    adjusted_averages[k] = v + calibration_map.get(k, 0)

# Unused recursive helper to increase cognitive load
def calculate_depth(data, depth=0):
    if not data or depth >= 2:
        return depth
    return calculate_depth(data[1:] if len(data) > 1 else [], depth + 1)

# Call but don't use result
tree_depth = calculate_depth(list(average_metrics.keys()))

# Key data structure for evaluation
metric_data = {
    'avg_temp': average_metrics['temp'],
    'avg_pressure': average_metrics['pressure'],
    'stability_index': len(raw_aggregation['temp']),  # number of samples
    'complex_flag': False
}

# Introduce red herring set
seen_sensors = set()
for s_type, _ in sensor_readings:
    seen_sensors.add(s_type)

# Update flag based on set size (semi-relevant but overcomplicated)
if len(seen_sensors) >= 3:
    metric_data['complex_flag'] = True

# Core logic hidden among distractions
def evaluate_performance(metrics, threshold):
    score = 0
    temp_deviation = abs(metrics['avg_temp'] - threshold)
    
    # Real scoring logic
    if temp_deviation < 1.0:
        score += 50
    elif temp_deviation < 2.0:
        score += 30
    else:
        score += 10
    
    # Pressure bonus
    if metrics['avg_pressure'] > 101.5:
        score += 20
    
    # Bonus for sufficient sample size
    if metrics['stability_index'] >= 3:
        score += 15
    
    # This block looks important but doesn't trigger
    if metrics.get('oxygen') and metrics['oxygen'] > 20.0:
        score += 100  # dead code
    
    return score

# Execute key statement
temp_debug_log = [f"Sample {i}: {v}" for i, v in enumerate(raw_aggregation['temp'])]
final_score = evaluate_performance(metric_data, base_threshold)

# Distractor: unused list comprehension
processed_flags = [1 if x > 23 else 0 for x in raw_aggregation['temp']]

# Output target result
print(f"Result: {final_score}")