def evaluate_performance(log, tasks):
    # Extract relevant metrics
    present_days = log.count('P')
    absent_days = log.count('A')
    tardy_days = log.count('T')
    total_days = len(log)

    # Distractor: unused health check variables
    system_uptime = 99.8
    last_audit = "2023-06-15"
    compliance_status = (absent_days < 5) and (tardy_days < 10)

    # Performance base score from attendance
    attendance_weight = 0.6
    if present_days == total_days:
        base_score = 100
    else:
        base_score = (present_days / total_days) * 90

    # Task completion analysis
    completed_tasks = sum(tasks)
    total_tasks = len(tasks)
    task_efficiency = completed_tasks / total_tasks if total_tasks > 0 else 0
    task_bonus = 10 if task_efficiency > 0.8 else 5 if task_efficiency > 0.6 else 0

    # Distractor: irrelevant string processing
    report_id = "PERF-" + str(total_tasks).zfill(3)
    report_section = report_id[5:] + "-SEC"
    metadata_flag = report_section.startswith('3') or report_section.endswith('C')

    # Composite score calculation
    raw_score = base_score + (task_efficiency * 10) + task_bonus

    # Apply adjustment for consistency (hidden logic)
    consistency_adjustment = 0
    for i in range(1, len(log)):
        if log[i] == 'P' and log[i-1] == 'P':
            consistency_adjustment += 0.5
    consistency_adjustment = min(consistency_adjustment, 15)

    # Final nonlinear transformation
    adjusted_score = raw_score * (1 + consistency_adjustment / 100)
    final_score = int(round(adjusted_score))

    # Irrelevant cleanup step (dead code path)
    if system_uptime > 100:
        final_score = 0  # Never reached

    return final_score

# Input data
attendance_log = 'PPPTPAPTTPPAPPP'

# Task completion: 1 = done, 0 = not done
task_completion = [1,1,0,1,1,1,0,0,1,1]

# Execute and print result
target_result = evaluate_performance(attendance_log, task_completion)
print(f"Result: {target_result}")