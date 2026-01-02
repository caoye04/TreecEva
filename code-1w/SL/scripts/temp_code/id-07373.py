from collections import defaultdict
import math

# Simulate employee performance metrics across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
    
    # Irrelevant aggregation (distractor)
    total_depts = len(stats)
    avg_per_dept = sum(v['output'] for v in stats.values()) / total_depts if total_depts else 0
    
    return stats

# Misleading helper that computes unused metric
def calculate_efficiency_index(tasks, errors, tenure):
    if tenure == 0:
        return 0
    base = (tasks / (errors + 1)) * 100
    decay = math.exp(-0.1 * tenure)
    return round(base * decay, 2)

# Core logic with interference
productivity = [85, 90, 78, 92, 88]
risk_factor = [0.15, 0.10, 0.25, 0.08, 0.12]

# Simulate raw data input (some fields irrelevant)
employee_data = [
    {'name': 'alice', 'department': 'engineering', 'tasks_completed': 45, 'mistakes': 2, 'tenure': 3},
    {'name': 'bob', 'department': 'engineering', 'tasks_completed': 38, 'mistakes': 5, 'tenure': 5},
    {'name': 'carol', 'department': 'design', 'tasks_completed': 30, 'mistakes': 1, 'tenure': 2},
    {'name': 'dave', 'department': 'design', 'tasks_completed': 35, 'mistakes': 3, 'tenure': 4},
    {'name': 'eve', 'department': 'research', 'tasks_completed': 20, 'mistakes': 0, 'tenure': 6}
]

# Distractor: Unused transformation
transformed = list(map(lambda x: {**x, 'efficiency': calculate_efficiency_index(x['tasks_completed'], x['mistakes'], x['tenure'])}, employee_data))

# Compute department-level stats (semi-relevant)
dept_summary = analyze_department_stats(employee_data)

# Generate auxiliary metrics with bit operations (misleading)
shifted_risks = [(int(r * 100) << 1) ^ 3 for r in risk_factor]  # Bitwise distraction

# Actual productivity adjustment based on risk
adjusted_productivity = []
for i, p in enumerate(productivity):
    adj = p * (1 - risk_factor[i])
    adjusted_productivity.append(adj)

# Aggregate with unnecessary set operation (interference)
unique_caps = set(math.ceil(p) for p in adjusted_productivity)
bonus_eligible = len(unique_caps & {80, 85, 90, 95})  # Only partially relevant

# Final evaluation using filtered criteria
threshold_met = sum(1 for ap in adjusted_productivity if ap >= 80)
score_modifier = bonus_eligible * 0.5 if threshold_met >= 3 else -1.5

# Core result computation
base_performance = sum(adjusted_productivity) / len(adjusted_productivity)
final_score = round(base_performance + score_modifier, 2)

# Print required output
print(f"Result: {final_score}")