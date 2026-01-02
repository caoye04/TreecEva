def analyze_system_logs(log_entries):
    # Irrelevant transformation: case conversion and string filtering
    normalized_logs = [entry.lower().strip() for entry in log_entries if entry]
    debug_flags = set()
    error_threshold = 7
    aggregate_score = 0
    temp_buffer = []
    severity_map = {'low': 1, 'medium': 2, 'high': 3}
    
    # Misleading counting loop (dead logic - never used later)
    critical_count = 0
    for log in normalized_logs:
        if 'critical' in log:
            critical_count += 1

    # Actual processing begins here
    active_alerts = []
    for i, log in enumerate(normalized_logs):
        if 'error' in log and 'resolved' not in log:
            score = 0
            if 'timeout' in log:
                score += severity_map['high']
            elif 'retry' in log:
                score += severity_map['medium']
            else:
                score += severity_map['low']
            
            # Bit manipulation red herring
            encoded_index = i ^ 0xFF & 0x0F
            if encoded_index % 3 == 0:
                score = score << 1  # Double score (but only in temp)
            
            temp_buffer.append(score)  # Unused buffer
            active_alerts.append(log)
    
    # Real aggregation
    for val in temp_buffer:
        aggregate_score += val >> 1  # Undo the shift
    
    # Set operations: filter resolved issues
    all_ids = {f'alert_{i}' for i in range(len(log_entries))}
    resolved_ids = {f'alert_{i}' for i in range(0, len(log_entries), 3)}
    unresolved_ids = all_ids - resolved_ids
    
    # Decoy data structure
    system_state = {
        'status': 'nominal',
        'checksum': sum([len(x) for x in log_entries]) ^ 0xFFFF,
        'version': '2.1.5'
    }
    
    # Final computation with distractors
    remaining_alerts = []
    for alert in active_alerts:
        base_id = f"alert_{normalized_logs.index(alert) % len(log_entries)}"
        if base_id in unresolved_ids:
            remaining_alerts.append(alert)
    
    # Key statement
    final_diagnostic = aggregate_score + len(remaining_alerts)
    
    # Print result for verification
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
logs = [
    "ERROR: timeout in module_3",           # -> high=3, shifted to 6, then halved back to 3
    "retry limit reached",                  # -> medium=2, no shift (index 1)
    "Error resolved by auto-restart",       # ignored (resolved)
    "CRITICAL FAILURE: retry needed",      # -> medium=2, shifted to 4, then halved to 2
    "Network timeout detected"             # -> high=3, no shift (index 4)
]

result = analyze_system_logs(logs)