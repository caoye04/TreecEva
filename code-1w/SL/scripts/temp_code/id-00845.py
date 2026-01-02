import itertools

def analyze_sequence(data):
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    return counts

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    max_metric = max(metrics.values())
    min_metric = min(metrics.values())
    
    # Distractor: Normalize metrics (not used in final calculation)
    normalized = {k: (v - min_metric) / (max_metric - min_metric + 1e-8) for k, v in metrics.items()}
    
    temp_result = 0
    for i, (key, weight) in enumerate(itertools.zip_longest(metrics.keys(), weights, fillvalue=1)):
        if key in ['latency', 'throughput', 'accuracy']:
            # Only these three contribute
            temp_result += metrics.get(key, 0) * weight
    
    # Additional distractor computation
    squared_devs = [(v - sum(metrics.values())/len(metrics))**2 for v in metrics.values()]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    
    # Final score depends only on temp_result and fixed offset
    adjustment = 5 if len(metrics) > 3 else -2
    final_value = temp_result + adjustment
    
    # Irrelevant sorting operation
    sorted_items = sorted(metrics.items(), key=lambda x: x[1], reverse=True)
    for idx, (name, val) in enumerate(sorted_items):
        if idx % 2 == 0:
            final_value -= 1  # Red herring adjustment that doesn't actually matter due to override below
    
    # Override: actual logic
    critical_flag = any(v > 90 for v in metrics.values())
    final_value = temp_result + (10 if critical_flag else 0)  # Correct path
    
    return final_value

# Main execution
raw_data = ['A', 'B', 'A', 'C', 'B', 'A']
data_counts = analyze_sequence(raw_data)

# Simulate system metrics from count distribution
metrics = {
    'latency': 85,
    'throughput': 95,
    'accuracy': 76,
    'reliability': 68,
    'scalability': 81
}
weights = [0.2, 0.3, 0.5]

# Extraneous loop with no impact
running_total = 0
for combo in itertools.combinations_with_replacement([1, 2], 3):
    running_total += sum(combo)

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")