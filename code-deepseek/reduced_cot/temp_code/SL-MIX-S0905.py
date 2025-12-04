performance_rating = 9
base_score = 85
bonus_points = 15
penalty = 10
# Calculate final score based on performance
final_score = base_score + bonus_points if performance_rating > 8 else base_score - penalty
print(f"Result: {final_score}")