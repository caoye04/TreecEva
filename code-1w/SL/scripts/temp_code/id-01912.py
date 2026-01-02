from collections import defaultdict, Counter

# Simulate sensor data with timestamps and types
data_stream = [
    ('temp', 23.5), ('pressure', 101.3), ('temp', 24.1), ('humidity', 45.2),
    ('temp', 22.8), ('humidity', 47.0), ('pressure', 100.7), ('temp', 24.0)
]

# Misleading variables - irrelevant to final result
dummy_weights = [0.1, 0.3, 0.2, 0.4]
scaling_factor = 1.05
temp_buffer = []

# Data aggregation structures
sensor_aggregates = defaultdict(list)
frequency_counter = Counter()

# Process raw data into grouped measurements
for sensor_type, value in data_stream:
    sensor_aggregates[sensor_type].append(value)
    frequency_counter[sensor_type] += 1

# Extract only temperature readings for primary analysis
temperature_readings = sensor_aggregates['temp']

# Red herring computation: average pressure (not used later)
avg_pressure = sum(sensor_aggregates['pressure']) / len(sensor_aggregates['pressure']) if sensor_aggregates['pressure'] else 0

# Compute rolling difference in temps (distractor)
rolling_diffs = []
for i in range(1, len(temperature_readings)):
    rolling_diffs.append(abs(temperature_readings[i] - temperature_readings[i-1]))

# Primary metric: mean temperature
mean_temp = sum(temperature_readings) / len(temperature_readings)

# Secondary metric: consistency penalty based on variation
consistency_penalty = 0
if len(rolling_diffs) > 0:
    max_diff = max(rolling_diffs)
    consistency_penalty = max_diff * 0.5

# Tertiary metric: data richness bonus (based on total unique sensor types)
sensor_types_present = list(frequency_counter.keys())
data_richness_bonus = len(sensor_types_present) * 0.25

# Prepare processed data structure
processed_data = {
    'base_value': mean_temp,
    'penalty': consistency_penalty,
    'bonus': data_richness_bonus,
    'sample_count': len(temperature_readings)
}

# Misleading function that looks important but isn't used
def compute_diagnostic_report(data):
    report = {}
    for k, v_list in data.items():
        report[k] = {
            'count': len(v_list),
            'avg': sum(v_list) / len(v_list),
            'peak': max(v_list)
        }
    return report

# Actual scoring function
def calculate_final_score(data_dict):
    score = data_dict['base_value']
    score -= data_dict['penalty']
    score += data_dict['bonus']
    adjustment = 0
    if data_dict['sample_count'] >= 4:
        adjustment = 1.5  # Reward sufficient sampling
    score += adjustment
    return round(score, 4)

# Critical execution point
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")