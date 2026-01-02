def evaluate_performance(feedbacks, criteria):
    base_weight = 0.8
    bonus_factor = 0.2
    
    # Irrelevant preprocessing: Normalize feedback indices (not used in final logic)
    normalized_indices = [f % 7 for f in feedbacks if f > 0]
    temp_sum = sum([n * 1.5 for n in normalized_indices if n < 5])

    # Distractor: Unused transformation chain
    transform = lambda x: (x ** 2) + 1
    mapped_values = [transform(val) for val in feedbacks if val % 2 == 0]
    discarded_total = sum(mapped_values) / len(mapped_values) if mapped_values else 0

    # Core logic begins
    valid_feedback = {f for f in feedbacks if f in criteria['thresholds']}
    adjustment = 1.0
    
    if len(valid_feedback) > 2:
        adjustment = 1.3
    elif len(valid_feedback) == 2:
        adjustment = 1.1
    else:
        adjustment = 0.9

    # Conditional expression with logical operations
    base_score = sum(f for f in feedbacks if f > 0) * base_weight
    bonus_eligible = any(f > 8 for f in feedbacks) and not (all(f < 5 for f in feedbacks))
    extra_bonus = bonus_factor * 15 if bonus_eligible else 0

    # Secondary distractor: complex but unused data structure manipulation
    snapshot = tuple(sorted(feedbacks, reverse=True))
    shadow_score = 0
    for idx, val in enumerate(snapshot):
        if idx % 3 == 0:
            shadow_score += val * 0.1
        elif idx % 3 == 1:
            shadow_score -= val * 0.05

    # Final computation
    final_score = (base_score + extra_bonus) * adjustment
    
    # Additional red herring: a function that's defined but never called
    def deprecated_calc(x): return x * 0.75
    
    return int(final_score)

# Setup inputs
criteria_config = {
    'thresholds': {3, 6, 7, 9},
    'weights': [0.1, 0.3, 0.6]
}

feedback_set = [4, 6, 7, 9, 2, -1, 8]
benchmark = criteria_config

# Execute
temp_var = [x for x in feedback_set if x % 2 != 0]
dummy_aggregate = sum(temp_var) * 0.3

final_score = evaluate_performance(feedback_set, benchmark)
print(f"Result: {final_score}")