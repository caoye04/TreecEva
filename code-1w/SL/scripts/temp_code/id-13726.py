def analyze_performance():
    raw_scores = [88, 92, 76, 94, 85, 90, 70, 80]
    thresholds = {'min_pass': 75, 'excellence': 90}
    
    # Normalize scores to a 0-100 scale (already are, but simulate adjustment)
    adjusted_scores = [score * 1.0 for score in raw_scores]
    
    # Identify high performers above excellence threshold
    high_performers = [score for score in adjusted_scores if score >= thresholds['excellence']]
    
    # Filter out below-minimum passing scores
    passing_scores = [score for score in adjusted_scores if score >= thresholds['min_pass']]
    
    # Apply performance decay for consecutive high scores (simulate fatigue)
    decayed_scores = []
    for i, score in enumerate(passing_scores):
        if i > 0 and passing_scores[i-1] >= thresholds['excellence']:
            decayed_scores.append(score * 0.95)
        else:
            decayed_scores.append(score)
    
    # Extract recent performance (last 5) using slicing
    recent_performance = decayed_scores[-5:]
    
    # Further filter based on consistency (within 10 points of median)
    sorted_recent = sorted(recent_performance)
    median = sorted_recent[len(sorted_recent)//2]
    filtered_performance = [s for s in recent_performance if abs(s - median) <= 10]
    
    total_score = sum(filtered_performance)
    return total_score

result = analyze_performance()
print(f"Result: {result}")