def calculate_final_score(raw_data, importance_weights):
    # Initialize tracking variables
    temp_sum = 0
    adjustment_factor = 0.95
    cumulative_offset = 0
    ignored_counter = 0  # Distractor: not used in final logic

    # Preprocess: normalize data using z-score (only some values are relevant)
    mean_val = sum(raw_data) / len(raw_data)
    variance = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data)
    std_dev = variance ** 0.5
    normalized = [(x - mean_val) / std_dev for x in raw_data]

    # Weighted scoring with alignment via enumerate and zip
    weighted_scores = []
    for i, (val, weight) in enumerate(zip(normalized, importance_weights)):
        if i % 2 == 0:
            # Even indices get boosted by index position
            boosted_val = val * (1 + i * 0.1)
        else:
            # Odd indices are dampened
            boosted_val = val * 0.9
        weighted_scores.append(boosted_val * weight)

    # Secondary processing: group scores by sign (distractor computation)
    positive_group = [v for v in weighted_scores if v > 0]
    negative_group = [v for v in weighted_scores if v < 0]
    group_diff = len(positive_group) - len(negative_group)  # Not used later

    # Real computation path: sum top 4 values only
    sorted_weights = sorted(weighted_scores, reverse=True)
    top_contributions = sum(sorted_weights[:4])

    # Apply adjustment factor (relevant)
    adjusted_total = top_contributions * adjustment_factor

    # Final nonlinear transformation
    final_score = int((adjusted_total ** 2) / 10 + 17)  # Deterministic integer result

    # Dead code path (mild red herring)
    if len(negative_group) > 10:
        final_score += 100

    return final_score

# Main execution
if __name__ == '__main__':
    data = [88, 92, 75, 85, 95, 80, 70, 90]
    weights = [0.8, 1.2, 0.9, 1.1, 0.7, 1.3, 0.6, 1.4]

    # Irrelevant precomputation
    avg_weight = sum(weights) / len(weights)
    scaled_data = [x * avg_weight for x in data]  # Unused

    final_score = calculate_final_score(data, weights)
    print(f"Result: {final_score}")