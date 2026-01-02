def analyze_efficiency(logs):
    total_ops = 0
    idle_periods = 0
    for log in logs:
        if log['status'] == 'active':
            total_ops += log['operations']
        elif log['status'] == 'idle':
            idle_periods += 1
    efficiency = total_ops / (len(logs) + 1e-5)
    return efficiency

logs_data = [
    {'status': 'active', 'operations': 45},
    {'status': 'idle', 'operations': 0},
    {'status': 'active', 'operations': 67},
    {'status': 'active', 'operations': 34},
    {'status': 'idle', 'operations': 0}
]

productivity = analyze_efficiency(logs_data)

# Irrelevant distraction: character frequency count (not used in final result)
document = "performance review quarterly report"
char_freq = {}
for c in document:
    char_freq[c] = char_freq.get(c, 0) + 1
vowel_count = sum(1 for c in document if c in 'aeiou')

# Another red herring: set operations with no downstream impact
project_teams = {'dev', 'qa', 'ux', 'ops'}
completed_tasks = {'dev', 'ux', 'security'}
pending_teams = project_teams - completed_tasks  # {'qa', 'ops'}
overlap = project_teams & completed_tasks

# Simulate error rates over time (some are irrelevant)
error_log = [2, 0, 5, 0, 3, 1]
errors = sum(error_log)
spurious_calc = len(error_log) * max(error_log + [1])

# Attendance tracking with linear search through days
work_days = [True, True, False, True, True, True, False]
current_day = 5
attendance = 0
for i in range(current_day + 1):
    if i >= len(work_days):
        break
    if work_days[i]:
        attendance += 1

# Distractor: unused helper function
def predict_future_efficiency(curr):
    return curr * 1.05 if curr < 50 else curr * 1.02

# Core logic buried among distractions
def evaluate_performance(prod, errs, attend):
    base = prod * 10
    penalty = errs * 5
    bonus = attend * 2
    # Normalize productivity to a 0-100 scale
    normalized_prod = min(max(base, 0), 100)
    score = normalized_prod - penalty + bonus
    return int(score)

# Key statement
final_score = evaluate_performance(productivity, errors, attendance)

print(f"Result: {final_score}")