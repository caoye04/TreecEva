def analyze_workload(tasks):
    # Irrelevant processing: task duration analysis (dead path)
    total_time = sum([t[1] for t in tasks])
    avg_time = total_time / len(tasks) if tasks else 0
    critical_tasks = [t for t in tasks if t[2] == 'high']

    # Distractor: unused complex calculation
    weighted_load = sum(t[1] * (2 if t[2] == 'high' else 1) for t in tasks)

    # Relevant: extract task types
    task_types = set(t[0] for t in tasks)
    return task_types


def compute_efficiency(logs):
    # Irrelevant: log compression simulation
    compressed_size = len(logs) * 0.75
    redundancy = 0.1 * compressed_size

    # Distractor: fake entropy calculation
    import math
    if logs:
        entropy = -sum(0.5 * math.log2(0.5) for _ in logs)
    else:
        entropy = 0.0

    # Relevant: count successful entries
    success_count = len([entry for entry in logs if entry['status'] == 'OK'])
    return success_count


def generate_baseline_reference():
    # Dead function: never actually used
    base_metrics = {i: (i ** 2) % 17 for i in range(1, 20)}
    return set(base_metrics.values())


def filter_outliers(data):
    # Real but misleading filtering
    mean_val = sum(data) / len(data) if data else 0
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5 if data else 0
    filtered = [x for x in data if abs(x - mean_val) <= 2 * std_dev]
    
    # Distractor: secondary transformation with no impact
    normalized = [(x - mean_val) / std_dev if std_dev != 0 else 0 for x in filtered]
    return set(filtered)


def evaluate_performance(metrics):
    # Core logic begins
    base_set = {2, 4, 6, 8, 10, 12}
    overlap = base_set & metrics  # Intersection
    bonus = len(overlap) * 7

    # Additional scoring rule
    if len(metrics) > 5:
        bonus += 5
    
    # Critical computation
    raw_score = sum(metrics) + bonus
    penalty = 0
    
    # Conditional penalty based on set properties
    if not metrics.issuperset({4, 8}):
        penalty += 15
    
    final_score = raw_score - penalty
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    task_list = [
        ('coding', 120, 'high'),
        ('review', 45, 'medium'),
        ('testing', 90, 'high'),
        ('docs', 30, 'low'),
        ('design', 60, 'medium')
    ]
    
    # Irrelevant call
    identified_types = analyze_workload(task_list)
    
    # Fake preprocessing chain
    log_data = [
        {'timestamp': 1, 'status': 'OK'},
        {'timestamp': 2, 'status': 'FAIL'},
        {'timestamp': 3, 'status': 'OK'},
        {'timestamp': 4, 'status': 'OK'}
    ]
    success_count = compute_efficiency(log_data)
    
    # Generate decoy metric sets
    decoy_metrics_a = {1, 3, 5, 7, 9}
    decoy_metrics_b = {2, 3, 5, 7, 11}
    baseline_ref = generate_baseline_reference()  # Unused
    
    # Real data preparation
    raw_performance_data = [10, 15, 20, 25, 30, 40]
    cleaned_data = filter_outliers(raw_performance_data)
    
    # Key assignment
    metric_set = cleaned_data | {6, 8}  # Add missing elements
    
    # Critical statement
    final_score = evaluate_performance(metric_set)
    
    print(f"Result: {final_score}")