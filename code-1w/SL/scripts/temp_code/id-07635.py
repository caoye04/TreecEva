def calculate_total(grades, adjustment):
    base_score = sum(grades)
    adjusted_bonus = adjustment(base_score)
    penalty = 0
    if base_score > 80:
        penalty = 5
    return base_score + adjusted_bonus - penalty

# Irrelevant string transformation (minor distraction)
user_input = "Alice"
formatted_name = user_input.lower().replace('a', 'A')

grades = [85, 90, 78, 92]
bonus_factor = 2
bonus_lambda = lambda x: (x * bonus_factor) // 10

# Key computation point
final_score = calculate_total(grades, bonus_lambda)
print(f"Result: {final_score}")