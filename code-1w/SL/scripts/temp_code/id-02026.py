def analyze_workload(tasks):
    total_effort = 0
    task_count = len(tasks)
    penalty_factor = 0.0
    bonus_credit = 0

    for i, task in enumerate(tasks):
        base_load = task['hours'] * task['complexity']
        if task['priority'] > 1:
            adjusted_load = base_load * 1.2
        else:
            adjusted_load = base_load * 0.9
        
        # Irrelevant computation - distractor
        temp_score = (i + 1) * base_load / (task['priority'] + 1)
        bonus_credit += temp_score * 0.05
        
        total_effort += adjusted_load

        if i % 2 == 0:
            penalty_factor += 0.01 * base_load

    net_productivity = total_effort - penalty_factor + bonus_credit
    return net_productivity, task_count


def calculate_optimal_threshold(workloads):
    # Dead function - not used, adds interference
    thresholds = [w * 0.75 for w in workloads]
    avg_threshold = sum(thresholds) / len(thresholds)
    return avg_threshold


def process_metrics(log_data):
    cumulative_metrics = []
    debug_trace = []
    
    for entry in log_data:
        workload, count = analyze_workload(entry['tasks'])
        efficiency = workload / (count + 1e-5)
        
        # Distractor: irrelevant normalization
        normalized_effort = (efficiency - min(100, efficiency)) / max(100, efficiency)
        debug_trace.append(normalized_effort)
        
        cumulative_metrics.append(efficiency)
    
    # Real computation path
    raw_total = sum(cumulative_metrics)
    sample_size = len(cumulative_metrics)
    adjustment = 0.85 if sample_size > 3 else 1.0
    
    # Key variable assignment
    efficiency_ratio = (raw_total * adjustment) / max(sample_size, 1)
    
    # More distractions below
    outlier_count = 0
    for val in cumulative_metrics:
        if val > 200:
            outlier_count += 1
    smoothing_factor = outlier_count * 0.02
    efficiency_ratio += smoothing_factor  # Minor tweak, but deterministic

    final_output = efficiency_ratio  # Critical execution point
    return final_output

# Input data
log_entries = [
    {'tasks': [
        {'hours': 4, 'complexity': 3, 'priority': 2},
        {'hours': 2, 'complexity': 5, 'priority': 1},
        {'hours': 6, 'complexity': 2, 'priority': 3}
    ]},
    {'tasks': [
        {'hours': 3, 'complexity': 4, 'priority': 2},
        {'hours': 5, 'complexity': 3, 'priority': 1}
    ]},
    {'tasks': [
        {'hours': 1, 'complexity': 8, 'priority': 3},
        {'hours': 7, 'complexity': 1, 'priority': 2},
        {'hours': 2, 'complexity': 2, 'priority': 1},
        {'hours': 4, 'complexity': 3, 'priority': 2}
    ]},
    {'tasks': [
        {'hours': 6, 'complexity': 2, 'priority': 1}
    ]},
    {'tasks': [
        {'hours': 3, 'complexity': 5, 'priority': 3},
        {'hours': 4, 'complexity': 4, 'priority': 2}
    ]}
]

result_value = process_metrics(log_entries)
print(f"Result: {result_value}")