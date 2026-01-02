def analyze_system_logs(log_entries):
    # Preprocess logs: extract numeric codes and flag anomalies
    event_codes = [int(entry.split()[0]) for entry in log_entries if entry.strip()]
    severity_levels = {code: (code // 100) for code in event_codes}
    anomalies = [code for code in event_codes if severity_levels[code] >= 4]

    # Distractor: irrelevant timestamp analysis
    timestamps = [entry.split(',')[1] for entry in log_entries if ',' in entry]
    total_time_span = len(timestamps) * 1.5 if timestamps else 0
    avg_interval = total_time_span / (len(timestamps) - 1) if len(timestamps) > 1 else 0

    # Baseline metrics computation (semi-relevant)
    base_count = len(event_codes)
    base_sum = sum(severity_levels.values())
    baseline_metrics = {
        'count': base_count,
        'average_severity': base_sum / base_count if base_count else 0,
        'peak': max(severity_levels.keys()) if severity_levels else 0
    }

    # Red herring: unused function definition
    compute_hash = lambda x: sum(ord(c) for c in str(x)) % 1000

    # Key logic: performance evaluator using lambda and filtering
    evaluate_performance = lambda anomalies, base: (
        sum(anomalies) - base['count'] * 2 + int(base['average_severity'] * 10)
    ) if anomalies else -1

    final_score = evaluate_performance(anomalies, baseline_metrics)
    
    # Superfluous state tracking
    status_log = []
    if final_score > 0:
        status_log.append('ELEVATED')
    elif final_score == -1:
        status_log.append('NO_ANOMALIES')
    else:
        status_log.append('CRITICAL')

    # Irrelevant string transformation chain
    debug_info = ''.join([chr(97 + (code % 26)) for code in event_codes[:5]]) if event_codes else ''
    
    return final_score

# Input data
logs = [
    "503 error occurred at 14:22,14:22:01",
    "404 resource not found,14:22:05",
    "200 OK,14:22:10",
    "500 server crash,14:22:15",
    "301 redirect,14:22:20"
]

result = analyze_system_logs(logs)
print(f"Result: {result}")