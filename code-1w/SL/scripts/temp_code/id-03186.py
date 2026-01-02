from collections import defaultdict
from itertools import combinations

# Simulate employee task logs over a week
task_logs = [
    {'employee': 'Alice', 'tasks_completed': 12, 'errors': 1, 'hours_worked': 40},
    {'employee': 'Bob', 'tasks_completed': 8, 'errors': 3, 'hours_worked': 35},
    {'employee': 'Charlie', 'tasks_completed': 15, 'errors': 5, 'hours_worked': 45},
    {'employee': 'Diana', 'tasks_completed': 10, 'errors': 0, 'hours_worked': 38}
]

# Irrelevant helper: counts character frequency in names (distractor)
def analyze_name_complexity(employees):
    char_freq = defaultdict(int)
    for emp in employees:
        for c in emp.lower():
            char_freq[c] += 1
    return char_freq

# Compute productivity score per hour with penalty for errors
def compute_productivity(logs):
    results = {}
    total_effort = 0  # distractor: not used later
    for log in logs:
        name = log['employee']
        hourly_rate = log['tasks_completed'] / log['hours_worked']
        error_penalty = log['errors'] * 2
        adjusted = max(hourly_rate * 10 - error_penalty, 0)
        results[name] = round(adjusted, 3)
        total_effort += log['hours_worked']  # dead-end accumulator
    return results

# Assess risk based on error-to-task ratio
def assess_risk(logs):
    risk_levels = {}
    high_risk_threshold = 0.2
    for log in logs:
        name = log['employee']
        ratio = log['errors'] / log['tasks_completed'] if log['tasks_completed'] > 0 else 1.0
        risk_levels[name] = 1 if ratio >= high_risk_threshold else 0
    
    # Distractor: generate all name pairs (unused)
    names = [log['employee'] for log in logs]
    pair_interactions = list(combinations(names, 2))
    
    return risk_levels

# Main evaluation function combining productivity and risk
def evaluate_performance(prod, risk):
    performance_tier = []
    base_score = 0
    bonus_credit = 0

    for emp, score in prod.items():
        if risk[emp] == 0:
            base_score += score * 1.1
            if score > 2.5:
                bonus_credit += 5  # high performer bonus
        else:
            base_score += score * 0.9

    # Apply team cohesion adjustment (fictional metric)
    team_size = len(prod)
    cohesion_factor = 1 + (0.05 if team_size >= 3 else 0)  # minor boost

    final_raw = base_score * cohesion_factor + bonus_credit

    # Normalize to integer scale
    return int(round(final_raw, 0))

# Execution flow
productivity = compute_productivity(task_logs)
risk_assessment = assess_risk(task_logs)

# Distractor: name complexity analysis (no impact)
employee_names = [log['employee'] for log in task_logs]
name_analysis = analyze_name_complexity(employee_names)

# Key statement
final_score = evaluate_performance(productivity, risk_assessment)

# Print result
print(f"Result: {final_score}")