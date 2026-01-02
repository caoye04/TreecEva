def evaluate_performance(metrics, data):
    # Irrelevant transformation
    temp_normalized = [round(x * 0.98 + 2.1, 2) for x in data if x > 5]
    
    # Distractor set: captures some values but not used in final logic
    outlier_threshold = 75
    outlier_pool = {x for x in data if x > outlier_threshold}
    processed_count = len(temp_normalized)

    # Core metric evaluation
    high_performers = {i for i, val in enumerate(data) if val >= 80}
    consistency_bonus = 0
    
    if len(high_performers) >= 3:
        # Additional condition using set operations
        recent_indices = {i for i in range(len(data)-5, len(data))}
        top_recent_overlap = high_performers & recent_indices
        
        if len(top_recent_overlap) >= 2:
            consistency_bonus = 15

    base_score = sum(data) / len(data)
    
    # Secondary distractor: unused advanced calculation
    variance_proxy = sum((x - base_score) ** 2 for x in data) / len(data)
    stability_index = 100 - variance_proxy if variance_proxy < 50 else 50

    # Conditional adjustment based on metric presence
    performance_level = 0
    if 'efficiency' in metrics:
        performance_level += 5
    if 'accuracy' in metrics and base_score >= 70:
        performance_level += 10

    # Final score computation
    final_score = base_score + consistency_bonus + performance_level
    
    # Dead code branch (never reached due to above logic)
    if stability_index < 0:
        final_score -= 10

    return int(final_score)

# Input data
benchmark_data = [85, 78, 92, 88, 76, 95, 87]
metric_set = {'accuracy', 'efficiency', 'latency'}

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")