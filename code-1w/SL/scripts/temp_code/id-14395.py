from itertools import compress, count

# Simulate employee performance metrics over a workweek
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
productivity = [8, 6, 9, 7, 10]  # Hours of effective work
effort_index = [0.95, 0.87, 0.93, 0.88, 0.96]
errors = [2, 1, 3, 0, 4]       # Number of critical errors per day
break_duration = [30, 45, 25, 35, 50]  # Minutes off-task

# Irrelevant helper: maps days to arbitrary risk factors
def daily_risk_factor(day):
    return {'Mon': 1.1, 'Tue': 0.9, 'Wed': 1.0, 'Thu': 0.8, 'Fri': 1.2}.get(day, 1.0)

risk_profile = list(map(daily_risk_factor, days))

# Misleading cumulative metric with no impact on final result
cumulative_effort = 0
for i in range(len(effort_index)):
    cumulative_effort += effort_index[i] * productivity[i]

# Distractor: analyze break patterns using lambda and filter
excessive_breaks = list(filter(lambda x: x > 40, break_duration))
break_alert_count = len(excessive_breaks)

# Real signal: calculate weighted productivity minus error penalty
adjusted_productivity = sum(p * (1 - 0.1 * e) for p, e in zip(productivity, errors))

# Use itertools.compress to select high-performance days (productivity >= 8)
high_perf_days = list(compress(productivity, (p >= 8 for p in productivity)))
top_performer_bonus = len(high_perf_days) * 5

# Dummy state tracker (not used in final computation)
state_log = []
tracker = count(1)
for _ in days:
    state_log.append(next(tracker))

# Core evaluation logic
penalty_rate = 7
base_score = adjusted_productivity
error_penalty = sum(errors) * penalty_rate
def evaluate_performance(prod, err):
    base = sum(prod)
    deductions = sum(e * penalty_rate for e in err)
    return base - deductions + top_performer_bonus

# Critical execution point
final_score = evaluate_performance(productivity, errors)

print(f"Result: {final_score}")