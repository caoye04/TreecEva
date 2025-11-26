import collections

def analyze_student_grades(student_records, passing_grade):
    grade_counter = collections.Counter()
    processed_grades = []
    temp_calculations = []
    
    for record in student_records:
        adjusted_grade = record + 2
        temp_calculations.append(adjusted_grade * 0.5)
        if record >= passing_grade:
            grade_counter['pass'] += 1
            processed_grades.append(record * 1.1)
        else:
            grade_counter['fail'] += 1
            processed_grades.append(record * 0.9)
    
    irrelevant_sum = sum(temp_calculations)
    bonus_points = len([g for g in student_records if g > 85])
    
    if grade_counter['pass'] > grade_counter['fail']:
        base_score = sum(processed_grades) / len(processed_grades)
    else:
        base_score = sum(student_records) / len(student_records)
    
    final_score = round(base_score + bonus_points, 2)
    return final_score

grades_data = [78, 92, 65, 88, 71, 95, 82, 69, 87, 74]
threshold = 75

result = analyze_student_grades(grades_data, threshold)
print(f"Result: {result}")