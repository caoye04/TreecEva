def evaluate_performance(metrics, weights):
    base_score = 0
    penalty = 0
    bonus = 0
    temp_result = {}
    
    # Irrelevant metric tracking (distractor)
    historical_data = {'peak': 0, 'trend': [], 'anomalies': set()}
    for k in ['latency', 'throughput', 'error_rate', 'uptime']:
        if k not in metrics:
            historical_data['anomalies'].add(k)

    # Real computation begins
    if 'latency' in metrics and metrics['latency'] < 100:
        base_score += 25
    elif 'latency' in metrics:
        penalty += 10

    if 'throughput' in metrics:
        base_score += min(metrics['throughput'] // 10, 30)

    consistency_log = []
    for i in range(3):
        consistency_log.append(True)  # Dead code path filler

    if 'error_rate' in metrics:
        if metrics['error_rate'] == 0:
            bonus += 20
        else:
            penalty += metrics['error_rate'] * 5

    if 'uptime' in metrics:
        base_score += metrics['uptime'] // 5

    # Weighted adjustment using dictionary
    adjusted_score = 0
    for key, value in weights.items():
        if key == 'latency' and 'latency' in metrics:
            adjusted_score += abs(value - metrics['latency']) // 10
        elif key == 'throughput' and 'throughput' in metrics:
            adjusted_score += (value + metrics['throughput']) // 20

    # Final logic with early exit red herring
    if base_score <= 10:
        return -1  # Unused path due to input values

    final_score = base_score - penalty + bonus - adjusted_score
    
    # Dummy set operations for interference
    tracked_ids = {1, 2, 3, 4}
    excluded_ids = {3, 4, 5, 6}
    intersection = tracked_ids & excluded_ids
    temp_result['overlap'] = len(intersection)
    
    return final_score

# Input data
metrics = {
    'latency': 80,
    'throughput': 150,
    'error_rate': 0,
    'uptime': 95
}

weights = {
    'latency': 90,
    'throughput': 100
}

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")