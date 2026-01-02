def evaluate_performance(data, limit):
    weighted_sum = 0
    scaling_factor = 1.5
    penalty_offset = 0.2
    temp_result = []

    for key, values in data.items():
        if 'response' in key:
            avg = sum(values) / len(values)
            if avg > limit:
                adjustment = (avg - limit) * scaling_factor
            else:
                adjustment = (limit - avg) * penalty_offset
            weighted_sum += adjustment
            temp_result.append(adjustment)

    # Irrelevant computation on similar-looking data
    outlier_check = [x for x in data.get('response_times', []) if x > 200]
    spike_count = len(outlier_check)
    debug_info = {'spikes': spike_count, 'status': 'analysis_complete'}

    # Dummy logic that looks important but doesn't affect final_score
    if spike_count > 5:
        debug_info['action'] = 'throttle'
    else:
        debug_info['action'] = 'monitor'

    # Actual determination of score based on adjusted weights
    multiplier = 1.0
    if weighted_sum < 0:
        multiplier = 0.9
    
    result = round(weighted_sum * multiplier, 4)

    # Dead code path - never executed due to logic above
    if False:
        fallback = sum(temp_result) * 0.8
        result = fallback

    return result

# Main execution
metrics = {
    'response_time_avg': [120, 135, 110, 150],
    'response_retries': [2, 1, 3],
    'response_codes_2xx': [98, 99, 100, 97],
    'response_times': [105, 140, 130, 115, 160, 175, 180, 195, 145, 138]
}

threshold = 125
initial_load = sum(metrics['response_times']) // len(metrics['response_times'])
correction_term = initial_load * 0.01
interim_value = initial_load + correction_term

# Unused variables to increase cognitive load
baseline_ref = 100
normalization_constant = 42.0
shadow_buffer = [0] * len(metrics)

final_score = evaluate_performance(metrics, threshold)
print(f"Result: {final_score}")