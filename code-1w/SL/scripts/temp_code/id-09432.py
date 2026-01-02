def calculate_final_score(grades, multiplier):
    base_sum = sum(grades.values())
    adjustments = 0
    for idx, (subject, score) in enumerate(zip(grades.keys(), grades.values())):
        if idx % 2 == 1:
            adjustments += len(subject) * 0.5
    weighted_bonus = multiplier * (base_sum / 10)
    return int(base_sum + adjustments + weighted_bonus)

# Irrelevant distraction variable
interim_result = "processing"

grades = {'math': 88, 'physics': 94, 'chemistry': 85, 'biology': 90}
bonus_multiplier = 1.2

# Key computation step
total_score = calculate_final_score(grades, bonus_multiplier)
print(f"Result: {total_score}")