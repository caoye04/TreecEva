def calculate_performance_rating():
    base_points = 85
    bonus_multiplier = 1.2
    penalty_rate = 0.85
    
    # Simulate various performance metrics with some irrelevant tracking
    attendance_record = [True, True, False, True, True]
    tasks_completed = 12
    total_tasks = 15
    efficiency_ratio = tasks_completed / total_tasks
    
    # Distractor: unused calculation for alternate scoring
    hypothetical_score = base_points * bonus_multiplier - 10
    adjustment_factor = 1.0
    
    if efficiency_ratio >= 0.8:
        adjustment_factor += 0.15
    elif efficiency_ratio >= 0.6:
        adjustment_factor += 0.05
    else:
        adjustment_factor -= 0.1

    # Irrelevant data structure (set usage as suggested)
    completed_task_ids = {1, 2, 3, 5, 7, 8, 9, 10, 11, 12}
    pending_task_ids = {4, 6, 13, 14, 15}
    overlap_check = len(completed_task_ids & pending_task_ids)  # Always 0, distractor

    # Multiple assignment and conditional expression
    quality_flag, rework_count = True, 3
    penalty_applied = rework_count > 2
    dynamic_penalty = penalty_rate if penalty_applied else 1.0

    # Core scoring logic with nested conditions and arithmetic
    intermediate_score = base_points * adjustment_factor
    if attendance_record.count(False) == 0:
        intermediate_score += 5
    elif attendance_record.count(False) == 1:
        intermediate_score += 2
    
    # Final score computation
    final_score = int(intermediate_score * dynamic_penalty)
    
    # Dead code path (never executed, adds distraction)
    if False:
        final_score = max(final_score, 95)
        backup_log = [base_points, efficiency_ratio]

    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Result: {target_result}")