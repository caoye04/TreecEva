def analyze_processor_performance():
    processor_specs = [3.2, 2.8, 4.1, 3.5, 2.9]
    efficiency_factors = [0.85, 0.92, 0.78, 0.88, 0.95]
    
    # Calculate performance scores
    performance_scores = []
    for i, (spec, eff) in enumerate(zip(processor_specs, efficiency_factors)):
        base_score = spec * eff * 100
        adjusted_score = base_score + (i * 5)  # Small processor index bonus
        performance_scores.append(adjusted_score)
    
    # Distractor calculations that don't affect final result
    temp_calc = sum(processor_specs) * len(efficiency_factors)
    unused_result = temp_calc / max(efficiency_factors)
    
    # Create enumerated results
    enumerated_results = list(enumerate(performance_scores))
    
    # Find best performing processor index
    performance_metric = max(enumerated_results, key=lambda x: x[1])[0]
    
    # Additional irrelevant operations
    backup_check = min(processor_specs) - max(efficiency_factors)
    
    print(f"Target result: {performance_metric}")
    return performance_metric

analyze_processor_performance()