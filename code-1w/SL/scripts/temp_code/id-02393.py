def calculate_total(grades, bonus_factors):
    base_total = sum(grades)
    adjusted_bonus = [factor * 1.5 for factor in bonus_factors if factor > 0]
    extra_credit = sum(adjusted_bonus)
    return base_total + extra_credit

# Student marks and adjustment factors
test_marks = [78, 85, 90]
adjustments = [2, -1, 3, 0]

# Irrelevant string operation (minor distraction)
discipline_status = 'good'.upper()

final_score = calculate_total(test_marks, adjustments)
print(f"Result: {final_score}")