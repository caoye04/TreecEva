def evaluate_performance(metrics):
    weights = [0.2, 0.3, 0.5]
    adjusted_metrics = [metric * 1.1 if metric < 80 else metric for metric in metrics]
    processed_values = list(map(lambda x: x[0] * x[1], zip(adjusted_metrics, weights)))
    total_score = sum(processed_values)
    return total_score

# Main execution
metrics_data = [75, 82, 90]
result = evaluate_performance(metrics_data)
total_score = result
print(f"Result: {total_score}")