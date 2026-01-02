def analyze_performance(raw_marks, weight_factor=1.2):
    raw_total = sum(raw_marks)
    adjusted_marks = [mark * weight_factor for mark in raw_marks]
    normalized_marks = [mark / max(adjusted_marks) * 100 for mark in adjusted_marks]
    
    # Irrelevant tracking variable (minor distraction)
    high_performer_count = len([m for m in normalized_marks if m >= 85])
    
    categories = ['A', 'B', 'C', 'D', 'F']
    bin_edges = [0, 60, 75, 85, 95, 100]
    
    # Create score bins using slicing and zip
    score_ranges = list(zip(bin_edges[:-1], bin_edges[1:]))
    distribution = {cat: 0 for cat in categories}
    
    for score in normalized_marks:
        for i, (low, high) in enumerate(score_ranges):
            if low <= score < high:
                distribution[categories[i]] += 1
                break

    # Compute final evaluation metrics
    passing_scores = [s for s in normalized_marks if s >= 60]
    normalized_scores = passing_scores if passing_scores else [0]
    
    # Key statement
    threshold_score = max(normalized_scores)
    
    # Print result for verification
    print(f"Result: {threshold_score}")
    
    return threshold_score

# Input data
exam_results = [78, 82, 91, 63, 85]
analyze_performance(exam_results)