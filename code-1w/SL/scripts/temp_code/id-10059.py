def calculate_performance(data):
    base = data['accuracy'] * 100
    bonus = len(data['features']) if data['stability'] > 0.9 else 0
    penalty = sum(1 for t in data['timings'][:3] if t > 50)
    return base + bonus - penalty

# Metrics dictionary with system performance data
timings_log = [45, 52, 48, 60, 55]
features_list = ['autoretry', 'cache', 'retry_backoff', 'circuit_breaker']

metrics = {
    'accuracy': 0.92,
    'stability': 0.93,
    'features': features_list,
    'timings': timings_log
}

final_score = calculate_performance(metrics)
print(f"Result: {final_score}")