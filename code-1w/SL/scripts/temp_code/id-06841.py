def evaluate_performance(feedback_set, criteria_map):
    base_points = 0
    penalty_adjustment = 0
    bonus_tracker = []

    # Irrelevant tracking variables (distractors)
    debug_log = []
    temp_result_cache = {}

    for item in feedback_set:
        if isinstance(item, tuple) and len(item) == 2:
            category, rating = item
            
            # Real logic branch: contributes to final result
            if category in criteria_map:
                base_points += criteria_map[category] * rating
                
                # Semi-relevant computation: affects bonus later
                if rating >= 4:
                    bonus_tracker.append(category)
            
            # Dead code path (misleading)
            if rating == 5:
                debug_log.append(f"Perfect score in {category}")  # Unused

    # Actual bonus calculation using set operations
    eligible_categories = set(bonus_tracker)
    priority_areas = {'usability', 'performance', 'security', 'compatibility'}
    high_priority_bonus = eligible_categories & priority_areas  # Intersection

    # Multiple assignment distractor
    extra_bonus, _ = divmod(len(high_priority_bonus), 2)

    # Final score computation (only this matters)
    final_score = base_points + len(high_priority_bonus) * 3 + extra_bonus

    # Unused dictionary aggregation (distractor)
    summary_report = {
        'total_categories': len(criteria_map),
        'achieved_bonuses': list(high_priority_bonus),
        'raw_points': base_points
    }

    return final_score

# Main execution
feedback_data = [
    ('usability', 5),
    ('performance', 4),
    ('documentation', 3),
    ('security', 5),
    ('compatibility', 2),
    ('maintainability', 4)
]

benchmark_criteria = {
    'usability': 8,
    'performance': 6,
    'security': 10,
    'compatibility': 7,
    'documentation': 5,
    'maintainability': 4
}

intermediate_calc = sum([v for v in benchmark_criteria.values()]) // len(benchmark_criteria)  # Distractor

final_score = evaluate_performance(feedback_data, benchmark_criteria)
print(f"Target result: {final_score}")