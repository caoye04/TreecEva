from collections import Counter
def analyze_pattern(sequence):
    count = Counter(sequence)
    modes = [k for k, v in count.items() if v == max(count.values())]
    return modes[0] if len(modes) == 1 else -1

def compute_efficiency(logs):
    total_entries = len(logs)
    valid_entries = sum(1 for log in logs if 'ERROR' not in log)
    redundancy_count = sum(log.count('retry') for log in logs)
    adjusted = valid_entries - redundancy_count // 2
    efficiency = adjusted / total_entries if total_entries > 0 else 0
    return efficiency

def detect_anomalies(logs):
    error_lines = [i for i, log in enumerate(logs) if 'CRITICAL' in log]
    severity_scores = []
    for line in logs:
        score = 0
        if 'WARNING' in line:
            score += 1
        if 'ERROR' in line:
            score += 2
        if 'CRITICAL' in line:
            score += 5
        severity_scores.append(score)
    avg_severity = sum(severity_scores) / len(severity_scores) if severity_scores else 0
    return len(error_lines), avg_severity

def evaluate_performance(efficiency, errors):
    base = efficiency * 100
    penalty = errors * 2.5
    final_score = base - penalty
    if final_score < 0:
        final_score = 0
    return int(final_score)

def main():
    system_logs = [
        'INFO: system startup',
        'INFO: user login',
        'WARNING: disk usage high',
        'INFO: retry connection',
        'ERROR: database timeout',
        'INFO: retry connection',
        'INFO: data sync complete',
        'CRITICAL: authentication failure',
        'WARNING: network latency',
        'INFO: session refresh'
    ]
    
    # Irrelevant pattern analysis (distractor)
    action_sequence = ['login', 'sync', 'refresh', 'login', 'login', 'sync']
    dominant_action = analyze_pattern(action_sequence)
    
    # Core metrics
    efficiency = compute_efficiency(system_logs)
    error_count, avg_severity = detect_anomalies(system_logs)
    
    # Misleading intermediate calculation (semi-relevant)
    log_summary = ''.join(system_logs)
    retry_count = log_summary.count('retry')
    warning_ratio = log_summary.count('WARNING') / len(log_summary)
    
    # Key execution point
    final_score = evaluate_performance(efficiency, error_count)
    
    # Additional red herring
    metadata = {'version': '2.1', 'mode': 'debug'}
    temp_result = [x for x in range(len(system_logs)) if 'INFO' in system_logs[x]]
    
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()