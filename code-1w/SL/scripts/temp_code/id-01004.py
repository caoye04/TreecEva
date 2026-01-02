def analyze_efficiency(metrics):
    if not metrics:
        return 0
    avg = sum(metrics) / len(metrics)
    variance = sum((x - avg) ** 2 for x in metrics) / len(metrics)
    efficiency = avg / (1 + variance) if variance > 0 else avg
    return round(efficiency, 3)

productivity = [85, 90, 78, 92, 88]
risk_events = ['minor', 'none', 'critical', 'none', 'minor']
base_weights = {'minor': 1, 'critical': 3, 'none': 0}

# Distractor: irrelevant string processing
log_entry = "ERROR: system_failure_45"
tokens = log_entry.lower().split('_')
error_code = ''.join([t[0] for t in tokens if t.isalpha()])

# Misleading intermediate calculation
phantom_risk = sum(1 for e in risk_events if e == 'critical') * 100

# Actual risk factor computation
temp_risk = sum(base_weights[e] for e in risk_events)
risk_factor = 1 + (temp_risk / len(risk_events))

# Simulated performance model
scaling_factor = 2.5 if risk_factor < 3 else 1.8
adjusted_productivity = [val * scaling_factor for val in productivity]

# Red herring: unused helper function
def calculate_stress_level(events):
    return len([e for e in events if e != 'none']) ** 2

# Conditional expression and string method distraction
critical_flag = 'CRITICAL' in log_entry.upper()
status_label = 'active' if critical_flag else 'normal'
status_weight = len(status_label.replace('a', ''))

# Key computational chain
efficiency_rating = analyze_efficiency(adjusted_productivity)
penalty_rate = 0.1 if risk_factor > 2 else 0.05
raw_score = efficiency_rating * (1 - penalty_rate)

# Final evaluation with conditional logic
baseline = 75.0 if 'critical' in risk_events else 80.0
final_score = raw_score if raw_score > baseline else baseline

# Output required format
print(f"Result: {final_score}")