def evaluate_performance(log, metric):
    base_rating = 100
    adjustment = 0

    # Analyze defense log using lambda to filter critical events
    critical_events = list(filter(lambda x: x['severity'] > 7, log))
    if len(critical_events) == 0:
        adjustment += 15
    elif len(critical_events) < 3:
        adjustment += 5
    else:
        adjustment -= 10

    # Efficiency impacts score directly
    if metric > 0.85:
        adjustment += 20
    elif metric > 0.7:
        adjustment += 10
    else:
        adjustment -= 5

    # Simulate early return for high-risk case
    risk_count = sum(1 for event in log if event['type'] == 'breach')
    if risk_count >= 2:
        return base_rating + adjustment - 20

    return base_rating + adjustment

# System performance data
defense_log = [
    {'timestamp': 1678886400, 'type': 'scan', 'severity': 5},
    {'timestamp': 1678886500, 'type': 'login_fail', 'severity': 8},
    {'timestamp': 1678886600, 'type': 'scan', 'severity': 6},
    {'timestamp': 1678886700, 'type': 'data_access', 'severity': 9}
]
efficiency_metric = 0.88

# Irrelevant auxiliary variable (minor distraction)
baseline_threshold = 0.75

final_score = evaluate_performance(defense_log, efficiency_metric)
print(f"Result: {final_score}")