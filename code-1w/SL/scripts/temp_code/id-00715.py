def calculate_final_score(points, penalties):
    base_score = points * 1.5
    deduction = penalties * 2.5
    if base_score >= 50 and deduction > 10:
        bonus = 15
    else:
        bonus = 5
    adjusted_score = base_score - deduction + bonus
    return int(adjusted_score)

# Simulation data
task_log = "completed_task_42"
raw_points = len(task_log.split('_')) * 10
penalty_count = task_log.count('t') % 4

final_score = calculate_final_score(raw_points, penalty_count)
print(f"Result: {final_score}")