def calculate_final_score(students):
    total_scores = []
    bonus_applied = 0
    for i, (name, score, active) in enumerate(students):
        if not active:
            continue
        adjusted_score = score + (5 if score < 70 else 0)
        rank = i + 1  # Rank based on order
        if adjusted_score >= 85 and bonus_applied < 2:
            adjusted_score += 3
            bonus_applied += 1
        total_scores.append(adjusted_score)
    
    avg_score = sum(total_scores) / len(total_scores) if total_scores else 0
    extra_credit = 7 if any(s >= 95 for s in total_scores) else 0
    final_average = avg_score + extra_credit
    return round(final_average)

# Irrelevant utility function (minor distraction)
def format_name(name):
    return name.strip().title()

# Main data
students_data = [
    ("Alice", 88, True),
    ("Bob", 65, True),
    ("Charlie", 92, False),
    ("Diana", 84, True),
    ("Eve", 96, True)
]

base_avg = sum(s[1] for s in students_data if s[2]) / len([s for s in students_data if s[2]])
count_high = len([s for s in students_data if s[1] > 90])

final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")