def calculate_performance_metrics(data_points):
    score_aggregator = {'raw': 0, 'processed': 0, 'temporary': 0}
    
    # Process each data point with multiple operations
    for i, value in enumerate(data_points):
        base_score = value * 2
        adjustment = (i % 3) + 1
        
        # Calculate intermediate metrics (some are distractors)
        raw_metric = base_score + adjustment
        processed_metric = raw_metric // 2
        temp_metric = processed_metric * 3
        
        # Update aggregator (only processed metric matters for final result)
        score_aggregator['raw'] += raw_metric
        score_aggregator['processed'] += processed_metric
        score_aggregator['temporary'] += temp_metric
    
    # Final calculation with some unnecessary complexity
    bonus_factor = len(data_points) // 2
    irrelevant_computation = bonus_factor * 7
    
    # The critical execution point
    final_score = score_aggregator['processed']
    
    print(f"Target result: {final_score}")

# Main execution
data_points = [15, 22, 8, 31, 12]
calculate_performance_metrics(data_points)