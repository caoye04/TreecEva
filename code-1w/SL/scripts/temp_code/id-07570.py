def analyze_performance(logs):
    total_score = 0
    base_penalty = 10
    critical_errors = []
    
    for index, log in enumerate(logs):
        if 'ERROR' in log:
            error_count = log.count('ERROR')
            penalty_adjustment = base_penalty * error_count
            performance_multiplier = 1 if index < len(logs) // 2 else 0.5
            total_score += penalty_adjustment * performance_multiplier
            
            # Irrelevant tracking (minor distraction)
            timestamp = log.split()[0] if log.startswith('202') else 'unknown'
            
            if error_count > 2:
                critical_errors.append((index, error_count))
    
    # Additional irrelevant operation
    avg_critical = sum(e[1] for e in critical_errors) / len(critical_errors) if critical_errors else 0
    
    return total_score

# Simulated system logs
event_logs = [
    "2024-01-01 10:00:00 STATUS OK",
    "2024-01-01 10:05:00 ERROR NETWORK TIMEOUT",
    "2024-01-01 10:10:00 ERROR DISK ERROR DISK ERROR",
    "2024-01-01 10:15:00 ERROR MEMORY ERROR CRITICAL ERROR",
    "2024-01-01 10:20:00 STATUS OK"
]

result = analyze_performance(event_logs)
print(f"Result: {result}")