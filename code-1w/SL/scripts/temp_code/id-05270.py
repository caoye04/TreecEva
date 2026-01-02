def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = sum(1 for log in logs if 'ERROR' not in log)
    error_rate = (total_entries - valid_count) / total_entries if total_entries > 0 else 0
    return error_rate

logs = [
    'INFO: system online',
    'DEBUG: module initialized',
    'ERROR: disk full',
    'WARNING: high memory usage',
    'INFO: user login',
    'ERROR: timeout exceeded'
]

error_profile = analyze_efficiency(logs)
dummy_metric = sum(ord(c) for c in 'placeholder') % 100

# Simulate team productivity metrics over 5 days
daily_output = [45, 52, 38, 61, 55]
baseline = 50
productivity = sum(max(0, day - baseline) for day in daily_output)
penalties = sum(abs(day - baseline) for day in daily_output if day < baseline)
efficiency_ratio = productivity / (penalties + 1)

# Risk assessment based on error rate and string patterns
critical_keywords = ['ERROR', 'FAILURE', 'CRITICAL']
flagged_logs = [log for log in logs if any(kw in log for kw in critical_keywords)]
alert_count = len(flagged_logs)
risk_factor = alert_count * (error_profile + 0.1)

# Distractor: unused complex calculation
temp_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
weighted_risk = sum(risk_factor * w for w in temp_weights[:3])  # Partial use only

# Core evaluation logic
def evaluate_performance(output, risk):
    base_score = output * 10
    adjustment = 50 * (1 - risk / 10)
    bonus = 10 if output > 40 else 0
    # Conditional expression with string method side-condition
    extra = 15 if ''.join(flagged_logs).upper().count('DISK') > 0 else 5
    return base_score + adjustment + bonus + extra

intermediate_result = evaluate_performance(productivity, 0)  # Red herring call
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")