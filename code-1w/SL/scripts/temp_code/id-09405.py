def calculate_overall_score(records):
    # Irrelevant pre-processing: normalize names (not used in scoring)
    normalized_names = [name.strip().title() for name in records.get('participants', [])]

    # Relevant data extraction
    scores = records.get('scores', [])
    weights = records.get('weights', [1] * len(scores))

    # Misleading intermediate: counting invalid entries (unused)
    invalid_count = sum(1 for s in scores if not isinstance(s, (int, float)))

    # Weighted sum calculation with filtering
    valid_weighted_sum = sum(
        score * weight 
        for score, weight in zip(scores, weights)
        if isinstance(score, (int, float)) and score >= 0
    )

    # Extra distraction: unused helper lambda
    adjust_outlier = lambda x: x * 0.9 if x > 100 else x

    # Another red herring: simulated time-based decay (not applied)
    time_decay_factor = 0.95 ** (records.get('days_since_test', 0) // 7)

    # Actual logic: cap maximum contribution per score to 80
    capped_scores = [min(s, 80) for s in scores if isinstance(s, (int, float))]
    capped_total = sum(c * w for c, w in zip(capped_scores, weights[:len(capped_scores)]))

    # Final aggregation: use capped weighted total but divide by number of tests
    test_count = len(capped_scores) or 1
    base_score = capped_total / test_count

    # Bonus logic: if more than 3 tests, add 5 point bonus
    bonus = 5 if test_count > 3 else 0

    # Final score computation
    final_score = base_score + bonus
    return final_score

# Input data
student_data = {
    'participants': [' alice ', 'bob', 'charlie'],
    'scores': [95, -10, 87, 90, 105],
    'weights': [0.5, 1.0, 1.5, 2.0, 1.0],
    'days_since_test': 14,
    'version': 'v2.1'
}

# Execute
final_score = calculate_overall_score(student_data)
print(f"Result: {final_score}")