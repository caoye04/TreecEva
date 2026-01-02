def evaluate_performance(feedback):
    base_score = 0
    bonus_tracker = []
    penalty_accumulator = 0

    # Irrelevant data structure - distractor
    historical_metrics = {'peak': 95, 'trough': 12, 'average': 47}
    temp_result = sum(historical_metrics.values()) % 7

    for category, ratings in feedback.items():
        raw_total = sum(ratings)
        count = len(ratings)
        avg_rating = raw_total / count if count > 0 else 0

        # Logical branching with mixed operations
        if avg_rating >= 4.0:
            base_score += 10
            if raw_total > 20:
                bonus_tracker.append(raw_total // 5)
        elif avg_rating >= 2.5:
            base_score += 5
        else:
            penalty_accumulator += 2

        # Bitwise red herring - doesn't affect final score
        mask = 0b1101
        masked_value = raw_total & mask
        debug_flag = (masked_value ^ 0b1010) > 5  # unused

    # Complex but irrelevant set operation
    unique_bonuses = set(bonus_tracker)
    adjustment_factor = len(unique_bonuses.intersection({3, 6, 9})) * 2

    # Dictionary-based mapping distractor
    level_map = {1: 'low', 2: 'mid', 3: 'high'}
    level_key = min(3, max(1, base_score // 10))
    level_str = level_map[level_key]  # unused string

    # Core computation embedded among noise
    stability_check = len(feedback.get('usability', [])) ^ len(feedback.get('performance', []))
    stability_bonus = 3 if stability_check & 1 else 0

    final_score = base_score - penalty_accumulator + stability_bonus + adjustment_factor

    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_data = {
    'usability': [4, 5, 4, 3],
    'performance': [3, 2, 5],
    'security': [1, 2],
    'documentation': [4, 4, 5, 4, 3]
}

# Execution point
final_score = evaluate_performance(feedback_data)