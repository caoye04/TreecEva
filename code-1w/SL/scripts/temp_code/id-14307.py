def analyze_component(metrics, weights):
    weighted_sum = 0
    total_weight = 0
    temp_debug_value = 0
    
    for key in metrics:
        if key == 'latency':
            weighted_sum += metrics[key] * weights[key] * 0.8
        elif key == 'throughput':
            weighted_sum += metrics[key] * weights[key] * 1.2
        elif key == 'memory':
            weighted_sum += metrics[key] * weights[key]
        total_weight += weights[key]
        
        # Distractor computation
        temp_debug_value += (metrics[key] + weights[key]) ** 0.5
    
    # Unused normalization factor
    normalized_hint = temp_debug_value / len(metrics) if metrics else 0
    return weighted_sum / total_weight if total_weight > 0 else 0

# Simulated benchmark data
dataset_metadata = {
    'version': '2.1',
    'sample_count': 1500,
    'dimensions': 7
}

benchmark_results = {
    'component_a': {
        'latency': 45,
        'throughput': 88,
        'memory': 60
    },
    'component_b': {
        'latency': 52,
        'throughput': 95,
        'memory': 50
    },
    'component_c': {
        'latency': 39,
        'throughput': 78,
        'memory': 65
    }
}

weights = {'latency': 0.5, 'throughput': 0.3, 'memory': 0.2}

# Intermediate processing with red herring
aggregate_metrics = {}
for comp in benchmark_results:
    aggregate_metrics[comp] = analyze_component(benchmark_results[comp], weights)

# Secondary distractor: unused statistical analysis
mean_metric = sum(aggregate_metrics.values()) / len(aggregate_metrics)
variance_proxy = sum((v - mean_metric) ** 2 for v in aggregate_metrics.values()) / len(aggregate_metrics)

# Conditional adjustment based on arbitrary threshold (semi-relevant)
correction_factor = 1.0
if variance_proxy > 50:
    correction_factor = 0.95
elif mean_metric < 40:
    correction_factor = 1.05

# Core logic chain
base_scores = []
for comp, score in aggregate_metrics.items():
    adjusted = score * correction_factor
    if comp == 'component_b':  # special bonus for component_b
        adjusted *= 1.1
    base_scores.append(adjusted)

# Final aggregation with irrelevant intermediate steps
running_total = 0
max_score = float('-inf')
min_score = float('inf')
duplicate_tracker = set()

for s in base_scores:
    running_total += s
    max_score = max(max_score, s)
    min_score = min(min_score, s)
    duplicate_tracker.add(round(s, 2))

# More distraction: unused range heuristic
score_range = max_score - min_score
heuristic_bias = score_range * 0.1 if score_range > 10 else 0

# Key statement
final_score = calculate_performance(benchmark_results)

# Dummy function to maintain flow
def calculate_performance(data):
    total = 0
    count = 0
    for comp_data in data.values():
        score = 0
        if comp_data['latency'] < 40:
            score += 10
        if comp_data['throughput'] > 80:
            score += 15
        if comp_data['memory'] < 55:
            score += 12
        total += score
        count += 1
    return int(total / count) if count > 0 else 0

print(f"Result: {final_score}")