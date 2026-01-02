def evaluate_performance(rate, faults):
    base = 100
    penalty = faults * 5
    bonus = 10 if rate > 80 else 0
    return base - penalty + bonus

# Employee metrics
tasks_completed = 45
hours_worked = 6
efficiency = (tasks_completed / hours_worked) * 10
productivity = round(efficiency)
errors = 3

# Irrelevant distraction: string processing (minimal interference)
log_entry = "EMP001|2023-06-15|TASK_COMPLETE"
date_part = log_entry.split('|')[1]
is_valid = 'TASK' in log_entry and 'COMPLETE' in log_entry.upper()

tier = (lambda x: 'Senior' if x > 75 else 'Junior')(productivity)

final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")