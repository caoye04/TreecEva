def calculate_weighted_score():
    # Simulating a ranked scoring system where position affects contribution
    scores = [8, 12, 5, 17, 3]
    weights = [2, 1, 3, 0, 4]
    offset = 7
    dummy_var = [x * 0 for x in weights]  # Irrelevant computation (distractor)

    total_score = 0
    for index, (score, weight) in enumerate(zip(scores, weights)):
        if weight % 2 == 0:
            points = [score + offset, score - 2, score // 2]
            total_score += points[index % len(points)] * (index + 1)
    
    return total_score

result = calculate_weighted_score()
print(f"Result: {result}")