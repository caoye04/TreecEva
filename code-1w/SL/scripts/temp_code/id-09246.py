def analyze_metrics(data_map):
    temp_results = {}
    for key, value in data_map.items():
        if len(key) % 2 == 0:
            temp_results[key] = sum(v ** 0.5 for v in value if v > 0)
        else:
            temp_results[key] = sum(v * 0.1 for v in value if v < 50)
    return temp_results


def filter_outliers(zipped_stream):
    filtered = []
    for index, (val_a, val_b) in enumerate(zipped_stream):
        if index % 3 == 0 and val_a > 10:
            filtered.append(val_b * 1.5)
        elif val_b < 20:
            filtered.append(val_a * 0.7)
    return filtered


def calculate_performance(raw_entries):
    # Initialize various tracking variables (some are distractions)
    baseline = 0
    offset_adjustment = 1.2
    accumulator = 0
    debug_trace = []  # unused tracking
    intermediate_sum = 0

    # Step 1: Extract benchmark values using enumerate and zip
    indexed = list(enumerate(raw_entries))
    paired = list(zip([x[1]['metric_a'] for x in indexed], [x[1]['metric_b'] for x in indexed]))

    # Step 2: Filter outliers from paired data
    cleaned = filter_outliers(paired)

    # Step 3: Analyze metrics on auxiliary structure
    aux_data = {'m1': [16, 25, 36], 'm2': [10, 40, 60], 'm3': [81, 100]}
    analysis = analyze_metrics(aux_data)

    # Step 4: Accumulate relevant parts
    for i, val in enumerate(cleaned):
        if i in analysis['m1'] or i == 0:
            accumulator += val * 0.5
        else:
            accumulator += val * 0.2

    # Step 5: Apply conditional adjustment based on dictionary keys
    key_count = sum(1 for k in aux_data.keys() if k.startswith('m'))
    if key_count > 2:
        baseline = 5

    # Step 6: Compute final score with red herring operation
    phantom_calc = sum(len(v) for v in aux_data.values()) * 0.3  # irrelevant
    intermediate_sum = sum(analysis['m1']) + sum(analysis['m2'])  # semi-relevant
    final_score = int(baseline + accumulator + intermediate_sum // 10)

    # Output result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
benchmark_data = [
    {'metric_a': 20, 'metric_b': 15},
    {'metric_a': 30, 'metric_b': 25},
    {'metric_a': 40, 'metric_b': 5}
]

# Execute function
final_score = calculate_performance(benchmark_data)