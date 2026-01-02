from collections import defaultdict, Counter

# Simulate sensor data with timestamps and types
data_stream = [
    (1, 'temp', 23.5), (2, 'pressure', 101.3), (3, 'temp', 24.1),
    (4, 'humidity', 45.2), (5, 'temp', 22.8), (6, 'pressure', 102.1),
    (7, 'temp', 25.0), (8, 'humidity', 47.8), (9, 'pressure', 100.7)
]

# Misleading variables - not used in final computation
dummy_counter = 0
redundant_sum = 0.0
placeholder_list = []
for i in range(len(data_stream)):
    if data_stream[i][1] == 'temp':
        dummy_counter += 1
        redundant_sum += data_stream[i][2] * 0.1
    placeholder_list.append(i * 2)

# Process data: group by type and compute averages
data_by_type = defaultdict(list)
for timestamp, sensor_type, value in data_stream:
    data_by_type[sensor_type].append(value)

# Compute moving average for temperature (window size 2) - partially relevant
moving_averages = []
temp_values = data_by_type['temp']
for i in range(1, len(temp_values)):
    avg = (temp_values[i-1] + temp_values[i]) / 2
    moving_averages.append(avg)

# Distractor: count transitions between sensor types
transition_count = 0
for i in range(1, len(data_stream)):
    if data_stream[i][1] != data_stream[i-1][1]:
        transition_count += 1

# Compute base metrics
base_metrics = {}
for stype, values in data_by_type.items():
    base_metrics[stype] = {
        'count': len(values),
        'avg': sum(values) / len(values),
        'variance': sum((x - sum(values)/len(values))**2 for x in values) / len(values)
    }

# Extract specific intermediate values
pressure_avg = base_metrics['pressure']['avg']
humidity_avg = base_metrics['humidity']['avg']
temp_moving_peak = max(moving_averages) if moving_averages else 0

# Simulate calibration offset (irrelevant but plausible)
calibration_map = {'temp': 0.2, 'pressure': -0.5, 'humidity': 0.8}
adjusted_temp_avg = base_metrics['temp']['avg'] + calibration_map['temp']

# Data validation check - distractor
valid_data_points = [v for v in data_stream if v[2] > 0]
dropped_points = len(data_stream) - len(valid_data_points)

# Processed data structure for main logic
processed_data = {
    'temp_raw_avg': base_metrics['temp']['avg'],
    'temp_peak_trend': temp_moving_peak,
    'sensor_coverage': len(data_by_type),
    'total_observations': sum(len(v) for v in data_by_type.values())
}

# Helper function with dead code path
def calculate_stability_index(data):
    if not data:
        return 0.0
    count = data.get('count', 0)
    if count == 0:
        stability = 0.0
    else:
        # Dead code below - never reached due to logic
        backup_ref = 999
        stability = (data['avg'] * 0.8) if data['variance'] < 1.0 else (data['avg'] * 0.5)
    return 1.0  # Constant return - red herring

# Main calculation function
def calculate_final_score(processed):
    raw_avg = processed['temp_raw_avg']
    peak_trend = processed['temp_peak_trend']
    coverage = processed['sensor_coverage']
    total_obs = processed['total_observations']
    
    # Core logic: weighted combination
    weight_a = 0.4
    weight_b = 0.6
    
    # Intermediate distraction
    obs_factor = total_obs / 10.0
    coverage_bonus = 5 if coverage >= 3 else 0
    
    # Actual computation
    trend_component = peak_trend * weight_a
    base_component = raw_avg * weight_b
    score = base_component + trend_component + coverage_bonus
    
    # Extra unused calculations to increase cognitive load
    potential_max = max(raw_avg, peak_trend) * 1.2
    decay_factor = 0.95 ** total_obs
    
    return int(round(score))

# Execute main statement
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")