def analyze_product_reviews():
    # Product review analysis system
    review_scores = [85, 92, 78, 96, 88, 74, 95, 81, 90, 77]
    threshold = 80
    
    # Calculate average (distractor - not used in final result)
    avg_score = sum(review_scores) / len(review_scores)
    
    # Filter high-quality reviews using list comprehension
    ratings_filtered = [score for score in review_scores if score >= threshold]
    
    # Calculate rating adjustment based on distribution
    rating_range = max(ratings_filtered) - min(ratings_filtered)
    adjustment_factor = rating_range // 5  # This is relevant
    
    # Unnecessary intermediate calculation (distractor)
    median_check = sorted(ratings_filtered)[len(ratings_filtered) // 2]
    
    # Final rating calculation
    final_rating = max(ratings_filtered) - adjustment_factor
    
    # Print result for verification
    print(f"Result: {final_rating}")
    return final_rating

# Execute the function
final_result = analyze_product_reviews()