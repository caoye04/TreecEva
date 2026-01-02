def preprocess_logs(raw):
    processed = []
    for item in raw:
        if 'ERROR' in item['level']:
            processed.append({
                'id': item['id'],
                'severity': len(item['message'].split()),
                'timestamp_norm': item['timestamp'] % 1000
            })
    return processed

# Irrelevant helper (distractor)
def calculate_health_score(metrics):
    score = 0
    for m in metrics:
        if m > 50:
            score += 1
    return score * 100  # Dead end

# Unused transformation function (red herring)
def transform_data(data_map):
    result = {}
    for k, v in data_map.items():
        if isinstance(v, list):
            result[k] = sum(v) // len(v) if v else 0
    return result

def filter_redundant(entries):
    seen = set()
    unique = []
    for e in entries:
        key = (e['id'], e['timestamp_norm'])
        if key not in seen:
            seen.add(key)
            unique.append(e)
    return unique

# Core logic buried among noise
def detect_anomaly_sequence(events):
    if len(events) < 3:
        return False
    for i in range(len(events) - 2):
        a, b, c = events[i:i+3]
        if a['severity'] < b['severity'] > c['severity'] and (b['timestamp_norm'] - a['timestamp_norm']) == (c['timestamp_norm'] - b['timestamp_norm']):
            return True
    return False

def count_critical_transitions(flags):
    transitions = 0
    state_map = {'active': 1, 'standby': 0, 'fault': -1}
    numeric_states = [state_map.get(f, 0) for f in flags]
    
    # Distracting computation
    avg_state = sum(numeric_states) / len(numeric_states) if numeric_states else 0
    fluctuation_index = 0
    for i in range(1, len(numeric_states)):
        if numeric_states[i] != numeric_states[i-1]:
            fluctuation_index += 1
    
    # Real logic
    for i in range(1, len(numeric_states)):
        if numeric_states[i-1] == 1 and numeric_states[i] == -1:
            transitions += 1
    return transitions

def analyze_pattern(logs, flags):
    # Heavy distraction: irrelevant aggregations
    severity_count = {i: 0 for i in range(1, 10)}
    timestamp_bins = {i: 0 for i in range(0, 1000, 100)}
    total_magnitude = 0
    
    for log in logs:
        s = log['severity']
        t = log['timestamp_norm']
        if s >= 1 and s <= 9:
            severity_count[s] += 1
        bin_key = (t // 100) * 100
        if bin_key in timestamp_bins:
            timestamp_bins[bin_key] += 1
        total_magnitude += s * (t % 50)
    
    # More distractions
    entropy = 0.0
    for count in severity_count.values():
        if count > 0:
            p = count / len(logs) if logs else 0
            entropy -= p * __import__('math').log(p) if p > 0 else 0
    
    # Actual key computation path
    anomaly_present = detect_anomaly_sequence(logs)
    critical_jumps = count_critical_transitions(flags)
    
    # Decoy intermediate
    fake_indicator = (len(logs) * critical_jumps) % 77
    
    # Final deterministic answer logic (non-obvious)
    base = 1000
    if anomaly_present:
        base += 250
    if critical_jumps > 0:
        base -= 42 * critical_jumps
    if len(logs) > 5:
        base += 17
    
    final_score = base + (total_magnitude % 23)
    
    # Red herring: unused complex structure
    report_summary = {
        'diagnostics': [
            {'type': 'timing', 'value': sum(timestamp_bins.values())},
            {'type': 'severity_mode', 'value': max(severity_count, key=severity_count.get)}
        ],
        'meta_hash': (len(logs) + len(flags)) ^ 3847
    }
    
    return final_score

# Simulated input data
raw_log_data = [
    {'id': 101, 'level': 'INFO', 'message': 'System boot', 'timestamp': 1000},
    {'id': 102, 'level': 'ERROR', 'message': 'Failed to connect peripheral', 'timestamp': 1050},
    {'id': 103, 'level': 'ERROR', 'message': 'Disk read timeout occurred abruptly', 'timestamp': 1100},
    {'id': 104, 'level': 'ERROR', 'message': 'Memory allocation failed during processing', 'timestamp': 1150},
    {'id': 105, 'level': 'ERROR', 'message': 'Network latency spike detected', 'timestamp': 1200},
    {'id': 106, 'level': 'ERROR', 'message': 'Invalid checksum in packet stream', 'timestamp': 1250}
]

system_diagnostics = ['active', 'active', 'fault', 'standby', 'fault', 'active']

# Preprocessing chain
cleaned_logs = preprocess_logs(raw_log_data)
filtered_logs = filter_redundant(cleaned_logs)

# Key execution point
final_diagnostic = analyze_pattern(filtered_logs, system_diagnostics)

# Output
print(f"Result: {final_diagnostic}")