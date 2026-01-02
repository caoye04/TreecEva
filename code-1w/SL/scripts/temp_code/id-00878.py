def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts


def normalize_values(raw_data):
    total = sum(raw_data)
    if total == 0:
        return [0 for _ in raw_data]
    return [round(v / total, 4) for v in raw_data]


def filter_outliers(values, limit=3.0):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    return [v for v in values if abs(v - mean_val) / std_dev <= limit], mean_val


def compute_final_score(dataset, thresholds):
    # Step 1: Extract and transform data
    flattened = []
    for record in dataset:
        flattened.extend(record['values'])
    
    # Irrelevant transformation (distractor)
    inverted_map = {i: val for i, val in enumerate([x * -1 for x in flattened if x > 0])}
    temp_debug_log = f'Inverted count: {len(inverted_map)}'
    
    # Step 2: Normalize and filter
    normalized = normalize_values(flattened)
    filtered, avg = filter_outliers([x * 100 for x in normalized])
    
    # Step 3: Categorize using threshold bands (semi-relevant)
    categories = {'low': [], 'medium': [], 'high': []}
    for val in filtered:
        if val < thresholds[0]:
            categories['low'].append(val)
        elif val < thresholds[1]:
            categories['medium'].append(val)
        else:
            categories['high'].append(val)
    
    # Step 4: Use set operations to find unique contribution zones
    high_set = set(range(len(filtered)))
    medium_set = set(range(len(filtered) // 2))
    overlap_zone = high_set.intersection(medium_set)
    adjustment_factor = len(overlap_zone) * 0.1
    
    # Step 5: Compute score with weighted contributions
    weights = {'low': 1, 'medium': 2, 'high': 3}
    base_score = 0
    for level, vals in categories.items():
        base_score += weights[level] * len(vals)
    
    # Step 6: Apply adjustment from set analysis and zip-based correlation check
    correlation_tally = 0
    shifted_vals = filtered[1:] + [filtered[0]]
    for a, b in zip(filtered, shifted_vals):
        if a > avg * 1.1 and b > avg * 1.1:
            correlation_tally += 1
    
    # Final computation
    stability_bonus = 5 if correlation_tally > len(filtered) // 3 else 0
    final_score = int(base_score * (1 + adjustment_factor) + stability_bonus)
    
    # Dead code path (red herring)
    if False:
        debug_snapshot = analyze_pattern([int(f) for f in filtered])
        print(debug_snapshot)
    
    return final_score

# Input data
thresholds_config = [25.0, 60.0]
data_entries = [
    {'id': 'A1', 'values': [10, 20, 30, 15]},
    {'id': 'B2', 'values': [5, 45, 55, 10]},
    {'id': 'C3', 'values': [25, 25, 25, 25]},
    {'id': 'D4', 'values': [50, 10, 5, 80]}
]

# Execute
final_score = compute_final_score(data_entries, thresholds_config)
print(f"Result: {final_score}")