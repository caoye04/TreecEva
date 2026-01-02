def analyze_log_integrity(log_entries):
    seen_hashes = set()
    duplicates = set()
    for entry in log_entries:
        entry_hash = hash(entry['timestamp'] + entry['event_type'])
        if entry_hash in seen_hashes:
            duplicates.add(entry_hash)
        else:
            seen_hashes.add(entry_hash)
    return len(duplicates)


def filter_critical_events(log_entries):
    critical_events = []
    priority_map = {'ERROR': 3, 'WARN': 2, 'INFO': 1}
    for entry in log_entries:
        if entry['severity'] in priority_map and priority_map[entry['severity']] >= 2:
            critical_events.append(entry)
    # Irrelevant sorting
    critical_events.sort(key=lambda x: x['timestamp'], reverse=True)
    return critical_events


def calculate_entropy(data_strings):
    from collections import Counter
    char_counts = Counter(''.join(data_strings))
    total_chars = sum(char_counts.values())
    entropy = 0.0
    for count in char_counts.values():
        prob = count / total_chars
        if prob > 0:
            entropy -= prob * (prob ** 0.5)  # Simulated approximation
    return round(entropy, 4)


def calculate_remaining_capacity(log_entries, system_threshold):
    base_capacity = 10000
    usage_per_entry = 17
    bonus_grace = 0
    
    # Track different event types
    event_types = set()
    severity_levels = []
    total_length = 0
    
    for entry in log_entries:
        event_types.add(entry['event_type'])
        severity_levels.append(entry['severity'])
        total_length += len(entry['details'])
    
    # Compute initial deduction
    used_capacity = len(log_entries) * usage_per_entry
    type_bonus = len(event_types) * 50
    
    # Apply conditional grace based on severity distribution
    if 'CRITICAL' in severity_levels:
        bonus_grace += 200
    elif 'ERROR' in severity_levels and severity_levels.count('ERROR') > 3:
        bonus_grace += 100

    # Red herring: entropy calculation not directly tied to capacity
    detail_texts = [e['details'] for e in log_entries]
    _ = calculate_entropy(detail_texts)
    
    # Another red herring: analyze integrity but only conditionally affect logic
    duplicate_count = analyze_log_integrity(log_entries)
    if duplicate_count > 2:
        type_bonus -= 30  # minor penalty
    
    # Filtered critical events (computed but only used for length bonus)
    critical_subset = filter_critical_events(log_entries)
    filtered_bonus = len(critical_subset) * 5
    
    # Final adjustments
    adjusted_usage = used_capacity - type_bonus - bonus_grace - filtered_bonus
    final_capacity = base_capacity - adjusted_usage
    
    # Non-impacting debug computation
    avg_detail_len = total_length / len(log_entries) if log_entries else 0
    scaling_factor = 1.0 + (avg_detail_len / 100)
    final_capacity = int(final_capacity / scaling_factor)

    return final_capacity

# Input data
log_entries = [
    {'timestamp': '2023-10-01T08:00:00', 'event_type': 'auth', 'severity': 'INFO', 'details': 'User login attempt'},
    {'timestamp': '2023-10-01T08:02:15', 'event_type': 'network', 'severity': 'WARN', 'details': 'High latency detected'},
    {'timestamp': '2023-10-01T08:04:30', 'event_type': 'auth', 'severity': 'ERROR', 'details': 'Failed login'},
    {'timestamp': '2023-10-01T08:06:45', 'event_type': 'system', 'severity': 'CRITICAL', 'details': 'Disk failure imminent'},
    {'timestamp': '2023-10-01T08:09:00', 'event_type': 'network', 'severity': 'ERROR', 'details': 'Packet loss'},
    {'timestamp': '2023-10-01T08:11:15', 'event_type': 'auth', 'severity': 'ERROR', 'details': 'Failed login'},
    {'timestamp': '2023-10-01T08:13:30', 'event_type': 'backup', 'severity': 'INFO', 'details': 'Scheduled backup started'},
    {'timestamp': '2023-10-01T08:15:45', 'event_type': 'system', 'severity': 'WARN', 'details': 'Memory pressure'}
]

system_threshold = 85

final_capacity = calculate_remaining_capacity(log_entries, system_threshold)
print(f"Target result: {final_capacity}")