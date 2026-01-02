def calculate_final_score(points, deductions):
    base = sum(points)
    penalty_sum = sum([d for d in deductions if d > 0])
    adjustment = -penalty_sum * 0.5 if penalty_sum > 0 else 0
    final = base + adjustment
    return int(final)

# Simulate student assessment results
test_results = [85, 92, 78, 96]
homework_results = [88, 76, 90]
raw_points = test_results + homework_results

# Track irrelevant metric for consistency check (not used in final score)
consistency_ratio = len(test_results) / (len(test_results) + len(homework_results))

penalties = [5, 0, 3, 2]  # Late submission penalties
is_excessive = any(p > 4 for p in penalties)

# Compute final score
total_score = calculate_final_score(raw_points, penalties)

print(f"Result: {total_score}")