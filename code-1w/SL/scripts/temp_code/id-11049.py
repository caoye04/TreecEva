def evaluate_system_performance():
    raw_metrics = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    weighted_values = [raw * weight for raw, weight in zip(raw_metrics, weights)]
    average = sum(weighted_values)
    adjustment_factor = 1.05 if average > 80 else 0.95
    adjusted_metrics = [val * adjustment_factor for val in raw_metrics]
    normalized_performance = [round((val - 70) / 10) for val in adjusted_metrics]
    final_score = sum(normalized_performance)
    return final_score

result = evaluate_system_performance()
print(f"Result: {result}")