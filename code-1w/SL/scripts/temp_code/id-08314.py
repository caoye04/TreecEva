def calculate_weighted_score():
    # Simulating a scoring system where positions and multipliers matter
    points = [10, -5, 8, 12, -3]
    weights = [1, 2, 1, 3, 2]
    total_score = 0
    adjustment_factor = 0.5  # Irrelevant to final result, minor distraction

    for index, (val, weight) in enumerate(zip(points, weights)):
        if val > 0:
            total_score += points[index] * (index + 1)
        else:
            total_score -= abs(val)
    
    # Final scaling (not applied, just present)
    final_scaling = len(points) * adjustment_factor  # Unused

    print(f"Result: {total_score}")

calculate_weighted_score()