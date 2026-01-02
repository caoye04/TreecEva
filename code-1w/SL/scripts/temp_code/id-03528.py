from collections import defaultdict

# Simulate system metrics over time
def collect_metrics():
    raw_data = [
        {'cpu': 75, 'memory': 80, 'latency': 20, 'requests': 150},
        {'cpu': 60, 'memory': 60, 'latency': 15, 'requests': 130},
        {'cpu': 90, 'memory': 85, 'latency': 30, 'requests': 170},
        {'cpu': 45, 'memory': 50, 'latency': 10, 'requests': 120}
    ]

    aggregated = defaultdict(float)
    counts = defaultdict(int)

    # Unnecessary aggregation step (distractor)
    temp_aggr = []
    for entry in raw_data:
        temp_aggr.append(entry['cpu'] * entry['memory'])

    avg_cpu_mem_product = sum(temp_aggr) / len(temp_aggr)

    # Actual metric collection
    for key in raw_data[0].keys():
        for entry in raw_data:
            aggregated[key] += entry[key]
            counts[key] += 1

    for key in aggregated:
        aggregated[key] /= counts[key]

    return dict(aggregated)

# Weighting logic with red herring
def apply_weights(metrics):
    base_weights = {'cpu': 0.3, 'memory': 0.3, 'latency': 0.25, 'requests': 0.15}
    adjustment_factor = 1.1

    # Distractor: irrelevant transformation
    transformed = {}
    for k, v in metrics.items():
        transformed[f'norm_{k}'] = round(v / 100, 2)

    # Another distractor: dead computation path
    outlier_count = 0
    for v in metrics.values():
        if v > 75:
            outlier_count += 1

    # Actual weight application
    adjusted_weights = {}
    total = sum(base_weights.values())
    scaling = 1.0
n    if total != 1.0:
        scaling = 1.0 / total

    for k, w in base_weights.items():
        adjusted_weights[k] = w * scaling

    return adjusted_weights

# Final evaluation
def evaluate_performance(metrics, weights):
    score_components = []

    # Normalize metrics to 0-1 scale (assume maxima)
    max_values = {'cpu': 100, 'memory': 100, 'latency': 50, 'requests': 200}
    for key, value in metrics.items():
        normalized = value / max_values[key]
        weighted_val = normalized * weights[key]
        score_components.append(weighted_val)

    raw_score = sum(score_components) * 100

    # Distractor: unused complexity
    penalty = 0
    if metrics['latency'] > 25:
        penalty = 5
    if metrics['cpu'] > 85:
        penalty += 3

    # Final nonlinear transformation (relevant)
    final_score = int((raw_score ** 1.05))  # Slight boost for high scores

    return final_score

# Execution flow
if __name__ == '__main__':
    metrics = collect_metrics()
    weights = apply_weights(metrics)
    final_score = evaluate_performance(metrics, weights)
    
    # Irrelevant post-processing (distractor)
    detailed_report = []
    for k, v in metrics.items():
        status = "OK" if v < 75 else "HIGH"
        detailed_report.append(f'{k}: {v} ({status})')
    
    print(f'Result: {final_score}')