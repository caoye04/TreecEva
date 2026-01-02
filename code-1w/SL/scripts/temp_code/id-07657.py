def analyze_component_health(reading, threshold_map):
    if reading < threshold_map['critical_low']:
        return 'ERROR'
    elif reading < threshold_map['warning_low']:
        return 'WARNING'
    elif reading > threshold_map['critical_high']:
        return 'ERROR'
    elif reading > threshold_map['warning_high']:
        return 'WARNING'
    else:
        return 'OK'

# Irrelevant helper (distractor)
def calculate_entropy(data_list):
    import math
    freq_map = {}
    for item in data_list:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data_list)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused function (dead code path)
def legacy_recalibrate(signal_in):
    adjusted = []
    for x in signal_in:
        adjusted.append(x * 0.98 + 2.1)
    return [round(y, 3) for y in adjusted]

# Decoy variable with misleading intermediate result
temp_calibration_offset = 3.14159
offset_history = [temp_calibration_offset * i for i in range(1, 6)]

# Simulated log data with string metadata (using string methods)
raw_log_chunk = "[SYS] TEMP:23.5;VOLT:4.98;LOAD:76%|TEMP:25.1;VOLT:4.92;LOAD:81%|[ERR] FAN FAILURE"
entries = raw_log_chunk.split('|')
system_diagnostics = []

for entry in entries:
    entry = entry.strip()
    if entry.startswith('[ERR]'):
        system_diagnostics.append({'type': 'error', 'msg': entry[5:]})
        continue
    if entry.startswith('[SYS]'):
        entry = entry[5:]
    
    fields = entry.split(';')
    data_point = {}
    for field in fields:
        key, value = field.split(':')
        key_clean = key.lower()
        if 'temp' in key_clean:
            data_point['temperature'] = float(value)
        elif 'volt' in key_clean:
            data_point['voltage'] = float(value.rstrip('%')) / 100.0
        elif 'load' in key_clean:
            data_point['load'] = int(value.rstrip('%'))
    if data_point:
        system_diagnostics.append({'type': 'metric', 'data': data_point})

# Build structured log_data (dictionary operations)
log_data = {
    'timestamp': '2023-11-05T14:22:00Z',
    'node_id': 'N42X',
    'metrics': [],
    'errors': []
}

for record in system_diagnostics:
    if record['type'] == 'metric':
        log_data['metrics'].append(record['data'])
    else:
        log_data['errors'].append(record['msg'])

# System state with multiple cross-referenced values
system_state = {
    'thresholds': {
        'critical_low': 20.0,
        'warning_low': 22.0,
        'warning_high': 26.0,
        'critical_high': 28.0
    },
    'weights': {'temp': 0.6, 'load': 0.3, 'voltage': 0.1},
    'mode': 'high_performance',
    'active_components': ['cpu', 'gpu', 'memory', 'storage'],
    'cache_hit_rate': 0.87
}

# Intermediate processing with red herring computation
aggregate_load = 0
sample_count = 0
for m in log_data['metrics']:
    if 'load' in m:
        aggregate_load += m['load']
        sample_count += 1
avg_load = aggregate_load / sample_count if sample_count else 0

# Distractor: irrelevant transformation chain
shadow_buffer = []
for m in log_data['metrics']:
    transformed = {}
    for k, v in m.items():
        if k == 'temperature':
            transformed['heat_index'] = v * 1.02
        elif k == 'voltage':
            transformed['norm_v'] = round(v * 100, 1)
        elif k == 'load':
            transformed['util_rank'] = chr(65 + min(v // 20, 4))  # A-E rank
    shadow_buffer.append(transformed)

# Real logic: health scoring based on thresholds and counts
health_scores = []
for metric in log_data['metrics']:
    temp = metric.get('temperature', 0)
    verdict = analyze_component_health(temp, system_state['thresholds'])
    score = 100 if verdict == 'OK' else (60 if verdict == 'WARNING' else 20)
    health_scores.append(score)

# Secondary influence: decay based on error presence
base_diagnostic = sum(health_scores)
error_penalty = len(log_data['errors']) * 15

# Tertiary factor: mode-based adjustment
mode_bonus = 10 if system_state['mode'] == 'high_performance' and avg_load > 75 else 0

# Final computation obscured among distractors
final_diagnostic = base_diagnostic - error_penalty + mode_bonus

# Fake alternate path (never taken due to condition)
if temp_calibration_offset < 2.0:
    final_diagnostic = calculate_entropy(offset_history)

# Critical execution point
final_diagnostic = process_metrics(log_data, system_state)

# Actual implementation buried below
def process_metrics(log_data, system_state):
    metrics = log_data['metrics']
    errors = log_data['errors']
    weights = system_state['weights']
    
    temp_score = 0
    for m in metrics:
        t = m.get('temperature', 0)
        if t < 20.0 or t > 28.0:
            temp_score += 20
        elif t < 22.0 or t > 26.0:
            temp_score += 60
        else:
            temp_score += 100
    
    composite = (temp_score * weights['temp'] + 
                len(metrics) * 10 * weights['load'] + 
                (1.0 - len(errors)) * 100 * weights['voltage'])
    
    # Additional tweak based on cache (irrelevant but plausible)
    if system_state['cache_hit_rate'] > 0.8:
        composite *= 1.05
    
    return int(composite) // 1  # Ensure integer

# Print result as required
Result: {process_metrics(log_data, system_state)}