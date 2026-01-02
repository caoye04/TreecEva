def analyze_throughput(data_points):
    total = 0
    count = 0
    for point in data_points:
        if point > 0:
            total += point ** 0.5
            count += 1
    return total / count if count else 0

process_metrics = {
    'stage_a': [16, 25, 36, 49],
    'stage_b': [10, -5, 15, 20],
    'stage_c': [8, 12, 18]
}

overhead_log = {
    'timestamp': [1, 2, 3, 4],
    'latency': [0.1, 0.2, 0.15, 0.3],
    'dummy_flag': True,
    'placeholder_data': [999, 888, 777]  # Irrelevant
}

# Misleading pre-processing
buffer_cache = []
for key in process_metrics:
    temp_sum = 0
    for val in process_metrics[key]:
        if val < 0:
            continue
        temp_sum += val % 7  # Distractor computation
    buffer_cache.append(temp_sum)

# Dummy state tracking
state_tracker = {'phase': 'init', 'status': 0}
state_tracker['phase'] = 'processing'
state_tracker['status'] = len(buffer_cache)  # Not used later

baseline = 0
for stage, values in process_metrics.items():
    baseline += sum(v for v in values if v > 0)

# Linear search for maximum valid throughput
max_valid = 0
for vals in process_metrics.values():
    for v in vals:
        if v > max_valid and v > 0:
            max_valid = v

scaling_factor = 2.5
adjustment = len(overhead_log['latency']) * 0.05  # Minor adjustment

# Core function with relevant logic
def calculate_efficiency(metrics, overhead):
    raw_total = 0
    entry_count = 0
    latency_impact = 0
    
    for log_entry in overhead['latency']:
        latency_impact += log_entry ** 2
    
    # Efficiency depends on scaled average of square roots
    for key, readings in metrics.items():
        for reading in readings:
            if reading > 0:
                raw_total += reading ** 0.5
                entry_count += 1
    
    average_sqrt = raw_total / entry_count if entry_count else 0
    
    # Secondary distraction: unused branch
    if 'dummy_flag' in overhead and overhead['dummy_flag']:
        shadow_value = sum(overhead['timestamp']) // 4  # Computed but not used
    
    # Actual efficiency formula
    base_efficiency = average_sqrt * scaling_factor
    final_efficiency = base_efficiency - (latency_impact * 10)
    
    return final_efficiency

# Key execution point
intermediate_result = analyze_throughput(process_metrics['stage_a'])
efficiency_ratio = calculate_efficiency(process_metrics, overhead_log)

# Print result as required
print(f"Result: {efficiency_ratio}")