def process_telemetry_data(log_entries):
    # Irrelevant preprocessing: case normalization and filtering
    normalized_logs = [entry.lower().strip() for entry in log_entries if 'debug' not in entry]
    error_count = sum(1 for log in normalized_logs if 'error' in log)
    warning_count = sum(1 for log in normalized_logs if 'warn' in log)
    
    # Misleading transformation chain
    temp_analysis = {}
    for i, log in enumerate(normalized_logs):
        if i % 3 == 0:
            temp_analysis[f'snap_{i}'] = len(log) ^ 255
    
    # Decoy statistical summary (never used later)
    stats_summary = {
        'total_entries': len(log_entries),
        'cleaned_size': len(normalized_logs),
        'error_to_warning_ratio': warning_count / (error_count + 1),
        'entropy_metric': error_count * 0.7 + warning_count * 0.3
    }

    # Actual relevant logic buried within
    critical_codes = [int(log.split()[0]) for log in log_entries if log[0].isdigit()]
    severity_score = sum(code for code in critical_codes if code > 500)
    return severity_score

# Simulated system flag processor with red herring paths
def evaluate_flag_consistency(flags):
    flag_integrity = {}
    for key, value in flags.items():
        if isinstance(value, str):
            flag_integrity[key] = value.upper().replace('_', '')
        else:
            flag_integrity[key] = value ^ 15
    
    # Dead path: complex but unused bitwise cascade
    mask = 0xFFFF
    for val in flag_integrity.values():
        if isinstance(val, int):
            mask &= (val ^ (val << 1)) & 0xFFFF
    
    # Relevant computation disguised as secondary
    active_alerts = sum(1 for v in flags.values() if v in ['ACTIVE', True, 1])
    return active_alerts

# Core analysis function with layered distractions
def analyze_system_state(logs, flags):
    # Distractor: string manipulation on log metadata
    log_headers = [log.split('|')[0].strip() for log in logs if '|' in log]
    header_lengths = {h: len(h) for h in log_headers}
    
    # Red herring: unused cryptographic-style hash
    pseudo_hash = 0
    for h in log_headers:
        xor_val = 0
        for char in h:
            xor_val ^= ord(char)
        pseudo_hash += xor_val * 17
    pseudo_hash = (pseudo_hash ^ 98765) % 10000
    
    # Key data extraction buried in middle
    raw_diagnostics = []
    for log in logs:
        parts = log.split()
        if len(parts) > 2 and parts[1].isdigit():
            raw_diagnostics.append(int(parts[1]))
    
    # Another decoy structure
    diagnostic_tree = {}
    for i, val in enumerate(raw_diagnostics):
        bin_key = f'{(i ^ val) & 0xFF:08b}'
        diagnostic_tree[bin_key] = val * 2
    
    # Critical calculation obscured by context
    base_metric = sum(d for d in raw_diagnostics if d % 4 == 0)
    flag_contribution = evaluate_flag_consistency(flags) * 100
    adjustment_factor = len([d for d in raw_diagnostics if d > 200])
    
    # Final synthesis with misleading intermediate names
    preliminary_diag = base_metric + flag_contribution
    refinement_offset = adjustment_factor * 17
    final_diagnostic = preliminary_diag - refinement_offset
    
    # Output required variable
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data with mixed relevance
operational_logs = [
    "503|SYS ERR 1024", "INFO 200 status ok", "DEBUG 150 ignored",
    "WARNING 305 threshold exceeded", "404|NET FAIL 800", 
    "error 100 retry", "CRITICAL 600 breach", "debug skip this"
]

system_flags = {
    'power': True,
    'network': 'ACTIVE',
    'thermal': 'STANDBY',
    'storage': 1,
    'cache': 0,
    'security': 'INACTIVE'
}

# Entry point
final_diagnostic = analyze_system_state(operational_logs, system_flags)