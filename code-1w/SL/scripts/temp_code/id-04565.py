from collections import defaultdict


def analyze_response_times(times):
    stats = defaultdict(int)
    for t in times:
        if t < 10:
            stats['fast'] += 1
        elif t < 50:
            stats['medium'] += 1
        else:
            stats['slow'] += 1
    return stats


def filter_outliers(data, factor=1.5):
    if len(data) == 0:
        return []
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[3 * len(sorted_data) // 4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]


def balance_workload(nodes, threshold):
    load_summary = defaultdict(float)
    temp_buffer = []
    
    for node_id, config in nodes.items():
        base_load = config.get('base', 0)
        priority = config.get('priority', 1)
        redundancy = config.get('redundancy', 1)
        
        # Misleading computation - not used in final result
        simulated_latency = (base_load * 0.3) ** 0.5 if base_load > 0 else 0
        temp_buffer.append(simulated_latency)
        
        adjusted_load = base_load * priority
        if redundancy > 1:
            adjusted_load /= redundancy
        
        capped_load = min(adjusted_load, threshold)
        scaled_load = capped_load * 1.75  # Scale for downstream processing
        
        # Only nodes with priority > 1 are counted in final workload
        if priority > 1:
            load_summary[node_id] = round(scaled_load, 4)
    
    # Irrelevant aggregation
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    adjustment_factor = 1.0 if avg_temp < 5 else 0.9
    
    total_load = sum(load_summary.values()) * adjustment_factor
    
    # Dead code - never executed under current logic
    if False:
        fallback = sum([v * 0.1 for v in load_summary.values()])
        total_load += fallback
    
    return int(total_load)

# Main execution
response_times = [5, 12, 45, 8, 52, 67, 10, 3]
time_stats = analyze_response_times(response_times)
cleaned_times = filter_outliers(response_times)

nodes = {
    'node_a': {'base': 20, 'priority': 2, 'redundancy': 2},
    'node_b': {'base': 35, 'priority': 1, 'redundancy': 1},
    'node_c': {'base': 15, 'priority': 3, 'redundancy': 3},
    'node_d': {'base': 50, 'priority': 2, 'redundancy': 1}
}

threshold = 30
final_load = balance_workload(nodes, threshold)

print(f"Result: {final_load}")