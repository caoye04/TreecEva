def calculate_final_score(students, thresholds):
    total_score = 0
    bonus_applied = 0
    
    for idx, (name, grades) in enumerate(students.items()):
        avg_grade = sum(grades) / len(grades)
        subject_count = len(grades)
        
        # Determine performance level
        if avg_grade >= thresholds['high']:
            level_multiplier = 1.5
        elif avg_grade >= thresholds['medium']:
            level_multiplier = 1.2
        else:
            level_multiplier = 1.0
        
        # Apply bonus for students with consistent performance
        grade_range = max(grades) - min(grades)
        if grade_range <= 5 and subject_count >= 3:
            bonus_applied += 1
            total_score += avg_grade * level_multiplier + 10
        else:
            total_score += avg_grade * level_multiplier
    
    # Adjustment factor based on number of students
    adjustment = len(students) // 2
    final_score = int(total_score + adjustment + bonus_applied)
    
    return final_score

# Dataset
students = {
    'Alice': [88, 92, 85],
    'Bob': [76, 81, 79, 83],
    'Charlie': [95, 93],
    'Diana': [82, 85, 80, 88]
}

thresholds = {
    'high': 85,
    'medium': 75
}

irrelevant_counter = 0
for i in range(10):
    irrelevant_counter += i**2

final_score = calculate_final_score(students, thresholds)
print(f"Result: {final_score}")