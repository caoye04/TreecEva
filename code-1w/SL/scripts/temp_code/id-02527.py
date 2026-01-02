def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = sum(1 for log in logs if 'ERROR' not in log)
    error_rate = (total_entries - valid_count) / total_entries if total_entries > 0 else 0
    return error_rate

logs_data = [
    'INFO: system online',
    'DEBUG: memory allocation',
    'ERROR: disk failure',
    'WARNING: high load',
    'INFO: user login',
    'ERROR: timeout exceeded',
    'INFO: backup started'
]

# Misleading preprocessing
formatted_logs = [log.upper().replace(':', ';') for log in logs_data]
dummy_analysis = list(map(lambda x: x.split(' ')[0], formatted_logs))
status_counts = {key: dummy_analysis.count(key) for key in set(dummy_analysis)}

error_rate = analyze_efficiency(logs_data)
productivity = 85.0
risk_factor = 1.0 if error_rate > 0.25 else 0.8

# Simulate performance scoring with red herring variables
temp_weights = [0.7, 0.9, 1.1]  # unused but plausible distraction
calibration_offset = sum([i * 0.1 for i in range(len(temp_weights))])  # irrelevant calc

stability_bonus = 5 if all('INFO' in log for log in logs_data[:3]) else 0  # semi-relevant

# Core logic hidden among distractions
def evaluate_performance(efficiency, risk):
    base_score = efficiency * 10
    adjusted = base_score / risk
    if adjusted > 90:
        adjusted -= 10
    elif adjusted < 70:
        adjusted += 5
    return int(adjusted + stability_bonus)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")