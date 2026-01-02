def calculate_final(scores, present_days):
    avg_score = sum(scores) / len(scores)
    bonus = 5 if all(s >= 60 for s in scores) else 0
    attendance_factor = 1 + (len([d for d in present_days if d]) / len(present_days)) * 0.1
    return round(avg_score * attendance_factor + bonus)

exam_scores = [78, 85, 92, 64, 81]
attendance = [True, True, False, True, True, True, False, True]

def analyze_performance():
    max_possible = max(exam_scores) + 10
    min_score = min(exam_scores)
    score_range = max_possible - min_score
    return score_range

# Irrelevant helper (mild distraction)
analyze_performance()

final_score = calculate_final(exam_scores, attendance)
print(f"Result: {final_score}")