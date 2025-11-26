def calculate_weighted_average(scores, weights):
    weighted_sum = 0
    total_weight = 0
    for i in range(len(scores)):
        weighted_sum += scores[i] * weights[i]
        total_weight += weights[i]
    return weighted_sum / total_weight if total_weight != 0 else 0

def process_review_data():
    raw_reviews = [85, 92, 78, 96, 88, 67, 91, 84, 79, 95]
    review_weights = [1, 2, 1, 3, 2, 1, 2, 1, 1, 3]
    
    # Irrelevant processing for distraction
    temp_scores = [score * 1.1 for score in raw_reviews[:5]]
    dummy_avg = sum(temp_scores) / len(temp_scores)
    
    # Main calculation
    weighted_avg = calculate_weighted_average(raw_reviews, review_weights)
    
    # More distractions
    review_dict = {i: score for i, score in enumerate(raw_reviews)}
    irrelevant_max = max(review_dict.values())
    
    # Key processing steps
    filtered_scores = [score for score in raw_reviews if score >= 80]
    filtered_weights = [review_weights[i] for i, score in enumerate(raw_reviews) if score >= 80]
    
    if len(filtered_scores) > 0:
        filtered_avg = calculate_weighted_average(filtered_scores, filtered_weights)
    else:
        filtered_avg = 0
    
    # Final aggregation with slicing operations
    aggregated_scores = [weighted_avg, filtered_avg, irrelevant_max]
    processed_indices = [0, 2, 1]
    
    # Dead code path
    if dummy_avg > 100:
        aggregated_scores[1] = 42
    
    # Target statement
    final_rating = aggregated_scores[processed_indices[1]]
    
    print(f"Result: {final_rating}")
    return final_rating

process_review_data()