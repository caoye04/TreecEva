from collections import defaultdict

# Simulate sensor data stream with noise and metadata
data_stream = [
    {'type': 'temp', 'value': 23.5, 'seq': 1},
    {'type': 'temp', 'value': 24.1, 'seq': 3},
    {'type': 'humid', 'value': 45.0, 'seq': 2},
    {'type': 'temp', 'value': 22.8, 'seq': 5},
    {'type': 'humid', 'value': 47.3, 'seq': 4},
    {'type': 'temp', 'value': 25.6, 'seq': 7},
    {'type': 'temp', 'value': 24.9, 'seq': 6}
]

# Distractor: unused transformation map for other sensor types
sensor_transforms = defaultdict(lambda: lambda x: x)
sensor_transforms['pressure'] = lambda x: x * 0.1
sensor_transforms['light'] = lambda x: x / 100

# State tracker for sequence validation
expected_next = 1
missing_seqs = []
redundant_seqs = []

temp_readings = []
humid_readings = []

for reading in sorted(data_stream, key=lambda x: x['seq']):
    if reading['seq'] > expected_next:
        missing_seqs.extend(range(expected_next, reading['seq']))
        expected_next = reading['seq'] + 1
    elif reading['seq'] == expected_next:
        expected_next += 1
    else:
        redundant_seqs.append(reading['seq'])
    
    # Filter and collect only temperature readings
    if reading['type'] == 'temp':
        temp_readings.append(reading['value'])
    elif reading['type'] == 'humid':
        humid_readings.append(reading['value'])

# Distractor: dead code path (no 'co2' type in input)
co2_compensated = []
for reading in data_stream:
    if reading['type'] == 'co2':
        compensated = reading['value'] * 1.2 if reading['value'] < 500 else reading['value'] * 0.9
        co2_compensated.append(compensated)

# Distractor: irrelevant statistical computation
avg_humidity = sum(humid_readings) / len(humid_readings) if humid_readings else 0
humidity_variance = sum((h - avg_humidity) ** 2 for h in humid_readings) / len(humid_readings) if humid_readings else 0

# Core logic: compute weighted trend from temperature sequence
def process_data(temps):
    if len(temps) < 2:
        return 0
    
    # Assign increasing weights to more recent readings
    weighted_sum = sum(temp * (i + 1) for i, temp in enumerate(temps))
    weight_total = sum(i + 1 for i in range(len(temps)))
    
    # Apply non-linear correction factor based on spread
    temp_range = max(temps) - min(temps)
    correction = 1.0 + (temp_range / 100)
    
    return round(weighted_sum / weight_total * correction, 4)

# Key statement
final_output = process_data(temp_readings)

# Additional distractor: unused helper using lambda
analyze_stability = lambda data: sum(abs(a - b) for a, b in zip(data, data[1:]))
stability_score = analyze_stability([round(t) for t in temp_readings])

print(f"Result: {final_output}")