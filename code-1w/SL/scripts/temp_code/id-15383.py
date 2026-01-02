def evaluate_performance(metrics, threshold):
    # Simulate evaluation of system performance based on metric compliance
    compliant_count = 0
    weighted_sum = 0.0
    penalty_factor = 1.0

    temp_result = 0  # Irrelevant accumulator (distractor)
    debug_log = []   # Unused logging structure (distractor)

    for metric in metrics:
        if 'response_time' in metric:
            value = metric['response_time']
            if value < threshold * 1.5:
                compliant_count += 1
                weighted_sum += value * 0.8
            else:
                penalty_factor *= 0.95  # Minor penalty per violation

        elif 'throughput' in metric:
            value = metric['throughput']
            normalized = value / (threshold * 10)
            if normalized > 1.0:
                compliant_count += 1
                weighted_sum += min(normalized, 2.0)

        elif 'error_rate' in metric:
            err = metric['error_rate']
            if err < 0.05:
                compliant_count += 1
            # Simulate unnecessary transformation
            adjusted_err = (err + 0.01) * 100  # Computed but unused
            temp_result += adjusted_err  # Distractor accumulation

    # Set of high-performing metric keys (set operation - required feature)
    metric_keys = {k for d in metrics for k in d.keys()}
    bonus_eligible = 'throughput' in metric_keys and 'response_time' in metric_keys

    # Additional irrelevant set computation (distractor)
    auxiliary_set = {x[:3] for x in metric_keys if len(x) >= 3}
    set_intersection_size = len(metric_keys & {'resp', 'thr', 'err'})  # Semi-relevant but not used directly

    # Complex conditional with short-circuit logic
    if bonus_eligible and compliant_count >= 2 or (compliant_count == 1 and weighted_sum > 5.0):
        weighted_sum *= 1.1  # Reward integrated systems

    final_score = int((weighted_sum * penalty_factor) + compliant_count)

    # Dead code path (distractor - never executed due to logic)
    if penalty_factor > 2.0:
        final_score = -1
        debug_log.append('Extreme penalty applied')

    return final_score


# Main execution context
base_threshold = 100
metric_set = [
    {'response_time': 120},
    {'throughput': 1150},
    {'error_rate': 0.03},
    {'response_time': 80}
]

# Key statement
final_score = evaluate_performance(metric_set, base_threshold)

print(f"Result: {final_score}")