def main():
    # Simulate user feedback analysis for a service quality evaluation
    responses = ["very good", "excellent", "good", "satisfactory", "needs improvement", "excellent", "good", "fair"]

    # Mapping of feedback to base scores
    score_map = {
        "excellent": 5,
        "very good": 4.5,
        "good": 4,
        "satisfactory": 3,
        "fair": 2,
        "needs improvement": 1
    }

    # Irrelevant distractor: unused alternative mapping
    alt_mapping = {"outstanding": 5, "average": 3, "poor": 1}

    # Compute frequency of each response (distractor computation)
    frequency_count = {resp: responses.count(resp) for resp in set(responses)}

    # Extract base scores for actual responses
    raw_scores = [score_map[resp] for resp in responses]

    # Apply dynamic adjustment based on position (recency bias: later responses weighted higher)
    adjusted_scores = [
        score * (1 + i * 0.05) for i, score in enumerate(raw_scores)
    ]

    # Normalize scores to 0-5 scale using min-max (unnecessary normalization)
    min_score, max_score = min(adjusted_scores), max(adjusted_scores)
    normalized_scores = [
        5 * (s - min_score) / (max_score - min_score) if max_score > min_score else 5
        for s in adjusted_scores
    ]

    # Simulate expert weighting tiers (actual relevant logic starts here)
    def get_weight(score):
        if score >= 4.5:
            return 1.2
        elif score >= 3.5:
            return 1.0
        else:
            return 0.8

    weights = [get_weight(s) for s in raw_scores]

    # Feedback levels with artificial categorization
    feedback_levels = [1 if s >= 4 else 0 for s in raw_scores]

    # Dead code path - never called
    def legacy_calculate(x):\n        return sum(x) / len(x) * 0.95

    # Core aggregation function with lambda and list comprehension
    aggregate_performance = lambda levels, w: sum(
        [lvl * wg for lvl, wg in zip(levels, w)]
    )

    # Critical statement
    final_score = aggregate_performance(feedback_levels, weights)

    # Distractor: unused derived metrics
    average_normalized = sum(normalized_scores) / len(normalized_scores)
    peak_response_index = [i for i, s in enumerate(raw_scores) if s == 5]
    decay_factor = 0.9 ** len(responses)

    # Print result as required
    print(f"Result: {final_score}")

main()