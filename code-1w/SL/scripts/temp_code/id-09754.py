from itertools import combinations

def evaluate_performance(metrics):
    base_score = sum(metrics.get('accuracy', 0) for _ in range(1))
    base_score += metrics.get('throughput', 0) // 10
    adjustment = 0
    
    # Consider interaction effects between latency and reliability
    if metrics.get('latency') < 50 and metrics.get('reliability') > 0.95:
        adjustment += 15
    elif metrics.get('latency') < 100 and metrics.get('reliability') > 0.9:
        adjustment += 8
    
    return base_score + adjustment

def calculate_final_score(test_results, multiplier):
    raw_scores = []n    for result in test_results.values():
        score = evaluate_performance(result)
        raw_scores.append(score)
    
    # Find best average among any pair of tests (if applicable)
    best_pair_avg = 0
    if len(raw_scores) >= 2:
        for pair in combinations(raw_scores, 2):
            avg_pair = sum(pair) / 2
            if avg_pair > best_pair_avg:
                best_pair_avg = avg_pair
    
    base_final = sum(raw_scores) / len(raw_scores)
    boosted = base_final * multiplier
    return int(boosted + best_pair_avg)

# Simulated system test results
test_data = {
    'test_alpha': {
        'accuracy': 88,
        'throughput': 120,
        'latency': 45,
        'reliability': 0.96
    },
    'test_beta': {
        'accuracy': 76,
        'throughput': 95,
        'latency': 80,
        'reliability': 0.92
    },
    'test_gamma': {
        'accuracy': 92,
        'throughput': 150,
        'latency': 120,
        'reliability': 0.88
    }
}
bonus_multiplier = 1.1

final_score = calculate_final_score(test_data, bonus_multiplier)
print(f"Target result: {final_score}")