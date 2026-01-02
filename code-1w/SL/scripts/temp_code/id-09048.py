def calculate_final_score(students):
    total_score = 0
    bonus_applied = False
    for i, (name, score) in enumerate(zip(students.keys(), students.values())):
        if score >= 85:
            total_score += score + 5
            bonus_applied = True
        elif score >= 70:
            total_score += score + 2
        else:
            total_score += score
    
    # Irrelevant tracking variable (minor distraction)
    average_length = sum(len(name) for name in students.keys()) / len(students)
    
    return total_score

students = {
    'Alice': 92,
    'Bob': 78,
    'Charlie': 67,
    'Diana': 85,
    'Eve': 90
}

total_score = calculate_final_score(students)
print(f"Target result: {total_score}")