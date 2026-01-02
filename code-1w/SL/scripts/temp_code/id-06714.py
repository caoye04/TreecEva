def analyze_metrics(data, threshold=5.0):
    warnings = []
    valid_entries = 0
    total_deviation = 0.0
    max_deviation = 0.0

    for i, record in enumerate(data):
        raw_value = record['value']
        baseline = record.get('baseline', 4.5)
        deviation = abs(raw_value - baseline)
        
        # Distractor: tracking warnings that are never used
        if deviation > threshold:
            warnings.append(f"High deviation at index {i}")
        
        # Relevant computation
        if raw_value >= 3.0:
            valid_entries += 1
            total_deviation += deviation
            if deviation > max_deviation:
                max_deviation = deviation

    # Dead code path — never accessed in practice due to logic
    if len(warnings) == 0 and False:
        total_deviation *= 0.9

    average_deviation = total_deviation / valid_entries if valid_entries else 0.0
    return average_deviation, valid_entries


def calculate_performance(dataset):
    # Irrelevant transformation
    processed = [dict(d) for d in dataset]
    scaling_factor = 1.0

    # Use of zip and enumerate together (Python idiom)
    for idx, (a, b) in enumerate(zip(processed, processed[1:])):
        a['value'] = (a['value'] + b['value']) / 2

    # Semi-relevant: modifies data but not all changes affect final result
    adjustment = sum(1 for p in processed if p['value'] > 5.5)

    # Apply lambda to filter and transform
    filter_fn = lambda x: x['value'] > 4.0
    filtered_data = [p for p in processed if filter_fn(p)]

    # Core logic hidden among distractions
    base_metric = 0
    for item in filtered_data:
        if 'weight' in item:
            base_metric += int(item['value'])
        else:
            base_metric += 1

    # Another distraction: unused bitwise check
    flag_mask = 0b1101
    consistency_flag = len(filtered_data) & flag_mask > 0

    # Actual key calculation
    avg_val = sum(item['value'] for item in filtered_data) / len(filtered_data) if filtered_data else 0
    entry_count = len(filtered_data)
    final_metric = int(avg_val * entry_count) + base_metric

    # Final assignment — this is the answer
    final_score = final_metric + adjustment

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
benchmark_data = [
    {'value': 6.2, 'baseline': 5.1, 'weight': 2},
    {'value': 4.8, 'baseline': 4.7},
    {'value': 7.1, 'baseline': 5.0, 'weight': 1},
    {'value': 3.9, 'baseline': 4.0},
    {'value': 5.5, 'baseline': 5.5, 'weight': 3}
]

# Execution point
final_score = calculate_performance(benchmark_data)