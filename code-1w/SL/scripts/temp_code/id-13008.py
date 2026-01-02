from collections import defaultdict

# Simulate employee performance tracking across departments
def analyze_department_efficiency(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
    
    # Irrelevant aggregation (distractor)
    total_depts = len(stats)
    avg_errors_per_dept = sum(stats[d]['errors'] for d in stats) / max(total_depts, 1)
    return stats

# Misleading helper that computes unused metric
def calculate_burnout_risk(employee_list):
    stress_sum = 0
    for e in employee_list:
        workload = e['tasks_completed'] * 1.5
        rest_ratio = (8 - e.get('overtime_hours', 0)) / 8
        stress_level = workload / (rest_ratio + 0.1)
        stress_sum += stress_level
    return stress_sum / len(employee_list) if employee_list else 0

# Core logic disguised among distractors
def evaluate_performance(output_level, risk_multiplier):
    base_score = 100
    adjustment = 0
    
    # Nested logic with interdependencies
    if output_level > 80:
        adjustment += 25
        if risk_multiplier < 2.0:
            adjustment += 15
        elif risk_multiplier < 4.0:
            adjustment += 5
        else:
            adjustment -= 20
    elif output_level > 50:
        adjustment += 10
        if risk_multiplier >= 3.0:
            adjustment -= 10
    else:
        adjustment -= 20
    
    # Apply non-linear bonus using lambda (required feature)
    bonus_fn = lambda x: x * 0.1 if x < 30 else 3 + (x - 30) * 0.05
    bonus = bonus_fn(adjustment)
    
    # Final computation chain
    raw_score = base_score + adjustment + bonus
    penalty = 0
    
    # Conditional expression distractor (semi-relevant)
    penalty = 10 if output_level < 60 and risk_multiplier > 3.5 else 5 if risk_multiplier > 4.5 else 0
    final_normalized = raw_score - penalty
    
    return int(final_normalized)

# Simulated dataset with meaningful structure
employee_data = [
    {'name': 'Alice', 'department': 'Engineering', 'tasks_completed': 95, 'mistakes': 3, 'overtime_hours': 3},
    {'name': 'Bob', 'department': 'Engineering', 'tasks_completed': 78, 'mistakes': 6, 'overtime_hours': 5},
    {'name': 'Charlie', 'department': 'QA', 'tasks_completed': 65, 'mistakes': 2, 'overtime_hours': 6},
    {'name': 'Diana', 'department': 'QA', 'tasks_completed': 88, 'mistakes': 8, 'overtime_hours': 2},
    {'name': 'Eve', 'department': 'DevOps', 'tasks_completed': 92, 'mistakes': 4, 'overtime_hours': 4}
]

# Extract aggregate productivity (relevant)
department_stats = analyze_department_efficiency(employee_data)
productivity = sum(stat['output'] for stat in department_stats.values()) // len(department_stats)

# Compute risk factor from seemingly unrelated data (intermediate step)
total_mistakes = sum(stat['errors'] for stat in department_stats.values())
risk_factor = total_mistakes * 0.85 + len([e for e in employee_data if e['overtime_hours'] > 4]) * 1.2

# Unused but plausible computation (dead code path - interference)
utilization_rate = sum(e['tasks_completed'] for e in employee_data) / (len(employee_data) * 100)

# Burnout risk computed but not used (misleading variable)
burnout_risk = calculate_burnout_risk(employee_data)

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Target result: {final_score}")