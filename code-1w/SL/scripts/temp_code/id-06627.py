from itertools import compress

def evaluate_performance(output, risk):
    baseline = 75
    if output > 80:
        adjustment = 12.5
    elif output > 60:
        adjustment = 5.0
    else:
        adjustment = -10.0
    
    # Apply risk penalty
    risk_penalty = -5 if risk else 0
    return baseline + adjustment + risk_penalty

# Simulate employee metrics
tasks_completed = [8, 5, 7, 9, 6]
days_active = 5
avg_tasks_per_day = sum(tasks_completed) / days_active

productivity = avg_tasks_per_day * 10
is_high_risk = False

# Irrelevant string processing (minor distraction)
status_label = "PERFORMANCE: ACTIVE"
status_clean = status_label.lower().replace(':', '').split()[1]

final_score = evaluate_performance(productivity, is_high_risk)
print(f"Target result: {final_score}")