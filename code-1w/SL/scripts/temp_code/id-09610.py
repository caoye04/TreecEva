def analyze_product_performance():
    # Simulated product ratings and weights
    raw_ratings = [4.2, 3.8, 4.5, 4.0, 3.9, 4.3, 4.1]
    weights = [0.2, 0.3, 0.1, 0.15, 0.05, 0.1, 0.1]

    # Irrelevant backup list (distractor)
    backup_ratings = [r * 2 for r in raw_ratings if r > 4.0]

    # Weighted average calculation
    weighted_avg = sum(r * w for r, w in zip(raw_ratings, weights))

    # Normalization factor based on min-max scaling
    min_rating = min(raw_ratings)
    max_rating = max(raw_ratings)
    normalized_ratings = [(r - min_rating) / (max_rating - min_rating) for r in raw_ratings]

    # Secondary processing: count high performers
    high_performers = 0
    for i, rating in enumerate(normalized_ratings):
        if rating >= 0.75:
            high_performers += 1

    # Adjustment logic based on performance spread
    rating_spread = max_rating - min_rating
    if rating_spread > 0.6:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.95

    # Final scoring with key assignment
    final_score = max(normalized_ratings) * adjustment_factor

    # Dead code path (distractor)
    if False:
        final_score *= 0.8
        temp = [x for x in backup_ratings if x < 5.0]
        _ = sum(temp) // 2 if temp else 0

    # Print result as required
    print(f"Result: {final_score}")

analyze_product_performance()