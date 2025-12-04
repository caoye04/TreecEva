def process_grades(raw_grades):
    # Convert letter grades to numeric values
    grade_map = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    numeric_grades = [grade_map[grade] for grade in raw_grades if grade in grade_map]
    
    # Apply bonus for grades above C
    bonus_grades = [grade + 0.5 if grade > 2.0 else grade for grade in numeric_grades]
    
    # Remove lowest grade and calculate final score
    if bonus_grades:
        processed_values = sorted(bonus_grades)[1:]
        final_score = sum(processed_values)
    else:
        final_score = 0
    
    print(f"Final result: {final_score}")
    return final_score

# Input data
student_grades = ['A', 'B', 'C', 'A', 'B']
final_score = process_grades(student_grades)