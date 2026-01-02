def evaluate_performance(weights, scores, adj):
    base = sum(w * s for w, s in zip(weights, scores))
    penalty = 0
    
    # Irrelevant computation: tracking unused performance tiers
    tiers = ['basic', 'intermediate', 'advanced']
    tier_index = len(scores) % 3
    temp_debug = f"Processing {tiers[tier_index]} tier"
    
    # Distractor: complex but unused transformation
    transformed = {i: (s ** 0.5 if s > 0 else 0) for i, s in enumerate(scores)}
    
    # Actual logic path
    multiplier = 1.0
    if base > 75:
        multiplier = 1.2
    elif base > 50:
        multiplier = 1.1
    else:
        multiplier = 0.9

    # Conditional adjustment using lambda (relevant)
    apply_bonus = lambda x, th: 10 if x > th else 0
    bonus = apply_bonus(base, 60)

    # Unused set operation (distractor)
    unique_weights = set(weights)
    weight_span = max(unique_weights) - min(unique_weights)

    # Core calculation with interference from irrelevant variables
    adjusted_base = base * multiplier + bonus
    final = adjusted_base * adj  # adj is 0.95 in call

    # Dead code branch (never executed due to fixed condition)
    if False:
        fallback = sum(transformed.values()) * 2
        final = fallback

    return int(final)

# Main execution
metric_weights = [0.2, 0.3, 0.3, 0.2]
raw_scores = [85, 70, 90, 65]
adjustment_factor = 0.95

# Unused tuple unpacking (distractor)
config_settings = ('enabled', 'strict', 1.0)
enabled_mode, validation_level, global_scale = config_settings

intermediate_total = sum(raw_scores) // len(raw_scores)  # distractor statistic

# Unused dictionary for logging
debug_log = {
    'input_checksum': hash(str(metric_weights + raw_scores)),
    'version': '2.1a'
}

final_score = evaluate_performance(metric_weights, raw_scores, adjustment_factor)
print(f"Result: {final_score}")