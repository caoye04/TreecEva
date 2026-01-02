def calculate_final_score(rank, points):
    bonus = 10 if rank <= 3 else (5 if rank <= 10 else 0)
    multiplier = 2 if rank <= 2 else 1
    adjusted_points = points * multiplier
    return adjusted_points + bonus

# Competition scoring logic
rank = 4
base_points = 85
previous_winner = True
consolation_prize = 5  # Irrelevant to final score calculation

# Key statement
total_score = calculate_final_score(rank, base_points)

# Output result
print(f"Result: {total_score}")