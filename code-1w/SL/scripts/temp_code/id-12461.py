from collections import defaultdict

# Simulate employee task logs with productivity metrics
task_logs = [
    {'employee': 'Alice', 'tasks_completed': 8, 'errors': 1, 'overtime_hours': 2},
    {'employee': 'Bob', 'tasks_completed': 5, 'errors': 3, 'overtime_hours': 4},
    {'employee': 'Charlie', 'tasks_completed': 10, 'errors': 0, 'overtime_hours': 1},
    {'employee': 'Alice', 'tasks_completed': 7, 'errors': 2, 'overtime_hours': 3},
    {'employee': 'Bob', 'tasks_completed': 6, 'errors': 1, 'overtime_hours': 2}
]

# Aggregate productivity per employee
productivity = defaultdict(lambda: {'tasks': 0, 'errors': 0, 'overtime': 0})
for log in task_logs:
    name = log['employee']
    productivity[name]['tasks'] += log['tasks_completed']
    productivity[name]['errors'] += log['errors']
    productivity[name]['overtime'] += log['overtime_hours']

# Compute efficiency scores (irrelevant to final result but adds cognitive load)
efficiency = {}
for emp, data in productivity.items():
    raw_efficiency = (data['tasks'] - data['errors']) / (data['overtime'] + 1)
    efficiency[emp] = round(raw_efficiency, 2)

# Distractor: Identify high-overtime employees
high_overtime_employees = {e for e, d in productivity.items() if d['overtime'] > 3}

# Risk assessment: employees with error rate > 20%
risk_candidates = set()
for emp, data in productivity.items():
    error_rate = data['errors'] / max(data['tasks'], 1)
    if error_rate > 0.2:
        risk_candidates.add(emp)

# Distractor: compute average tasks (not used later)
avg_tasks = sum(d['tasks'] for d in productivity.values()) / len(productivity)

# Use set operations to refine risk group
all_employees = {e for e in productivity.keys()}
risk_set = risk_candidates & all_employees  # Redundant, but mimics real code patterns

# Auxiliary function to calculate performance penalty
def calculate_penalty(employee_data):
    base_penalty = 0
    for _, data in employee_data.items():
        if data['errors'] > 2:
            base_penalty += 5
        if data['overtime'] > 4:
            base_penalty += 3
    return base_penalty

# Another distractor: unused helper
def forecast_stress_level(metrics):
    stress = 0
    for data in metrics.values():
        stress += data['overtime'] * 0.5 + data['errors'] * 0.7
    return round(stress, 1)

stress_index = forecast_stress_level(productivity)  # Computed but unused

# Core logic: evaluate performance based on completed tasks and apply risk penalty
def evaluate_performance(perf_data, risky):
    total_tasks = sum(data['tasks'] for data in perf_data.values())
    risk_penalty = 10 if 'Bob' in risky else 0  # Only Bob has high error rate
    bonus = 15 if perf_data['Alice']['errors'] == 3 else 0  # Alice had 1+2=3 errors
    return total_tasks - risk_penalty + bonus

# Key statement
final_score = evaluate_performance(productivity, risk_set)

print(f"Result: {final_score}")