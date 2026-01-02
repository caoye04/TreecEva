def analyze_metrics(data_map):
    processed = {}
    temp_aggregate = 0

    for key, values in data_map.items():
        if len(values) == 0:
            processed[key] = 0
            continue

        avg_val = sum(values) / len(values)
        max_val = max(values)
        min_val = min(values)
        
        # Distractor: irrelevant computation
        outlier_count = sum(1 for v in values if v > avg_val * 1.5)
        
        # Semi-relevant transformation
        normalized = [(v - min_val) / (max_val - min_val + 1e-8) for v in values]
        normalized_avg = sum(normalized) / len(normalized)
        
        processed[key] = normalized_avg * 100
        
        # Distractor: accumulates but not used later
        temp_aggregate += max_val - min_val

    return processed


def filter_stages(stage_data):
    # Irrelevant filtering path
    valid_stages = []
    for stage, metrics in stage_data.items():
        if sum(metrics) > 50:
            valid_stages.append(stage)
    return valid_stages  # Unused in main logic


def calculate_performance(results):
    # Main logic starts here
    scores = analyze_metrics(results)
    
    # Distractor variables
    debug_trace = []
    total_weight = 0.0
    
    performance_list = []
    for k, v in scores.items():
        weight = 1.0
        if 'critical' in k:
            weight = 2.0
        elif 'aux' in k:
            weight = 0.5
            
        # This affects final result
        performance_list.append(v * weight)
        
        # Dead code path
        if False:
            debug_trace.append(f'{k}: {v * weight}')

    base_score = sum(performance_list)
    adjustment_factor = len(performance_list) / 4.0  # Assume 4 expected components
    
    # Final computation
    final_score = int(base_score / adjustment_factor)
    
    # This print is required
    print(f"Target result: {final_score}")
    
    return final_score

# Input data
benchmark_results = {
    'critical_path_latency': [12, 15, 10, 18],
    'throughput_rate': [88, 92, 85],
    'auxiliary_response_time': [200, 210, 195],
    'critical_error_rate': [3, 5, 2]
}

# Execution point of interest
final_score = calculate_performance(benchmark_results)