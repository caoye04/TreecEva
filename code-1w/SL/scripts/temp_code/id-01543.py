def analyze_fault_sequence(log_entries, profile):
    # Irrelevant transformation: frequency analysis of codes (unused)
    code_frequency = {}
    for entry in log_entries:
        code = entry.split('_')[0]
        code_frequency[code] = code_frequency.get(code, 0) + 1
    
    # Distractor: unused statistical summary
    avg_length = sum(len(e) for e in log_entries) / len(log_entries) if log_entries else 0
    max_code = max(code_frequency.keys()) if code_frequency else ''

    # Core logic begins: filter critical faults
    critical_prefixes = {'ERR', 'FTL', 'BRK'}
    critical_set = set()
    for entry in log_entries:
        prefix = entry.split('_')[0]
        if prefix in critical_prefixes:
            try:
                seq_id = int(entry.split('_')[1])
                critical_set.add(seq_id)
            except (IndexError, ValueError):
                continue

    # Secondary filter based on system profile
    allowed_range = profile.get('fault_tolerance_window', (0, 100))
    filtered_ids = {sid for sid in critical_set if allowed_range[0] <= sid < allowed_range[1]}

    # Red herring: complex bit manipulation on unused variable
    shift_accumulator = 0
    for x in code_frequency.values():
        if x > 1:
            shift_accumulator ^= (x << 2) | (x >> 1)
    
    # Decoy function definition (never called)
    def calculate_stability_score():
        return sum(1 for c in code_frequency if c.startswith('WARN')) * 0.5

    # Destructuring distraction
    config_backup = profile.get('backup_config', {})
    primary_node, secondary_node = config_backup.get('primary', 1), config_backup.get('secondary', 0)
    node_ratio = primary_node / (secondary_node + 1)

    # Real computation path
    base_score = 1000
    if 'critical_safety_lock' in profile and not profile['critical_safety_lock']:
        base_score += 50
    
    # Character counting in fault messages
    total_chars = sum(len(e) for e in log_entries)
    char_penalty = total_chars // 10

    # Conditional override simulation (unused)
    override_active = False
    for entry in log_entries:
        if 'OVR' in entry and '999' in entry:
            override_active = True
            break

    # Main score calculation
    anomaly_count = len([e for e in log_entries if e.startswith('FTL')])
    recovery_attempts = len([e for e in log_entries if 'RTRY' in e])
    
    intermediate = base_score - char_penalty
    intermediate += anomaly_count * 25
    intermediate -= recovery_attempts * 15

    # Set operations relevant to final result
    known_abnormal = {101, 102, 104, 107, 111}
    detected_critical = {sid for sid in filtered_ids if sid % 2 == 1}  # odd IDs are confirmed critical
    confirmed_threats = known_abnormal & detected_critical  # intersection is key

    threat_penalty = len(confirmed_threats) * 100
    final_diagnostic = intermediate - threat_penalty

    # Dead code path: never reached due to logic
    if final_diagnostic < 0 and profile.get('enable_cascade_failures', False):
        final_diagnostic = -999999

    return final_diagnostic

# Input data setup
fault_log = [
    'ERR_50', 'INFO_01', 'FTL_101', 'BRK_205', 'WARN_88',
    'FTL_102', 'ERR_51', 'BRK_107', 'RTRY_001', 'FTL_111',
    'OVR_999', 'SYS_777', 'BRK_104'
]
system_profile = {
    'version': '2.5.1',
    'fault_tolerance_window': (90, 200),
    'critical_safety_lock': False,
    'backup_config': {'primary': 3, 'secondary': 1},
    'enable_cascade_failures': False
}

# Execution point
final_diagnostic = analyze_fault_sequence(fault_log, system_profile)
print(f"Result: {final_diagnostic}")