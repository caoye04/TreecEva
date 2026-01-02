def calculate_final_score(ranks, points):
    total_score = 0
    for i, (rank, pt) in enumerate(zip(ranks, points)):
        adjustment = 1 if rank <= 3 else 0.5
        bonus = 10 if i % 2 == 0 else 5
        total_score += pt * adjustment + bonus
    return total_score

# Simulated competition data
base_points = [25, 20, 15, 10, 5]
rankings = [1, 4, 2, 6, 3]
extraneous_data = [99, 88, 77]  # Unused

# Key computation
final_result = calculate_final_score(rankings, base_points)
total_score = final_result

print(f"Result: {total_score}")