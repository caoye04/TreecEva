def evaluate_performance():
    raw_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    # Calculate weighted base scores
    base_ratings = [score * weight for score, weight in zip(raw_scores, weights)]
    
    # Bonus adjustment based on position
    adjustments = []
    for i, rating in enumerate(base_ratings):
        if i % 2 == 0:
            adjustments.append(rating * 0.1)
        else:
            adjustments.append(rating * 0.05)
    
    # Apply adjustments
    adjusted_ratings = [base + adj for base, adj in zip(base_ratings, adjustments)]
    
    # Final aggregation
    total_score = sum(adjusted_ratings)
    
    # Irrelevant tracking variable (minimal distraction)
    final_count = len(adjusted_ratings)
    
    print(f"Result: {total_score}")

evaluate_performance()