def evaluate_performance(log, thresh):
    # Initialize tracking variables
    success_count = 0
    penalty_points = 0
    transient_buffer = []
    cumulative_offset = 0.0

    for entry in log:
        # Extract relevant data
        task_id = entry['id']
        execution_time = entry['time']
        errors = entry['errors']
        priority = entry.get('priority', 1)

        # Irrelevant debug computation (distractor)
        debug_checksum = (len(task_id) * 37) % 101
        if debug_checksum > 50:
            transient_buffer.append(debug_checksum * 0.1)

        # Core logic: check performance against threshold
        if execution_time < thresh:
            multiplier = 2 if priority > 1 else 1
            success_count += 1 * multiplier
        else:
            # Apply penalty scaled by error count
            penalty_points += min(errors * 2, 10)

        # Dead code path - never affects final score (distractor)
        if execution_time == -1:
            cumulative_offset += priority / (len(task_id) + 1)

    # Composite scoring with fake complexity
    base_score = success_count * 10
    deduction = penalty_points * 3
    adjustment_factor = len(transient_buffer) * 0.5  # Unused influence

    # Final score calculation (only base_score and deduction matter)
    final_score = base_score - deduction

    # Additional red herring: modify offset but don't use it
    cumulative_offset = round(cumulative_offset + adjustment_factor, 3)

    return int(final_score)

# Simulation data
metrics_log = [
    {'id': 'T001', 'time': 120, 'errors': 3, 'priority': 2},
    {'id': 'T002', 'time': 80, 'errors': 0, 'priority': 1},
    {'id': 'T003', 'time': 95, 'errors': 1, 'priority': 3},
    {'id': 'T004', 'time': 200, 'errors': 5, 'priority': 1},
    {'id': 'T005', 'time': 60, 'errors': 0, 'priority': 2}
]
threshold = 100

# Key statement
final_score = evaluate_performance(metrics_log, threshold)
print(f"Result: {final_score}")