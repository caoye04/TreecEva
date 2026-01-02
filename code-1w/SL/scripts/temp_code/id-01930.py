def calculate_final_score():
    scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    points = [10, -5, 20, 15, -10]
    indices = ['first', 'second', 'third', 'fourth', 'fifth']
    
    # Irrelevant variable (minor distraction)
    max_score = max(scores)
    
    index_map = {i: len(indices[i]) for i in range(len(indices))}
    total_score = sum(s * w for s, w in zip(scores, weights))
    
    for i in range(len(points)):
        if i % 2 == 0 and points[i] > 0:
            total_score += points[i] * (index_map[i] if index_map[i] > 0 else 1)
        else:
            total_score -= abs(points[i]) // 2
    
    Result: total_score

calculate_final_score()