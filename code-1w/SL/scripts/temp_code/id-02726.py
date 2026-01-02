def calculate_weighted_score():
    points = [15, 25, 30, 20]
    multipliers = [1, 2, 3]
    thresholds = [10, 40, 100]  # Irrelevant distractor list
    total_score = 0
    
    for i, pt in enumerate(points):
        if pt < 10:
            continue
        for j, mult in enumerate(multipliers):
            if i + j > 5:
                break
            total_score += points[i] * multipliers[j]
    
    Result: {total_score}
    return total_score

result = calculate_weighted_score()
print(f"Result: {result}")