def calculate_performance(batches):
    base_multiplier = 1.5
    penalty_rate = 0.1
    bonus_threshold = 5
    final_score = 0
    total_items = 0
    overflow_flag = False

    # Irrelevant tracking variables (distractors)
    debug_log = []
    temp_sum = 0
    placeholder_value = 0

    for i, batch in enumerate(batches):
        batch_size = len(batch)
        valid_count = 0
        error_flags = []

        for j, (idx, item) in enumerate(zip(range(len(batch)), batch)):
            if item < 0:
                error_flags.append(j)
                continue
            if item > 100:
                overflow_flag = True
                continue
            valid_count += 1
            temp_sum += item  # Used only for distraction

        # Semi-relevant intermediate calculation (not directly used)
        average_valid = valid_count / batch_size if batch_size > 0 else 0

        # Core logic: score contribution based on valid items
        batch_contribution = valid_count * base_multiplier

        # Apply bonus if above threshold (only if no overflow in this batch)
        if not overflow_flag and valid_count >= bonus_threshold:
            batch_contribution *= 1.2

        # Accumulate score
        final_score += batch_contribution

        # Update total items (used to influence later batches)
        total_items += batch_size

        # Dead code path: never accessed due to condition
        if len(debug_log) > 1000:
            placeholder_value += 1

    # Final adjustment: reduce score if global overflow occurred
    if overflow_flag:
        final_score -= 5

    # Additional irrelevant computation
    scaling_factor = 1 + (total_items * 0.01)
    adjusted_score = final_score * scaling_factor  # Not used

    return int(final_score)

# Input data
batches = [
    [85, 90, -5, 95, 101, 70],
    [88, 82, 76, 91, 85, 87],
    [105, 90, 92, -3, 88]
]

# Execution point
final_score = calculate_performance(batches)
print(f"Result: {final_score}")