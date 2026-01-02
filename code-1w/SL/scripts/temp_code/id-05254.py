def analyze_component_health(health_flags):
    accumulated_risk = 0
    for flag in health_flags:
        if flag == 'overheat':
            accumulated_risk += 3
        elif flag == 'pressure_drop':
            accumulated_risk += 2
        elif flag == 'vibration_spike':
            accumulated_risk += 4
    return accumulated_risk

# Irrelevant helper (decoy)
def calculate_efficiency_score(readings):
    base = sum(readings) / len(readings)
    return round(base * 0.87, 2)

# Unused function (dead path)
def legacy_diagnostic(data):
    return [x ^ 5 for x in data if x > 10]

# Main processing pipeline
def process_metrics(entries, state):
    severity_map = {'critical': 5, 'warning': 3, 'info': 1}
    event_count = {level: 0 for level in severity_map}
    timestamps = []
    
    # Parse log entries
    for entry in entries:
        timestamp_str, level, code = entry.split('|')
        timestamps.append(int(timestamp_str))
        if level in event_count:
            event_count[level] += 1
    
    # Compute time-based metrics
    time_span = max(timestamps) - min(timestamps) if timestamps else 0
    avg_interval = time_span / len(timestamps) if timestamps else 0
    
    # Distractor variables
    dummy_mask = [t & 0xFF for t in timestamps]
    checksum = sum(dummy_mask) % 1000
    normal_ops = event_count['info']
    
    # Health flags from system state
    active_alarms = state.get('active_alarms', [])
    risk_level = analyze_component_health(active_alarms)
    
    # Conditional expression with distractors
    base_score = event_count['critical'] * severity_map['critical'] + \
                 event_count['warning'] * severity_map['warning']
    adjustment_factor = 0.9 if state.get('redundancy_active') else 1.2
    
    # Multiple data structures interaction
    diagnostics = {
        'base': base_score,
        'risk': risk_level,
        'time_penalty': int(avg_interval // 10),
        'final_raw': 0
    }
    
    # Secondary processing with dictionary operations
    temp_log = {}
    for k, v in diagnostics.items():
        temp_log[f'temp_{k}'] = v * 2 if k != 'final_raw' else 0
    
    # Real computation path
    raw_value = diagnostics['base'] + diagnostics['risk'] + diagnostics['time_penalty']
    adjusted_value = raw_value * adjustment_factor
    
    # Case conversion decoy
    mode_flag = state.get('mode', 'STANDBY').lower()
    if mode_flag == 'overload':
        adjusted_value *= 1.5
    
    # Final assignment (key statement)
    final_diagnostic = int(round(adjusted_value))
    
    # Dead-end computation (red herring)
    outlier_count = len([x for x in timestamps if x % 100 == 0])
    buffer_health = ''.join([chr(t % 26 + 65) for t in timestamps[:3]]) if timestamps else ''
    
    return final_diagnostic

# Input data
log_entries = [
    "1003|critical|ERR502",
    "1018|warning|WARN101",
    "1022|warning|WARN102",
    "1035|info|OK200",
    "1041|critical|ERR503"
]

system_state = {
    'active_alarms': ['overheat', 'vibration_spike'],
    'redundancy_active': True,
    'mode': 'NORMAL'
}

# Execution
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Target result: {final_diagnostic}")