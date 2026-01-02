def calculate_final_score(records, importance):
    # Irrelevant transformation: convert to set and back (no effect on order in this case)
    unique_ids = list(set([r['id'] for r in records]))
    sorted_ids = sorted(unique_ids)

    # Distractor: unused aggregation
    total_age = sum(r['age'] for r in records)
    avg_age = total_age / len(records)

    # Relevant computation: weighted sum using lambda
    weighted_values = map(lambda r: r['value'] * importance[r['category']], records)
    raw_score = sum(weighted_values)

    # Semi-relevant filtering: only high-value entries contribute fully
    high_value_threshold = 100
    adjustment_factor = 0.9 if any(r['value'] > high_value_threshold for r in records) else 1.0

    # Dead code path: never executed due to fixed condition
    debug_mode = False
    extra_penalty = 0
    if debug_mode:
        extra_penalty = -10 * len(records)

    # Key state tracking with distraction
    status_flags = {r['id']: (r['value'] > 50) for r in records}
    active_flags = sum(status_flags.values())

    # Final score calculation — depends only on raw_score and adjustment_factor
    base_adjusted = raw_score * adjustment_factor
    penalty = 5 * (len(records) - active_flags)  # minor penalty component
    final_score = base_adjusted - penalty

    return final_score

# Input data
weights = {'A': 1.2, 'B': 0.8, 'C': 1.5}
data_set = [
    {'id': 101, 'value': 120, 'category': 'A', 'age': 25},
    {'id': 102, 'value': 45, 'category': 'B', 'age': 30},
    {'id': 103, 'value': 200, 'category': 'C', 'age': 35},
    {'id': 104, 'value': 60, 'category': 'A', 'age': 28},
    {'id': 105, 'value': 30, 'category': 'B', 'age': 40}
]

# Execution
final_score = calculate_final_score(data_set, weights)
print(f"Result: {final_score}")