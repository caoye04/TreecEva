from collections import defaultdict
import itertools

# Simulate employee task logs over a workweek
task_logs = [
    {'employee': 'Alice', 'tasks_completed': 8, 'errors': 1, 'overtime_hours': 2},
    {'employee': 'Bob', 'tasks_completed': 5, 'errors': 0, 'overtime_hours': 5},
    {'employee': 'Charlie', 'tasks_completed': 10, 'errors': 3, 'overtime_hours': 1},
    {'employee': 'Diana', 'tasks_completed': 7, 'errors': 2, 'overtime_hours': 3}
]

# Initialize trackers
productivity = defaultdict(float)
risk_assessment = {}
bonus_pool = 0.0

# Step 1: Compute productivity score and detect high-effort employees
for log in task_logs:
    emp = log['employee']
    tasks = log['tasks_completed']
    errors = log['errors']
    overtime = log['overtime_hours']

    efficiency = (tasks - errors) / (1 + overtime * 0.1)
    productivity[emp] = round(efficiency, 2)

    # Distractor: bonus eligibility (not used in final logic)
    if tasks > 7 and errors == 0:
        bonus_pool += 500

    # Risk factor based on error rate and fatigue
    error_rate = errors / tasks if tasks > 0 else 0
    fatigue_factor = overtime * 0.15
    risk_assessment[emp] = round(error_rate + fatigue_factor, 3)

# Step 2: Identify performance quartiles (semi-relevant for context)
sorted_productivity = sorted(productivity.values(), reverse=True)
quartile_break = len(sorted_productivity) // 2
high_performer_threshold = sorted_productivity[quartile_break] if quartile_break > 0 else 0

# Distractor: group combinations (itertools usage - not directly relevant)
name_perms = list(itertools.permutations(['Alice', 'Bob'], 2))
combination_count = len(name_perms)  # Unused beyond this

# Step 3: Aggregate metrics for evaluation
aggregate_efficiency = sum(productivity.values())
average_risk = sum(risk_assessment.values()) / len(risk_assessment)

# Step 4: Simulate weighted evaluation function
def evaluate_performance(perf_dict, risk_dict):
    base_score = 0
    penalty = 0

    for emp, perf in perf_dict.items():
        base_score += perf * 10
        if risk_dict[emp] > 0.3:
            penalty += 5
        elif perf < 5.0:
            penalty += 2

    # Final scoring with arbitrary scaling
    return int((base_score - penalty * 3) * 0.9)

# Key statement
final_score = evaluate_performance(productivity, risk_assessment)

# Irrelevant set operation (distractor)
unique_employees = set([log['employee'] for log in task_logs])
dummy_set = {1, 2, 3} | unique_employees  # Mixed type set (ignored)

# Output result
print(f"Result: {final_score}")