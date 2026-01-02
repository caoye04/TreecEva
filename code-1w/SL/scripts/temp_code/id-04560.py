from collections import defaultdict

def calculate_final_score(ranks, coeffs):
    score_map = defaultdict(float)
    
    # Process each participant and their ranked performance
    for idx, (name, rank_list) in enumerate(ranks.items()):
        base_score = 0
        for i, rank in enumerate(rank_list):
            base_score += (i + 1) * rank  # Weighted sum of positions
        normalized = base_score / len(rank_list)
        score_map[name] = round(normalized, 3)
    
    # Apply external weighting based on experience level
    weighted_scores = []
    for name, score in score_map.items():
        weight = coeffs.get(name, 1.0)
        weighted_scores.append(score * weight)
    
    total = sum(weighted_scores)
    return int(total)

# Input data
rankings = {
    'Alice': [4, 2, 5],
    'Bob': [3, 3, 4],
    'Charlie': [5, 1, 3]
}

weights = {
    'Alice': 1.2,
    'Bob': 0.9,
    'Charlie': 1.1
}

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")