def analyze_performance():
    raw_scores = [88, 92, 76, 85, 94, 90, 83]
    passing_grade = 85
    
    # Calculate average for reference
    avg_score = sum(raw_scores) / len(raw_scores)
    
    # Irrelevant intermediate (minimal distraction)
    adjusted_scores = [score * 1.05 for score in raw_scores]
    
    # Core logic: filter scores above average
    filtered_scores = [score for score in raw_scores if score > avg_score]
    
    # Key assignment point
    threshold_score = max(filtered_scores)
    
    print(f"Result: {threshold_score}")

analyze_performance()