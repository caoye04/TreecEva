def calculate_weighted_score(scores):
    total_score = 0
    offset = 2  # Irrelevant variable (minimal distraction)
    scaling = 1.0  # Irrelevant variable (minimal distraction)
    
    points = [s + 1 for s in scores]
    indices = list(range(len(points)))
    
    for index, score_val in enumerate(points):
        if score_val % 2 == 0:
            total_score += points[index] * (index + 1)
        else:
            total_score -= points[index] // 2
    
    extra = sum(1 for x in points if x > 3)  # Slight distraction, not used in main logic
    return total_score

result = calculate_weighted_score([4, -1, 3, 0, 2])
print(f"Result: {result}")