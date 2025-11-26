def analyze_performance(metrics):
    base_scores = [metric * 1.5 for metric in metrics]
    temp_buffer = [score + 2 for score in base_scores]
    
    processed_data = []
    for score in base_scores:
        processed_data.append(round(score * 0.8, 2))
    
    adjustment_factor = len(metrics) * 1.25
    intermediate_calc = sum(temp_buffer) / len(temp_buffer)
    
    final_score = processed_data[-1] - adjustment_factor
    print(f"Target result: {final_score}")

performance_data = [12, 18, 24, 30, 36]
analyze_performance(performance_data)