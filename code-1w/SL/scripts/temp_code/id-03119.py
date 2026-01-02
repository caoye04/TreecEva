def calculate_final_score(students):
    # Extract passing students with grades >= 75 using list comprehension
    passing = [s for s in students if s['grade'] >= 75]
    
    # Calculate bonus based on attendance using conditional expression
    bonus = sum(2 if s['attendance'] > 90 else 1 for s in passing)
    
    # Compute base score from average grade of passing students
    base_score = sum(s['grade'] for s in passing) / len(passing) if passing else 0
    
    # Final score calculation
    final_score = base_score + bonus
    return final_score

# Dataset of student records
students = [
    {'name': 'Alice', 'grade': 85, 'attendance': 95},
    {'name': 'Bob', 'grade': 67, 'attendance': 88},
    {'name': 'Charlie', 'grade': 90, 'attendance': 92},
    {'name': 'Diana', 'grade': 78, 'attendance': 85},
    {'name': 'Eve', 'grade': 94, 'attendance': 96}
]

# Compute final score
final_score = calculate_final_score(students)
print(f"Result: {final_score}")