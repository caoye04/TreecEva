def calculate_student_performance(assignment_scores, exam_scores):
    # Combine and filter scores
    all_scores = list(zip(assignment_scores, exam_scores))
    valid_pairs = [(a, e) for a, e in all_scores if a >= 50 and e >= 40]
    
    # Calculate weighted scores (distractor - not used in final result)
    weighted_scores = [a * 0.4 + e * 0.6 for a, e in valid_pairs]
    
    # Extract valid assignment scores only
    valid_assignments = [a for a, e in valid_pairs]
    
    # Calculate statistics (some are distractors)
    avg_assignment = sum(valid_assignments) / len(valid_assignments) if valid_assignments else 0
    max_exam = max(e for _, e in valid_pairs) if valid_pairs else 0
    
    # Enumerate and filter high-performing students
    valid_scores = []
    for idx, (assignment, exam) in enumerate(valid_pairs):
        if assignment > 70 or exam > 75:
            valid_scores.append(assignment + exam)
    
    # Calculate bonus (distractor - calculated but not used)
    bonus_calc = len([s for s in valid_scores if s > 150])
    
    # Final result calculation
    final_score = sum(valid_scores)
    
    print(f"Target result: {final_score}")
    return final_score

# Test data
assignments = [85, 60, 45, 90, 55]
exams = [78, 65, 50, 82, 38]
calculate_student_performance(assignments, exams)