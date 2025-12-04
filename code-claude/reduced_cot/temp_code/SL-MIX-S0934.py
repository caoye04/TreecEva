import itertools

# Image processing threshold analysis
def analyze_thresholds(data_points, thresholds):
    # Analyze various thresholds for image segmentation
    results = {}
    reference_value = 75  # Baseline reference value
    
    # Process each threshold
    for t in thresholds:
        # Calculate quality metrics for this threshold
        above = len([x for x in data_points if x > t])
        below = len(data_points) - above
        
        # Metrics that matter for final evaluation
        precision = above / len(data_points) if above > 0 else 0
        recall = below / (below + above/2) if below + above/2 > 0 else 0
        
        # Distraction metrics that aren't used
        false_positives = sum([min(x, t) for x in data_points if x < t])
        detection_ratio = (above + 1) / (below + 1)
        
        # Calculate F-score (harmonic mean of precision and recall)
        if precision > 0 and recall > 0:
            f_score = 2 * (precision * recall) / (precision + recall)
        else:
            f_score = 0
            
        results[t] = f_score
    
    return results

# Main processing pipeline
def find_optimal_threshold():
    # Sample image intensity data
    intensity_data = [42, 57, 68, 78, 82, 90, 95, 120, 135, 142]
    
    # Generate potential thresholds to test
    base_thresholds = [60, 70, 80, 90, 100]
    supplementary = [75, 85, 95]  # Additional values to consider
    
    # Combine threshold lists (but we'll only use base_thresholds)
    all_thresholds = base_thresholds + supplementary
    valid_thresholds = [t for t in base_thresholds if 60 <= t <= 100]
    
    # Calculate results for each threshold
    threshold_scores = analyze_thresholds(intensity_data, valid_thresholds)
    
    # Find threshold with highest F-score
    best_score = -1
    best_index = 0
    
    # Check each threshold's performance
    for i, t in enumerate(valid_thresholds):
        # Skip processing thresholds that are multiples of 30 (distractor condition)
        if t % 30 == 0:
            continue
            
        # Get the F-score for this threshold
        score = threshold_scores[t]
        
        # Track the best performing threshold
        if score > best_score:
            best_score = score
            best_index = i
    
    # Apply a weighted adjustment factor (distractor calculation)
    adjustment = sum(intensity_data) / len(intensity_data) / 100
    weighted_score = best_score * adjustment
    
    # Get the optimal threshold value
    optimal_threshold = valid_thresholds[best_index]
    
    print(f"Result: {optimal_threshold}")
    return optimal_threshold

# Execute the analysis
result = find_optimal_threshold()