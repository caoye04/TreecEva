def calculate_performance(data):
    base = data['accuracy'] * 100
    penalty = 0
    if data['latency'] > 50:
        penalty += (data['latency'] - 50) * 0.1
    if data['errors'] > 0:
        penalty += data['errors'] * 2
    return base - penalty

# Irrelevant auxiliary metric
temp_threshold = 75

metrics = {
    'accuracy': 0.92,
    'latency': 65,
    'errors': 3
}

initial_estimate = metrics['accuracy'] * 100  # Distractor calculation

final_score = calculate_performance(metrics)
print(f"Target result: {final_score}")