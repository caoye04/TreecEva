def calculate_total(grades, adjustment):
    base_total = sum(grades)
    adjusted = list(map(lambda x: x * 1.1 if x < 75 else x, grades))
    bonus = adjustment(base_total)
    return int(base_total + sum(adjusted) / len(adjusted) + bonus)

# Irrelevant distraction: unused variable
placeholder = "debug_mode_off"

# Main data
grades = [88, 72, 91, 65, 83]
scaling_factor = 0.05

# Bonus logic with lambda
bonus_lambda = lambda total: 5 if total > 300 else 10

# Execution point of interest
final_score = calculate_total(grades, bonus_lambda)

# Output result
print(f"Result: {final_score}")