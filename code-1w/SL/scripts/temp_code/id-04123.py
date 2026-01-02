def evaluate_performance(log_entries):
    total_score = 0
    warning_count = 0
    critical_flag = False

    for index, entry in enumerate(log_entries):
        if 'ERROR' in entry:
            warning_count += 1
            if 'CRITICAL' in entry:
                critical_flag = True

    status_codes = [200, 404, 500, 403]
    matched_pairs = list(zip(log_entries, status_codes))

    base_penalty = 0
    for log, code in matched_pairs:
        if code >= 400:
            base_penalty += 1

    if critical_flag:
        penalty_adjustment = warning_count * -10
    else:
        penalty_adjustment = warning_count * -5

    total_score += penalty_adjustment
    total_score += len(log_entries) * 2

    # Irrelevant string operation (minimal distraction)
    summary = "Summary: " + " | ".join([e.split()[0] for e in log_entries if e])

    print(f"Result: {total_score}")

# Input data
logs = [
    "INFO System started",
    "WARNING Disk usage high",
    "ERROR CRITICAL Database failure",
    "ERROR File not found"
]

evaluate_performance(logs)