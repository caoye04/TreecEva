from collections import defaultdict

# Simulate employee task logs with hours worked per day
task_logs = {
    'alice': [8, 7, 6, 9, 8],
    'bob': [5, 6, 7, 5, 4],
    'charlie': [10, 10, 9, 8, 9]
}

# Irrelevant metrics (distractor)
stress_levels = defaultdict(int)
stress_conversion = {'high': 3, 'medium': 2, 'low': 1}
for emp in task_logs:
    total_hours = sum(task_logs[emp])
    if total_hours > 40:
        stress_levels[emp] = 'high'
    elif total_hours > 35:
        stress_levels[emp] = 'medium'
    else:
        stress_levels[emp] = 'low'

# Productivity metric: average over median-adjusted workday
productivity = {}
baseline = 8  # standard workday
for emp, hours in task_logs.items():
    median_hour = sorted(hours)[len(hours)//2]
    adjusted_hours = [h for h in hours if h >= median_hour - 1]
    avg = sum(adjusted_hours) / len(adjusted_hours)
    productivity[emp] = avg - baseline  # deviation from baseline

# Risk factor based on hour inconsistency (variance proxy)
risk_factor = {}
for emp, hours in task_logs.items():
    mean = sum(hours) / len(hours)
    variance_proxy = sum((h - mean) ** 2 for h in hours) / len(hours)
    risk_factor[emp] = variance_proxy * 0.1

# Distractor computation: workload streaks
streak_data = {}
for emp, hours in task_logs.items():
    streak = 0
    max_streak = 0
    for h in hours:
        if h >= 8:
            streak += 1
        else:
            max_streak = max(max_streak, streak)
            streak = 0
    max_streak = max(max_streak, streak)
    streak_data[emp] = max_streak

# Secondary distractor: efficiency ratio (not used)
efficiency_ratio = {}
for emp, hours in task_logs.items():
    peak = max(hours)
    avg = sum(hours) / len(hours)
    efficiency_ratio[emp] = round(avg / peak, 2) if peak else 0

# Core logic: performance evaluation
def evaluate_performance(prod_dict, risk_dict):
    weighted_sum = 0.0
    count = 0
    for emp in prod_dict:
        # Only consider employees with moderate or lower risk
        if risk_dict[emp] <= 1.5:
            # Performance score: reward positive productivity, penalize inconsistency
            score = prod_dict[emp] * 10 - risk_dict[emp] * 5
            weighted_sum += score
            count += 1
    return int(weighted_sum) if count > 0 else 0

# Execution point of interest
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Target result: {final_score}")