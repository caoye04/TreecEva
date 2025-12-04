# Function to analyze student performance data across multiple exams
def calculate_metrics(student_data):
    # Extract student names and scores
    names = [student[0] for student in student_data]
    all_scores = [student[1] for student in student_data]
    
    # Track some statistics that might be useful
    highest_score = -1
    lowest_score = 101
    total_students = len(student_data)
    passing_threshold = 60
    
    # Process scores with validation
    valid_scores = []
    invalid_count = 0
    
    # Calculate letter grades distribution (not used in final calculation)
    grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    # Process each student's data
    for i, (name, scores) in enumerate(zip(names, all_scores)):
        # Calculate average score for this student
        student_avg = sum(scores) / len(scores)
        
        # Determine letter grade
        if student_avg >= 90:
            grade = 'A'
        elif student_avg >= 80:
            grade = 'B'
        elif student_avg >= 70:
            grade = 'C'
        elif student_avg >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        grade_distribution[grade] += 1
        
        # Only include valid scores (between 0 and 100)
        if 0 <= student_avg <= 100:
            valid_scores.append(student_avg)
            # Update highest and lowest scores
            if student_avg > highest_score:
                highest_score = student_avg
            if student_avg < lowest_score:
                lowest_score = student_avg
        else:
            invalid_count += 1
    
    # Calculate class statistics
    passing_count = sum(1 for score in valid_scores if score >= passing_threshold)
    failing_count = len(valid_scores) - passing_count
    
    # Calculate median score (not used in final calculation)
    sorted_scores = sorted(valid_scores)
    if len(sorted_scores) % 2 == 0:
        median = (sorted_scores[len(sorted_scores)//2] + sorted_scores[len(sorted_scores)//2 - 1]) / 2
    else:
        median = sorted_scores[len(sorted_scores)//2]
    
    # Calculate final average score
    average_score = round(sum(valid_scores) / len(valid_scores), 2)
    
    # Calculate standard deviation (not used in final calculation)
    variance = sum((x - average_score) ** 2 for x in valid_scores) / len(valid_scores)
    std_deviation = round(variance ** 0.5, 2)
    
    return average_score

# Sample student data: (name, [exam_scores])
student_data = [
    ("Alice", [92, 88, 95, 91]),
    ("Bob", [75, 82, 79, 88]),
    ("Charlie", [65, 71, 68, 74]),
    ("Diana", [55, 63, 58, 61]),
    ("Ethan", [88, 84, 91, 87])
]

result = calculate_metrics(student_data)
print(f"Result: {result}")