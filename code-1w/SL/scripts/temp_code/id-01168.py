def calculate_final_score(items, importance_weights):
    base_values = [x['value'] for x in items]
    categories = [x['category'] for x in items]
    
    # Irrelevant preprocessing: reverse and pad (distractor)
    padded_categories = [cat[::-1] + '_rev' for cat in categories]
    dummy_lookup = {i: cat for i, cat in enumerate(padded_categories)}

    # Semi-relevant normalization (only some affect final result)
    max_base = max(base_values)
    normalized = [round(val / max_base, 4) for val in base_values]

    # Weight application using zip and lambda (core logic)
    weighted_func = lambda x, w: x * w
    weighted_vals = [weighted_func(norm, importance_weights[i]) for i, norm in enumerate(normalized)]

    # Secondary transformation with enumerate (mix of relevant and irrelevant)
    adjusted = []
    temp_offsets = []
    for idx, wv in enumerate(weighted_vals):
        if idx % 2 == 0:
            adjusted.append(wv * 1.1)
            temp_offsets.append(0.1 * wv)
        else:
            adjusted.append(wv * 0.95)
            temp_offsets.append(-0.05 * wv)

    # Dummy dictionary aggregation (distractor)
    debug_info = {
        'offsets': temp_offsets,
        'total_offset': sum(temp_offsets),
        'max_normalized': max(normalized),
        'version': 'debug_v1'
    }

    # Core accumulation (depends on prior steps)
    raw_total = sum(adjusted)

    # Conditional scaling based on category pattern (actual dependency)
    category_pattern_match = any(categories[i] == 'priority' and base_values[i] > 50 for i in range(len(categories)))
    
    if category_pattern_match:
        raw_total *= 1.25
    else:
        raw_total *= 0.9

    # Final non-linear adjustment (subtle but deterministic)
    final_score = round(raw_total ** 1.08, 3)
    
    return final_score

# Main data setup
data = [
    {'value': 85, 'category': 'priority'},
    {'value': 42, 'category': 'standard'},
    {'value': 67, 'category': 'priority'},
    {'value': 33, 'category': 'standard'}
]

weights = [0.4, 0.3, 0.5, 0.2]

# Execution with print
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")