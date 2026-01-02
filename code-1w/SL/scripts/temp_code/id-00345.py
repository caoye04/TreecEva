def analyze_status(flags, log):
    # Core diagnostic logic
    severity_levels = {'critical': 3, 'warning': 2, 'info': 1}
    alert_count = {key: 0 for key in severity_levels.keys()}

    # Parse log entries and count severity
    for entry in log:
        if 'severity' in entry and entry['severity'] in alert_count:
            alert_count[entry['severity']] += 1

    base_score = (alert_count['critical'] * 5) + (alert_count['warning'] * 2) + alert_count['info']

    # Set operations to determine active modules
    expected_modules = {'power', 'network', 'storage', 'io', 'thermal'}
    active_modules = set()
    for flag in flags:
        if flag.startswith('mod_') and flag.endswith('_active'):
            module_name = flag[4:-7]
            active_modules.add(module_name)
    
    missing_modules = expected_modules - active_modules
    module_penalty = len(missing_modules) * 4

    # Bitwise health signature from flag states
    signature = 0
    for i, flag in enumerate(sorted(flags)):
        if 'error' in flag or 'failed' in flag:
            signature |= (1 << (i % 8))
    
    # Irrelevant cryptographic simulation (distractor)
    encryption_key = 0xABCDEF
    cipher_state = (signature ^ encryption_key) & 0xFFFF
    encoded_frame = ((cipher_state >> 8) | (cipher_state << 8)) & 0xFFFF  # byte swap
    # End of irrelevant crypto block

    # String-based configuration parser (partially relevant)
    config_blob = "HEALTH_THRESH=75; DEBUG_MODE=OFF; POLL_RATE=500"
    config_pairs = config_blob.split(';')
    config_map = {}
    for pair in config_pairs:
        if '=' in pair:
            k, v = pair.strip().split('=', 1)
            config_map[k] = v
    
    threshold_str = config_map.get('HEALTH_THRESH', '100')
    try:
        health_threshold = int(threshold_str)
    except ValueError:
        health_threshold = 90

    # Secondary diagnostic chain with dead code path
    temp_readings = [23.5, 25.1, 24.8, 26.0, 25.3]
    avg_temp = sum(temp_readings) / len(temp_readings)
    overheat_alert = False
    if avg_temp > 30:
        overheat_alert = True  # Dead code - never triggered
        base_score += 10

    # Data structure transformation (irrelevant)
    temp_stats = {
        'min': min(temp_readings),
        'max': max(temp_readings),
        'range': max(temp_readings) - min(temp_readings)
    }

    # Main score calculation
    raw_diagnostic = base_score - module_penalty
    
    # Conditional override based on critical failure presence
    if 'system_failed' in flags or alert_count['critical'] > 2:
        final_weight = 0.5
    else:
        final_weight = 1.2

    # Final computation
    intermediate = raw_diagnostic * final_weight
    
    # Red herring: unused normalization
    normalized = intermediate / (health_threshold + 1) if health_threshold != -1 else intermediate
    adjustment_factor = 1.0
    if 'debug_enabled' in flags:
        adjustment_factor = 0.8  # Unused branch
    
    final_diagnostic = int(intermediate + 0.5)  # Round to nearest integer
    
    # Spurious dictionary update (dead code)
    diagnostic_trace = {}
    diagnostic_trace['stage1'] = base_score
    diagnostic_trace['stage2'] = raw_diagnostic
    if False:  # Simulated dead path
        diagnostic_trace['adjusted'] = normalized
        diagnostic_trace['flags'] = flags

    return final_diagnostic

# Execution setup
operational_flags = [
    'mod_power_active',
    'mod_network_active',
    'mod_storage_active',
    'io_error_detected',           # contributes to signature
    'thermal_regulating',         # not an active module
    'backup_inactive'             # missing module
]

system_log = [
    {'event': 'disk_slow', 'severity': 'warning'},
    {'event': 'mem_leak', 'severity': 'critical'},
    {'event': 'ui_lag', 'severity': 'info'},
    {'event': 'disk_full', 'severity': 'critical'},
    {'event': 'reboot_ok', 'severity': 'info'}
]

# Trigger point
final_diagnostic = analyze_status(operational_flags, system_log)
print(f"Result: {final_diagnostic}")