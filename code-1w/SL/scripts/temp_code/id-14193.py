from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, 'temp', 23.5), (101, 'pressure', 1013.25), (102, 'temp', 24.1),
    (103, 'humidity', 45), (104, 'temp', 22.9), (105, 'pressure', 1012.8),
    (106, 'humidity', 47), (107, 'temp', 25.3), (108, 'pressure', 1014.1)
]

# Misleading variables - not used in final computation
dummy_counter = 0
placeholder_value = None
irrelevant_sum = 0

# Group readings by type
data_by_type = defaultdict(list)
for ts, reading_type, value in timestamped_readings:
    data_by_type[reading_type].append(value)
    dummy_counter += 1  # Distractor: increments but not used meaningfully

# Compute rolling averages for each sensor (only temp is actually used later)
averages = {}
for key in data_by_type:
    values = data_by_type[key]
    avg = sum(values) / len(values)
    averages[key] = round(avg, 2)

# Extract specific trends
pressure_trend = data_by_type['pressure'][-1] - data_by_type['pressure'][0] if 'pressure' in data_by_type else 0
humidity_trend = len([v for v in data_by_type['humidity'] if v > 45])  # semi-relevant but unused

# Process temperature anomalies
baseline_temp = averages['temp']
temp_anomalies = []
for value in data_by_type['temp']:
    if abs(value - baseline_temp) > 1.0:
        temp_anomalies.append(value)

# Simulate correction pass (distractor loop)
corrected_values = []
for val in data_by_type['temp']:
    corrected = val * 0.98 + 0.5
    if corrected < 20:
        corrected = 20
    corrected_values.append(round(corrected, 2))

# State tracking across phases
state_log = []
phase_weights = {'initial': 0.3, 'anomaly_adjusted': 0.7}

# Initial score based on average temperature
initial_score = baseline_temp * 10

# Adjust score based on anomaly count and magnitude
anomaly_penalty = 0
for anomaly in temp_anomalies:
    deviation = abs(anomaly - baseline_temp)
    anomaly_penalty += deviation * 2

adjusted_score = initial_score - anomaly_penalty

# Apply phase weighting (only one phase actually matters)
final_phase_score = adjusted_score * phase_weights['anomaly_adjusted']

# Additional irrelevant calculation
aggregate_variance = 0
all_vals = data_by_type['temp'] + data_by_type['pressure']
mean_all = sum(all_vals) / len(all_vals)
for v in all_vals:
    aggregate_variance += (v - mean_all) ** 2
aggregate_variance /= len(all_vals)

# Final scoring function
def calculate_final_score(data):
    base = data['score_input']
    multiplier = 1.0
    
    # Nested logic with red herring conditions
    if data['anomaly_count'] > 2:
        multiplier *= 0.9
    elif data['anomaly_count'] == 2:
        multiplier *= 0.95
    else:
        multiplier *= 1.05  # This will be the path taken
    
    # Extra nesting for complexity
    if data['source_count'] > 1:
        if 'calibration_offset' in data:
            base -= data['calibration_offset']
    
    return int(base * multiplier)

# Prepare processed data
processed_data = {
    'score_input': final_phase_score,
    'anomaly_count': len(temp_anomalies),
    'source_count': len(data_by_type),
    'calibration_offset': 3.5  # This gets subtracted in one branch, but not triggered
}

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")