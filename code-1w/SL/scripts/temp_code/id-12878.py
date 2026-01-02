def process_results(entries, scaling_factors):
    base_scores = []
    adjustments = []
    temp_offset = 0

    for entry in entries:
        raw = entry['value']
        category = entry['type']
        
        # Real computation branch
        if category == 'A':
            base = raw * 1.5
        elif category == 'B':
            base = raw * 0.8
        else:
            base = raw * 0.3

        base_scores.append(base)

        # Distractor: complex-looking but unused adjustment logic
        if raw > 10:
            adj = (raw // 2) ^ 3
            adjustments.append(adj)
        else:
            adj = -((raw + 1) << 1)
            adjustments.append(adj)

    # Real weighting calculation
    weighted_sum = sum(base_scores[i] * scaling_factors[i] for i in range(len(base_scores)))
    total_weight = sum(scaling_factors)
    average_weighted = weighted_sum / total_weight

    # Irrelevant slicing and lambda red herring
    sliced_data = entries[1:-1]
    transform = lambda x: x ** 2 + 1
    ignored_transformations = [transform(s['value']) for s in sliced_data]

    # Dummy dictionary operations that don't affect outcome
    stats = {"count": len(entries), "max_base": max(base_scores)}
    stats["offset"] = temp_offset
    stats["dummy_key"] = "irrelevant"

    # Actual final score computation
    final_score = int(average_weighted + 0.5)  # Round to nearest integer

    # Another dead-end path with misleading early return hint
    if len(entries) > 100:
        return -999  # Dead code (never reached)

    return final_score

# Input data
input_entries = [
    {'value': 12, 'type': 'A'},
    {'value': 8, 'type': 'B'},
    {'value': 15, 'type': 'A'},
    {'value': 5, 'type': 'C'}
]
weights = [0.4, 0.2, 0.3, 0.1]

# Execution point
final_score = process_results(input_entries, weights)
print(f"Result: {final_score}")