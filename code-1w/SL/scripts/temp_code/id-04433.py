def analyze_performance(values, limits):
    filtered = [v for v in values if v > limits[0] and v < limits[1]]
    sorted_scores = sorted(filtered, reverse=True)
    valid_indices = [i for i, x in enumerate(sorted_scores) if x % 2 == 0]
    adjustment_factor = 0.95 if len(valid_indices) > 2 else 1.05
    threshold_score = sorted_scores[valid_indices[-1]] * adjustment_factor
    return threshold_score

raw_data = [88, 92, 76, 95, 84, 73, 98, 81]
extremes = [75, 90]
result = analyze_performance(raw_data, extremes)
print(f"Result: {result}")