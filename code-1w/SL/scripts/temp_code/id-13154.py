from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
data_stream = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1013, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.1, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 45, 'status': 'error'},
    {'sensor': 'temp', 'value': 22.8, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1016, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 47, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.3, 'status': 'ok'},
]

# Irrelevant transformation: convert to uppercase keys (unused)
uppercase_data = [{k.upper(): v for k, v in item.items()} for item in data_stream]

# Extract only valid temperature readings
temp_readings = [entry['value'] for entry in data_stream if entry['sensor'] == 'temp' and entry['status'] == 'ok']

# Misleading statistical distraction
mean_temp = sum(temp_readings) / len(temp_readings)
variance_temp = sum((x - mean_temp) ** 2 for x in temp_readings) / len(temp_readings)
adjusted_values = [x * 0.98 + 0.5 for x in temp_readings]  # Not used later

# Track occurrences of each sensor type
sensor_counter = Counter(entry['sensor'] for entry in data_stream)

# Build structured dataset by sensor
sensor_data = defaultdict(list)
for entry in data_stream:
    sensor_data[entry['sensor']].append(entry['value'])

# Compute aggregates (some are red herrings)
aggregates = {}
for sensor, values in sensor_data.items():
    aggregates[sensor] = {
        'count': len(values),
        'total': sum(values),
        'valid_ratio': len([e for e in data_stream if e['sensor'] == sensor and e['status'] == 'ok']) / len(data_stream),
        'flagged': False
    }

# Introduce unrelated flag computation
if aggregates['temp']['count'] > 3:
    aggregates['temp']['flagged'] = True
if aggregates['pressure']['total'] > 3000:
    aggregates['pressure']['flagged'] = True  # Never triggered

# Simulate calibration offset (not actually applied)
calibration_map = {'temp': 0.2, 'pressure': -5, 'humidity': 1.5}

# Process data: only temperature affects final score
processed_data = []
def process_entry(val):
    if val > mean_temp:
        return val * 1.05
    else:
        return val * 0.95

for val in temp_readings:
    processed_data.append(process_entry(val))

# Secondary distraction: string-based status encoding
status_flags = ''.join(sorted(set(e['status'] for e in data_stream)))
encoded_flag = sum(ord(c) for c in status_flags)  # Computed but unused

# Core logic hidden among distractions
def calculate_stability_index(vals):
    diffs = [abs(a - b) for a, b in zip(vals, vals[1:])]
    return sum(diffs) / len(diffs) if diffs else 0.0

stability = calculate_stability_index(temp_readings)

# Final scoring function depends only on processed temp data and stability
def calculate_final_score(clean_temps):
    base = sum(clean_temps)
    penalty = stability * 10
    bonus = 50 if len(clean_temps) >= 4 else 25
    return int(base - penalty + bonus)

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")