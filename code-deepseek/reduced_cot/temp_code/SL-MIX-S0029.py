def analyze_performance(metrics):
    baseline = sum(metrics[:3])  # Not used in final calculation
    processed = []
    temp_buffer = 0
    
    for idx, value in enumerate(metrics):
        temp_buffer += value * 2  # Distractor calculation
        if idx % 2 == 0:
            processed.append(value + 5)
        else:
            processed.append(value - 3)
    
    # Intermediate calculations that don't affect final result
    running_total = sum(processed)
    average_metric = running_total / len(processed) if processed else 0
    
    # Key processing with slicing and enumerate
    performance_data = []
    for i, val in enumerate(processed[1:]):
        performance_data.append(val * (i + 1))
    
    final_score = performance_data[-1]
    print(f"Result: {final_score}")

# Input data
performance_metrics = [12, 8, 15, 6, 20, 10]
analyze_performance(performance_metrics)