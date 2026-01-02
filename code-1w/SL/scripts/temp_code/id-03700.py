def calculate_final_score(students):
    total_score = 0
    bonus_multiplier = 1.1  # Unused in logic path, minor distraction
    score_map = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
    
    for i, (name, grade) in enumerate(students):
        base_score = score_map[grade]
        adjustment = 5 if i % 2 == 0 else -5
        total_score += base_score + adjustment
    
    extra_point_award = sum(1 for _, grade in students if grade == 'A')  # Distractor
    return int(total_score)

students = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A')]
total_score = calculate_final_score(students)
print(f"Result: {total_score}")