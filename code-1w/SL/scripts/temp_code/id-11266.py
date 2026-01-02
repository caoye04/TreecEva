from collections import defaultdict

# Simulate system diagnostics with performance metrics
def analyze_system_logs(log_entries):
    severity_count = defaultdict(int)
    error_locations = []
    total_chars = 0

    for entry in log_entries:
        total_chars += len(entry)
        if 'ERROR' in entry:
            severity_count['critical'] += 1
            location = entry.split(' ')[0]
            error_locations.append(location)
        elif 'WARNING' in entry:
            severity_count['warning'] += 1
        elif 'INFO' in entry:
            severity_count['info'] += 1

    # Distractor: unused computation
    avg_length = total_chars / len(log_entries) if log_entries else 0
    redundant_sum = sum(len(loc) for loc in error_locations)

    efficiency = len(log_entries) - severity_count['critical'] * 2
    raw_errors = severity_count['critical']
    raw_warnings = severity_count['warning']

    # Intermediate transformation with red herring variables
    temp_factor = 1.5 if avg_length > 50 else 1.0
    adjustment = (redundant_sum // 10) if redundant_sum > 0 else 0  # Not actually used later

    # Key logic chain
    base_score = efficiency * 10
    penalty = (raw_errors * 7) + (raw_warnings * 3)
    bonus = 20 if severity_count['info'] > 5 else 5

    final_score = evaluate_performance(efficiency, raw_errors, raw_warnings)

    return final_score


def evaluate_performance(efficiency, errors, warnings):
    # Core scoring formula
    score = efficiency * 8
    if errors == 0:
        score += 25
    elif errors >= 3:
        score -= 20
    
    if warnings < 2:
        score += 10
    
    # Complex condition with short-circuiting
    debug_mode = False
    extra_diagnostic = (errors > 0) and debug_mode and (warnings % 2 == 0)
    
    # Final adjustment
    multiplier = 1.1 if (efficiency >= 10 and warnings == 0) else 1.0
    score = round(score * multiplier)
    
    return score

# Simulated input data
logs = [
    "SRV1 ERROR disk failure detected",
    "NET2 WARNING high latency observed",
    "DB3 INFO connection pool initialized",
    "API4 INFO request throughput normal",
    "SRV1 ERROR memory overflow",
    "SEC5 WARNING unauthorized access attempt",
    "DB3 INFO backup completed successfully",
    "MON6 INFO system health check passed",
    "NET2 WARNING retry limit exceeded",
    "API4 INFO new session established"
]

# Execute main analysis
result = analyze_system_logs(logs)
final_score = result
print(f"Result: {final_score}")