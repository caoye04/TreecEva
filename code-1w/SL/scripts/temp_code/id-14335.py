def analyze_performance(record):
    base_rating = sum(record.values()) / len(record)
    bonus = 0
    penalty = 0

    if base_rating > 80:
        bonus = 15
    elif base_rating < 50:
        penalty = 10

    adjusted = base_rating + bonus - penalty
    return adjusted


def calculate_consistency(data):
    max_val = max(data.values())
    min_val = min(data.values())
    range_diff = max_val - min_val
    consistency = 100 - range_diff if range_diff <= 50 else 50
    noise_variable = [x ** 0.5 for x in data.values() if x > 0]  # unused list comprehension (distractor)
    return consistency


def calculate_final_score(metrics, adjustments):
    raw_score = 0
    multiplier = 1.0

    for key, value in metrics.items():
        if key in adjustments:
            effect = adjustments[key]
            if effect == 'boost':
                raw_score += value * 1.2
            elif effect == 'reduce':
                raw_score -= 5
            else:
                raw_score += value * 0.9
        else:
            raw_score += value

    temp_result = raw_score / len(metrics)  # intermediate step

    flag = temp_result > 70
    multiplier += 0.1 if flag else 0.0

    final = temp_result * multiplier

    extra_calc = [(i, i**2) for i in range(1, 6)]  # dead code path
    unused_dict = {f'key_{i}': i * 2 for i in range(3)}  # irrelevant dictionary

    return int(final)

# Main execution
student_data = {
    'quiz_1': 85,
    'quiz_2': 78,
    'midterm': 92,
    'project': 88,
    'final_exam': 81
}

modifiers = {
    'midterm': 'boost',
    'project': 'boost',
    'final_exam': 'normal'
}

# Irrelevant preprocessing
normalized = {k: v / 100 for k, v in student_data.items()}
scaled_scores = [round(v * 10) for k, v in normalized.items() if v > 0.7]

performance_rating = analyze_performance(student_data)
consistency_score = calculate_consistency(student_data)

stats = {
    'base': performance_rating,
    'stability': consistency_score,
    'peak': max(student_data.values()),
    'avg_component': sum(student_data.values()) / len(student_data)
}

final_score = calculate_final_score(stats, modifiers)

Result: {final_score}