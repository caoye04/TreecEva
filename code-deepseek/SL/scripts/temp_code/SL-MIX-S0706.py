def calculate_performance(metrics):
    base_scores = [x * 2 for x in metrics if x > 0]
    temp_products = [score * 3 for score in base_scores]
    
    # Distractor calculations that don't affect final result
    irrelevant_sum = sum([x % 5 for x in metrics])
    bonus_pool = len([x for x in base_scores if x % 2 == 0])
    
    core_sum = sum(base_scores)
    processed_sum = core_sum + (len(metrics) * 2)
    
    # More distraction operations
    dummy_metric = processed_sum ^ 15
    bonus_adj = 7 if len(metrics) > 3 else 10
    
    final_score = processed_sum - bonus_adj
    print(f"Result: {final_score}")

# Main execution
performance_metrics = [3, 7, 2, 5, 4]
calculate_performance(performance_metrics)