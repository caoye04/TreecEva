from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'temp': 45, 'load': 0.7, 'errors': 2, 'active': True},
    {'node': 'B', 'temp': 65, 'load': 0.9, 'errors': 5, 'active': True},
    {'node': 'C', 'temp': 30, 'load': 0.4, 'errors': 0, 'active': True},
    {'node': 'D', 'temp': 85, 'load': 0.95, 'errors': 12, 'active': False}
]

# Irrelevant helper (decoy)
def calculate_efficiency_rating(node_data):
    base = node_data.get('load', 0) * 100
    penalty = node_data.get('errors', 0) * 2
    return max(0, base - penalty - node_data.get('temp', 0))

# Unused transformation path
def legacy_normalization(data_list):
    normalized = []
    for entry in data_list:
        if entry['active']:
            norm_val = (entry['temp'] * entry['load']) / (entry['errors'] + 1)
            normalized.append(norm_val)
    return normalized

# Distractor: fake aggregation
temp_history = defaultdict(list)
for i, entry in enumerate(telemetry_stream):
    temp_history[entry['node']].append(entry['temp'] + i)  # i is irrelevant

# Another red herring: error clustering
error_clusters = defaultdict(list)
for idx, record in enumerate(telemetry_stream):
    if record['errors'] > 3:
        error_clusters['high'].append((idx, record['node']))
    else:
        error_clusters['low'].append((idx, record['node']))

# Real processing begins here
log_entries = []
for entry in telemetry_stream:
    status_flag = 0
    if entry['temp'] > 80:
        status_flag |= 4
    if entry['load'] > 0.85:
        status_flag |= 2
    if entry['errors'] > 4:
        status_flag |= 1
    
    log_entries.append({
        'id': entry['node'],
        'flag': status_flag,
        'critical': status_flag == 7,
        'score': entry['temp'] * 0.3 + entry['load'] * 10 + entry['errors'] * 2
    })

# System state summary - relevant
system_state = {
    'nodes_online': sum(1 for e in telemetry_stream if e['active']),
    'total_errors': sum(e['errors'] for e in telemetry_stream),
    'overloaded_nodes': len([e for e in telemetry_stream if e['load'] > 0.8]),
    'high_temp_count': len([e for e in telemetry_stream if e['temp'] > 75])
}

# Fake diagnostic chain (dead path)
def generate_health_report(state):
    report = {'status': 'stable'}
    if state['overloaded_nodes'] > 2:
        report['status'] = 'stress'
    if state['total_errors'] > 15:
        report['status'] = 'critical'
    return report

# Unused but plausible-looking analysis
health_snapshot = []
for i, (entry, log) in enumerate(zip(telemetry_stream, log_entries)):
    snapshot = {
        'index': i,
        'node_id': entry['node'],
        'risk_level': bin(log['flag']).count('1'),
        'baseline_offset': i * 0.1  # meaningless
    }
    health_snapshot.append(snapshot)

# Real function that contributes to answer
def analyze_flags(logs):
    flag_counter = Counter(log['flag'] for log in logs)
    dominant_flag = max(flag_counter, key=flag_counter.get)
    return flag_counter, dominant_flag

# Another distractor: temporal weighting (unused)
weights = [0.8 ** i for i in range(len(log_entries))]
weighted_score = sum(w * log['score'] for w, log in zip(weights, log_entries))

# Core logic buried among noise
def process_metrics(entries, state):
    counter, primary = analyze_flags(entries)
    
    # Key calculation: diagnostic weight
    severity_base = 0
    for flag, count in counter.items():
        if flag & 4:  # high temp
            severity_base += count * 10
        if flag & 2:  # high load
            severity_base += count * 8
        if flag & 1:  # high errors
            severity_base += count * 5
    
    # Conditional modulation based on system state
    multiplier = 1.0
    if state['nodes_online'] < 3:
        multiplier *= 1.5
    if state['overloaded_nodes'] >= 2:
        multiplier *= 1.3
    if state['high_temp_count'] >= 1:
        multiplier *= 1.2
    
    intermediate_result = int(severity_base * multiplier)
    
    # Final adjustment using bit manipulation (actual key step)
    final_value = intermediate_result ^ 0xAB  # XOR with magic number
    final_value = (final_value << 1) | (final_value >> 7)  # rotate left 1 bit equivalent
    final_value &= 0xFFFF  # clamp to 16 bits
    
    # This is the actual target
    final_diagnostic = (final_value + 17) // 3
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_state)

# Irrelevant cleanup
if __name__ == '__main__':
    print(f"Result: {final_diagnostic}")