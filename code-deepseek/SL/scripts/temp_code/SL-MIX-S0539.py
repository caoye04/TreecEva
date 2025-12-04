from collections import Counter

def analyze_performance(metrics):
    # Performance metrics for quality assessment
    scores = []
    for metric in metrics:
        if metric['type'] == 'accuracy':
            scores.append(metric['value'])
    
    # Calculate final score as range of accuracy values
    final_score = max(scores) - min(scores)
    print(f"Result: {final_score}")

# Sample performance data
performance_data = [
    {'type': 'accuracy', 'value': 87},
    {'type': 'precision', 'value': 92},
    {'type': 'accuracy', 'value': 91},
    {'type': 'recall', 'value': 85},
    {'type': 'accuracy', 'value': 78}
]

analyze_performance(performance_data)