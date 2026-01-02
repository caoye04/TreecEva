def analyze_system_logs(log_entries):
    critical_keywords = {'error', 'failure', 'critical', 'timeout'}
    warning_keywords = {'warn', 'retry', 'degraded'}

    log_summary = []
    severity_tally = {"CRITICAL": 0, "WARNING": 0, "INFO": 0}

    for entry in log_entries:
        entry_lower = entry.lower()
        if any(kw in entry_lower for kw in critical_keywords):
            severity_tally["CRITICAL"] += 1
            log_summary.append("CRIT: " + entry[:60])
        elif any(kw in entry_lower for kw in warning_keywords):
            severity_tally["WARNING"] += 1
            log_summary.append("WARN: " + entry[:60])
        else:
            severity_tally["INFO"] += 1

    active_alerts = set()
    for key, count in severity_tally.items():
        if count > 1 and key != "INFO":
            active_alerts.add(key)

    concatenated_logs = " ".join(log_entries)
    word_tokens = concatenated_logs.split()
    unique_words = set(word.strip('.,') for word in word_tokens)

    suspicious_patterns = {word for word in unique_words if word.isalpha() and len(word) >= 8 and word.islower()}
    filtered_logs = [word for word in suspicious_patterns if word.startswith('over') or word.endswith('ing')]

    filtration_score = len(filtered_logs)
    return filtration_score

log_input = [
    "System error detected in module XYZ",
    "Network timeout observed during data transfer",
    "Performance degradation in overheat protection circuit",
    "User session expired due to inactivity",
    "Critical failure in main power supply",
    "Background process handling large data streaming"
]

result = analyze_system_logs(log_input)
print(f"Result: {result}")