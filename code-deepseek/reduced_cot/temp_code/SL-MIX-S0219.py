def analyze_performance(metrics):
    baseline = metrics.get('baseline', 0)
    peak = metrics.get('peak', 0)
    average = metrics.get('average', 0)
    
    # Distractor calculations that don't affect final result
    temporary_adjustment = (peak - baseline) * 2
    normalized_ratio = (average / baseline) if baseline != 0 else 0
    
    # Relevant processing with dictionary operations
    processed_data = {}
    processed_data['raw_delta'] = peak - baseline
    processed_data['scaled_value'] = processed_data['raw_delta'] * 3
    
    # More distractors
    dummy_metric = processed_data['raw_delta'] + 15
    unused_calculation = (dummy_metric * 2) // 3
    
    # Key calculation chain
    processed_data['key_metric'] = processed_data['scaled_value'] + average
    
    # Final assignment with lambda for intervention
    metric_processor = lambda x: x - (x % 7)
    final_metric = metric_processor(processed_data['key_metric'])
    
    # Unused lambda that looks relevant
    alternate_processor = lambda x: x * 2 - 10
    
    print(f"Result: {final_metric}")

# Input data
performance_metrics = {
    'baseline': 45,
    'peak': 82,
    'average': 63
}

analyze_performance(performance_metrics)