def evaluate_performance(metrics, threshold):
    score = 0
    penalty_adjustment = 0.0
    temp_buffer = []

    for key, values in metrics.items():
        if 'response_time' in key:
            avg_response = sum(values) / len(values)
            if avg_response < threshold * 1.5:
                score += 10
            else:
                penalty_adjustment += 2.5
        elif 'error_rate' in key:
            max_error = max(values)
            if max_error < 0.05:
                score += 15
            else:
                temp_buffer.append(max_error)
                penalty_adjustment += max_error * 100
        elif 'throughput' in key:
            total_throughput = sum(values)
            normalized_throughput = total_throughput % 100
            if normalized_throughput > 50:
                score += 5

    consistency_check = len(temp_buffer) % 2
    if consistency_check == 0 and penalty_adjustment > 0:
        penalty_adjustment *= 0.8

    intermediate_result = score - int(penalty_adjustment)
    outlier_flag = False

    for val in metrics.get('response_time_samples', []):
        if val > 200:
            outlier_flag = True
            break

    if outlier_flag:
        score -= 3

    debug_log = f'Final adjustments: score={score}, penalty={penalty_adjustment}'
    final_score = intermediate_result + 5  
    return final_score

base_threshold = 100
metric_data = {
    'response_time_prod': [90, 95, 110, 87],
    'error_rate_prod': [0.03, 0.06, 0.02],
    'throughput_weekly': [45, 55, 60, 40, 50],
    'response_time_samples': [88, 92, 195, 103]
}

# Extraneous helper function (not directly affecting core logic)
def calculate_efficiency_ratio(x, y):
    return (x * 0.95) / (y + 1) if y != 0 else 0

auxiliary_counter = 0
while auxiliary_counter < 3:
    auxiliary_counter += 1
    shadow_value = auxiliary_counter ** 2

final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")