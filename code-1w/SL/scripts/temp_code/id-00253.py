def analyze_performance():
    raw_scores = [85, 90, 78, 92, 88, 76, 95]
    threshold = 85
    
    # Normalize scores around the threshold
    adjusted_scores = [score - threshold for score in raw_scores]
    
    # Identify performances above threshold
    positive_impact = {i for i, val in enumerate(adjusted_scores) if val > 0}
    
    # Extract original scores for high performers
    high_performers = [raw_scores[i] for i in positive_impact]
    
    # Apply experience bonus: +2 for each score over 90
    bonus_applied = [
        score + 2 if score > 90 else score
        for score in high_performers
    ]
    
    # Filter only those with bonus adjustments
    filtered_performance = [val for val in bonus_applied if val != 90]
    
    final_score = sum(filtered_performance)
    return final_score

result = analyze_performance()
print(f"Result: {result}")