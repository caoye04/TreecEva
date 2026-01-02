def calculate_performance(data):
    weights = {'accuracy': 0.5, 'precision': 0.3, 'recall': 0.2}
    weighted_sum = sum(data[metric] * weights[metric] for metric in weights)
    return round(weighted_sum, 3)

# Irrelevant auxiliary data (minimal distraction)
baseline = {'accuracy': 0.8, 'precision': 0.75, 'recall': 0.7}
noise_variable = [x ** 2 for x in range(5)]

# Main computation
metrics = {'accuracy': 0.92, 'precision': 0.85, 'recall': 0.78}
final_score = calculate_performance(metrics)
print(f"Result: {final_score}")