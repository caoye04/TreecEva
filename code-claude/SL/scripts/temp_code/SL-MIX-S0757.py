def filter_selector(samples, metrics):
    # Calculate baseline metrics
    baseline_mean = sum(samples) / len(samples)
    baseline_variance = sum((x - baseline_mean) ** 2 for x in samples) / len(samples)
    
    # Potential thresholds to evaluate
    candidate_thresholds = [round(baseline_mean * factor, 2) for factor in [0.8, 0.9, 1.0, 1.1, 1.2]]
    
    # Track noise levels for analysis (not directly used in selection)
    noise_levels = [sum(1 for x in samples if x < t) / len(samples) for t in candidate_thresholds]
    
    # Helper function to calculate quality score
    quality_score = lambda threshold: (
        sum(1 for x in samples if x >= threshold) / len(samples) * 
        metrics['precision'] + 
        (threshold / baseline_mean) * metrics['efficiency']
    )
    
    # Alternate scoring method (not used in final selection)
    alternate_scores = {t: abs(t - baseline_mean) * metrics['stability'] for t in candidate_thresholds}
    
    # Select threshold with highest quality score
    scores = [(t, quality_score(t)) for t in candidate_thresholds]
    best_threshold = max(scores, key=lambda pair: pair[1])[0]
    
    # Normalize based on target range (if specified in metrics)
    if 'normalize' in metrics and metrics['normalize']:
        normalization_factor = metrics.get('factor', 1.0)
        normalized = best_threshold * normalization_factor
        return normalized
    
    # Apply minimum threshold if needed
    min_acceptable = metrics.get('min_threshold', 0)
    return max(best_threshold, min_acceptable)

# Sample data points representing signal strengths
data_points = [7.2, 6.8, 8.1, 7.5, 6.9, 7.8, 6.5, 7.3]

# Configuration metrics
metrics = {
    'precision': 0.7,
    'efficiency': 0.3,
    'stability': 0.5,  # Not used in primary calculation
    'normalize': True,
    'factor': 1.2,
    'min_threshold': 5  # Not relevant as our value will be higher
}

# Calculate the optimal threshold for filtering
optimal_threshold = filter_selector(data_points, metrics)
print(f"Result: {optimal_threshold}")
