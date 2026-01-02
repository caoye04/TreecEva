def analyze_component_health(sensor_data, threshold_map):
    accumulated_risk = 0
    for entry in sensor_data:
        temp_score = entry['temp'] * 0.7 + entry['pressure'] * 0.3
        if temp_score > threshold_map['critical_temp']:
            accumulated_risk += 2
        elif temp_score > threshold_map['elevated_temp']:
            accumulated_risk += 1
    return accumulated_risk

def evaluate_connectivity(nodes):
    connection_count = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i]['linked'] and nodes[j]['linked']:
                connection_count += 1
    return connection_count if connection_count > 5 else 0

def compute_stability_index(config_layers):
    index = 1.0
    for layer in config_layers:
        if layer['active']:
            index *= (layer['replicas'] / (layer['failures'] + 1))
    return round(index, 4)

def filter_noisy_logs(raw_logs):
    cleaned = []
    for log in raw_logs:
        if 'ERROR' in log['level'] or 'CRITICAL' in log['level']:
            cleaned.append(log)
    return cleaned  # Unused in final computation

def dummy_aggregation(x, y):
    result = 0
    for i in range(min(x, y)):
        result += (i * i) % 7
    return result  # Dead code path

def process_metrics(entries, state):
    error_count = sum(1 for e in entries if e['type'] == 'system' and e['severity'] > 1)
    warning_ratio = sum(1 for e in entries if 'WARN' in e.get('tag', '')) / max(len(entries), 1)
    base_score = error_count * 100 + int(warning_ratio * 50)
    
    health_status = {'optimal': 0, 'degraded': 1, 'faulty': 2}
    status_value = health_status.get(state.get('status'), 99)
    
    mode_factor = 2 if state.get('mode') == 'diagnostic' else 1
    
    diagnostic_flag = (status_value >= 1) and (base_score > 150)
    
    # Key distraction: irrelevant data transformation
    transformed_entries = [
        {**e, 'flagged': 'CRITICAL' in str(e.get('details', ''))} for e in entries
    ]
    critical_flags = sum(1 for e in transformed_entries if e['flagged'])
    
    # Another red herring: unused function call with side effect simulation
    _ = [entry.update({'processed': False}) for entry in transformed_entries]
    
    # Distractor variables
    temporal_weight = len(entries) % 13
    phantom_score = dummy_aggregation(error_count, len(entries))
    
    # Conditional expression (required Python feature)
    adjustment = 50 if any(e['source'] == 'sensor_hub' for e in entries) else 25
    
    # Linear search for specific pattern (suggested paradigm)
    first_critical_index = -1
    for idx, entry in enumerate(entries):
        if entry.get('priority') == 'critical' and entry['type'] == 'system':
            first_critical_index = idx
            break
    
    # Character counting in metadata (suggested paradigm)
    total_chars = sum(len(str(v)) for entry in entries for v in entry.values() if isinstance(v, str))
    char_bonus = 10 if total_chars > 500 else 0
    
    # Main computation chain
    intermediate = base_score + adjustment + char_bonus
    if mode_factor > 1:
        intermediate = int(intermediate * 1.2)
    if first_critical_index >= 0:
        intermediate += 75
    
    # Final logic step
    final_diagnostic = intermediate - (status_value * 40)
    
    # Irrelevant secondary processing
    redundancy_check = evaluate_connectivity(state.get('network_nodes', []))
    stability = compute_stability_index(state.get('config_layers', []))
    
    return final_diagnostic

# Simulated input data
log_entries = [
    {'type': 'system', 'severity': 2, 'tag': 'WARN_init', 'source': 'sensor_hub', 'priority': 'normal'},
    {'type': 'app', 'severity': 1, 'tag': 'INFO_flow', 'source': 'svc_a', 'priority': 'low'},
    {'type': 'system', 'severity': 3, 'tag': 'WARN_retry', 'source': 'sensor_hub', 'priority': 'critical'},
    {'type': 'system', 'severity': 2, 'tag': 'WARN_timeout', 'source': 'gateway', 'priority': 'normal'},
    {'type': 'system', 'severity': 4, 'details': 'CRITICAL FAILURE IN ARRAY', 'source': 'sensor_hub', 'priority': 'critical'}
] + [{'type': 'debug', 'severity': 0, 'source': f'trace_{i}', 'priority': 'low'} for i in range(8)]

system_state = {
    'status': 'degraded',
    'mode': 'diagnostic',
    'network_nodes': [
        {'id': 'A', 'linked': True}, {'id': 'B', 'linked': True},
        {'id': 'C', 'linked': False}, {'id': 'D', 'linked': True},
        {'id': 'E', 'linked': True}, {'id': 'F', 'linked': True}
    ],
    'config_layers': [
        {'active': True, 'replicas': 3, 'failures': 1},
        {'active': True, 'replicas': 2, 'failures': 0},
        {'active': False, 'replicas': 1, 'failures': 1}
    ]
}

# Execute key statement
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Result: {final_diagnostic}")