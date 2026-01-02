from collections import Counter

def calculate_final_score(scores, multiplier):
    adjusted = [score * multiplier for score in scores]
    total = sum(adjusted)
    penalty = 0
    score_counts = Counter(scores)
    # Check for repeated low scores
    if score_counts[1] > 1:
        penalty = 10
    return total - penalty

# Irrelevant auxiliary data (minimal distraction)
student_data = {'name': 'Alice', 'grade_level': 10}
temp_result = "analysis_complete"

raw_scores = [3, 5, 1, 4, 1]  # Two 1s will trigger penalty
bonus_multiplier = 2
final_score = calculate_final_score(raw_scores, bonus_multiplier)
print(f"Result: {final_score}")