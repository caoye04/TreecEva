def analyze_system_performance(log_entries):
    # Irrelevant transformation - distractor
    normalized_logs = [entry.strip().lower() for entry in log_entries if len(entry) > 3]
    
    # Decoy variables and operations
    checksum = 0
    for entry in normalized_logs:
        checksum += len(entry)
    checksum = checksum % 7

    # Key data extraction (relevant)
    cycle_metrics = []
    for entry in log_entries:
        parts = entry.split(',')
        if len(parts) < 4:
            continue
        try:
            # Extract numeric cycle time (in ms), efficiency flag, and phase id
            cycle_time = float(parts[1])
            is_efficient = parts[2].strip() == 'True'
            phase_id = int(parts[3])
            
            # Irrelevant string processing - red herring
            status_code = ''.join([c for c in parts[0] if c.isalpha()])
            priority = len(status_code) % 3
            
            # Actual logic contribution: only high-phase, efficient cycles under 150ms counted
            if phase_id > 2 and is_efficient and cycle_time < 150.0:
                cycle_metrics.append(int(cycle_time))
            
            # Dead code path - looks important but unused
            if cycle_time > 200:
                fallback_rank = priority * 2
        except (ValueError, IndexError):
            continue
    
    # Another decoy: complex but unused calculation
    if cycle_metrics:
        average_metric = sum(cycle_metrics) / len(cycle_metrics)
        deviation = sum([(x - average_metric)**2 for x in cycle_metrics])
        stability_index = deviation / len(cycle_metrics) if deviation > 0 else 0
    
    # Filtering distraction: multiple conditions applied
    filtered_cycles = []
    for val in cycle_metrics:
        # Only include values with even digit sum (real filter)
        digit_sum = sum(int(d) for d in str(abs(val)))
        if digit_sum % 2 == 0:
            filtered_cycles.append(val)
    
    # Critical assignment point
    filtration_score = sum(filtered_cycles)
    
    # Final red herring: unrelated transformation
    summary_tag = ''.join([str(len(word)) for word in normalized_logs[:3]]) if normalized_logs else '0'
    
    return filtration_score

# Simulated input data - deterministic
log_data = [
    "ERR,125.0,True,3",
    "WARN,145.5,True,4",
    "INFO,110.0,False,5",
    "DEBUG,95.0,True,1",
    "CRIT,160.0,True,4",
    "TRACE,132.0,True,3",
    "ALERT,108.0,True,4"
]

result = analyze_system_performance(log_data)
print(f"Target result: {result}")