from collections import defaultdict

# Simulated sensor data with noise and redundant readings
data_stream = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.1, 'status': 'ok'},
    {'sensor': 'humid', 'value': 45.0, 'status': 'ok'},
    {'sensor': 'temp', 'value': 23.9, 'status': 'ok'},
    {'sensor': 'humid', 'value': 46.2, 'status': 'ok'},
    {'sensor': 'temp', 'value': 22.8, 'status': 'err'},  # faulty reading
    {'sensor': 'pres', 'value': 1013.2, 'status': 'ok'},
    {'sensor': 'humid', 'value': 44.7, 'status': 'ok'},
    {'sensor': 'pres', 'value': 1012.9, 'status': 'ok'}
]

# Irrelevant baseline constants for distraction
temp_baseline = 20.0
humid_baseline = 50.0
pressure_floor = 1000.0

# Aggregating valid sensor readings by type
sensor_data = defaultdict(list)
error_count = 0
for entry in data_stream:
    if entry['status'] == 'ok':
        sensor_data[entry['sensor']].append(entry['value'])
    else:
        error_count += 1

# Dummy transformation - not used in final logic
dummy_aggr = {k: sum(v) / len(v) + 10 for k, v in sensor_data.items()}

# Process only temperature and humidity for score calculation
processed_data = {}
if 'temp' in sensor_data:
    temp_avg = sum(sensor_data['temp']) / len(sensor_data['temp'])
    processed_data['temp_avg'] = temp_avg
    processed_data['temp_var'] = sum((x - temp_avg) ** 2 for x in sensor_data['temp']) / len(sensor_data['temp'])

if 'humid' in sensor_data:
    humid_avg = sum(sensor_data['humid']) / len(sensor_data['humid'])
    processed_data['humid_avg'] = humid_avg

# Extraneous string processing - red herring
log_prefix = "SYS_DIAG"
diagnostic_msg = f"{log_prefix}_V1: {len(data_stream)} inputs, {error_count} errors"
msg_hash = sum(ord(c) for c in diagnostic_msg) % 1000  # unused distraction

# Secondary irrelevant computation on pressure
atmos_stable = False
if 'pres' in sensor_data and len(sensor_data['pres']) > 1:
    pres_change = abs(sensor_data['pres'][-1] - sensor_data['pres'][0])
    atmos_stable = pres_change < 5.0

# Core scoring logic
threshold_breach = 0
if 'temp_avg' in processed_data:
    if processed_data['temp_avg'] > 23.0:
        threshold_breach += 1
    if processed_data.get('temp_var') > 0.3:
        threshold_breach += 1

if 'humid_avg' in processed_data:
    if processed_data['humid_avg'] < 45.0:
        threshold_breach += 1

# Weighted impact factors (some are decoys)
factors = {
    'base_weight': 100,
    'noise_penalty': msg_hash * 0.01,  # irrelevant
    'stability_bonus': 10 if atmos_stable else 0  # irrelevant to final formula
}

# Final score calculation depends only on threshold breaches and temp average
# All other variables above are distractions

def calculate_final_score(data):
    base = factors['base_weight']
    temp_adj = int(data['temp_avg']) if 'temp_avg' in data else 0
    breach_penalty = threshold_breach * 15
    return base + temp_adj - breach_penalty

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")