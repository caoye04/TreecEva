import math

# Simulated telemetry data from a distributed sensor network
telemetry_stream = [
    'SNSR1|23.5|OK|2023-04-05',
    'SNSR2|18.9|WARN|2023-04-05',
    'SNSR3|25.1|OK|2023-04-05',
    'SNSR1|24.0|OK|2023-04-06',
    'SNSR2|19.1|OK|2023-04-06',
    'SNSR4|30.2|ALERT|2023-04-06'
]

# Irrelevant lookup table for deprecated sensors
deprecated_sensors = {'SNSR0': '2020-12-01', 'SNSR5': '2021-03-15'}
legacy_mapping = {k: v.split('-')[0] for k, v in deprecated_sensors.items()}

# Parse and filter current active sensors
active_readings = {}
for entry in telemetry_stream:
    parts = entry.split('|')
    sensor_id, temp_str, status, date = parts
    temperature = float(temp_str)
    
    if sensor_id not in active_readings:
        active_readings[sensor_id] = []
    active_readings[sensor_id].append({
        'temp': temperature,
        'status': status,
        'date': date
    })

# Decoy aggregation: unused average per sensor (red herring)
unused_avg_per_sensor = {}
for sid, records in active_readings.items():
    total = sum(r['temp'] for r in records)
    unused_avg_per_sensor[sid] = round(total / len(records), 2)

# Historical baselines (partially relevant)
baselines = {
    'SNSR1': 22.0, 'SNSR2': 18.5, 'SNSR3': 24.0, 'SNSR4': 28.0
}

# Complex transformation: extract latest readings only
latest_readings = {}
for sid, records in active_readings.items():
    latest = max(records, key=lambda x: x['date'])
    latest_readings[sid] = latest['temp']

# Bit manipulation decoy: simulate checksum (not actually used)
def compute_fake_checksum(data_dict):
    keys = sorted(data_dict.keys())
    chk = 0
    for i, k in enumerate(keys):
        val = int(data_dict[k])
        chk ^= (val << 2) | (i & 3)
    return chk ^ 0xFF

fake_checksum = compute_fake_checksum(latest_readings)  # Dead-end computation

# Distractor: mock anomaly detection with no impact
def scan_for_outliers(vals, threshold=2.0):
    mean_val = sum(vals) / len(vals)
    variance = sum((v - mean_val) ** 2 for v in vals) / len(vals)
    std_dev = math.sqrt(variance)
    return [v for v in vals if abs(v - mean_val) > threshold * std_dev]

all_temps = list(latest_readings.values())
outlier_list = scan_for_outliers(all_temps)  # Computed but unused

# Real processing begins: build log data structure
log_data = []
for entry in telemetry_stream:
    comp = entry.upper().replace('-', '').split('|')
    code_sum = sum(ord(c) for c in comp[0] if c.isalpha())
    log_data.append(code_sum * 0.1)

# System state depends on status severity counts
severity_map = {'OK': 0, 'WARN': 1, 'ALERT': 2}
state_counter = {0: 0, 1: 0, 2: 0}
for records in active_readings.values():
    for r in records:
        sev = severity_map[r['status']]
        state_counter[sev] += 1

system_state = tuple(state_counter[i] for i in range(3))

# Auxiliary function: maps log features to weighted index
def integrate_logs(logs):
    smoothed = [math.cos(math.pi * x / 100.0) for x in logs]
    return sum(smoothed) * 100

# Another distractor: string-based validation (unused path)
concat_stream = ''.join(telemetry_stream)
validation_key = concat_stream.count('OK') * concat_stream.index('SNSR1')
if validation_key > 100:
    validation_flag = True
    secondary_check = concat_stream.split('|')
    token_group = [t for t in secondary_check if t.startswith('S')]
else:
    validation_flag = False

# Core logic hidden in complex conditional
primary_keys = sorted(latest_readings.keys())
delta_total = 0.0
for k in primary_keys:
    base = baselines.get(k, 20.0)
    latest_temp = latest_readings[k]
    deviation = abs(latest_temp - base)
    if k == 'SNSR4':
        delta_total += deviation * 2
    else:
        delta_total += deviation

evaluation_score = delta_total / len(primary_keys)

# Final processing function
def process_metrics(log_metrics, sys_state):
    # Irrelevant unpacking
    ok_count, warn_count, alert_count = sys_state
    
    # Fake entropy calculation
    if alert_count > 0:
        risk_factor = 3.0
    elif warn_count > 2:
        risk_factor = 1.8
    else:
        risk_factor = 1.0
    
    # Actual signal extraction from log_metrics
    raw_signal = integrate_logs(log_metrics)
    
    # Critical dependency on evaluation_score from outer scope (closure-like)
    nonlocal evaluation_score
    
    # Main formula
    result = raw_signal + (evaluation_score * 100) - (risk_factor * 50)
    
    # Red herring: modify result based on fake_checksum (but don't use)
    temp_result = result
    if fake_checksum > 0:
        temp_result -= (fake_checksum % 7)
    
    # Final adjustment: only this matters
    final_value = round(result, 4)
    
    return final_value

# Key execution point
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")