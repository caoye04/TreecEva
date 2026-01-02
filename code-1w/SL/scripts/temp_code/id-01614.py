def calculate_total(grades, extra):
    base = sum(grades)
    adjustment = (lambda x: x ** 2 if x < 5 else x)(len(grades))
    weighted_bonus = extra * 0.5 if len(grades) > 3 else extra
    return base + weighted_bonus + adjustment

# Irrelevant variable (minor distraction)
initial_threshold = 75

grades = [85, 90, 78, 92]
bonus = 10

# Key computation step
final_score = calculate_total(grades, bonus)
print(f"Result: {final_score}")