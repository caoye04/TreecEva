from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
technical_logs = [
    {'timestamp': 1001, 'type': 'IO', 'value': 23, 'status': 'OK'},
    {'timestamp': 1003, 'type': 'CPU', 'value': 88, 'status': 'WARN'},
    {'timestamp': 1005, 'type': 'MEM', 'value': 45, 'status': 'OK'},
    {'timestamp': 1009, 'type': 'IO', 'value': 12, 'status': 'OK'},
    {'timestamp': 1012, 'type': 'CPU', 'value': 95, 'status': 'ALERT'},
    {'timestamp': 1015, 'type': 'NET', 'value': 67, 'status': 'OK'},
    {'timestamp': 1018, 'type': 'MEM', 'value': 82, 'status': 'WARN'},
    {'timestamp': 1022, 'type': 'IO', 'value': 33, 'status': 'OK'}
]

# Irrelevant auxiliary data (distractor)
system_inventory = {
    'servers': ['alpha', 'beta', 'gamma'],
    'locations': {'us': 2, 'eu': 1},
    'uptime_days': [45, 120, 67]
}

# Misleading preprocessing path (dead code)
def legacy_transform(logs):
    result = []
    for log in logs:
        if log['type'] == 'CPU':
            result.append({**log, 'value': min(log['value'] * 1.1, 100)})
    return result

# Unused transformation function (decoy)
def smooth_data(data_list):
    smoothed = []
    for i in range(len(data_list)):
        neighbors = [data_list[j]['value'] for j in range(max(0, i-1), min(len(data_list), i+2))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Real processing begins here
filtered_logs = [log for log in technical_logs if log['status'] in ['WARN', 'ALERT']]

# Extract baseline metrics (partially relevant)
baseline = defaultdict(list)
for entry in technical_logs:
    baseline[entry['type']].append(entry['value'])

avg_metrics = {k: sum(v) // len(v) for k, v in baseline.items()}  # Integer division

# Spurious correlation attempt (distractor)
correlation_score = 0
for i in range(1, len(filtered_logs)):
    if filtered_logs[i]['type'] != filtered_logs[i-1]['type']:
        correlation_score += 5

# Flag-based weighting system
system_flags = {
    'overload_threshold': 90,
    'warning_decay': 0.85,
    'priority_types': {'CPU', 'MEM'},
    'adjustment_factor': 1.7
}

# Red herring computation with sets
active_types = set(entry['type'] for entry in technical_logs)
priority_pending = active_types & system_flags['priority_types']
diagnostic_trace = set()
for t in priority_pending:
    diagnostic_trace.add(hash(t) % 100)

# Meaningless enumeration with zip (distraction)
indices = list(enumerate([x['value'] for x in technical_logs if x['type'] == 'IO']))
shifted = [v + i for i, v in indices]
zip_result = list(zip(indices, shifted))

# Core logic buried in distractions
def analyze_severity(log_list, flags):
    severity = 0
    history = Counter()
    
    for log in log_list:
        base_val = log['value']
        type_key = log['type']
        
        # Accumulate historical frequency
        history[type_key] += 1
        
        # Primary contribution to severity
        if base_val > flags['overload_threshold']:
            severity += 13
        elif log['status'] == 'WARN':
            severity += 5
        
        # Priority multiplier
        if type_key in flags['priority_types']:
            severity += int(3 * history[type_key])
    
    return severity

# Secondary metric with modular arithmetic
def compute_stability_index(entries):
    total = 0
    for i, entry in enumerate(entries):
        total += (entry['timestamp'] + entry['value']) % (i + 3)
    return total // 4

# Main processing function combining multiple concepts
def process_metrics(log_entries, config):
    # Step 1: Filter critical entries
    alerts = [e for e in log_entries if e['status'] == 'ALERT']
    warnings = [e for e in log_entries if e['status'] == 'WARN']
    
    # Step 2: Compute weighted severity
    primary_score = analyze_severity(warnings + alerts, config)
    
    # Step 3: Calculate temporal stability
    stability = compute_stability_index(log_entries)
    
    # Step 4: Apply adjustment using dictionary lookup and float math
    factor = config.get('adjustment_factor', 1.0)
    adjusted = primary_score * factor
    
    # Step 5: Incorporate historical averages via set intersection logic
    high_avg_types = {k for k, v in avg_metrics.items() if v > 60}
    common_with_priority = high_avg_types & config['priority_types']
    bonus = len(common_with_priority) * 7
    
    # Step 6: Final composition with integer truncation
    raw_final = int(adjusted + stability + bonus)
    
    # Step 7: Apply modular cap to prevent overflow
    final_value = raw_final % 10000
    
    # Step 8: Correct answer derivation
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(log_entries=technical_logs, system_flags=system_flags)

# Print target result
print(f"Target result: {final_diagnostic}")