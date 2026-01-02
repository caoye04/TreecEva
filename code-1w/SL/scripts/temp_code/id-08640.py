def analyze_system_load(raw_logs):
    # Irrelevant preprocessing: normalize log format (distractor)
    cleaned_logs = [entry.strip().lower() for entry in raw_logs if entry.strip()]
    debug_mode = len(cleaned_logs) > 5
    temp_flags = [1 if 'error' in entry else 0 for entry in cleaned_logs]
    error_count = sum(temp_flags)

    # Distractor: unused data transformation
    severity_map = {"info": 1, "warn": 2, "error": 3}
    severity_scores = [severity_map.get(entry.split()[0], 0) for entry in cleaned_logs if ' ' in entry]

    # Real computation begins: extract numeric load values
    loads = []
    for entry in raw_logs:
        words = entry.split()
        for word in words:
            if word.isdigit():
                loads.append(int(word))

    # Misleading intermediate: average without using it directly
    avg_load = sum(loads) / len(loads) if loads else 0
    peak_load = max(loads) if loads else 0

    # Red herring function definition (never called)
    def calculate_health_score(data):
        return sum([x ** 0.5 for x in data]) * 0.1

    # Another decoy: simulate historical comparison
    historical_baseline = [75, 80, 85, 90, 95]
    deviation = abs(avg_load - historical_baseline[-1]) if historical_baseline else 0

    # Core logic disguised among noise
    overload_events = [x for x in loads if x > 90]
    critical_count = len(overload_events)

    # Conditional expression with lambda abstraction (required feature)
    adjust_threshold = lambda x: x * 1.1 if debug_mode else x * 0.9
    dynamic_limit = adjust_threshold(90)

    # Key branching logic with string methods and case conversion (required features)
    filtered_actions = []
    for entry in raw_logs:
        action = entry.split(':')[-1].strip() if ':' in entry else ''
        if 'RESTART' in action.upper():
            filtered_actions.append(action.replace('RESTART', '').strip())

    # Actual decision logic buried here
    if critical_count > 2 and peak_load >= 100:
        status_code = 503
    elif critical_count == 0:
        status_code = 200
    else:
        status_code = 403

    # Final metric computation
    stability_ratio = (len(loads) - critical_count) / len(loads) if loads else 1
    normalized_ratio = round(stability_ratio * 100, 2)

    # Real answer path
    compliance_check = all(x <= dynamic_limit for x in loads)
    final_diagnostic = 0
    if status_code == 200:
        final_diagnostic = 987
    elif not compliance_check:
        final_diagnostic = -status_code * normalized_ratio  # Influenced by multiple factors
    else:
        final_diagnostic = int(normalized_ratio)

    # Dead code path (never reached due to above assignments)
    if final_diagnostic < 0:
        recovery_steps = ['isolate', 'diagnose', 'repair']
        final_diagnostic += len(recovery_steps) * 10

    return final_diagnostic


# Simulated input logs with mixed content
log_entries = [
    "INFO: System boot complete",
    "LOAD: 85",
    "WARN: High memory usage",
    "ERROR: Disk full at 95",
    "CRITICAL: CPU spike detected at 102",
    "ACTION: RESTART required immediately",
    "LOAD: 91",
    "LOAD: 101",
    "ERROR: Service timeout",
    "LOAD: 88"
]

system_threshold = 90

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_threshold) if 'process_metrics' in globals() else analyze_system_load(log_entries)

# Correction: fix undefined function name
final_diagnostic = analyze_system_load(log_entries)

print(f"Result: {final_diagnostic}")