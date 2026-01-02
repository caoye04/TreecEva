def analyze_system_health():
    # Simulated system log entries with timestamps and status codes
    raw_logs = [
        (1623456780, 'INFO', 'service_a', 200),
        (1623456789, 'WARN', 'service_b', 404),
        (1623456795, 'ERROR', 'service_c', 500),
        (1623456801, 'INFO', 'service_a', 200),
        (1623456810, 'WARN', 'service_b', 403),
        (1623456815, 'ERROR', 'service_c', 500),
        (1623456820, 'INFO', 'service_d', 200)
    ]

    # Irrelevant transformation: convert to strings for no reason
    string_logs = [f'{t}:{lvl}:{srv}:{code}' for t, lvl, srv, code in raw_logs]
    joined_log = '|'.join(string_logs)
    split_back = joined_log.split('|')

    # Extract only relevant fields (timestamp, level, service, code)
    log_entries = []
    for entry in split_back:
        parts = entry.split(':')
        timestamp = int(parts[0])
        level = parts[1]
        service = parts[2]
        code = int(parts[3])
        log_entries.append((timestamp, level, service, code))

    # System flags - some are relevant, most are red herrings
    system_flags = {
        'disk_usage_pct': 78,
        'cpu_temp_c': 65,
        'active_connections': 124,
        'memory_leak_detected': False,
        'redundant_flag_1': True,
        'legacy_mode_active': False,
        'maintenance_window': True,
        'redundant_flag_2': 'inactive',
        'security_audit_needed': True,
        'degraded_mode': False
    }

    # Decoy function that does nothing important
    def validate_checksum(data):
        checksum = 0
        for char in str(data):
            checksum += ord(char) % 7
        return checksum > 5  # Always true for most inputs

    # Another irrelevant utility
    def get_service_tiers():
        tiers = {'service_a': 'premium', 'service_b': 'standard', 'service_c': 'standard', 'service_d': 'basic'}
        tier_codes = {k: {'premium': 3, 'standard': 2, 'basic': 1}[v] for k, v in tiers.items()}
        return tier_codes  # Never actually used

    # Real processing begins here
    error_count = 0
    warning_count = 0
    service_errors = {}
    recent_errors = []

    for ts, level, service, code in log_entries:
        if level == 'ERROR':
            error_count += 1
            service_errors[service] = service_errors.get(service, 0) + 1
            recent_errors.append(code)
        elif level == 'WARN':
            warning_count += 1

    # Compute derived metrics (some used, some not)
    total_events = len(log_entries)
    error_rate = error_count / total_events if total_events else 0
    warning_rate = warning_count / total_events if total_events else 0

    # Unused complex data structure transformation
    indexed_logs = list(enumerate(log_entries))
    zipped_pairs = list(zip([x[0] for x in indexed_logs], [x[1][2] for x in indexed_logs]))
    service_sequence = [s for _, s in zipped_pairs]
    unique_services = set(service_sequence)
    service_transition_count = sum(1 for i in range(1, len(service_sequence)) if service_sequence[i] != service_sequence[i-1])

    # Bit manipulation red herring
    flag_signature = 0
    for flag_value in system_flags.values():
        if isinstance(flag_value, bool):
            flag_signature ^= hash(str(flag_value))
    flag_signature &= 0xFFFF  # Keep within 16 bits

    # String-based decoy analysis
    log_text = ''.join([level.lower() for _, level, _, _ in log_entries])
    suspicious_patterns = log_text.count('err') + log_text.count('warn')
    pattern_score = len(log_text) - suspicious_patterns

    # Real diagnostic logic buried among distractions
    base_score = 100
    if error_count > 2:
        base_score -= 30
    elif error_count > 0:
        base_score -= 15

    if warning_count > 3:
        base_score -= 10

    if system_flags['degraded_mode']:
        base_score -= 25

    if system_flags['maintenance_window']:
        base_score += 10  # Offset some penalty

    # Critical adjustment based on specific error recurrence
    critical_services_down = sum(1 for svc, cnt in service_errors.items() if cnt >= 2 and svc in ['service_c', 'service_a'])
    base_score -= critical_services_down * 12

    # Final heuristic: if same error repeats consecutively
    consecutive_critical = 0
    for i in range(1, len(recent_errors)):
        if recent_errors[i] == recent_errors[i-1] == 500:
            consecutive_critical += 1

    if consecutive_critical >= 1:
        base_score -= 8

    final_diagnostic = base_score

    # Dead code path - never reached due to logic above
    if final_diagnostic < 0 and system_flags['legacy_mode_active']:
        backup_diagnostic = sum(hash(str(v)) for v in system_flags.values()) % 100
        final_diagnostic = (final_diagnostic + backup_diagnostic) // 2

    # Print result as required
    print(f"Result: {final_diagnostic}")

analyze_system_health()