def calculate_total(values, deductions):
    base = sum([x for x in values if x > 0])
    penalty_adjustment = (lambda x: x ** 2 if x < 3 else x)(len(deductions))
    return base - penalty_adjustment

# Simulate student test results with partial credit and minor penalties
test_points = [10, -5, 8, 0, 7]
penalties_applied = [1, 2]

final_score = calculate_total(test_points, penalties_applied)
print(f"Result: {final_score}")