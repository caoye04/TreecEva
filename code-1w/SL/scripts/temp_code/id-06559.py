from collections import Counter

def analyze_threats(log_entries):
    threat_levels = []n    for entry in log_entries:
        if 'ERROR' in entry:
            threat_levels.append('high')
        elif 'WARNING' in entry:
            threat_levels.append('medium')
        elif 'INFO' in entry:
            threat_levels.append('low')
    return Counter(threat_levels)

def evaluate_performance(defense_log, attack_count):
    counts = analyze_threats(defense_log)
    base_score = 100
    base_score -= counts['high'] * 5
    base_score -= counts['medium'] * 2
    adjustment = 10 if attack_count > 20 else 5
    final_score = base_score + adjustment
    return final_score

defense_log = [
    'INFO: System boot',
    'WARNING: High memory usage',
    'ERROR: Failed login attempt',
    'WARNING: Disk space low',
    'ERROR: Timeout on service',
    'INFO: User logout'
]
attack_count = 25

final_score = evaluate_performance(defense_log, attack_count)
print(f"Result: {final_score}")