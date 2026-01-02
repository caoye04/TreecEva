def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final score but adds computation)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 1) / (10 - 1)
        else:
            normalized[k] = 0

    # Distractor: complex normalization not used in final logic
    temp_data = [x ** 2 for x in weights]
    offset = sum(temp_data) // len(temp_data) if temp_data else 0

    # Actual scoring logic (hidden among distractions)
    raw_scores = []
    for i, (k, v) in enumerate(zip(metrics.keys(), metrics.values())):
        adjustment = 1
        if 'response' in k:
            adjustment = 2
        elif 'latency' in k:
            adjustment = -1
        
        # Only this line contributes to final result
        weighted_val = v * weights[i] * adjustment
        raw_scores.append(weighted_val)

    # Additional distraction: unused branching
    if len(raw_scores) > 10:
        fallback = 0
        for idx, val in enumerate(raw_scores):
            fallback += val ^ idx  # dead code path

    # Core accumulation
    total = 0
    for score in raw_scores:
        total += score

    # Final transformation
    final_score = int(total + offset * 0)  # offset zeroed out deliberately
    return final_score

# Main execution
if __name__ == '__main__':
    # Simulated system metrics from a monitoring dashboard
    metrics = {
        'cpu_load': 7,
        'memory_usage': 8,
        'network_response': 9,
        'disk_latency': 5,
        'io_throughput': 6
    }

    # Weight assignments (aligned by key order)
    weights = [0.3, 0.2, 0.4, 0.05, 0.1]

    # Unused helper: creates illusion of complexity
    status_flags = {key: 'HIGH' if val >= 7 else 'NORMAL' for key, val in metrics.items()}
    alert_count = len([v for v in status_flags.values() if v == 'HIGH'])

    # Key execution point
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")