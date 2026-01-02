import math

# Simulated telemetry data from a distributed sensor network
telemetry_packets = [
    {'id': 'S1', 'readings': [23.4, 19.1, 25.6, 18.3], 'status': 'active'},
    {'id': 'S2', 'readings': [20.2, 21.5, 19.8, 20.1], 'status': 'active'},
    {'id': 'S3', 'readings': [], 'status': 'failed'},
    {'id': 'S4', 'readings': [17.6, 18.2, 19.1, 17.9], 'status': 'active'}
]

# Irrelevant auxiliary mapping (distractor)
unit_conversions = {
    'CtoF': lambda x: x * 9/5 + 32,
    'FtoC': lambda x: (x - 32) * 5/9,
    'KtoC': lambda x: x - 273.15
}

# Misleading preprocessing function (partially dead code)
def normalize_readings(data):
    normalized = []
    for packet in data:
        if packet['status'] == 'active' and packet['readings']:
            avg = sum(packet['readings']) / len(packet['readings'])
            # Unused transformation (red herring)
            normalized.append([round((r - avg) * 1.05, 2) for r in packet['readings']])
    return normalized  # Never actually used in final logic

# Decoy statistical analysis (dead path)
def compute_entropy(values):
    if not values:
        return 0.0
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Real processing begins here — but obscured by prior noise
log_data = "ERR|WARN|INFO|DEBUG|CRITICAL|WARN|ERR|ERR"
split_logs = log_data.split('|')
error_count = sum(1 for entry in split_logs if entry == 'ERR')
warning_count = sum(1 for entry in split_logs if entry == 'WARN')
info_count = sum(1 for entry in split_logs if entry == 'INFO')

distinct_log_types = set(split_logs)
log_risk_score = 0
for log_type in distinct_log_types:
    if log_type in ['CRITICAL', 'ERR']:
        log_risk_score += 3
    elif log_type == 'WARN':
        log_risk_score += 1

# System state with multiple fields (only some are relevant)
system_state = {
    'cpu_load': 78.2,
    'memory_usage': 85.6,
    'disk_io': 44.1,
    'active_threads': 128,
    'network_latency_ms': 27.4,
    'temperature_c': 67.3,
    'fan_speed_rpm': 3200,
    'power_cycles': 157,
    'uptime_hours': 2193
}

# Irrelevant bit manipulation (distractor function)
def scramble_value(x):
    x ^= 0xAB
    x = (x << 3) & 0xFF
    x |= (x >> 5)
    return x % 100

# Unused health index calculation (misleading intermediate)
bogus_health = 0
for key, value in system_state.items():
    if isinstance(value, float):
        bogus_health += int(value // 10)
bogus_health = scramble_value(bogus_health)

# Actual critical metric extraction
active_sensor_count = sum(1 for p in telemetry_packets if p['status'] == 'active')
avg_sensor_readings = []
for packet in telemetry_packets:
    if packet['status'] == 'active' and packet['readings']:
        avg_sensor_readings.append(sum(packet['readings']) / len(packet['readings']))

if avg_sensor_readings:
    mean_environmental_reading = sum(avg_sensor_readings) / len(avg_sensor_readings)
else:
    mean_environmental_reading = 0.0

# Conditional logic chain with string methods
log_signature = ''.join(s[0] for s in distinct_log_types)  # → 'EDWIC'
log_signature_filtered = log_signature.replace('I', '').replace('D', '')  # → 'EW'C'

alert_level = 0
if 'C' in log_signature_filtered:
    alert_level += 5
if 'E' in log_signature_filtered and error_count > 2:
    alert_level += 3
if 'W' in log_signature_filtered:
    alert_level += 1

# Key variable computation buried in complexity
def process_metrics(logs, state):
    base_score = alert_level * 10
    
    # Red herring: unused nested structure
    internal_audit = {
        'stage1': {'passed': True, 'score': base_score},
        'stage2': {'errors': error_count, 'warnings': warning_count}
    }
    
    # Relevant dependency on system load
    load_factor = 1
    if state['cpu_load'] > 75 and state['memory_usage'] > 80:
        load_factor = 2
    
    # Final diagnostic combines logs, alerts, and environmental average
    temperature_band = int(state['temperature_c'] // 10)
    env_contribution = round(mean_environmental_reading * 2, 1)
    
    # Critical formula — only this matters
    result = (env_contribution + log_risk_score) * load_factor + (temperature_band * alert_level)
    
    # Distracting string padding (irrelevant)
    padded_result_str = f"{int(result)}".zfill(8)
    masked = ''.join(str((int(c) + 7) % 10) for c in padded_result_str)
    
    return result  # This is what gets returned

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_state)

print(f"Result: {final_diagnostic}")