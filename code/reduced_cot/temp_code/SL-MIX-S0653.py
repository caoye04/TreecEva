def calculate_performance(metrics):
    raw_scores = [x * 2 for x in metrics]
    processed = lambda x: (x // 2) + (x % 3)
    processed_scores = list(map(processed, raw_scores))
    
    # Distractor calculations
    temp_sum = sum(metrics)
    max_score = max(raw_scores)
    average_metric = temp_sum / len(metrics)
    
    relevant_scores = processed_scores[:3]
    adjusted_scores = [score + 5 for score in relevant_scores]
    
    # More distraction
    unused_multiplier = len(metrics) * 2
    dummy_operation = unused_multiplier - 10
    
    final_score = adjusted_scores[0]
    print(f"Result: {final_score}")

# Main execution
performance_data = [12, 8, 15, 6, 9]
calculate_performance(performance_data)