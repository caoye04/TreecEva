base_score = 185
bonus_points = 42
max_possible = 200

# Calculate final score with modular arithmetic
final_score = (base_score + bonus_points) % max_possible

print(f"Result: {final_score}")