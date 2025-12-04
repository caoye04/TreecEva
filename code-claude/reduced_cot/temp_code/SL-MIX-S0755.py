def calculate_student_performance(raw_scores):
    # Process student exam scores and calculate final grade average
    passing_threshold = 60
    bonus_points = 5
    
    # Clean up any invalid scores (negative values)
    valid_scores = [max(0, score) for score in raw_scores]
    
    # Apply bonus points to scores below threshold
    adjusted_scores = []
    for score in valid_scores:
        if score < passing_threshold:
            adjusted_scores.append(score + bonus_points)
        else:
            adjusted_scores.append(score)
    
    # Keep only scores that are now passing
    final_grades = [score for score in adjusted_scores if score >= passing_threshold]
    
    # Calculate the average of passing grades
    grade_average = sum(final_grades) / len(final_grades)
    
    # Format grade report
    report = f"Class average: {grade_average:.1f}%"
    
    return report

# Student raw exam scores
exam_scores = [58, 91, 72, 65, 49, 85, 75]
result = calculate_student_performance(exam_scores)
print(f"Result: {result}")