def process_score(score_data):
    base_score = score_data.get('exam', 0)
    bonus = score_data.get('bonus', 0)
    penalty = score_data.get('penalty', 0)
    temp_calc = base_score * 2 + bonus - penalty
    intermediate = temp_calc // 2
    adjusted = intermediate + 5 if intermediate > 50 else intermediate - 3
    return adjusted

student_data = {
    'S001': {'exam': 85, 'bonus': 10, 'penalty': 5},
    'S002': {'exam': 72, 'bonus': 8, 'penalty': 2},
    'A003': {'exam': 90, 'bonus': 5, 'penalty': 0},
    'S004': {'exam': 68, 'bonus': 7, 'penalty': 3}
}

processed_scores = {k: process_score(v) for k, v in student_data.items() if k.startswith("S")}
total_points = sum(processed_scores.values())
average_bonus = sum(v.get('bonus', 0) for v in student_data.values()) // len(student_data)
final_score = total_points - average_bonus

print(f"Target result: {final_score}")