def analyze_metrics(data_map):
    temp_results = {}
    for key, values in data_map.items():
        if len(values) == 0:
            temp_results[key] = 0
            continue
        avg_val = sum(values) / len(values)
        outlier_threshold = avg_val * 0.1
        filtered = [v for v in values if abs(v - avg_val) > outlier_threshold]
        temp_results[key] = len(filtered)
    
    # Irrelevant computation: tracking unused statistics
    total_entries = sum(len(v) for v in data_map.values())
    zero_count = sum(1 for v in data_map.values() if len(v) == 0)
    dummy_ratio = total_entries / (zero_count + 1)
    
    return temp_results


def calculate_performance(raw_data):
    processed = {}
    for k, v in raw_data.items():
        squared_sum = 0
        for num in v:
            if num > 0:
                squared_sum += num ** 2
        processed[k] = squared_sum ** 0.5
    
    # Dead code path: never accessed
    debug_info = {}
    for k, v in processed.items():
        debug_info[k] = f"Value: {v:.2f}"
    
    base_score = sum(processed.values())
    penalty = 0
    for val in raw_data['system_load']:
        if val > 80:
            penalty += 5
    
    final_score = int(base_score - penalty)
    
    # Additional distraction: irrelevant list processing
    status_flags = [True, False, True]
    override_flag = any(status_flags) and not all(status_flags)
    temp_array = [i * 2 for i in range(len(status_flags))]
    
    return final_score

# Main execution block
benchmark_data = {
    'cpu_usage': [75, 80, 90, 85],
    'memory_usage': [60, 70, 65],
    'disk_io': [40, 50, 55, 60, 45],
    'network_latency': [],
    'system_load': [78, 82, 88, 76, 91]
}

interim_analysis = analyze_metrics(benchmark_data)
calibration_offset = sum(len(v) for v in benchmark_data.values()) // 4
reference_key = list(benchmark_data.keys())[2]
placeholder_list = [calibration_offset * i for i in range(3)]

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")