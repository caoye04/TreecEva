def calculate_final_score(records, importance):
    base_total = 0
    adjustment_factor = 0.0
    temp_result = []
    outlier_count = 0

    for record in records:
        # Extract components
        name = record['name']
        score_str = str(record['score'])
        category = record['type']

        # Irrelevant string processing (distractor)
        reversed_name = name[::-1]
        if 'x' in reversed_name.lower():
            adjustment_factor += 0.1

        # Core logic: extract numeric score and normalize
        raw_score = float(score_str)
        normalized = raw_score / 100.0

        # Weighted contribution
        weight_key = category + '_weight'
        if weight_key in importance:
            weighted_val = normalized * importance[weight_key]
            temp_result.append(weighted_val)

        # Outlier detection (semi-relevant but doesn't affect final path)
        if raw_score < 10 or raw_score > 95:
            outlier_count += 1

    # Secondary loop: aggregate with conditional scaling
    scaled_sum = 0.0
    for i, val in enumerate(temp_result):
        if i % 2 == 0:
            scaled_sum += val * 1.1
        else:
            scaled_sum += val * 0.95

    # Dummy dictionary operation (distractor)
    stats_summary = {
        'count': len(temp_result),
        'outliers': outlier_count,
        'version': 'v2.1'
    }
    stats_summary['processed'] = True
    version_parts = stats_summary['version'].split('.')
    adjustment_factor += int(version_parts[0])

    # Final computation chain
    base_total = sum(temp_result)
    fluctuation = abs(scaled_sum - base_total)
    final_score = int((base_total * 500) + (fluctuation * 20))

    # Dead code path (irrelevant)
    if adjustment_factor > 100:
        final_score = -1

    return final_score

# Input data
entry_data = [
    {'name': 'Alice', 'score': 88, 'type': 'primary'},
    {'name': 'Bob', 'score': 76, 'type': 'secondary'},
    {'name': 'Charlie', 'score': 92, 'type': 'primary'},
    {'name': 'Diana', 'score': 65, 'type': 'secondary'},
    {'name': 'Eve', 'score': 94, 'type': 'primary'}
]

weights_map = {
    'primary_weight': 0.6,
    'secondary_weight': 0.4
}

# Execute
final_score = calculate_final_score(entry_data, weights_map)
print(f"Result: {final_score}")