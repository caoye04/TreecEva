def analyze_product_performance():
    base_ratings = [4.2, 3.8, 4.5, 4.0, 3.9]
    sales_volume = [120, 200, 90, 180, 150]
    thresholds = {'high': 150, 'medium': 100}
    
    # Irrelevant transformation (distractor)
    adjusted_sales = [x * 1.1 for x in sales_volume if x > 100]
    temp_offsets = [0.1 * i for i in range(len(adjusted_sales))]
    
    # Real computation begins
    weighted_rating = 0.0
    total_weight = 0
    for i, rating in enumerate(base_ratings):
        weight = 1 + (sales_volume[i] / sum(sales_volume))
        weighted_rating += rating * weight
        total_weight += weight
    
    avg_weighted_rating = weighted_rating / total_weight
    
    # Normalize ratings based on relative performance
    normalized_ratings = []
    for i, (rating, sale) in enumerate(zip(base_ratings, sales_volume)):
        bonus = 0.2 if sale > thresholds['high'] else 0.1 if sale > thresholds['medium'] else 0
        normalized = min(rating + bonus, 5.0)
        normalized_ratings.append(round(normalized, 2))
    
    # Secondary distractor: unused state tracking
    status_log = {}
    for idx, val in enumerate(normalized_ratings):
        status_log[f'entry_{idx}'] = 'flagged' if val < 4.0 else 'normal'
    
    peak_season_multiplier = 1.15
    off_peak_discount = 0.95
    season_factor = peak_season_multiplier  # Assume peak season
    
    # Key statement with target variable
    adjustment_factor = season_factor if sum(sales_volume) > 500 else off_peak_discount
    final_score = max(normalized_ratings) * adjustment_factor
    
    # Red herring computation
    projected_growth = (final_score * 0.05) * len([v for v in sales_volume if v > 150])
    
    print(f"Result: {final_score}")

analyze_product_performance()