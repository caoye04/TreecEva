def parse_log_segment(entry):
    if 'ERROR' in entry:
        return {'level': 3, 'timestamp': entry.split()[0], 'valid': True}
    elif 'WARN' in entry:
        return {'level': 2, 'timestamp': entry.split()[0], 'valid': True}
    elif 'INFO' in entry:
        return {'level': 1, 'timestamp': entry.split()[0], 'valid': False}
    else:
        return {'level': 0, 'timestamp': None, 'valid': False}

# Simulated system log with mixed severity entries
temp_buffer = [
    "14:22:10 ERROR Disk usage at 95%",
    "14:23:05 WARN Network latency high",
    "14:24:00 INFO User login successful",
    "14:25:15 ERROR Failed to write file",
    "14:26:10 WARN CPU temperature rising",
    "14:27:00 INFO Backup completed"
]

log_entries = []
for item in temp_buffer:
    parsed = parse_log_segment(item)
    if parsed['valid']:
        log_entries.append(parsed)

# Irrelevant auxiliary computation - red herring
checksum = 0
for char in ''.join(temp_buffer):
    checksum += ord(char) % 7
classification_threshold = 42  # Unused constant (distractor)

# System flags with bit-encoded statuses
system_flags = {
    'overload': True,
    'io_frozen': False,
    'legacy_mode': True,
    'debug_enabled': True
}

# Decoy function that is never called
def compute_health_score(metrics):
    score = 0
    for m in metrics:
        score += m['level'] * 10
        if m['timestamp'].startswith('14:2'):
            score += 1
    return max(score, 5)

# Another dead path - unused transformation
shadow_copy = [entry for entry in log_entries if entry['level'] > 1]
sorted_shadow = sorted(shadow_copy, key=lambda x: x['timestamp'], reverse=True)

# Core diagnostic logic with string and conditional complexity
def analyze_severity(patterns):
    critical_count = 0
    warning_count = 0
    for p in patterns:
        time_str = p['timestamp']
        minutes = int(time_str[3:5])
        seconds = int(time_str[6:8])
        # Only count events in even-numbered minutes with odd seconds as valid stress indicators
        if minutes % 2 == 0 and seconds % 2 == 1 and p['level'] >= 2:
            if p['level'] == 3:
                critical_count += 1
            elif p['level'] == 2:
                warning_count += 1
    return critical_count * 10 + warning_count

# Misleading intermediate metric
phantom_load = len(temp_buffer) * (1 if system_flags['debug_enabled'] else 0) - 2

# String-based routing decision (uses string method)
mode_selector = "diagnostic_stress_test".upper().replace('_', '')
if 'STRESS' in mode_selector:
    base_offset = 17
else:
    base_offset = 0

# Main aggregation function
def aggregate_metrics(events, flags):
    severity_score = analyze_severity(events)
    
    # Bitwise-inspired flag contribution (logical but not arithmetic bitwise)
    flag_boost = 0
    if flags['overload']:
        flag_boost += 5
    if not flags['io_frozen']:
        flag_boost += 3
    if flags['legacy_mode']:
        flag_boost -= 2  # Penalty
    if flags['debug_enabled']:
        flag_boost += 1
    
    # Conditional override based on string content analysis
    debug_hints = [e for e in temp_buffer if 'DEBUG' in e.upper()]
    if len(debug_hints) > 0:  # Never true, but present
        flag_boost = 0
    
    # Final computation with offset
    raw_diagnostic = severity_score + flag_boost + base_offset
    
    # Post-processing filter: ignore results divisible by 5 unless from critical logs
    has_critical = any(e['level'] == 3 for e in events)
    if raw_diagnostic % 5 == 0 and not has_critical:
        raw_diagnostic += 1
    
    # Normalize using length of actual error messages (string manipulation)
    error_messages = [item[11:] for item in temp_buffer if 'ERROR' in item]
    total_chars = sum(len(msg) for msg in error_messages)
    scaling_factor = (total_chars // 10) or 1
    
    final_diagnostic = raw_diagnostic * scaling_factor
    
    # Dead code branch - unreachable due to structure
    if False:
        final_diagnostic = -999
    
    return final_diagnostic

# Key execution point
final_diagnostic = aggregate_metrics(log_entries, system_flags)
print(f"Result: {final_diagnostic}")