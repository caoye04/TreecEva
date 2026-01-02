from collections import defaultdict

# Simulate employee performance metrics across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    total_hours = 0
    temp_factor = 1.0

    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
        total_hours += emp['hours_worked']

        # Irrelevant intermediate calculation (distractor)
        if emp['seniority'] > 2:
            temp_factor *= 1.1

    # Unused derived values (dead code path)
    avg_output_per_dept = {dept: data['output'] / len([e for e in employees if e['department'] == dept]) 
                           for dept, data in stats.items()}

    return stats, total_hours

# Evaluate individual productivity with risk adjustment
def compute_productivity_index(base, experience, pressure_level):
    modifier = 1.0
    if experience < 2:
        modifier = 0.6
    elif experience >= 5:
        modifier = 1.3
    else:
        modifier = 0.9

    raw_productivity = base * modifier

    # Simulate stress impact (not actually used later - misleading)
    stress_penalty = pressure_level * 0.05 if pressure_level > 3 else 0

    # Final index is adjusted but ignores stress (distractor logic)
    return int(raw_productivity + 10)

# Main evaluation function combining multiple factors
def evaluate_performance(p, risk):
    threshold_map = {'low': 50, 'medium': 30, 'high': 10}
    base_threshold = threshold_map.get(risk, 20)

    adjustment = 0
    if p > 80:
        adjustment = 15
    elif p > 60:
        adjustment = 8
    else:
        adjustment = -5

    # Secondary conditional expression (semi-relevant)
    multiplier = 1.2 if p > 70 and risk == 'low' else 1.0

    # Complex but deterministic computation
    score = (p - base_threshold) * multiplier + adjustment

    # Additional noise variables
    debug_trace = [score * 0.1, score * 0.2]
    normalization_offset = sum(debug_trace) / 2

    # Final score uses only part of the computed values
    final = int(score - normalization_offset)  # Only uses derived offset, not full trace

    return final

# Dataset initialization
employee_data = [
    {'name': 'Alice', 'department': 'engineering', 'tasks_completed': 45, 'mistakes': 3, 'hours_worked': 160, 'seniority': 4},
    {'name': 'Bob', 'department': 'sales', 'tasks_completed': 30, 'mistakes': 7, 'hours_worked': 155, 'seniority': 2},
    {'name': 'Charlie', 'department': 'engineering', 'tasks_completed': 52, 'mistakes': 1, 'hours_worked': 165, 'seniority': 6},
    {'name': 'Diana', 'department': 'marketing', 'tasks_completed': 38, 'mistakes': 5, 'hours_worked': 158, 'seniority': 3}
]

# Step 1: Analyze department-level statistics
dept_analysis, total_work_hours = analyze_department_stats(employee_data)

# Step 2: Compute individual productivity index
individual_base = sum(emp['tasks_completed'] for emp in employee_data) // len(employee_data)
senior_count = sum(1 for emp in employee_data if emp['seniority'] >= 5)
pressure_metric = len(employee_data) if total_work_hours > 600 else 2

productivity = compute_productivity_index(individual_base, senior_count, pressure_metric)

# Step 3: Determine risk profile based on error rate
total_tasks = sum(emp['tasks_completed'] for emp in employee_data)
total_errors = sum(emp['mistakes'] for emp in employee_data)
error_rate = total_errors / total_tasks if total_tasks > 0 else 0

if error_rate < 0.05:
    risk_factor = 'low'
elif error_rate < 0.1:
    risk_factor = 'medium'
else:
    risk_factor = 'high'

# Step 4: Compute final performance score
final_score = evaluate_performance(productivity, risk_factor)

# Output result
print(f"Result: {final_score}")