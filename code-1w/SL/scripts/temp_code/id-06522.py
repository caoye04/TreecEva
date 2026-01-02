def parse_timestamp(ts):
    return sum(int(part) for part in ts.split(':'))


def extract_severity(event):
    if 'ERR' in event:
        return 3
    elif 'WARN' in event:
        return 2
    elif 'INFO' in event:
        return 1
    return 0

# Irrelevant helper that's never called
def decrypt_hash(h):
    return sum(ord(c) for c in h) % 100

# Misleading data structure with decoy entries
system_status = {
    'node_1': {'load': 0.85, 'temp': 67, 'uptime': 1240},
    'node_2': {'load': 0.92, 'temp': 70, 'uptime': 1100},
    'node_3': {'load': 0.45, 'temp': 50, 'uptime': 2000}
}

# Unused function to create red herring
def calculate_stability_score(node_data):
    scores = []
    for node, metrics in node_data.items():
        score = (1 / metrics['load']) * (metrics['temp'] + metrics['uptime'])
        scores.append(score)
    return sum(scores) / len(scores)

# Decoy variables with plausible but unused values
baseline_threshold = 0.75
maintenance_window = ['02:00', '04:00']
critical_events_log = []

# Core diagnostic tags - some are distractors
system_flags = {
    'overload_risk': True,
    'io_bottleneck': False,
    'memory_leak_suspected': True,
    'redundant_power': True,
    'legacy_protocol': False
}

# Simulated log stream with mixed content
raw_logs = [
    "[10:23:45] INFO: System initialized",
    "[10:24:10] WARN: High memory pressure on node_2",
    "[10:24:15] ERR: Failed to sync backup server",
    "[10:24:30] INFO: User authentication successful",
    "[10:24:45] WARN: Disk usage above 85%",
    "[10:25:00] ERR: Database connection timeout",
    "[10:25:15] INFO: Cache cleared",
    "[10:25:30] WARN: Latency spike detected"
]

# Process logs into structured format
log_entries = []
for entry in raw_logs:
    timestamp_str = entry[1:9]  # Extract HH:MM:SS
    full_text = entry[12:]
    code = extract_severity(full_text)
    time_weight = parse_timestamp(timestamp_str) // 10
    category = 'error' if 'ERR' in full_text else 'warning' if 'WARN' in full_text else 'info'
    priority = code * (time_weight % 5)
    
    # Irrelevant transformation
    masked_id = ''.join([c.lower() if c.isupper() else c for c in full_text[:8]])
    
    log_entries.append({
        'raw': entry,
        'severity': code,
        'timestamp': timestamp_str,
        'type': category,
        'priority': priority,
        'key_token': masked_id
    })

# Decoy aggregation that isn't used
total_warnings = len([e for e in log_entries if e['type'] == 'warning'])

# Real computation buried in noise
flag_weights = {
    'overload_risk': 15,
    'io_bottleneck': 10,
    'memory_leak_suspected': 20,
    'redundant_power': -5,
    'legacy_protocol': 3
}

# Heavily interwoven logic with distractions
def aggregate_metrics(logs, flags):
    base_score = 0
    
    # Real signal: count high-severity logs
    critical_count = 0
    for log in logs:
        if log['severity'] >= 3:
            critical_count += 1
            base_score += log['priority']
    
    # Distractor: process all logs regardless
    avg_priority = sum(log['priority'] for log in logs) / len(logs) if logs else 0
    
    # Another decoy path
    temporal_pattern = []
    for log in logs:
        h, m, s = map(int, log['timestamp'].split(':'))
        if m % 2 == 0:
            temporal_pattern.append(s % 7)
    
    # Actual flag contribution
    flag_bonus = 0
    for f, active in flags.items():
        if active:
            flag_bonus += flag_weights[f]
    
    # Irrelevant string transformation
    signature_chars = {c for log in logs for c in log['key_token'] if c.isalpha()}
    alphabet_score = sum(ord(c.upper()) - 64 for c in signature_chars) % 11
    
    # Critical calculation chain
    intermediate = (base_score * 2) + flag_bonus  # Step 1
    intermediate -= len(temporal_pattern)         # Step 2 (mostly noise)
    intermediate += alphabet_score                # Step 3 (minor effect)
    intermediate *= (1 + (critical_count > 0))    # Step 4: double if any critical
    intermediate += (avg_priority // 2)           # Step 5: small addition
    
    # Final adjustment based on real condition
    if flags['memory_leak_suspected'] and critical_count >= 2:
        intermediate += 25  # Significant bonus
    
    return int(intermediate)

# Key execution point
final_diagnostic = aggregate_metrics(log_entries, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")