def process_diagnostics(raw_data, config):
    # Irrelevant preprocessing block (distractor)
    sanitized = [x.strip() for x in raw_data if x != '']
    filtered = [s.lower() for s in sanitized if s.isalpha()]
    lookup_table = {chr(i): i - 97 for i in range(97, 123)}
    entropy_score = sum([lookup_table[c] for c in filtered if c in lookup_table])

    # Core timing analysis (relevant)
    timing_log = []
    errors_occurred = set()
    recovery_attempts = 0

    for entry in raw_data:
        if not entry:
            continue
        
        # Parse timestamp and status
        parts = entry.split('|')
        if len(parts) < 3:
            errors_occurred.add('malformed_entry')
            continue
        
        timestamp_str = parts[0].strip()
        module_id = parts[1].strip()
        status_flag = parts[2].strip()
        
        # Extract numeric time using string slicing
        if len(timestamp_str) >= 6:
            try:
                seconds = int(timestamp_str[-6:-3])
                millis = int(timestamp_str[-3:])
                total_ms = seconds * 1000 + millis
                timing_log.append((module_id, total_ms, status_flag))
            except ValueError:
                errors_occurred.add('timestamp_parse')
        else:
            errors_occurred.add('invalid_timestamp')

        # Simulated recovery logic (partially relevant)
        if status_flag == 'ERR':
            recovery_attempts += 1
            if recovery_attempts > config.get('max_retries', 3):
                break  # Early termination condition

    # Decoy data transformation (irrelevant)
    decoy_map = {i: (i ** 2) % 19 for i in range(15)}
    shadow_accum = 0
    for k, v in decoy_map.items():
        if v % 2 == 0:
            shadow_accum ^= k  # Bitwise red herring

    # Real aggregation function (nested)
    def aggregate_metrics(log, error_set):
        base_score = 1000
        penalty = 0
        
        # Analyze timing distribution
        times_only = [t[1] for t in log]
        if times_only:
            avg_time = sum(times_only) / len(times_only)
            base_score -= int(avg_time / 10)

        # Apply penalties based on error types
        critical_errors = {'malformed_entry', 'timestamp_parse'}
        if error_set & critical_errors:
            penalty += 150
        
        # Use set difference to compute non-critical issues
        non_critical_count = len(error_set - critical_errors)
        penalty += non_critical_count * 25
        
        # Bonus logic: perfect timing streak (conditional)
        success_times = [t[1] for t in log if t[2] == 'OK']
        if len(success_times) >= 3:
            sorted_streak = sorted(success_times[:3])
            if sorted_streak[2] - sorted_streak[0] <= 50:  # Within 50ms
                base_score += 75

        # Final adjustment using modular arithmetic
        adjusted = (base_score - penalty) % 8999
        return adjusted

    # Misleading alternate computation (dead path)
    if len(errors_occurred) == 0:
        dummy_result = sum([len(x) for x in filtered]) * 17
    else:
        temp_state = set(filtered)
        temp_state.add('degraded')

    # Key statement
    final_diagnostic = aggregate_metrics(timing_log, errors_occurred)
    
    # Output requirement
    print(f"Result: {final_diagnostic}")

# Input data with mixed validity
input_trace = [
    "123456|MOD_A|OK",
    "124012|MOD_B|ERR",  # Slightly longer
    "124045|MOD_A|OK",  # Close in time to previous
    "125100|MOD_C|OK",
    "|MOD_D|ERR",         # Malformed timestamp
    "126200|MOD_A|OK"
]

# Configuration
system_config = {"max_retries": 2}

# Execute
process_diagnostics(input_trace, system_config)