def evaluate_performance(metrics, flags):
    base = sum(metrics)
    penalty = 0
    if len(flags) > 2:
        penalty += 15
    if 0 in flags:
        penalty += 10
    return base - penalty

# Simulate employee performance evaluation
hours_worked = [8, 7, 9, 6, 8]
code_commits = [3, 5, 4, 2, 6]
bugs_found = [1, 0, 2, 1, 3]

# Irrelevant aggregation (distractor)
total_activities = []
for i in range(len(hours_worked)):
    total_activities.append(hours_worked[i] + code_commits[i])

# Compute productivity score using slicing (relevant)
recent_productivity = hours_worked[-3:]  # last 3 days
recent_commits = code_commits[1:4]      # middle segment
productivity = [p * 2 for p in recent_productivity]
productivity.append(sum(recent_commits))

# Risk flag setup with set operations (relevant + distraction)
risk_candidates = {1, 2, 3, 4, 5}
high_risk_days = {2, 4}
low_risk_days = {1, 3, 5}
risk_set = risk_candidates & high_risk_days  # intersection: {2, 4}
backup_flags = low_risk_days - risk_candidates  # empty set, irrelevant

# Auxiliary computation (dead code path)
supplementary_score = 0
if len(backup_flags) > 0:
    supplementary_score = max(backup_flags) * 100  # never executed

# Key state tracking variables
efficiency_ratio = len(productivity) / len(hours_worked)  # 4/5 = 0.8
normalization_factor = efficiency_ratio * 10  # 8.0

# Final evaluation (target statement)
final_score = evaluate_performance(productivity, risk_set)

# Print result
print(f"Result: {final_score}")