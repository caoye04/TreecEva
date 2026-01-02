tasks_completed = 8
min_required = 5
target = 7
base_points = 150
adjustment_factor = 1.2
adjusted_base = base_points * adjustment_factor

# Bonus logic based on performance
difficulty_level = 3
bonus = 25 if difficulty_level > 2 else 10

completed_tasks = tasks_completed

# Critical statement
final_score = adjusted_base + (bonus if completed_tasks >= target else 0)

print(f"Result: {final_score}")