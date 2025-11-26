def compute_final_evaluation(metrics):
    process_metrics = lambda x: sum([v * 2 for v in x if v > 0]) - len([v for v in x if v < 0])
    
    data_points = [3, -2, 7, -1, 5, -4, 2]
    intermediate_sum = sum([abs(v) for v in data_points])
    temp_calculation = process_metrics(data_points) * 1.5
    
    # Distractor operations that don't affect final result
    unused_metrics = [v ** 2 for v in data_points]
    processed_count = len([v for v in data_points if v % 2 == 0])
    
    adjustment_factor = 0.75
    final_score = int(temp_calculation * adjustment_factor)
    
    print(f"Result: {final_score}")

compute_final_evaluation(None)