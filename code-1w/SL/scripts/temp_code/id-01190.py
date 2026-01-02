from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'id': 101, 'type': 'sensor', 'value': 42.5, 'status': 'active'},
    {'id': 102, 'type': 'actuator', 'value': 18.2, 'status': 'idle'},
    {'id': 103, 'type': 'sensor', 'value': 67.1, 'status': 'active'},
    {'id': 104, 'type': 'sensor', 'value': 23.9, 'status': 'failed'},
    {'id': 105, 'type': 'actuator', 'value': 91.0, 'status': 'active'},
    {'id': 106, 'type': 'sensor', 'value': 55.3, 'status': 'active'}
]

# Irrelevant auxiliary mapping (distractor)
device_names = {
    101: 'ThermSensor_A1', 102: 'Motor_X9', 103: 'Pressure_S2',
    104: 'FlowMeter_C3', 105: 'Pump_Z5', 106: 'TempProbe_M7'
}

# Misleading aggregation structures (red herring)
raw_aggregates = defaultdict(list)
for entry in telemetry_stream:
    raw_aggregates[entry['type']].append(entry['value'])

summary_stats = {}
for dtype, values in raw_aggregates.items():
    summary_stats[dtype] = {
        'count': len(values),
        'sum': sum(values),
        'fake_metric': math.sin(sum(values) / len(values))  # Distractor computation
    }

# Decoy function with unused recursion (dead path)
def recursive_denoise(data, depth=0):
    if depth >= 3 or not data:
        return []
    cleaned = [x for x in data if x > 20.0]
    return recursive_denoise(cleaned, depth + 1)

# Unused transformation chain (irrelevant processing)
filtered_telemetry = [x for x in telemetry_stream if x['status'] == 'active']
denoised_values = [t['value'] for t in filtered_telemetry if t['value'] > 30.0]
sorted_pairs = sorted([(t['id'], t['value']) for t in filtered_telemetry], key=lambda x: x[1])

# Core diagnostic logic disguised among noise
failure_count = sum(1 for t in telemetry_stream if t['status'] == 'failed')
active_sensors = [t for t in telemetry_stream if t['type'] == 'sensor' and t['status'] == 'active']
avg_active_sensor_value = sum(s['value'] for s in active_sensors) / len(active_sensors) if active_sensors else 0

# Bit manipulation decoy (misleading)
bit_encoded = 0
for s in telemetry_stream:
    bit_encoded ^= int(s['value']) & 0xFF

# Conditional complexity with nested logic
base_rating = 50
if avg_active_sensor_value > 50.0:
    base_rating += 20
elif avg_active_sensor_value > 30.0:
    base_rating += 10

if failure_count == 0:
    base_rating += 15
else:
    base_rating -= 10 * failure_count

# Red herring: unused counter logic
status_counter = Counter(entry['status'] for entry in telemetry_stream)
most_common_status = status_counter.most_common(1)[0][0]

# Simulated historical drift analysis (irrelevant)
historical_bias = 0.0
for i in range(1, len(active_sensors)):
    historical_bias += abs(active_sensors[i]['value'] - active_sensors[i-1]['value'])
historical_correction = math.log(1 + historical_bias) if historical_bias > 0 else 0

# Actual performance evaluation function (core logic)
def evaluate_performance(log, threshold):
    sensor_data = [e for e in log if e['type'] == 'sensor']
    actuator_data = [e for e in log if e['type'] == 'actuator']
    
    # Real metric extraction
    valid_readings = [s['value'] for s in sensor_data if s['status'] == 'active']
    if not valid_readings:
        return 0
    
    mean_reading = sum(valid_readings) / len(valid_readings)
    reading_variance = sum((x - mean_reading) ** 2 for x in valid_readings) / len(valid_readings)
    stability_score = 100 / (1 + reading_variance)  # Inverse relationship
    
    # Actuator influence
    active_actuators = sum(1 for a in actuator_data if a['status'] == 'active')
    actuator_bonus = 5 * active_actuators
    
    # Threshold-based multiplier
    multiplier = 1.2 if mean_reading >= threshold else 0.8
    
    # Final composition
    raw_score = (stability_score + base_rating + actuator_bonus)
    final_component = raw_score * multiplier
    
    # This line produces the target result
    return int(round(final_component))

# Key execution point
threshold = 45.0
metrics_log = telemetry_stream
final_score = evaluate_performance(metrics_log, threshold)
print(f"Target result: {final_score}")