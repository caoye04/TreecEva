def analyze_performance(data_points, threshold=75):
    # Performance analysis for data validation
    filtered = list(filter(lambda x: x > threshold, data_points))
    if len(filtered) > len(data_points) / 2:
        return sum(filtered) / len(filtered) if filtered else 0
    else:
        return sum(data_points) / len(data_points) if data_points else 0

def calculate_bonus_points(attendance, participation):
    # Calculate bonus based on attendance and participation
    potential_bonus = attendance * 0.5 + participation * 2
    # Apply logarithmic scaling to prevent excessive bonuses
    import math
    scaled_bonus = math.log(potential_bonus + 1) * 5 if potential_bonus > 0 else 0
    return min(scaled_bonus, 15)  # Cap bonus at 15 points

def process_grades(grades, weights):
    # Process and normalize grades
    normalized = []
    weight_sum = sum(weights)
    
    # Apply weights to grades
    for i, grade in enumerate(grades):
        if i < len(weights):
            normalized.append(grade * weights[i] / weight_sum)
        else:
            normalized.append(grade / len(grades))
    
    # This normalization is actually not used in final calculation
    return normalized

def apply_curve(score, curve_factor=1.1):
    # Apply curve to scores below threshold
    if score < 60:
        return score * curve_factor
    elif score < 70:
        return score * 1.05
    else:
        return score

def calculate_final_score(student_data):
    # Extract student data
    exam_scores = student_data.get('exams', [70, 85, 90])
    assignments = student_data.get('assignments', [75, 80, 85, 90])
    attendance = student_data.get('attendance', 80)
    participation = student_data.get('participation', 7)
    extra_credit = student_data.get('extra_credit', False)
    
    # Calculate exam average - this is the core component
    exam_weights = [0.2, 0.3, 0.5]  # Last exam worth more
    weighted_exam_score = 0
    for i, score in enumerate(exam_scores):
        if i < len(exam_weights):
            weighted_exam_score += score * exam_weights[i]
    
    # Process assignments - using lambda for variety
    assignment_score = sum(map(lambda x: min(x, 95), assignments)) / len(assignments)
    
    # Calculate performance metrics (not used in final calculation)
    performance_rating = analyze_performance(exam_scores + assignments)
    
    # Potential penalty calculation (not applied)
    penalty = 0
    if attendance < 70:
        penalty = (70 - attendance) * 0.5
    
    # Calculate bonus
    bonus = calculate_bonus_points(attendance, participation)
    if extra_credit:
        bonus += 5
    
    # Calculate base score
    base_score = weighted_exam_score * 0.7 + assignment_score * 0.3
    
    # Misleading intermediate calculation
    adjusted_score = (base_score + bonus - penalty) * 0.95
    
    # The actual final calculation
    result = base_score + bonus
    
    # Apply curve to final result
    result = apply_curve(result)
    
    # Cap at 100
    return min(round(result, 2), 100)

# Student data
student_data = {
    'exams': [82, 88, 91],
    'assignments': [78, 85, 92, 88],
    'attendance': 85,
    'participation': 8,
    'extra_credit': True
}

# Misleading alternative data
alternative_data = {
    'exams': [75, 80, 85],
    'assignments': [70, 75, 80, 85],
    'attendance': 70,
    'participation': 5,
    'extra_credit': False
}

# Process grades with weights (not used in final calculation)
processed_grades = process_grades(student_data['exams'], [1, 1, 2])

# Calculate final score
final_score = calculate_final_score(student_data)

# Print result
print(f"Result: {final_score}")
