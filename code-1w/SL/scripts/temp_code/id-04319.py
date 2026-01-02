def analyze_pattern(entries, flags):
    # Core analysis variables
    event_count = 0
    error_threshold = 3
    warning_sequence = []
    
    # Distractor: irrelevant timing simulation
    base_timing = 1.5
    jitter_factor = 0.12
    adjusted_timing = base_timing + jitter_factor * 2
    
    # Real logic begins: parse and filter log entries
    relevant_events = []
    for entry in entries:
        if 'ERROR' in entry:
            event_count += 1
            warning_sequence.append(entry.strip().count('!'))
        elif 'WARNING' in entry and 'disk' in entry.lower():
            relevant_events.append(entry)
    
    # Distractor: unused data structure manipulation
    temp_snapshot = tuple(reversed(warning_sequence))
    snapshot_sum = sum(temp_snapshot) if temp_snapshot else 0
    
    # State tracking with conditional escalation
    system_state = 'STABLE'
    if event_count >= error_threshold:
        system_state = 'CRITICAL'
    elif len(relevant_events) > 1:
        system_state = 'WARNING'
    
    # Use of string methods for pattern extraction
    critical_chars = ''.join([e.split()[-1] for e in entries if 'ERROR' in e])
    digit_filter = ''.join(filter(str.isdigit, critical_chars))
    
    # Distractor: dead computation path
    placeholder_score = 0
    for c in digit_filter:
        placeholder_score += int(c) * 2  # Not used later
    
    # Actual result derivation
    flag_sum = sum(flags)
    sequence_product = 1
    for val in warning_sequence:
        sequence_product *= (val + 1)  # Avoid zero multiplication
    
    # Final diagnostic calculation
    final_diagnostic = event_count * 10 + sequence_product + flag_sum
    
    # Distractor: meaningless formatting
    report_line = f"Diag={final_diagnostic:.2f}".replace('=', ':').upper()
    
    return final_diagnostic

# Input setup
log_entries = [
    "[ERR] Disk ERROR!!! Code 445",
    "INFO: System heartbeat",
    "ERROR: Memory overflow detected!!!",
    "WARNING: High disk latency observed",
    "ERROR: Timeout during write operation!"
]
system_flags = [1, 0, 1, 1]

# Execution point
final_diagnostic = analyze_pattern(log_entries, system_flags)
print(f"Result: {final_diagnostic}")