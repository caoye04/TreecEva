def calculate_final_score(points, penalties):
    base_score = points * 1.5
    deduction = penalties * 2.5
    adjusted_score = base_score - deduction
    
    # Apply bonus if performance is strong
    if adjusted_score > 75:
        adjusted_score += 10
    
    return int(adjusted_score)

# Simulate student assessment data
test_results = 'Pass'
raw_points = 80
penalty_count = 5
extra_credit = 0  # Not used in calculation (minor distraction)

final_score = calculate_final_score(raw_points, penalty_count)
print(f"Result: {final_score}")