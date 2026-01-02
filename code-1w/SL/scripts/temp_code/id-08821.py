def calculate_final_score(students):
    total_scores = []
    bonus_applied = 0
    
    for i, (name, score) in enumerate(students):
        adjusted_score = score + len(name)
        if adjusted_score % 2 == 0:
            adjusted_score += 3
            bonus_applied += 1
        total_scores.append(adjusted_score)
    
    avg_base = sum(score for _, score in students) / len(students)
    total_adjusted = sum(total_scores)
    final_score = total_adjusted - avg_base
    
    # Irrelevant string operation (minor distraction)
    status = "Processed: " + ", ".join(name.title() for name, _ in students)
    status_len = len(status)
    
    return int(final_score)

# Dataset
students_data = [
    ('alice', 76),
    ('bob', 85),
    ('charlie', 90),
    ('diana', 83)
]

final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")