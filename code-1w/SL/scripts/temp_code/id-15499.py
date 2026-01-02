def analyze_employee_performance(employee_data, thresholds):
    # Irrelevant helper that isn't used
    def unused_helper(x):
        return x ** 2 + 3 * x - 1

    base_multiplier = 1.5
    adjustment_factor = 0.8
    temp_result = []
    cumulative_shift = 0

    # Distractor: dead code path
    if len(employee_data) > 100:
        dummy_cache = {i: i**3 for i in range(10)}
        for k in dummy_cache:
            cumulative_shift += k % 7

    performance_bins = {'high': [], 'medium': [], 'low': []}
    bonus_eligibility = set()

    # Real logic begins: categorize employees and compute adjusted scores
    for idx, (name, metrics) in enumerate(employee_data.items()):
        productivity = metrics['output'] / (metrics['hours'] + 1e-8)
        quality = metrics['quality_score']
        team_impact = metrics.get('team_impact', 1.0)

        raw_score = productivity * 0.4 + quality * 0.3 + team_impact * 0.3

        # Apply threshold-based scaling using zip for parallel comparison
        scaling_factors = [1.0, 1.2, 1.5]
        tier_bounds = [thresholds['low'], thresholds['medium'], thresholds['high']]
        applied_factor = 1.0
        for bound, factor in zip(tier_bounds, scaling_factors):
            if raw_score >= bound:
                applied_factor = factor

        adjusted_score = raw_score * applied_factor * base_multiplier
        temp_result.append(adjusted_score)

        # Categorize based on final adjusted score
        if adjusted_score >= 85:
            performance_bins['high'].append(name)
            if quality > 4.0:
                bonus_eligibility.add(name)
        elif adjusted_score >= 60:
            performance_bins['medium'].append(name)
        else:
            performance_bins['low'].append(name)

        # Distractor: unnecessary string processing
        name_parts = name.split(' ')
        reversed_parts = [part[::-1] for part in name_parts]
        obfuscated_tag = ''.join(reversed_parts)
        _ = len(obfuscated_tag)  # used only to justify computation

    # Real aggregation: use lambda to filter high performers above average
    avg_score = sum(temp_result) / len(temp_result) if temp_result else 0
    top_performer_filter = lambda s: s > avg_score * 1.1
    top_scores = list(filter(top_performer_filter, temp_result))

    # Final score computed from weighted combination
    exploration_bonus = len(bonus_eligibility) * 2.5
    stability_penalty = len(performance_bins['low']) * 1.2
    final_score = (sum(top_scores) + exploration_bonus - stability_penalty) * adjustment_factor

    # Additional distraction: unused nested loop
    metadata_summary = {}
    for category, emp_list in performance_bins.items():
        count = len(emp_list)
        for e in emp_list:
            if e.startswith('A'):
                metadata_summary[category] = count  # partial update, not fully used

    return final_score

# Input data
employee_records = {
    'Alice Johnson': {'output': 420, 'hours': 78, 'quality_score': 4.6, 'team_impact': 1.4},
    'Bob Chen': {'output': 380, 'hours': 80, 'quality_score': 4.1, 'team_impact': 1.2},
    'Carol Ruiz': {'output': 200, 'hours': 75, 'quality_score': 3.2, 'team_impact': 0.9},
    'Dan Patel': {'output': 150, 'hours': 70, 'quality_score': 2.1, 'team_impact': 0.7},
    'Eva Kim': {'output': 400, 'hours': 82, 'quality_score': 4.3, 'team_impact': 1.3}
}

performance_thresholds = {
    'low': 40,
    'medium': 60,
    'high': 75
}

# Execution point of interest
final_score = process_performance_metrics = analyze_employee_performance(employee_records, performance_thresholds)
print(f"Result: {final_score}")