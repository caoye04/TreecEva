def main():
    # Define student performance sets
    exam_scores = [85, 92, 78, 96, 88]
    project_scores = [88, 90, 85, 94]

    # Convert to sets for overlap analysis
    exam_set = set(exam_scores)
    project_set = set(project_scores)

    # Irrelevant distraction: unused variable (minimal interference)
    quiz_set = {80, 82, 85, 90}

    # Core logic using lambda for dynamic weighting
    common_scores = exam_set & project_set
    weight_func = lambda x: 1.1 if x >= 90 else 1.0

    # Calculate weighted contribution from exams
    exam_weighted = sum(score * weight_func(score) for score in exam_set)

    # Calculate base project total
    project_total = sum(project_set)

    # Final score computation
    bonus = len(common_scores) * 5
    final_score = int((exam_weighted + project_total) / 10) + bonus

    return final_score

result = main()
print(f"Result: {result}")