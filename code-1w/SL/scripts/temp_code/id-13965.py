def evaluate_performance(log_entries, baseline):
    total_events = len(log_entries)
    critical_count = 0
    warning_count = 0
    efficiency_ratio = 0.0
    
    # Irrelevant preprocessing: reverse and slice (distractor)
    reversed_logs = log_entries[::-1]
    mid_section = reversed_logs[len(reversed_logs)//4 : 3*len(reversed_logs)//4]
    
    temp_sum = 0
    for entry in log_entries:
        level = entry['level']
        code = entry['code']
        
        # Real logic: count critical events
        if level == 'CRITICAL':
            critical_count += 1
            temp_sum += code % 7
        elif level == 'WARNING':
            warning_count += 1
            temp_sum += code % 3
    
    # Distractor computation: unused efficiency metric
    if total_events > 0:
        efficiency_ratio = (warning_count + 0.5 * critical_count) / total_events
    
    # Simulate data smoothing (irrelevant)
    smoothed_values = []
    for i in range(len(log_entries)):
        window = log_entries[max(0, i-1):i+2]
        avg_code = sum(e['code'] for e in window) / len(window)
        smoothed_values.append(avg_code)
    
    # Core logic: baseline adjustment with conditional override
    adjusted_base = baseline
    if critical_count >= 3:
        adjusted_base *= 0.8
    elif warning_count > 5:
        adjusted_base *= 0.9
    else:
        adjusted_base *= 1.1
    
    # Final score depends only on critical_count and baseline
    anomaly_penalty = critical_count * 15
    final_score = int(adjusted_base - anomaly_penalty)
    
    # Dead code path (never reached due to logic above)
    if efficiency_ratio > 1.0:
        final_score += 100  # unreachable
    
    return final_score

# Simulated system log data
log_data = [
    {'timestamp': '10:01', 'level': 'INFO', 'code': 201},
    {'timestamp': '10:02', 'level': 'WARNING', 'code': 305},
    {'timestamp': '10:03', 'level': 'CRITICAL', 'code': 502},
    {'timestamp': '10:04', 'level': 'DEBUG', 'code': 100},
    {'timestamp': '10:05', 'level': 'WARNING', 'code': 307},
    {'timestamp': '10:06', 'level': 'CRITICAL', 'code': 503},
    {'timestamp': '10:07', 'level': 'WARNING', 'code': 301},
    {'timestamp': '10:08', 'level': 'CRITICAL', 'code': 505},
    {'timestamp': '10:09', 'level': 'WARNING', 'code': 309},
    {'timestamp': '10:10', 'level': 'WARNING', 'code': 310}
]

baseline_value = 150

# Key execution point
final_score = evaluate_performance(log_data, baseline_value)
print(f"Target result: {final_score}")