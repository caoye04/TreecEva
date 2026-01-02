def calculate_final_score(ranks, points):
    adjusted = [points / (i + 1) for i in range(len(ranks))]
    bonuses = [val * 0.5 if rank <= 3 else val * 0.1 for rank, val in zip(ranks, adjusted)]
    total = sum(bonuses)
    penalty = 10 if len(ranks) > 5 else 0
    return int(total - penalty)

# Simulated competition rankings and base points
rankings = [1, 4, 2, 6, 3, 8]
base_points = 100

final_score = calculate_final_score(rankings, base_points)
print(f"Result: {final_score}")