def calculate_performance_rating():
    # Employee productivity tracking data
    tasks_completed = [8, 12, 5, 15, 10]
    hours_logged = [9, 10, 6, 14, 8]
    efficiency_ratio = []

    # Compute hourly completion rate with filtering
    for i, tasks in enumerate(tasks_completed):
        if hours_logged[i] > 0:
            ratio = tasks / hours_logged[i]
            efficiency_ratio.append(round(ratio, 2))

    # Baseline performance thresholds
    above_threshold = [r for r in efficiency_ratio if r >= 1.0]
    avg_efficiency = sum(efficiency_ratio) / len(efficiency_ratio)

    # Bonus calculation based on streaks
    streak_bonus = 0
    current_streak = 0
    for ratio in efficiency_ratio:
        if ratio >= 1.0:
            current_streak += 1
            streak_bonus += current_streak * 0.1
        else:
            current_streak = 0

    # Irrelevant distraction: string processing (minimal interference)
    employee_codes = ['E001', 'E002', 'E003', 'E004', 'E005']
    valid_prefix = [code.startswith('E') for code in employee_codes]
    code_lengths = [len(code) for code in employee_codes]

    # Final score computation
    base_score = avg_efficiency * 100
    adjusted_score = base_score + streak_bonus * 10
    final_score = int(round(adjusted_score))

    return final_score

# Execute and print result
target_result = calculate_performance_rating()
print(f"Result: {target_result}")