def calculate_final_score(students, threshold):
    weighted_sum = 0
    count = 0
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_score = 0
    
    for idx, (name, scores) in enumerate(students.items()):
        homework_avg = sum(scores['homework']) / len(scores['homework'])
        exam_score = scores['exam']
        
        if exam_score >= threshold:
            # Apply weight: 30% homework, 70% exam
            final_grade = 0.3 * homework_avg + 0.7 * exam_score
            weighted_sum += final_grade
            count += 1
    
    return int(weighted_sum) if count > 0 else 0

# Main data structure with realistic context
students = {
    'Alice': {'homework': [85, 90, 88], 'exam': 92},
    'Bob': {'homework': [78, 80, 85], 'exam': 88},
    'Charlie': {'homework': [90, 92, 87], 'exam': 84},
    'Diana': {'homework': [95, 93, 96], 'exam': 95}
}

passing_threshold = 85
bonus_adjustment = 5  # Unused but plausible distraction (intervention level 4)

total_score = calculate_final_score(students, passing_threshold)
print(f"Result: {total_score}")