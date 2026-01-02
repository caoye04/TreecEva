def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = sum([d * 2 for d in deductions if d > 0])
    adjustment = len(set(points))  # bonus for unique scores
    return base_score - penalty_total + adjustment

# Simulation data
raw_points = [85, 90, 78, 90, 82]
penalties = [5, 0, 3]

initial_total = sum(raw_points)  # irrelevant tracking variable
note = "Processing complete"  # unused metadata

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")