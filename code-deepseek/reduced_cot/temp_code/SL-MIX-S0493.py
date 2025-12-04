def calculate_student_performance():
    student_records = [
        {'name': 'Alice', 'scores': [85, 92, 78, 95]},
        {'name': 'Bob', 'scores': [72, 88, 91, 67]},
        {'name': 'Charlie', 'scores': [95, 89, 94, 82]}
    ]
    
    # Calculate average scores for each student
    average_scores = []
    for record in student_records:
        total = sum(record['scores'])
        count = len(record['scores'])
        avg = total / count
        average_scores.append(avg)
    
    # Find the highest average score (distractor - not used in final result)
    max_avg = max(average_scores)
    min_avg = min(average_scores)
    
    # Process top students (this affects the final result)
    grade_sum = 0
    bonus_points = 0
    threshold = 85.0
    
    for i, avg_score in enumerate(average_scores):
        if avg_score > threshold:
            grade_sum += int(avg_score)
            if avg_score > 90:
                bonus_points += 5
    
    # Some intermediate calculations (distractors)
    temp_multiplier = len([x for x in average_scores if x > 80])
    unused_calc = temp_multiplier * 2.5
    
    # Final calculation
    multiplier = 1.2
    final_score = grade_sum * multiplier + bonus_points
    
    # Print the target result
    print(f"Target result: {final_score}")

calculate_student_performance()