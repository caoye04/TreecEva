def calculate_student_performance():
    student_scores = [88, 92, 79, 85, 95]
    weight_factors = [0.2, 0.25, 0.15, 0.2, 0.2]
    
    # Calculate weighted scores (distractor - not used in final result)
    weighted_scores = []
    for i, score in enumerate(student_scores):
        weighted_scores.append(score * weight_factors[i])
    
    # Find maximum score (semi-relevant but not directly used)
    max_score = max(student_scores)
    
    # Calculate weighted total (key computation)
    weighted_total = 0
    for score, weight in zip(student_scores, weight_factors):
        weighted_total += score * weight
    
    # Calculate average (distractor - not used)
    average_score = sum(student_scores) / len(student_scores)
    
    # Penalty adjustment based on conditions
    late_submissions = 2
    bonus_points = 0
    
    if late_submissions > 1:
        penalty_adjustment = 3.5
    else:
        penalty_adjustment = 1.0
    
    # Final score calculation
    final_score = weighted_total - penalty_adjustment
    
    # Unused computation (pure distraction)
    temp_adjustment = penalty_adjustment * 1.1
    normalized_scores = [score / 100 for score in student_scores]
    
    print(f"Target result: {final_score}")

calculate_student_performance()