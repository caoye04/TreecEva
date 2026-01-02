def calculate_final_score(scores, deductions):
    base_total = sum(scores)
    penalty_sum = sum(deductions) if len(deductions) > 0 else 0
    adjusted = base_total - penalty_sum
    
    # Apply bonus if performance set is exceptional (above threshold)
    performance_set = {s for s in scores if s >= 90}
    bonus = 10 if len(performance_set) >= 3 else 0
    
    return adjusted + bonus

# Input data
test_results = [85, 92, 95, 87, 90]
fine_prints = ["A", "B", "C"]  # Irrelevant string data (minimal distraction)
penalty_points = [5, 3]

# Computation
raw_scores = test_results
penalties = penalty_points
final_score = calculate_final_score(raw_scores, penalties)
print(f"Result: {final_score}")