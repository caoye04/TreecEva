def calculate_gpa(grades):
    # Convert letter grades to points
    grade_points = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7,
        'F': 0.0
    }
    
    total_points = 0
    count = 0
    
    for grade in grades:
        if grade in grade_points:
            total_points += grade_points[grade]
            count += 1
    
    return total_points / max(1, count)

def analyze_attendance(data):
    present_days = sum(1 for status in data if status.lower() == 'present')
    absent_days = sum(1 for status in data if status.lower() == 'absent')
    late_days = sum(1 for status in data if status.lower() == 'late')
    
    # This calculation isn't actually used
    attendance_score = (present_days * 2 - absent_days * 3 + late_days * 0.5) / len(data)
    return present_days / max(1, len(data))

def process_submission_times(timestamps):
    early_bonus = 0
    late_penalty = 0
    
    for timestamp in timestamps:
        # Positive means days before deadline, negative means days after
        if timestamp > 3:
            early_bonus += 2
        elif timestamp > 0:
            early_bonus += 1
        elif timestamp < -2:
            late_penalty += 3
        elif timestamp < 0:
            late_penalty += 1
    
    # This result isn't used in the main calculation
    unused_metric = early_bonus * 2 - late_penalty * 1.5
    return early_bonus, late_penalty

def calculate_adjusted_score(student_data):
    # Extract relevant data
    raw_score = student_data['exam_score']
    attendance = student_data['attendance']
    timestamps = student_data['submission_times']
    letter_grades = student_data['previous_grades']
    participation = student_data.get('participation', 50)
    
    # Calculate various factors
    attendance_rate = analyze_attendance(attendance)
    early_bonus, late_penalty = process_submission_times(timestamps)
    
    # Calculate GPA from previous grades
    gpa = calculate_gpa(letter_grades)
    
    # Various misleading calculations
    potential_bonus = (gpa * 10) - (100 - participation) / 2
    complex_factor = (attendance_rate ** 2) * 100 - late_penalty * 2
    weighted_score = raw_score * 0.8 + potential_bonus * 0.2
    
    # Create a dictionary of potential adjustments
    adjustments = {
        'attendance': attendance_rate * 15,
        'submission': early_bonus - late_penalty,
        'history': min(10, gpa * 2.5),
        'participation': (participation - 50) / 10
    }
    
    # Apply only specific adjustments based on student ID
    student_id = student_data['id']
    adjustment_total = 0
    
    # Only use certain adjustments based on student ID's last digit
    if student_id % 10 in [3, 6, 9]:
        adjustment_total += adjustments['attendance']
    if student_id % 10 in [1, 4, 7]:
        adjustment_total += adjustments['submission']
    if student_id % 10 in [2, 5, 8]:
        adjustment_total += adjustments['history']
    if student_id % 10 in [0]:
        adjustment_total += adjustments['participation']
    
    # Apply a scale factor based on the raw score
    scale_factor = 1.0
    if raw_score > 85:
        scale_factor = 0.8
    elif raw_score > 70:
        scale_factor = 0.9
    elif raw_score < 50:
        scale_factor = 1.2
    
    # Final calculation uses only some of the computed values
    final = raw_score + (adjustment_total * scale_factor)
    
    # Apply upper and lower bounds
    return max(0, min(100, round(final, 2)))

# Student data with a mix of relevant and irrelevant information
student_data = {
    'id': 123456,
    'name': 'Alex Johnson',
    'major': 'Computer Science',
    'year': 3,
    'exam_score': 78.5,
    'attendance': ['Present', 'Present', 'Absent', 'Late', 'Present', 
                  'Present', 'Present', 'Late', 'Present', 'Present'],
    'submission_times': [4, 2, -1, 5, 1],
    'previous_grades': ['B+', 'A-', 'B', 'C+', 'A'],
    'group_project': {
        'role': 'Team Lead',
        'peer_rating': 4.2,
        'contribution': 35
    },
    'participation': 65
}

# Generate some unused metrics for distraction
distractor_metrics = {}
for i in range(5):
    key = f'metric_{i}'
    value = (i * student_data['year']) + (student_data['exam_score'] % 10) * 2
    distractor_metrics[key] = value

# Process the student data
final_score = calculate_adjusted_score(student_data)
print(f"Result: {final_score}")