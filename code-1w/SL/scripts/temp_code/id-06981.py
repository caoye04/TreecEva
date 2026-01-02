from collections import defaultdict

# Simulate employee task tracking across departments
task_logs = [
    ('engineering', 'task1', 45), ('sales', 'task2', 30), ('engineering', 'task3', 60),
    ('marketing', 'task4', 25), ('sales', 'task5', 35), ('engineering', 'task6', 50),
    ('marketing', 'task7', 20), ('sales', 'task8', 40)
]

# Aggregate total time spent per department
department_time = defaultdict(int)
for dept, task, duration in task_logs:
    department_time[dept] += duration

# Misleading computation: average task count (not used in final logic)
task_count = len(task_logs)
avg_tasks_per_dept = task_count / len(department_time)  # Distractor

# Identify high-effort departments (threshold > 35 mins total)
high_effort_departments = {k for k, v in department_time.items() if v > 35}

# Simulate individual employee productivity scores (irrelevant to core logic but plausible)
employee_data = {
    'alice': {'tasks': 5, 'rating': 4.2},
    'bob': {'tasks': 3, 'rating': 3.8},
    'charlie': {'tasks': 6, 'rating': 4.5}
}
productivity = sum(emp['tasks'] for emp in employee_data.values())  # Used later

# Compute risk factor based on department diversity in high-effort group
departments_set = set(department_time.keys())
risk_factor = len(departments_set.symmetric_difference({'engineering', 'finance', 'hr'}))

# Auxiliary function with red herring parameters
def analyze_workload(data, min_duration=20, normalize=True):
    total = sum(duration for _, _, duration in data)
    long_tasks = [t for t in data if t[2] > min_duration]
    ratio = len(long_tasks) / len(data) if data else 0
    return total * 0.1 if normalize else total  # Computation not directly used

# Call function but don't use result — dead code path
dummy_load = analyze_workload(task_logs)

# Core evaluation logic
safety_margin = 1.5
base_threshold = 10

if len(high_effort_departments) >= 2:
    base_threshold += 5

if 'engineering' in high_effort_departments:
    safety_margin *= 1.2

adjusted_productivity = productivity * safety_margin

if adjusted_productivity > 15:
    base_threshold += 3

# Final performance score
def evaluate_performance(p, r):
    return int((p - r) * base_threshold)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")