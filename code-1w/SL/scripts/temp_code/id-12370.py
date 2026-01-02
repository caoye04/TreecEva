def analyze_productivity(hours_worked, breaks_taken, tasks_completed):
    efficiency_ratio = max(0.5, min(1.5, tasks_completed / (hours_worked + 0.1)))
    break_penalty = 0.1 * breaks_taken if breaks_taken > 2 else 0
    adjusted_hours = max(1, hours_worked - breaks_taken * 0.5)
    
    # Distractor: unused intermediate calculation
    theoretical_capacity = (hours_worked * 60 - breaks_taken * 15) // 25
    fatigue_factor = 1 - (breaks_taken * 0.05) if hours_worked > 6 else 1
    
    base_performance = (tasks_completed * efficiency_ratio) / adjusted_hours
    performance_bonus = 10 if tasks_completed >= 8 and hours_worked <= 6 else 0
    
    return base_performance * fatigue_factor + performance_bonus


def evaluate_performance(employee_data):
    total_hours = sum(record['hours'] for record in employee_data)
    total_breaks = sum(record['breaks'] for record in employee_data)
    total_tasks = sum(record['tasks'] for record in employee_data)
    
    # Distractor: irrelevant string manipulation
    employee_ids = [str(emp['id']) for emp in employee_data]
    id_concat = ''.join(employee_ids)
    id_sum_check = sum(int(d) for d in id_concat if d.isdigit())
    
    # Early return red herring (not taken)
    if len(employee_data) == 0:
        return 0.0
    
    productivity = analyze_productivity(total_hours, total_breaks, total_tasks)
    
    # Conditional expression with semi-relevant adjustment
    bonus_multiplier = 1.2 if id_sum_check % 2 == 0 else 1.0
    
    # Final score computation
    final_score = int(productivity * bonus_multiplier)
    
    # Additional distractor loop (no effect on result)
    temp_accum = 0
    for i in range(len(employee_data)):
        temp_accum += len(str(employee_data[i]['id']))
    temp_accum *= 0  # Neutralize
    
    return final_score

# Input data
employees = [
    {'id': 123, 'hours': 7, 'breaks': 3, 'tasks': 9},
    {'id': 456, 'hours': 6, 'breaks': 1, 'tasks': 7},
    {'id': 789, 'hours': 5, 'breaks': 2, 'tasks': 6}
]

result = evaluate_performance(employees)
print(f"Target result: {result}")