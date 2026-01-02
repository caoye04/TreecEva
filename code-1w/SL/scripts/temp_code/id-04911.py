def evaluate_performance(metrics, threshold):
    # Irrelevant preprocessing: normalize irrelevant features
    normalized_metrics = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]
    filtered_metrics = [x for x in normalized_metrics if x > 10]

    # Distractor: unused transformation
    squared_devs = [(x - sum(metrics)/len(metrics))**2 for x in metrics]
    variance_proxy = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Real logic begins: count how many original metrics exceed threshold
    above_threshold = len([x for x in metrics if x >= threshold])

    # Use set operations to eliminate duplicates in a transformed view
    boosted_set = set()
    for val in metrics:
        if val > threshold:
            boosted_set.update([val + 1, val + 2])

    # Slice top half of sorted boosted values
    sorted_boosted = sorted(list(boosted_set), reverse=True)
    top_half_slice = sorted_boosted[:len(sorted_boosted)//2] if sorted_boosted else []

    # Secondary distractor: dead code path (never affects output)
    penalty = 0
    if len(top_half_slice) > 10:
        penalty = sum([p for p in top_half_slice if p % 3 == 0])

    # Core calculation: combine count and unique boosts
    base_score = above_threshold * 10
    bonus = len(top_half_slice) * 2

    # Final score computation
    final_score = base_score + bonus - penalty  # penalty always 0 due to input size

    # Debugging red herring (unused)
    debug_info = {
        'raw': metrics,
        'normalized': normalized_metrics,
        'variance_proxy': variance_proxy
    }

    return final_score

# Main execution
metrics_data = [85, 90, 78, 92, 88, 76, 95, 89]
threshold = 85

# Key statement
final_score = evaluate_performance(metrics_data, threshold)
print(f"Result: {final_score}")