import itertools

def evaluate_performance(metrics, weights):
    # Normalize metrics to z-scores (irrelevant for final logic but adds distraction)
    mean_metric = sum(metrics) / len(metrics)
    variance = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_metric) / std_dev for x in metrics] if std_dev != 0 else [0] * len(metrics)

    # Weighted score calculation – only this part matters
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    total_weight = sum(weights)
    raw_score = weighted_sum / total_weight if total_weight != 0 else 0

    # Apply non-linear boost (relevant)
    boosted_score = raw_score * (1 + 0.1 * (raw_score > 80))

    # Conditional adjustment based on metric diversity (semi-relevant)
    unique_metrics = len(set(round(m, 2) for m in metrics))
    diversity_bonus = 5 if unique_metrics >= 4 else 0

    # Dummy state tracking (distractor)
    history = []
    for i in range(3):
        temp_val = (i + 1) * 10
        history.append(temp_val)  # never used again

    # Final performance logic
    if boosted_score >= 75:
        final_score = boosted_score + diversity_bonus
    else:
        final_score = boosted_score - 10  # penalty

    # Red herring: complex dictionary aggregation (not affecting final_score)
    stats_summary = {
        'count': len(metrics),
        'z_mean': sum(z_scores) / len(z_scores),
        'max_z': max(z_scores),
        'weight_config': ''.join(str(int(w)) for w in weights),
        'dummy_flag': any(z > 2 for z in z_scores)
    }

    # Another distraction: unused itertools product
    combinations = list(itertools.product([1, 2], ['a', 'b']))  # not used

    return final_score

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

intermediate_total = sum(metrics) * 0.01  # irrelevant computation
buffer_array = [0] * len(metrics)  # dead storage
for idx in range(len(buffer_array)):
    buffer_array[idx] = idx * 2  # unused side effect

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")