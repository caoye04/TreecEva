def evaluate_performance(weights, data):
    # Preprocess: normalize data using min-max scaling
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in data]

    # Irrelevant transformation: circular shift (not used in final result)
    shifted = [normalized[-1]] + normalized[:-1]
    inverted = [1 - x for x in shifted]  # Distractor computation

    # Weight application using lambda for dynamic scoring
    weighted_scorer = lambda val, weight: val ** weight
    weighted_scores = [weighted_scorer(norm, weights[i % len(weights)]) for i, norm in enumerate(normalized)]

    # Aggregate score with damping factor (irrelevant intermediate)
    raw_aggregate = sum(weighted_scores)
    damping_factor = 0.98 + 0.02 * (len(data) % 5)  # Minor perturbation
    damped_score = raw_aggregate * damping_factor

    # Conditional bonus based on pattern detection (dead code path due to fixed input)
    has_pattern = all(abs(normalized[i] - normalized[i-1]) < 0.1 for i in range(1, len(normalized)))
    bonus_awarded = 10 if has_pattern else 0  # Never triggered in this case

    # Core logic: apply bitwise influence from weight keys (actual contributor)
    bit_influence = 0
    for w in weights:
        w_int = int(w * 100)
        bit_influence ^= (w_int & 0b1111)  # Use lower 4 bits of scaled weight

    # Final score combines damped weighted score and bit influence
    final_component_a = damped_score * 100
    final_component_b = bit_influence * 5
    final_score = int(final_component_a + final_component_b)

    return final_score

# Main execution context
metric_weights = [0.85, 0.72, 0.93, 0.64]
raw_data = [23, 85, 47, 61, 12, 77]

# Extraneous dictionary operations for distraction
stats_summary = {
    'count': len(raw_data),
    'peak': max(raw_data),
    'baseline': sum(raw_data) / len(raw_data),
    'flags': [x > 50 for x in raw_data],
    'meta': {
        'version': '2.1',
        'mode': 'standard'
    }
}

# Dead-end function that's defined but not called
def calculate_risk_profile(dataset):
    risk = 0
    for x in dataset:
        if x > 80:
            risk += 3
        elif x > 60:
            risk += 2
        else:
            risk += 1
    return risk / len(dataset)

# Actual critical execution point
final_score = evaluate_performance(metric_weights, raw_data)
print(f"Result: {final_score}")