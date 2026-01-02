from collections import defaultdict
from itertools import combinations

# Simulate employee task logs over a workday
task_logs = [
    {'employee': 'alice', 'tasks_completed': 8, 'errors': 1, 'hours_worked': 7.5},
    {'employee': 'bob', 'tasks_completed': 6, 'errors': 0, 'hours_worked': 8.0},
    {'employee': 'charlie', 'tasks_completed': 10, 'errors': 3, 'hours_worked': 6.0},
    {'employee': 'alice', 'tasks_completed': 5, 'errors': 0, 'hours_worked': 4.5},
    {'employee': 'bob', 'tasks_completed': 7, 'errors': 2, 'hours_worked': 7.0},
    {'employee': 'diana', 'tasks_completed': 9, 'errors': 1, 'hours_worked': 8.0}
]

# Aggregate data by employee
work_summary = defaultdict(lambda: {'tasks': 0, 'errors': 0, 'hours': 0.0})
for log in task_logs:
    emp = log['employee']
    work_summary[emp]['tasks'] += log['tasks_completed']
    work_summary[emp]['errors'] += log['errors']
    work_summary[emp]['hours'] += log['hours_worked']

# Compute efficiency metrics
productivity = {}
error_rate = {}
for emp, data in work_summary.items():
    productivity[emp] = data['tasks'] / data['hours'] if data['hours'] > 0 else 0
    error_rate[emp] = data['errors'] / data['tasks'] if data['tasks'] > 0 else 0

# Identify high performers based on productivity threshold
high_performers = [e for e, p in productivity.items() if p >= 1.4]

# Generate all possible pairs of high performers for collaboration analysis
pairwise_combinations = list(combinations(high_performers, 2))

# Dummy metric: total interaction potential (not used but adds distraction)
interaction_potential = sum(len(p) for p in pairwise_combinations) * 1.5 if pairwise_combinations else 0.0

# Simulate bonus eligibility via lambda
is_bonus_eligible = lambda rate: rate < 0.15
bonus_eligible_count = sum(1 for er in error_rate.values() if is_bonus_eligible(er))

# Irrelevant statistical calculation (adds interference)
dummy_variance_proxy = sum((p - 1.5)**2 for p in productivity.values()) / len(productivity) if productivity else 0

# Core evaluation function
def evaluate_performance(prod_dict, err_dict):
    base_score = 0
    adjustment = 0
    for emp in prod_dict:
        # Base score from normalized productivity
        base_score += min(prod_dict[emp] * 10, 20)
        # Penalty for error rate
        err_ratio = err_dict.get(emp, 0)
        if err_ratio > 0.2:
            adjustment -= 5
        elif err_ratio > 0.1:
            adjustment -= 2
        else:
            adjustment += 1
    return int(base_score + adjustment)

# Misleading intermediate variable (dead-end)
temp_aggregate = sum(work_summary[e]['tasks'] for e in work_summary)

# Key statement
final_score = evaluate_performance(productivity, error_rate)

# Output result
print(f"Result: {final_score}")