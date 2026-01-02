def analyze_performance(marks, thresholds):
    # Irrelevant helper computation (distractor)
    avg_mark = sum(marks) / len(marks)
    above_threshold = [m for m in marks if m > thresholds['high']]
    below_minimum = len([m for m in marks if m < thresholds['low']])

    # Misleading statistical transform (not used in final result)
    normalized = list(map(lambda x: (x - min(marks)) / (max(marks) - min(marks)), marks))

    # Core logic disguised among distractions
    bonus = 0
    if len(above_threshold) >= 3:
        bonus += 10
    elif len(above_threshold) == 2:
        bonus += 5

    penalty = 0
    if below_minimum > 1:
        penalty = 15

    base_score = sum(marks) // len(marks)

    # Simulated weighting (partially relevant)
    weights = {'quiz': 0.3, 'midterm': 0.3, 'final': 0.4}
    weighted_total = base_score * (weights['quiz'] + weights['midterm'] + weights['final'])

    # Actual key calculation
    def calculate_final_score(score, extra_bonus=False):
        adjusted = score + bonus - penalty
        if extra_bonus and adjusted > 75:
            adjusted += 5
        return adjusted

    # Dead code path (never executed but adds cognitive load)
    if False:
        fallback_scores = tuple(sorted(marks, reverse=True)[:2])
        backup = sum(fallback_scores) // 2

    # Key execution point
    final_score = calculate_final_score(weighted_total, extra_bonus='A' in [chr(65)] and True)

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
student_marks = [88, 76, 92, 85, 67]
score_thresholds = {'high': 80, 'low': 60}

# Execute
analyze_performance(student_marks, score_thresholds)