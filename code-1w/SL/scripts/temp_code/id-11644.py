def calculate_final_score(students):
    total = 0
    count = 0
    threshold_name_length = 5
    bonus_points = 2

    for student in students:
        name = student['name']
        score = student['score']
        
        # Only consider students with longer names for scoring
        if len(name) > threshold_name_length:
            adjusted_score = score + bonus_points if name.endswith('a') else score
            total += adjusted_score
            count += 1
    
    return total // count if count > 0 else 0

# Irrelevant auxiliary data (mild distraction)
extra_data = [1, 2, 3]
dummy_flag = True

students = [
    {'name': 'Elena', 'score': 88},
    {'name': 'Thomas', 'score': 92},
    {'name': 'Sofia', 'score': 76},
    {'name': 'Marcus', 'score': 85},
    {'name': 'Lena', 'score': 90}
]

final_score = calculate_final_score(students)
print(f"Result: {final_score}")