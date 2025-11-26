def analyze_student_grades():
    student_scores = [85, 92, 78, 85, 96, 78, 88, 92, 74, 85]
    score_set = set(student_scores)
    passing_scores = {score for score in score_set if score >= 80}
    failing_scores = score_set - passing_scores
    filtered_unique_count = len(passing_scores)
    final_count = filtered_unique_count * 2
    return filtered_unique_count

result = analyze_student_grades()
final_count = result + 3
print(f"Target result: {final_count}")