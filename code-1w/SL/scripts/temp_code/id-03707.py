def calculate_final_score(students):
    scores = []
    for i, (name, grades) in enumerate(students):
        avg_grade = sum(grades) / len(grades)
        bonus = 5 if avg_grade >= 85 else 0
        adjusted_score = avg_grade + bonus
        scores.append(adjusted_score)
    
    # Irrelevant utility: counts how many students have names starting with vowel
    vowel_names = [name for name in [s[0] for s in students] if name[0].lower() in 'aeiou']
    vowel_count = len(vowel_names)  # Distractor variable (minimal interference)

    total_score = sum(scores) / len(scores)  # Final average of adjusted scores
    return total_score

# Data setup
students_data = [
    ("Alice", [92, 88, 91]),
    ("Bob", [76, 81, 74]),
    ("Eve", [89, 85, 87]),
    ("Charlie", [73, 70, 75])
]

# Calculation
final_avg = calculate_final_score(students_data)

# Key variable assignment
total_score = final_avg

print(f"Result: {total_score}")