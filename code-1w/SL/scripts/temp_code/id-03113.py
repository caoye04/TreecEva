from itertools import accumulate

def calculate_final_score(points, deductions):
    # Apply cumulative penalty reduction to raw points
    adjusted = [p - d for p, d in zip(points, deductions)]
    running_total = list(accumulate(adjusted))
    peak_performance = max(running_total)
    final_score = peak_performance // len(running_total)
    return final_score

# Simulate student assessment data
raw_points = [85, 90, 78, 92, 88]
penalties = [5, 8, 6, 10, 4]

# Irrelevant distraction: unused variable
baseline_average = sum(raw_points) / len(raw_points)

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")