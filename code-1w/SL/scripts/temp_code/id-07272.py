import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 45.2, 'timestamp': 1623456780},
    {'sensor': 'pressure', 'value': 101.3, 'timestamp': 1623456781},
    {'sensor': 'temp', 'value': 47.8, 'timestamp': 1623456782},
    {'sensor': 'vibration', 'value': 0.65, 'timestamp': 1623456783},
    {'sensor': 'temp', 'value': 44.1, 'timestamp': 1623456784}
]

# Irrelevant baseline catalog (distractor)
sensor_catalog = {
    'temp': {'unit': 'C', 'range': (-40, 125)},
    'pressure': {'unit': 'kPa', 'range': (0, 200)},
    'vibration': {'unit': 'mm/s', 'range': (0, 5)},
    'humidity': {'unit': '%', 'range': (0, 100)}
}

# System thresholds for anomaly detection
system_thresholds = {
    'temp_high': 46.0,
    'temp_fluctuation': 5.0,
    'pressure_stable': 101.0,
    'vibration_limit': 0.7
}

# Historical fake cache (dead code path)
cached_diagnostics = {
    'last_run': 1623456000,
    'anomalies': [],
    'checksum': 'a1b2c3d4'
}

# Misleading pre-processing function (partially unused)
def normalize_reading(value, sensor_type):
    if sensor_type == 'temp':
        return (value - 273.15) if value > 100 else value
    elif sensor_type == 'pressure':
        return value * 0.145 if value > 100 else value * 0.1
    return value

# Decoy transformation (never called)
transform_data = lambda x: [\{'processed': round(math.log(v['value'] + 1), 3)} for v in x if v['sensor'] != 'humidity']

# Extract relevant entries and convert to flat list
log_entries = []
for entry in telemetry_stream:
    normalized_val = normalize_reading(entry['value'], entry['sensor'])
    log_entries.append({
        'type': entry['sensor'],
        'val': normalized_val,
        'sec': entry['timestamp'] % 1000
    })

# Red herring: unused statistical summary
mean_temp = sum(e['val'] for e in log_entries if e['type'] == 'temp') / len([e for e in log_entries if e['type'] == 'temp'])
median_vibration = sorted([e['val'] for e in log_entries if e['type'] == 'vibration'])[0] if [e for e in log_entries if e['type'] == 'vibration'] else 0

# Real processing begins: detect temperature anomalies
temp_readings = [e for e in log_entries if e['type'] == 'temp']
anomalies = 0

if temp_readings:
    high_count = sum(1 for r in temp_readings if r['val'] > system_thresholds['temp_high'])
    fluctuation_exceeded = False
    for i in range(1, len(temp_readings)):
        if abs(temp_readings[i]['val'] - temp_readings[i-1]['val']) > system_thresholds['temp_fluctuation']:
            fluctuation_exceeded = True
            break
    
    # Conditional expression with distractor variables
    base_score = 10 if high_count >= 2 else (5 if fluctuation_exceeded else 0)
    pressure_stable = all(abs(e['val'] - system_thresholds['pressure_stable']) < 0.5 
                          for e in log_entries if e['type'] == 'pressure')
    vibration_ok = all(e['val'] <= system_thresholds['vibration_limit'] 
                       for e in log_entries if e['type'] == 'vibration')
    
    # Unused intermediate calculation (misleading)
    safety_margin = (system_thresholds['vibration_limit'] - median_vibration) * 100 if median_vibration else 0
    
    # Core logic: multiple conditions combined
    if not pressure_stable:
        anomalies += 1
    if not vibration_ok:
        anomalies += 2
    if base_score > 0:
        anomalies += base_score // 5

# Dictionary-based state machine (irrelevant but plausible)
state_transitions = {
    ('idle', 'normal'): 'stable',
    ('stable', 'anomaly'): 'warning',
    ('warning', 'anomaly'): 'critical'
}

# Actual metric processor
config_flags = {"debug": False, "strict": True}

def process_metrics(entries, thresholds):
    # Extract values using dictionary operations
    temps = [e['val'] for e in entries if e['type'] == 'temp']
    if not temps:
        return -1
    
    # Compute rolling differences
    diffs = [abs(temps[i] - temps[i-1]) for i in range(1, len(temps))]
    max_diff = max(diffs) if diffs else 0
    
    # Use lambda to compute weighted impact
    severity_weight = lambda d, t: 3 if d > t['temp_fluctuation'] else (2 if d > t['temp_fluctuation']*0.8 else 1)
    total_impact = sum(severity_weight(d, thresholds) for d in diffs)
    
    # Final computation with conditional expression
    adjustment = 0.5 if config_flags["debug"] else 1.0
    result = int((total_impact * adjustment) + (len(temps) % 3))
    
    # Inject irrelevant bit manipulation (distractor)
    decoy_flag = 0b1010 ^ 0b1100 & 0b1111
    decoy_flag <<= 2
    
    return result + decoy_flag  # decoy_flag = 20, but non-obvious

# Key execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result
print(f"Target result: {final_diagnostic}")