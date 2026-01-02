from itertools import compress

# Simulate employee performance metrics over a workweek
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
base_hours = [7.5, 8.0, 6.5, 8.5, 7.0]
errors = [2, 1, 3, 0, 1]
pauses = [4, 3, 5, 2, 3]  # number of interruptions

# Calculate daily productivity scores with diminishing returns
productivity = []
for i in range(len(days)):
    raw_efficiency = base_hours[i] * 10 - errors[i] * 5
    penalty = min(pauses[i] * 2, 10)  # max penalty cap
    adjusted_efficiency = raw_efficiency - penalty
    if adjusted_efficiency < 0:
        adjusted_efficiency = 0
    productivity.append(adjusted_efficiency)

# Irrelevant distraction: analyze pause distribution (not used later)
unique_pauses = set(pauses)
median_pause = sorted(pauses)[len(pauses)//2]
mode_pause = max(set(pauses), key=pauses.count)

# Calculate weekly consistency metric (unused distractor)
consistency_deviation = sum((productivity[i] - productivity[i-1])**2 for i in range(1, len(productivity)))

# Risk factor based on error trends and late-week fatigue
recent_errors = errors[-2:]
late_productivity = productivity[-2:]
error_trend = sum(recent_errors) / 2
fatigue_index = 10 - sum(late_productivity) / 2
risk_factor = error_trend * 3 + fatigue_index * 0.5

# Mask creation using slicing and conditionals (semi-relevant)
good_days_mask = [p > 60 for p in productivity]
top_performing_days = list(compress(days, good_days_mask))
high_performers = productivity[1:4]  # middle three days

# Final performance evaluation incorporating risk adjustment
def evaluate_performance(efficiency_list, risk):
    base_score = sum(efficiency_list)
    risk_adjustment = 100 / (1 + risk)  # higher risk → lower score
    bonus = 10 if len(top_performing_days) >= 2 else 0
    # Apply non-linear scaling
    final = (base_score * 0.8 + bonus) * (risk_adjustment / 10)
    return int(final)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Debugging leftovers (distractor variables)
total_compensated_hours = sum(base_hours) + 0.5 * len([e for e in errors if e == 0])
avg_daily_score = final_score / 5

print(f"Result: {final_score}")