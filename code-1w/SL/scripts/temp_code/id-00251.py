def calculate_performance(metrics):
    base_score = metrics['accuracy'] * 100
    if metrics['latency'] < 50:
        base_score += 10
    if metrics['reliability'] >= 0.95:
        base_score += 15
    return base_score

bonus_metrics = {
    'accuracy': 0.87,
    'latency': 45,
    'reliability': 0.96,
    'version': '2.1'
}

final_score = calculate_performance(bonus_metrics)
print(f"Result: {final_score}")