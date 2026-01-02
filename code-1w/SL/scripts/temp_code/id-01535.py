def calculate_final_score(students, bonus):
    total_score = 0
    scores = []
    for student in students:
        base = student['grade']
        extra = len(student['name'])
        if base >= 70:
            scores.append(base + extra)
    for idx, val in enumerate(scores):
        total_score += val * (idx + 1)
    total_score += bonus
    return total_score

# Irrelevant auxiliary data (minor distraction)
subjects = ['math', 'science', 'english']
dummy_map = {i: s.upper() for i, s in enumerate(subjects)}

# Main input data
data_input = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 90},
    {'name': 'Charlie', 'grade': 65},
    {'name': 'Diana', 'grade': 78}
]
bonus_points = 7

result = calculate_final_score(data_input, bonus_points)
print(f"Result: {result}")