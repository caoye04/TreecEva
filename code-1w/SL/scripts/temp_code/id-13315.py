def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_total = sum([d for d in deductions if d > 0])
    adjustment = len(points) // 2
    return base - penalty_total + adjustment

# Data from user assessment
raw_points = [85, 90, 78, 92]
penalties = [5, 0, 3]
extra_attempts = 2  # Irrelevant variable (minimal interference)

# Compute final score
total_possible = 400  # Distractor: not used in calculation
final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")