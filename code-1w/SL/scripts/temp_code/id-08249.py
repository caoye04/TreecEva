def evaluate_performance(metrics, data_map):
    baseline = 100
    adjustment = 0
    temp_result = 0
    
    # Initialize performance flags and auxiliary tracking
    high_precision = data_map['precision'] > 0.85
    low_latency = data_map['latency'] < 50
    consistency_flag = data_map['variance'] < 5

    # Distractor: Irrelevant computation on unused metric
    outlier_count = 0
    for val in data_map['raw_samples']:
        if val > 95:
            outlier_count += 1  # Not used later

    # Compute score components with conditional expressions
    accuracy_weight = 1.5 if high_precision else 0.8
    speed_weight = 1.2 if low_latency else 0.7
    stability_weight = 1.0 if consistency_flag else 0.5

    # Real computation path
    raw_accuracy = data_map['accuracy'] * accuracy_weight
    raw_speed = (100 - data_map['latency']) * speed_weight
    raw_stability = 10 - (data_map['variance'] * 0.2) * stability_weight

    # Set operations to determine bonus eligibility
    required_metrics = {'accuracy', 'precision', 'latency'}
    optional_metrics = {'throughput', 'variance', 'reliability'}
    provided_metrics = set(data_map.keys())
    
    bonus_eligible = required_metrics.issubset(provided_metrics) and len(provided_metrics.intersection(optional_metrics)) >= 2

    # Secondary distractor: unused recursive function
    def calculate_depth(n):
        return 1 + calculate_depth(n-1) if n > 0 else 0  # Never called

    # Aggregate base score
    base_score = raw_accuracy + raw_speed + raw_stability

    # Apply bonus logic using bitwise check on metric count
    metric_count = len(provided_metrics)
    bonus_trigger = (metric_count & 3) == 0  # True when divisible by 4

    bonus = 15 if bonus_eligible and bonus_trigger else 0

    # Final adjustment with distractor variable
    decay_factor = 0.95  # Computed but not used
    final_score = base_score + bonus + adjustment  # adjustment remains 0

    return int(final_score)

# Main execution context
benchmark_data = {
    'accuracy': 88,
    'precision': 0.87,
    'latency': 45,
    'variance': 3.2,
    'raw_samples': [88, 90, 92, 96, 91, 89],
    'throughput': 1200,
    'reliability': 0.99
}

metric_set = ['accuracy', 'precision', 'latency', 'variance']

final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")