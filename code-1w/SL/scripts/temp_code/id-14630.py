from collections import Counter
def calculate_final_score(scores, penalties):
    base_score = sum(scores)
    penalty_count = Counter(penalties)
    deduction = penalty_count['minor'] * 2 + penalty_count['major'] * 5
    adjusted_score = base_score - deduction
    if adjusted_score > 90:
        result = adjusted_score + 10
    else:
        result = adjusted_score
    return result

scores = [85, 78, 92]
penalties = ['minor', 'major', 'minor']
result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")