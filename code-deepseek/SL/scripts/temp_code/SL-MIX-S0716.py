def process_student_data(students, scores):
    # Irrelevant dictionary initialization
    temp_dict = {'a': 15, 'b': 27, 'c': 33, 'd': 42}
    dummy_sum = sum(temp_dict.values())
    
    # Main processing with zip and enumerate
    student_grades = {}
    grade_total = 0
    irrelevant_counter = 0
    
    for idx, (student, score) in enumerate(zip(students, scores)):
        # Distractor: unused condition
        if idx % 2 == 0:
            irrelevant_counter += 1
        
        # Actual grade calculation with complex logic
        if score >= 90:
            grade = 'A'
            bonus = 5
        elif score >= 80:
            grade = 'B'
            bonus = 3
        elif score >= 70:
            grade = 'C'
            bonus = 1
        else:
            grade = 'F'
            bonus = -2
        
        # Misleading intermediate calculation
        temp_adjustment = (idx * 2) - 1
        
        # Store grade and accumulate total
        student_grades[student] = grade
        grade_total += score + bonus
        
        # Dead code path - never executed
        if score > 200:
            grade_total *= 2
    
    # Additional irrelevant processing
    string_ops = ['python', 'java', 'cpp']
    concat_result = ''.join([s.upper() for s in string_ops])
    
    # Final result calculation
    average_grade = grade_total / len(students)
    adjustment_factor = len([s for s in student_grades.values() if s == 'A'])
    final_result = round((average_grade * adjustment_factor) - (dummy_sum % 10), 2)
    
    return final_result

# Main execution
students = ['Alice', 'Bob', 'Charlie', 'Diana']
scores = [92, 85, 78, 95]

# Misleading variable assignment
intermediate_value = sum(scores) + len(students) * 10
unused_calc = intermediate_value // 3

# Key statement
result = process_student_data(students, scores)
final_result = result + (len(students) % 2)

print(f"Target result: {final_result}")