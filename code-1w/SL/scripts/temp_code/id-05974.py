def calculate_final_score(students):
    total_score = 0
    bonus_applied = False
    for i, (name, score) in enumerate(students):
        if score >= 85 and not bonus_applied:
            score += 5  # performance bonus
            bonus_applied = True
        grade_letter = 'A' if score >= 90 else 'B' if score >= 80 else 'C'
        adjustment = 2 if grade_letter == 'A' and i % 2 == 0 else 0
        total_score += score + adjustment
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_length = sum(len(name) for name, _ in students) / len(students) if students else 0
    
    return total_score

# Dataset: student names and their initial scores
students = [
    ('Alice', 88),
    ('Bob', 92),
    ('Charlie', 76),
    ('Diana', 85),
    ('Evan', 94)
]

total_score = calculate_final_score(students)
print(f"Result: {total_score}")