def analyze_metrics(raw_data, thresholds):
    processed = {}
    temp_values = []
    adjustment_factor = 1.2

    for key, values in raw_data.items():
        avg = sum(values) / len(values)
        if avg > thresholds.get(key, 50):
            status = 'optimal'
        else:
            status = 'suboptimal'

        processed[key] = {'average': avg, 'status': status}
        temp_values.append(avg * adjustment_factor)

    outlier_count = 0
    for val in temp_values:
        if val > 100:
            outlier_count += 1

    # Irrelevant aggregation
    dummy_metric = sum(temp_values) / len(temp_values) if temp_values else 0

    return processed, dummy_metric, outlier_count


def generate_feedback(diagnostic):
    feedback_map = {}
    for k, v in diagnostic.items():
        if v['status'] == 'optimal':
            feedback_map[k] = f"Stable: {v['average']:.1f}"
        else:
            feedback_map[k] = f"Warning: {v['average']:.1f}"
    
    # Red herring computation
    total_chars = sum(len(msg) for msg in feedback_map.values())
    average_length = total_chars / len(feedback_map) if feedback_map else 0

    return feedback_map, average_length


def evaluate_performance(feedback_log):
    score = 100
    penalty_per_item = 5

    # Real logic affecting final result
    for log in feedback_log.values():
        if 'Warning' in log:
            score -= penalty_per_item

    # Distractor: complex but unused calculation
    warnings_list = [1 for msg in feedback_log.values() if 'Warning' in msg]
    warning_density = len(warnings_list) / len(feedback_log) if feedback_log else 0
    adjusted_density = warning_density * 100

    return int(score)

# Main execution
raw_system_data = {
    'latency': [45, 60, 52, 88],
    'throughput': [78, 91, 85, 73],
    'error_rate': [3, 7, 5, 4],
    'memory_usage': [67, 72, 80, 75]
}

thresholds_config = {
    'latency': 55,
    'throughput': 80,
    'error_rate': 5,
    'memory_usage': 75
}

diagnostic_report, base_avg, outliers = analyze_metrics(raw_system_data, thresholds_config)
feedback_summary, mean_msg_len = generate_feedback(diagnostic_report)
final_score = evaluate_performance(feedback_summary)

print(f"Result: {final_score}")