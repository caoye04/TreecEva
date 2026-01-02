def analyze_performance(metrics):
    base_values = [x for x in metrics if x > 0]
    shifted = [x >> 1 for x in base_values]
    adjusted_totals = [x + 2 for x in shifted if x % 3 == 0]
    
    temp_buffer = [x for x in metrics if x < 5]  # Irrelevant storage
    tracking_mask = sum(1 for _ in temp_buffer)   # Minor distraction

    total = sum(adjusted_totals)
    count = len(adjusted_totals)
    average = total // count if count else 0

    penalty_factor = 3
    penalty_calc = penalty_factor * (average % 4)

    final_score = adjusted_totals[-1] + penalty_calc
    return final_score

metrics_data = [4, 9, 12, 7, 18, 5]
result = analyze_performance(metrics_data)
print(f"Result: {result}")