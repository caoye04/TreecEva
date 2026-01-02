def calculate_rating(data, weight_map):
    base_score = 0
    bonus_tracker = []
    penalty_accum = 0

    for idx, (key, val) in enumerate(data.items()):
        if idx % 2 == 0:
            temp_val = val * weight_map.get(key, 1)
            base_score += temp_val
            bonus_tracker.append(temp_val)
        else:
            adjusted = val * 0.9
            penalty_accum += val * 0.1
            base_score += adjusted

    avg_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0
    
    # Irrelevant smoothing operation
    smoothed_vals = [x * 0.95 for x in bonus_tracker]
    ignored_result = max(smoothed_vals) - min(smoothed_vals) if smoothed_vals else 0

    # Dummy list comprehension with zip
    aux_data = [a + b for a, b in zip([10, 20, 30], [1, 2, 3])]
    extra_offset = sum(aux_data) // 10  # Not used in final logic

    # Final rating with forced conversion
    raw_final = base_score - penalty_accum + avg_bonus
    scaling_factor = 1.1
    final_rating = int(raw_final * scaling_factor)

    return final_rating

# Main execution context
user_interactions = {"clicks": 150, "views": 300, "shares": 45, "saves": 20}
feature_weights = {"clicks": 1.2, "views": 0.8, "shares": 2.0, "saves": 1.5}

intermediate_metric = sum(user_interactions.values()) / len(user_interactions)  # Distractor

# Unused transformation
transformed = {k: v ** 0.5 for k, v in user_interactions.items()}
dummy_pairs = list(enumerate(transformed.keys()))

final_score = calculate_rating(user_interactions, feature_weights)
print(f"Result: {final_score}")