def evaluate_performance(items, limit):
    # Irrelevant counters (distractor variables)
    total_accesses = 0
    cache_misses = 0
    debug_log = []

    # Core data transformation
    normalized = {}
    for key, val in items.items():
        if isinstance(val, str):
            cleaned = val.strip().lower()
            length_factor = len(cleaned) % 7
            normalized[key] = hash(cleaned) % 100 + length_factor
        else:
            normalized[key] = int(val) % 50

    # Secondary processing with red herring logic
    temp_results = []
    for k, v in normalized.items():
        total_accesses += 1  # Distractor: not used later
        if 'temp' in k:  # Misleading condition that never triggers
            cache_misses += 1
        adjusted = v * 1.1 if v > 40 else v * 0.9
        temp_results.append(adjusted)

    # Actual decision logic
    base_score = sum(temp_results)
    penalty = 0
    for v in temp_results:
        if v > 55:
            penalty += 3
    final_score = int(base_score - penalty * 2.5)

    # Dead code path (never reached)
    if False:
        debug_log.append('Final score computed')
        return -1

    return final_score

# Setup input data
product_data = {
    'item_a': '  HighQuality  ',
    'item_b': 'Low Defect Rate',
    'item_c': 87,
    'config_x': 'STANDBY',
    'status': 'Active'
}
threshold = 50

# Execute main logic
temp_var = [x for x in range(3)]  # Useless list comprehension
unused_flag = len(temp_var) > 5  # Irrelevant boolean check

final_score = evaluate_performance(product_data, threshold)
print(f"Result: {final_score}")