def evaluate_performance(feedback):
    base_score = 0
    penalty_factor = 0.9
    bonus_tracker = []
    temp_result = 0

    # Irrelevant accumulator for distraction
    dummy_sum = 0
    for i in range(10):
        dummy_sum += i * 0.1  # Non-impacting floating point additions

    # Real logic begins: score based on feedback categories
    weights = {'accuracy': 0.4, 'speed': 0.3, 'clarity': 0.2, 'engagement': 0.1}
    weighted_total = 0.0
    max_deviation = 0.0

    for category, score in feedback.items():
        if category in weights:
            contribution = score * weights[category]
            weighted_total += contribution

            # Track deviation from ideal (5.0) for no real use - red herring
            deviation = abs(5.0 - score)
            if deviation > max_deviation:
                max_deviation = deviation

            # Bonus logic: hidden rule - if any score >= 4.8, add to bonus tracker
            if score >= 4.8:
                bonus_tracker.append(contribution)

    # Unused recursive helper - misleading complexity
    def calculate_decay(n):
        if n <= 1:
            return 1
        return n * 0.95 + calculate_decay(n - 1) * 0.05

    # Actual scoring rule: apply bonus only if at least two high scores
    extra_bonus = 0.0
    if len(bonus_tracker) >= 2:
        extra_bonus = 5.0  # Flat bonus for strong performance

    # Final adjustment
    final_score = weighted_total * 100 + extra_bonus  # Scale to percentage-like score

    # Dead code branch - never executed due to data
    if 'debug_mode' in feedback and feedback['debug_mode']:
        temp_result = final_score * 0.9  # Distractor

    return int(final_score)

# Input data
feedback_map = {
    'accuracy': 4.9,
    'speed': 4.85,
    'clarity': 4.7,
    'engagement': 4.95,
    'notes': 'Excellent performance overall',  # Irrelevant field
    'timestamp': 1712345678  # Unused metadata
}

# Execution
final_score = evaluate_performance(feedback_map)
print(f"Result: {final_score}")