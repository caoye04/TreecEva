def evaluate_performance(metrics):
    base_values = [m * 1.5 for m in metrics]
    adjusted_totals = []
    
    for val in base_values:
        if val > 20:
            adjusted_totals.append(val * 0.9)
        else:
            adjusted_totals.append(val + 5)
    
    temp_result = sum(adjusted_totals) / len(adjusted_totals)
    final_score = max(adjusted_totals)
    
    # Irrelevant tracking variables (low interference)
    count_above_threshold = len([x for x in adjusted_totals if x > 15])
    normalization_factor = temp_result / 10
    
    print(f"Result: {final_score}")

# Input data
data_stream = [8, 12, 16, 22]
evaluate_performance(data_stream)