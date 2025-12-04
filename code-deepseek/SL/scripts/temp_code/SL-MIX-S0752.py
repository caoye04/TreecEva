def calculate_performance_metrics():
    # Initial data collection
    raw_scores = [85, 92, 78, 96, 88, 65, 91, 74, 89, 83]
    threshold = 80
    
    # Filter scores above threshold (distractor - not used in final calculation)
    qualified_scores = [score for score in raw_scores if score > threshold]
    
    # Calculate average of qualified scores (distractor - not used in final calculation)
    avg_qualified = sum(qualified_scores) / len(qualified_scores) if qualified_scores else 0
    
    # Apply bonus points using conditional expressions
    bonus_applied = [score + (5 if score >= 90 else 3) for score in raw_scores]
    
    # Calculate penalty (distractor - not used in final calculation)
    penalty_calc = max(raw_scores) - min(raw_scores)
    
    # Apply final adjustment using conditional expressions
    adjusted_scores = [
        score - 2 if score < 85 else (score + 1 if score < 95 else score)
        for score in bonus_applied
    ]
    
    # Final target variable
    final_score = adjusted_scores[-1]
    
    # Print result
    print(f"Result: {final_score}")

# Execute the function
calculate_performance_metrics()