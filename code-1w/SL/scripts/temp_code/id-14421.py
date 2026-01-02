def analyze_product_performance():
    base_ratings = [4.2, 3.8, 4.5, 4.0, 3.9]
    sales_volume = [120, 200, 90, 180, 140]
    weights = [0.6, 0.8, 0.5, 0.7, 0.9]

    # Irrelevant transformation (distractor)
    adjusted_weights = [w ** 2 for w in weights if w > 0.5]
    temp_sum = sum(adjusted_weights[:3])

    # Core logic: compute weighted normalized ratings
    total_sales = sum(sales_volume)
    normalized_sales = [s / total_sales for s in sales_volume]

    normalized_ratings = []
    for i, rating in enumerate(base_ratings):
        contribution = rating * normalized_sales[i] * 100
        normalized_ratings.append(contribution)

    # Secondary distraction: unused data structure manipulation
    sales_pairs = list(zip(base_ratings, sales_volume))
    high_performers = {idx: rate for idx, rate in enumerate(base_ratings) if rate >= 4.0}
    avg_rating = sum(base_ratings) / len(base_ratings)

    # Real computation continues
    aggregate_score = sum(normalized_ratings)
    performance_bins = [0, 0, 0, 0, 0]
    for i, nr in enumerate(normalized_ratings):
        bin_index = min(int(nr // 10), 4)
        performance_bins[bin_index] += 1

    # Boost factor depends on max normalized rating
    peak_normalized = max(normalized_ratings)
    boost_factor = 1.0
    if peak_normalized > 40:
        boost_factor = 1.2
    elif peak_normalized > 30:
        boost_factor = 1.1

    # Key assignment
    final_score = max(normalized_ratings) * boost_factor

    # Dead code path (distractor)
    if len(performance_bins) > 10:
        fallback = sum(performance_bins) / 100
    else:
        pass  # Placeholder

    print(f"Result: {final_score}")

analyze_product_performance()