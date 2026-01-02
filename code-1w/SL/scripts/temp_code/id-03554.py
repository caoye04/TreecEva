subjects = ['math', 'physics', 'chemistry', 'biology']
grades = [85, 92, 78, 88]
weights = {'math': 0.3, 'physics': 0.25, 'chemistry': 0.2, 'biology': 0.25}

# Normalize grades to weighted scores
weighted_grades = [grades[i] * weights[subj] for i, subj in enumerate(subjects)]

# Apply curve: add 5 points, cap at 100
curved_grades = [min(100, g + 5) for g in weighted_grades]

# Filter passing grades (above 75)
passing_grades = [g for g in curved_grades if g > 75]

# Unrelated distraction variables
student_id = 12345
enrollment_year = 2023
temp_result = "N/A"

# Process final scores with offset correction
offset = 2.5
processed_grades = [g - offset for g in passing_grades]

total_score = sum(processed_grades)
print(f"Result: {total_score}")