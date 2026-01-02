def evaluate_performance(feedback):
    # Mapping of employee feedback to performance metrics
    ratings = {'excellent': 5, 'good': 4, 'satisfactory': 3, 'needs_improvement': 2, 'poor': 1}
    
    # Irrelevant utility: counts characters in feedback keys (distractor)
    key_length_sum = sum(len(k) for k in feedback.keys())
    temp_offsets = [key_length_sum % r for r in ratings.values()]
    adjustment_factor = sum(temp_offsets) // len(temp_offsets) if temp_offsets else 0

    # Relevant logic: compute base score from values
    raw_values = [ratings.get(v, 0) for v in feedback.values()]
    base_score = sum(raw_values) * len(feedback)

    # Secondary processing using lambda and set operations
    unique_scores = set(raw_values)
    multiplier_fn = lambda x: 2 if x >= 4 else 1
    bonus = sum(map(multiplier_fn, unique_scores))

    # Conditional branch based on team size (simulated via dictionary size)
    team_size = len(feedback)
    if team_size > 3:
        growth_potential = 10
        # Nested condition with red herring calculation
        if 'excellent' in feedback.values():
            phantom_impact = growth_potential * 0.1
            growth_potential += adjustment_factor  # semi-relevant use of distractor
    else:
        growth_potential = 5

    # Core computation chain
    intermediate = base_score + bonus
    volatility_index = abs(intermediate - sum(unique_scores) * 2.5)
    normalized_volatility = int(volatility_index // (team_size or 1))

    # Final score computation (key statement)
    final_score = intermediate + growth_potential - normalized_volatility

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Data setup
feedback_map = {
    'alice': 'excellent',
    'bob': 'good',
    'charlie': 'good',
    'diana': 'excellent',
    'evan': 'satisfactory'
}

# Execution point
final_score = evaluate_performance(feedback_map)