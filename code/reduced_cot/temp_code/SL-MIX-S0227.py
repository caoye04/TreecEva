def analyze_student_grades(grade_records):
    # Process student grades with various operations
    grade_sum = sum(grade_records)
    grade_count = len(grade_records)
    
    # Distractor calculations that don't affect final result
    average_temp = (grade_sum * 1.8) / grade_count + 32
    weighted_sum = grade_sum * 1.1
    
    # Key operations using list comprehensions and conditional expressions
    passing_grades = [grade for grade in grade_records if grade >= 70]
    bonus_scores = [grade + 5 if grade > 85 else grade for grade in passing_grades]
    
    # More distractors
    max_possible = max(grade_records) * len(grade_records)
    score_ratio = grade_sum / max_possible if max_possible > 0 else 0
    
    # Core logic with nested operations
    sorted_results = sorted(bonus_scores, reverse=True)
    top_students = [score for score in sorted_results if score > 90]
    
    # Final answer computation
    final_result = sorted_results[-1]
    
    print(f"Target result: {final_result}")
    return final_result

# Main execution
student_grades = [88, 92, 67, 95, 74, 81, 79, 91]
analyze_student_grades(student_grades)