def analyze_system_logs():
    # Simulated system diagnostic data
    raw_entries = ['ERROR', 'WARNING', 'INFO', 'ERROR', 'DEBUG', 'ERROR', 'WARNING']
    severity_map = {'ERROR': 3, 'WARNING': 2, 'INFO': 1, 'DEBUG': 0}
    
    # Data transformation and filtering
    filtered_entries = [entry for entry in raw_entries if entry in ['ERROR', 'WARNING']]
    entry_counts = {}
    for entry in filtered_entries:
        entry_counts[entry] = entry_counts.get(entry, 0) + 1

    # Misleading computation: frequency analysis not used in final result
    total_warnings = entry_counts.get('WARNING', 0)
    total_errors = entry_counts.get('ERROR', 0)
    redundancy_check = total_warnings // max(1, total_errors) if total_errors > 0 else 0

    # Active logs: only errors are considered critical
    active_logs = [level for level in raw_entries if level == 'ERROR']
    base_score = len(active_logs) * severity_map['ERROR']

    # Auxiliary state tracking (some irrelevant)
    system_state = {"active": True, "mode": "diagnostic", "version": "2.1.5"}
    temp_flags = set()
    for i in range(len(raw_entries)):
        if i % 3 == 0:
            temp_flags.add(f'flag_{i}')
    flag_count = len(temp_flags)  # Unused variable (distraction)

    # Conditional correction factor based on pattern
    unique_severities = set(severity_map.keys())
    high_severity_present = 'ERROR' in unique_severities
    medium_severity_present = 'WARNING' in unique_severities
    
    if high_severity_present and not medium_severity_present:
        correction_factor = 5
    elif high_severity_present and medium_severity_present:
        correction_factor = 3
    else:
        correction_factor = 0

    # Key statement
    final_diagnostic = base_score + len(active_logs) * correction_factor
    
    # Print result for evaluation
    print(f"Result: {final_diagnostic}")

analyze_system_logs()