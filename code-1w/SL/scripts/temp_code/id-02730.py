def calculate_performance(data):
    base_scores = [d['score'] for d in data]
    weights = list(map(lambda x: 0.8 if x < 70 else 1.2, base_scores))
    weighted_sum = sum(score * weight for score, weight in zip(base_scores, weights))
    adjustment = len([s for s in base_scores if s > 80]) * 2.5
    return weighted_sum + adjustment

benchmark_data = [
    {'id': 'A', 'score': 65, 'type': 'cpu'},
    {'id': 'B', 'score': 92, 'type': 'gpu'},
    {'id': 'C', 'score': 77, 'type': 'ram'},
    {'id': 'D', 'score': 88, 'type': 'ssd'},
    {'id': 'E', 'score': 54, 'type': 'io'}
]

# Irrelevant auxiliary variable (minor distraction)
summary_stats = {'count': len(benchmark_data), 'active': True}

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")