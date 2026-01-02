def calculate_final_score(data, weights):
    base_total = 0
    adjustment_factor = 0.85
    temp_results = []
    
    # Process each rank entry with weighted contribution
    for entry in data:
        rank = entry['rank']
        base_value = 100 - (rank ** 1.5)
        if rank <= 3:
            base_value *= 1.2  # Top performers get multiplier
        temp_results.append(base_value)
    
    # Irrelevant statistical distraction
    mean_temp = sum(temp_results) / len(temp_results) if temp_results else 0
    variance_proxy = sum((x - mean_temp) ** 2 for x in temp_results) / len(temp_results) if temp_results else 0
    stability_index = 1 / (1 + variance_proxy)  # Not actually used later

    # Apply weight mapping from dictionary
    weighted_contributions = []
    for i, value in enumerate(temp_results):
        weight_key = min(i, len(weights) - 1)
        weight = weights.get(weight_key, 1.0)
        weighted_contributions.append(value * weight)
    
    # Secondary adjustment using modular arithmetic for rotation effect
    rotated_values = []
    for i, val in enumerate(weighted_contributions):
        shift = i % 4
        shifted = val * ((adjustment_factor + shift * 0.05) % 1.2)
        rotated_values.append(shifted)
    
    # Final aggregation with capped average
    raw_sum = sum(rotated_values)
    cap_limit = 500
    censored_sum = min(raw_sum, cap_limit)
    
    # Dummy combinatorics calculation (dead code, just distractor)
    n = len(rotated_values)
    combinations_2 = n * (n - 1) // 2 if n >= 2 else 0
    entropy_proxy = -(sum(v / raw_sum * (v / raw_sum).__log__() for v in rotated_values if v > 0)) if raw_sum > 0 else 0
    
    # Actual final score computation
    final_score = int(censored_sum // 1)  # Truncate to integer
    return final_score

# Main execution
if __name__ == '__main__':
    # Dataset: competition rankings
    rank_data = [
        {'id': 'A', 'rank': 1, 'category': 'alpha'},
        {'id': 'B', 'rank': 2, 'category': 'beta'},
        {'id': 'C', 'rank': 4, 'category': 'gamma'},
        {'id': 'D', 'rank': 6, 'category': 'delta'},
        {'id': 'E', 'rank': 3, 'category': 'epsilon'}
    ]

    # Bonus weights by index
    bonus_weights = {0: 1.3, 1: 1.1, 2: 0.9, 3: 0.7}

    # Extraneous pre-computation (distractor)
    predicted_ranks = [entry['rank'] for entry in rank_data]
    avg_predicted = sum(predicted_ranks) / len(predicted_ranks)
    rank_variance = sum((r - avg_predicted) ** 2 for r in predicted_ranks)

    # Key statement
    final_score = calculate_final_score(rank_data, bonus_weights)
    
    # Additional irrelevant transformations
    normalized_score = final_score / 100.0
    score_category = 'high' if normalized_score > 3.0 else 'medium' if normalized_score > 2.0 else 'low'
    
    print(f"Result: {final_score}")