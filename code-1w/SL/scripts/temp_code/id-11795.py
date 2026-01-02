from collections import defaultdict

# Simulate employee performance metrics across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
    
    # Irrelevant aggregation (distractor)
    total_depts = len(stats)
    avg_error_rate = sum(s['errors'] for s in stats.values()) / max(total_depts, 1)
    
    return stats

# Misleading helper that computes unused metric
def calculate_tenure_bonus(tenure_list):
    adjusted_bonuses = []
    for t in tenure_list:
        if t < 2:
            bonus = 0
        elif t < 5:
            bonus = t * 1.5
        else:
            bonus = t * 2.3
        adjusted_bonuses.append(round(bonus, 2))
    
    # This average is never used
    mean_bonus = sum(adjusted_bonuses) / len(adjusted_bonuses)
    return mean_bonus

# Core logic with moderate nesting and conditional expressions
def evaluate_performance(output_log, risk_level):
    base_score = 0
    penalty_adjustment = 0
    
    for entry in output_log:
        # Complex condition with string methods (real computation)
        urgency_flag = entry['priority'].strip().upper()
        critical = urgency_flag.startswith('URG') or 'HIGH' in urgency_flag
        
        task_weight = 1.0
        if critical:
            task_weight = 2.5 if 'TIME-SENSITIVE' in entry['notes'].upper() else 2.0
        
        # Actual contribution to score
        if entry['completed']:
            base_score += task_weight * entry['complexity']
        else:
            penalty_adjustment += 0.8 * task_weight
    
    # Real dependency on risk_level (boolean logic + arithmetic)
    risk_factor = 1.2 if risk_level else 0.9
    productivity = max(base_score - penalty_adjustment, 0)
    
    # Final calculation (target answer)
    final_score = round(productivity * risk_factor, 2)
    
    # Dead code path (distractor)
    if final_score > 100:
        compliance_status = "AUDIT_REQUIRED"
        threshold_check = compliance_status.lower().count('a')
    
    return final_score

# Input data setup
employee_data = [
    {'name': 'Alice', 'department': 'Engineering', 'tasks_completed': 12, 'mistakes': 2, 'tenure': 6},
    {'name': 'Bob', 'department': 'QA', 'tasks_completed': 8, 'mistakes': 5, 'tenure': 3},
    {'name': 'Charlie', 'department': 'Engineering', 'tasks_completed': 15, 'mistakes': 1, 'tenure': 7}
]

log_entries = [
    {
        'task_id': 'T101',
        'priority': ' URGENT ',
        'notes': 'Fix critical bug in payment module',
        'completed': True,
        'complexity': 3
    },
    {
        'task_id': 'T102',
        'priority': 'normal',
        'notes': 'Update documentation',
        'completed': True,
        'complexity': 1
    },
    {
        'task_id': 'T103',
        'priority': 'HIGH',
        'notes': 'TIME-SENSITIVE: Deploy patch before launch',
        'completed': False,
        'complexity': 4
    },
    {
        'task_id': 'T104',
        'priority': 'low',
        'notes': 'Refactor legacy code',
        'completed': True,
        'complexity': 2
    }
]

tenure_years = [emp['tenure'] for emp in employee_data]

# Execute analysis (unused)
department_summary = analyze_department_stats(employee_data)

# Compute irrelevant bonus (distraction)
bogus_bonus_avg = calculate_tenure_bonus(tenure_years)

# Key execution point
final_score = evaluate_performance(log_entries, risk_level=True)
print(f"Target result: {final_score}")