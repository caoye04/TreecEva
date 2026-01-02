def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = sum([d * 2 for d in deductions if d > 0])
    adjustment = len(points) % 4
    return base_score - penalty_total + adjustment

# Simulation data from user activity tracking
raw_points = [15, 23, 8, 19, 31]
penalties = [3, 0, 5, 2]
extra_flags = ['A', 'C']  # Irrelevant metadata
initial_count = len(raw_points)  # Minor distraction

# Core computation
final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")