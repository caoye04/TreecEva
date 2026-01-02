def analyze_sensor_data(log_stream: str) -> int:
    # Simulated sensor data analysis with embedded diagnostics
    tokens = log_stream.split('|')
    
    # Irrelevant transformation chain (distractor)
    temp_buffer = [t.strip().upper() for t in tokens if len(t) > 3]
    filtered = list(filter(lambda x: 'ERR' not in x, temp_buffer))
    shadow_count = len(filtered) * 2

    # Critical diagnostic variables
    error_flags = []
    checksum = 0
    phase_state = {'active': False, 'cycle': 0}

    for entry in tokens:
        cleaned = entry.strip()
        if not cleaned:
            continue

        # Parse timestamp and code (format: T123:C45)
        if ':' in cleaned:
            timestamp_part, code_part = cleaned.split(':', 1)
            
            # Extract numeric parts
            time_val = int(timestamp_part[1:]) if timestamp_part.startswith('T') else 0
            code_val = int(code_part[1:]) if code_part.startswith('C') else 0

            # Misleading intermediate calculation (red herring)
            dummy_metric = (time_val ^ 7) % 100
            if dummy_metric > 50:
                phase_state['cycle'] += 1

            # Real logic: collect error codes starting with C and odd values
            if code_part.startswith('C') and code_val % 2 == 1:
                error_flags.append(code_val)
                checksum ^= code_val  # Bitwise accumulation

            # Dead branch: never executed due to condition mismatch (distractor)
            if 'DEBUG' in cleaned and phase_state['active']:
                shadow_count -= 1

    # Secondary processing on flags
    unique_errors = list(set(error_flags))
    sorted_errors = sorted(unique_errors, reverse=True)

    # String-based filtering using meaningful but distracting method
    error_names = [f'ERR{code}' for code in sorted_errors]
    valid_name_count = sum(1 for name in error_names if name.endswith('1'))

    # Decoy aggregation (looks important but unused in final result)
    decoy_aggregate = 0
    for i, err in enumerate(sorted_errors):
        decoy_aggregate += err * (i + 1)
    decoy_aggregate = decoy_aggregate % 999

    # Core answer computation — only this matters
    base_score = sum(sorted_errors)
    adjustment = len(sorted_errors) << 2  # Multiply by 4 using bit shift
    final_diagnostic = base_score - adjustment + checksum

    # Print required output
    return final_diagnostic

# Simulated input with mixed signal and noise
log_input = 'T100:C10|T105:C7|T110:C13|T115:C7|T120:C19|T125:INFO|T130:C21'
result = analyze_sensor_data(log_input)
print(f"Result: {result}")