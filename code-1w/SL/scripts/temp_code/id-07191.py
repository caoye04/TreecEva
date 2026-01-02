def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 1) / (10 - 1)
        else:
            normalized[k] = 0
    
    # Irrelevant transformation: reverse string keys (dead computation)
    reversed_keys = {k[::-1]: v for k, v in normalized.items()}

    # Actual logic begins: filter high-impact metrics
    filtered_metrics = {}
    for metric_name, value in metrics.items():
        if 'response' in metric_name or 'latency' in metric_name:
            filtered_metrics[metric_name] = value

    # Apply bitwise mask to latency values (semi-relevant)
    masked_values = []
    for name, val in filtered_metrics.items():
        if 'latency' in name:
            masked_values.append(val & 7)  # Keep only last 3 bits
        else:
            masked_values.append(val)

    # Weighted sum using zip and enumerate
    weighted_sum = 0.0
    total_weight = 0
    weight_list = [weights[k] for k in filtered_metrics.keys()]
    
    for i, (val, w) in enumerate(zip(masked_values, weight_list)):
        if i % 2 == 0:
            weighted_sum += val * w
        else:
            weighted_sum += (val + 1) * w  # Slight adjustment on odd indices
        total_weight += w

    # Final aggregation with rounding
    average_contribution = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Secondary distraction: process duplicates in a list that's not used
    temp_data = [10, 5, 3, 5, 8, 10]
    seen = set()
    duplicates = [x for x in temp_data if x in seen or seen.add(x)]

    # Critical assignment
    final_score = int(round(average_contribution * 100))
    return final_score

# Main execution
metrics = {
    'response_time': 9,
    'error_rate': 2,
    'throughput': 7,
    'latency_p95': 12,
    'latency_p99': 14
}
weights = {
    'response_time': 0.3,
    'throughput': 0.1,
    'latency_p95': 0.4,
    'latency_p99': 0.2
}

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")