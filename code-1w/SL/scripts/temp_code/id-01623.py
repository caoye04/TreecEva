from itertools import accumulate

def calculate_final_score(rank, raw_points):
    # Apply diminishing returns to points based on rank
    scaling_factor = 1 / (rank + 1)
    adjusted_points = [p * scaling_factor for p in raw_points]
    
    # Compute cumulative progression of points
    cumul_progress = list(accumulate(adjusted_points))
    
    # Bonus logic: if top performer (rank == 0), add average of cumulative progression
    bonus = 0
    if rank == 0 and len(cumul_progress) > 0:
        avg_progress = sum(cumul_progress) / len(cumul_progress)
        bonus = avg_progress * 0.5

    final_score = int(sum(adjusted_points) + bonus)
    return final_score

# Simulation data
rank = 1
base_points = [10, 20, 30, 40]
offset_correction = 5
points = [p - offset_correction for p in base_points]  # Irrelevant adjustment (minor distraction)

final_score = calculate_final_score(rank, points)
print(f"Result: {final_score}")