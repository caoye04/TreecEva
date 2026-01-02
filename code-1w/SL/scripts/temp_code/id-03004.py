def analyze_performance(ratings, threshold=5):
    """Analyze user ratings and compute adjusted performance score."""
    total_entries = len(ratings)
    filtered_ratings = [r for r in ratings if r >= threshold]
    valid_count = len(filtered_ratings)
    
    # Normalize ratings to 0-1 scale
    min_rating = min(ratings)
    max_rating = max(ratings)
    rating_range = max_rating - min_rating if max_rating != min_rating else 1
    normalized_ratings = [(r - min_rating) / rating_range for r in ratings]
    
    # Calculate base metrics
    average_normalized = sum(normalized_ratings) / len(normalized_ratings)
    high_performance_count = sum(1 for nr in normalized_ratings if nr > 0.7)
    
    # Adjustment logic based on distribution
    if high_performance_count / total_entries > 0.5:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.9
    
    final_score = max(normalized_ratings) * adjustment_factor
    
    # Irrelevant distraction: string processing unrelated to final_score
    status_label = "PERFORMANCE REVIEW"
    cleaned_label = status_label.lower().replace(" ", "_").strip()
    label_length = len(cleaned_label)
    
    print(f"Result: {final_score}")

# Execute with sample data
data_input = [3, 7, 8, 6, 9, 7, 8]
analyze_performance(data_input)