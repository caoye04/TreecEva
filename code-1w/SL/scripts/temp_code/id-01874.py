import itertools

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant smoothing pass (distractor)
    smoothed = [trend[0]]
    for i in range(1, len(trend)-1):
        smoothed.append((trend[i-1] + trend[i] + trend[i+1]) // 3)
    smoothed.append(trend[-1])

    # Actual logic: count direction changes
    changes = 0
    for j in range(1, len(trend)):
        if trend[j] != 0 and trend[j] != trend[j-1]:
            changes += 1
    return changes


def evaluate_thresholds(values, low=10, high=90):
    # Dead code path - never used
    if len(values) == 0:
        return 0
    
    above = sum(1 for v in values if v > high)
    below = sum(1 for v in values if v < low)
    total_extremes = above + below  # unused variable (distractor)
    
    # Only this line matters
    return sum(v for v in values if low <= v <= high)


def process_results(data):
    # Extract relevant metrics
    base_values = [item['metric'] for item in data]
    
    # Distractor: complex unpacking and case conversion
    labels = [item['label'].upper() for item in data]
    key_pairs = [(lbl[0], val) for lbl, val in zip(labels, base_values)]
    grouped = {k: [v for lbl, v in key_pairs if lbl == k] for k in set(lbl[0] for lbl in labels)}
    
    # Red herring with itertools
    flat_combinations = list(itertools.chain.from_iterable(
        [list(itertools.combinations(group, 2)) for group in grouped.values() if len(group) >= 2]
    ))
    combination_sum = sum(len(flat_combinations))  # Computed but irrelevant
    
    # Real work begins
    filtered_data = evaluate_thresholds(base_values, 15, 85)
    pattern_change_count = analyze_pattern(base_values)
    
    # Key computation
    adjustment_factor = len([x for x in base_values if x % 2 == 0])  # count even numbers
    raw_score = filtered_data + (pattern_change_count * 10)
    final_score = raw_score - adjustment_factor
    
    # Debug print that doesn't affect result (distractor)
    debug_info = {
        'length': len(base_values),
        'first_label': labels[0] if labels else None,
        'combinations': combination_sum
    }
    
    return final_score

# Main execution
assessment_data = [
    {'label': 'alpha', 'metric': 5},
    {'label': 'beta', 'metric': 22},
    {'label': 'gamma', 'metric': 45},
    {'label': 'delta', 'metric': 67},
    {'label': 'epsilon', 'metric': 89},
    {'label': 'zeta', 'metric': 12},
    {'label': 'eta', 'metric': 33}
]

result = process_results(assessment_data)
print(f"Target result: {result}")