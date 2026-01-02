def evaluate_performance():
    base_metrics = [85, 90, 78, 92, 88]
    adjustment_factors = [0.95, 1.02, 0.98, 1.05, 1.00]
    
    # Calculate adjusted performance scores
    adjusted_scores = [base * adj for base, adj in zip(base_metrics, adjustment_factors)]
    
    # Determine which scores meet the high-performance threshold
    threshold = 85.0
    high_performance = [score >= threshold for score in adjusted_scores]
    
    # Filter only the scores that are both adjusted and above threshold
    filtered_performance = [score for score in adjusted_scores if score >= threshold]
    
    # Irrelevant tracking variable (minimal distraction)
    count_processed = len(base_metrics)
    
    final_score = sum(filtered_performance)
    return final_score

result = evaluate_performance()
print(f"Result: {result}")