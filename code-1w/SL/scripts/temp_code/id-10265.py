def calculate_weighted_score():
    # Simulating a scoring system where earlier achievements are weighted more
    points = [10, -5, 8, 12, -3]
    weights = [0] * len(points)
    total_score = 0
    
    for i, (val, idx) in enumerate(zip(points, range(len(points)))):
        if val > 0:
            index = len(points) - i  # Later entries get smaller positional index
            total_score += points[i] * (index + 1)
            weights[i] = index + 1
        else:
            # Negative points are logged but not added
            weights[i] = 0
    
    # Irrelevant tracking variable (minor distraction)
    max_weight = max(weights) if weights else 0
    
    print(f"Result: {total_score}")

calculate_weighted_score()