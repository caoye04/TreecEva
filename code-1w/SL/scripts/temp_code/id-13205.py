def calculate_final_score(points, penalties):
    base_score = points * 1.5
    deduction = penalties * 10
    if base_score > 100:
        base_score = 100
    adjusted_score = base_score - deduction
    return round(adjusted_score, 2)

# Simulate student assessment results
test_results = "Pass"
raw_points = 75
penalty_count = 3
extra_time_used = False

final_score = calculate_final_score(raw_points, penalty_count)

# Output result
print(f"Result: {final_score}")