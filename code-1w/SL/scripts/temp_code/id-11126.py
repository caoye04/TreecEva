def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_logs = [entry for entry in logs if 'ERROR' not in entry]
    error_count = total_entries - len(valid_logs)
    
    # Irrelevant transformation
    reversed_logs = [log[::-1] for log in logs]
    palindrome_count = sum(1 for log in reversed_logs if log == log[::-1])

    return len(valid_logs), error_count

# Simulated system logs
timestamps = [1205, 1206, 1207, 1208, 1209, 1210, 1211]
raw_data = ['OK: task_1', 'ERROR: timeout', 'OK: task_3', 'OK: task_4', 'ERROR: io_fail', 'OK: task_6', 'OK: task_7']

# Extraneous processing
formatted_data = list(map(lambda x: f'[LOG] {x}', raw_data))
summary_stats = {"count": len(raw_data), "chars": sum(len(d) for d in raw_data)}

# Core metrics
good_ops, faults = analyze_efficiency(raw_data)
productivity = good_ops / len(raw_data)

# Secondary distraction: character frequency analysis
all_chars = ''.join(formatted_data)
char_freq = {c: all_chars.count(c) for c in set(all_chars) if c.isalpha()}
dominant_char = max(char_freq, key=lambda k: char_freq[k])

def evaluate_performance(efficiency, bugs):
    base_score = efficiency * 100
    penalty = 0
    
    if bugs > 0:
        penalty += bugs * 5.5
    if efficiency < 0.7:
        penalty += 10
    
    # Unused branch (dead code path)
    if False:
        adjustment = sum(1 for c in char_freq.keys() if c > 'm')
        base_score -= adjustment
        
    return round(base_score - penalty, 2)

# Misleading intermediate calculation
temp_diagnostic = sum(timestamps) + summary_stats["count"]

final_score = evaluate_performance(productivity, faults)
Result: {final_score}