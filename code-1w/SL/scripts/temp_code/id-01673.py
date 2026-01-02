def evaluate_performance(results, threshold):
    # Initialize tracking variables
    success_count = 0
    penalty_adjustment = 0
    transient_buffer = [0] * len(results)
    overflow_flag = False

    for i, entry in enumerate(results):
        # Irrelevant signal processing simulation (distractor)
        filtered_value = (entry >> 2) & 0xFF
        if filtered_value > 200:
            overflow_flag = True
            penalty_adjustment -= 1

        # Core logic: count passes above threshold
        if entry >= threshold:
            success_count += 1
            # Bitwise tagging of successful tasks (semi-relevant)
            transient_buffer[i] = entry ^ 0x5A
        else:
            transient_buffer[i] = entry | 0x0F

    # Simulate data smoothing (irrelevant to final result)
    smoothed = transient_buffer[1:-1]
    neighbor_influence = 0
    for j in range(len(smoothed)):
        neighbor_influence += abs(smoothed[j] - smoothed[j-1]) if j > 0 else 0

    # Normalize success rate
    completion_rate = success_count / len(results)

    # Apply hidden bonus for consecutive wins (core logic)
    streak_bonus = 0
    current_streak = 0
    for val in results:
        if val >= threshold:
            current_streak += 1
            if current_streak == 3:
                streak_bonus += 5
                current_streak = 0  # Reset to allow overlapping bonuses
        else:
            current_streak = 0

    # Final score computation
    base_score = int(completion_rate * 100)
    final_score = base_score + streak_bonus + penalty_adjustment

    # Dead code path - never executed due to fixed input
    if overflow_flag and len(results) > 100:
        final_score = int(final_score * 0.9)

    return final_score

# Input setup
task_results = [85, 90, 88, 76, 92, 87, 94, 73, 85, 90]
base_threshold = 85

# Key execution point
final_score = evaluate_performance(task_results, base_threshold)
print(f"Result: {final_score}")