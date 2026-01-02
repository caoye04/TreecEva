def evaluate_performance(metrics):
    raw_values = [metric['value'] for metric in metrics]
    max_value = max(raw_values)
    normalized = [val / max_value for val in raw_values]
    
    adjustments = [0.1, -0.05, 0.0, 0.15, -0.1]
    adjusted_normalized = [n + adj for n, adj in zip(normalized, adjustments)]
    
    filtered = [val for val in adjusted_normalized if val >= 0.5]
    total_score = sum(filtered)
    
    # Irrelevant tracking variables (low interference)
    count_processed = len(raw_values)
    average_score = sum(raw_values) / len(raw_values)
    
    return total_score

# Input data
evaluation_data = [
    {'name': 'latency', 'value': 80},
    {'name': 'throughput', 'value': 100},
    {'name': 'reliability', 'value': 90},
    {'name': 'scalability', 'value': 70},
    {'name': 'efficiency', 'value': 60}
]

result = evaluate_performance(evaluation_data)
print(f"Result: {result}")