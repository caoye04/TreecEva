from collections import defaultdict, Counter

def analyze_grades(grades):
    letter_counts = Counter(grades)
    # Calculate average using ASCII values (not used in final calculation)
    ascii_sum = sum(ord(g) for g in grades)
    avg_ascii = ascii_sum / len(grades) if grades else 0
    
    # Convert letter grades to numeric values
    grade_values = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    numeric_grades = [grade_values.get(g, 0) for g in grades]
    
    return sum(numeric_grades) / len(numeric_grades) if numeric_grades else 0

def calculate_attendance_points(attendance_data):
    # Parse attendance data and calculate points
    attendance_log = attendance_data.split(',')
    
    # Count different attendance types
    present_count = attendance_log.count('P')
    absent_count = attendance_log.count('A')
    late_count = attendance_log.count('L')
    
    # Calculate potential extra credit (not used in final calculation)
    potential_extra = present_count * 0.5 - absent_count * 1.5
    
    # Actual attendance score calculation
    total_days = len(attendance_log)
    attendance_score = (present_count + late_count * 0.5) / total_days * 100
    
    return min(attendance_score, 100)  # Cap at 100

def calculate_weighted_score(student_data, course_weights):
    # Extract student performance data
    exam_scores = student_data['exams']
    project_score = student_data['project']
    homework_grades = student_data['homework_grades']
    attendance = student_data['attendance']
    
    # Process exam scores
    exam_avg = sum(exam_scores) / len(exam_scores)
    
    # Analyze letter grades for homework
    homework_gpa = analyze_grades(homework_grades)
    
    # Convert homework GPA to percentage scale
    homework_percent = homework_gpa * 25
    
    # Calculate attendance points
    attendance_points = calculate_attendance_points(attendance)
    
    # Alternative calculation method (not used in final result)
    alternative_score = (exam_avg * 0.4 + project_score * 0.3 + 
                        homework_percent * 0.2 + attendance_points * 0.1)
    
    # Calculate weighted score using the course weights
    weighted_score = (
        exam_avg * course_weights['exams'] +
        project_score * course_weights['project'] +
        homework_percent * course_weights['homework'] +
        attendance_points * course_weights['attendance']
    )
    
    # Round to 1 decimal place
    return round(weighted_score, 1)

# Student data
student_data = {
    'name': 'Alex Johnson',
    'id': 'AJ2023',
    'exams': [87, 92, 78],
    'project': 91,
    'homework_grades': 'ABBCBA',
    'attendance': 'P,P,P,L,P,A,P,P,L,P'
}

# Course weight configuration
course_weights = {
    'exams': 0.4,
    'project': 0.3,
    'homework': 0.2,
    'attendance': 0.1
}

# Calculate the student's final score
final_score = calculate_weighted_score(student_data, course_weights)
print(f"Result: {final_score}")
