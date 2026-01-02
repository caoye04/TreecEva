def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics)) * 100) for m in metrics]
    
    # Semi-relevant pre-processing
    weighted = []
    for i, val in enumerate(metrics):
        weight = 0.8 if val >= thresholds[i] else 0.4
        weighted.append(val * weight)
    
    # Distractor: unused intermediate
    ranking = sorted(enumerate(weighted), key=lambda x: x[1], reverse=True)
    rank_index_map = {idx: rank for rank, (idx, _) in enumerate(ranking)}

    # Core logic: count how many exceed threshold with bonus for consecutive
    bonus_counter = 0
    base_count = 0
    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        if metric > threshold:
            base_count += 1
            bonus_counter += 1
        else:
            bonus_counter = max(bonus_counter - 1, 0)  # partial reset
    
    # Another distractor: complex but unused set logic
    unique_windows = set()
    for i in range(len(metrics) - 1):
        window = tuple(sorted(metrics[i:i+2]))
        unique_windows.add(window)
    diversity_score = len(unique_windows) * 0.5  # not used directly

    # Final aggregation with red herring variables
    stability_penalty = len(metrics) - len(set(round(m, 1) for m in metrics))
    adjustment_factor = 1 + (diversity_score / len(metrics)) if metrics else 1
    
    # Actual answer depends only on base_count and bonus_counter
    final_value = base_count * 10 + bonus_counter
    return int(final_value)

# Input data
metrics_data = [85, 90, 78, 92, 88]
threshold_config = [80, 87, 85, 89, 85]

# Unused helper (dead code path - distractor)
def auxiliary_diagnostic(data):
    return sum(1 for a, b in zip(data, data[1:]) if a > b)

# Key execution point
final_score = analyze_performance(metrics_data, threshold_config)

# Print result
print(f"Result: {final_score}")