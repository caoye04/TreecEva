def calculate_final_score(results):
    total = 0
    bonus_applied = False
    for subject, data in results.items():
        score_str = data['score']
        if score_str.isdigit():
            score = int(score_str)
        else:
            continue
        weight = data['weight']
        weighted_score = score * weight
        if score > 85 and not bonus_applied:
            weighted_score += 5
            bonus_applied = True
        total += weighted_score
    return total

exam_results = {
    'math': {'score': '92', 'weight': 3},
    'physics': {'score': '78', 'weight': 2},
    'chemistry': {'score': '88', 'weight': 2},
    'literature': {'score': 'invalid', 'weight': 1}
}

# Irrelevant utility variable (minimal distraction)
temp_log = []

final_score = calculate_final_score(exam_results)
print(f"Result: {final_score}")