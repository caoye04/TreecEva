from collections import defaultdict, Counter

# Simulated sensor network data analysis with diagnostic logic

# Raw sensor inputs (simulated)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = [
    (102, 'S1', 'temp'), (156, 'S2', 'temp'), (98, 'S3', 'temp'), (201, 'S4', 'temp'),
    (45, 'S1', 'humid'), (67, 'S2', 'humid'), (52, 'S3', 'humid'), (88, 'S4', 'humid'),
    (11, 'S1', 'flow'), (18, 'S2', 'flow'), (14, 'S3', 'flow'), (22, 'S4', 'flow')
]

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'pressure': [101.3, 102.1, 100.9],
    'vibration': [0.02, 0.04, 0.01],
    'optical_density': [0.88, 0.91]
}

# Mapping of expected thresholds by type and sensor (used in final logic)
threshold_map = defaultdict(lambda: defaultdict(int))
for sid in sensor_ids:
    threshold_map['temp'][sid] = 150
    threshold_map['humid'][sid] = 75
    threshold_map['flow'][sid] = 20

# Decoy configuration (dead path)
config_flags = {
    'enable_telemetry': False,
    'debug_mode': True,
    'log_level': 'VERBOSE',
    'use_legacy_parser': None  # Unused
}

# Data aggregation phase
aggregated = defaultdict(list)
for value, sensor, reading_type in raw_readings:
    aggregated[(sensor, reading_type)].append(value)

# Compute averages per (sensor, type)
averages = {}
for (sensor, r_type), values in aggregated.items():
    averages[(sensor, r_type)] = sum(values) / len(values)

# Misleading intermediate summary (looks important but unused later)
summary_stats = {
    'max_temp': max(v for k, v in averages.items() if 'temp' in k),
    'min_humid': min(v for k, v in averages.items() if 'humid' in k),
    'avg_flow': sum(v for k, v in averages.items() if 'flow' in k) / 4
}

# Processed data structure for analysis (key relevant input)
processed_data = []
for (sensor, r_type), avg_val in averages.items():
    processed_data.append({
        'sensor': sensor,
        'type': r_type,
        'value': avg_val,
        'status': 'normal'
    })

# Red herring function (never called)
def legacy_calibrate(data):
    return [d * 0.95 for d in data if d > 10]

# Auxiliary counting logic (partially relevant)
type_counter = Counter(r_type for _, _, r_type in raw_readings)

# Diagnostic engine core
warning_log = []
critical_count = 0
minor_count = 0

for entry in processed_data:
    s = entry['sensor']
    t = entry['type']
    v = entry['value']
    thresh = threshold_map[t][s]
    
    # Logical branching with bit manipulation red herring
    flag_code = 0
    if v > thresh:
        flag_code |= 1  # Set bit 0
        if 'temp' in t:
            flag_code |= 2  # Set bit 1
        warning_log.append(f'{s}:{t}={v}>thresh{thresh}')
        if 'temp' in t and v > thresh + 50:
            critical_count += 1
        else:
            minor_count += 1
    elif v < thresh * 0.3:
        flag_code |= 4  # Set bit 2 (unused case)

    entry['flags'] = flag_code

# Another decoy: unused transformation
transformed_data = [
    {**item, 'adjusted': item['value'] * 1.05 if item['type'] == 'fake'} 
    for item in processed_data
]

# Real diagnostic logic
stable_sensors = set()
affected_types = set()
for item in processed_data:
    if item['flags'] == 0:
        stable_sensors.add(item['sensor'])
    if item['flags'] & 1:  # Had threshold breach
        affected_types.add(item['type'])

# Final scoring heuristic
base_score = 100
base_score -= 15 * critical_count
base_score -= 5 * minor_count

if len(stable_sensors) < 2:
    base_score -= 20

# Influence from type diversity of issues
if len(affected_types) >= 2:
    base_score -= 12

# Normalize to avoid negative scores
final_diagnostic = max(base_score, 0)

# Dead code branch (never reached)
if config_flags['enable_telemetry']:
    upload_payload = {'diagnostic': final_diagnostic, 'stable': list(stable_sensors)}

# Output result
print(f"Result: {final_diagnostic}")