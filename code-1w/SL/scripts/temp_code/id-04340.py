def evaluate_performance(scores):
    total_score = 0
    penalty_deductions = 0
    bonus_applied = False

    for i, (index, score) in enumerate(zip(range(len(scores)), scores)):
        if score < 0:
            continue
        total_score += score

        if total_score > 50 and not bonus_applied:
            total_score += 10
            bonus_applied = True

        if total_score >= 75:
            break

        penalty_deductions += 2  # Minor distraction

    final_result = total_score - penalty_deductions  # Not used
    return total_score

result = evaluate_performance([20, -5, 30, 15, 25])
print(f"Target result: {result}")