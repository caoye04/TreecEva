def calculate_final_score(raw_data, limits):
    # Preprocess: filter valid entries using set operations
    valid_ids = {x for x in range(100, 200)}
    observed_ids = {item['id'] for item in raw_data if 'id' in item}
    common_ids = valid_ids & observed_ids  # Intersection to find valid observations

    # Irrelevant computation: statistical dispersion (not used later)
    mean_val = sum(item['value'] for item in raw_data) / len(raw_data)
    variance = sum((item['value'] - mean_val) ** 2 for item in raw_data) / len(raw_data)
    std_dev = variance ** 0.5

    # Distractor: secondary threshold logic with dead-end path
    high_precision = [item for item in raw_data if item['accuracy'] > 0.95]
    if len(high_precision) > 10:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 1.0  # Not actually applied

    # Core logic: count how many exceed dynamic thresholds
    count_a = 0
    count_b = 0
    for item in raw_data:
        if item['id'] in common_ids:
            if item['value'] > limits['primary']:
                count_a += 1
            if item['value'] < limits['secondary'] and item['flag']:
                count_b += item['weight']

    # Secondary distraction: unused transformation chain
    transformed = [abs(x['value'] - mean_val) for x in raw_data]
    normalized = [(t / (std_dev + 1e-8)) for t in transformed]
    outlier_count = len([z for z in normalized if z > 2.0])

    # Final score depends only on count_a and count_b
    base_score = count_a * 15
    bonus = count_b * 3
    final_score = base_score + bonus

    return final_score

# Input data setup
data_set = [
    {'id': 101, 'value': 45, 'accuracy': 0.92, 'flag': True, 'weight': 4},
    {'id': 105, 'value': 67, 'accuracy': 0.88, 'flag': False, 'weight': 2},
    {'id': 110, 'value': 73, 'accuracy': 0.96, 'flag': True, 'weight': 5},
    {'id': 145, 'value': 88, 'accuracy': 0.81, 'flag': True, 'weight': 3},
    {'id': 160, 'value': 52, 'accuracy': 0.75, 'flag': True, 'weight': 4},
    {'id': 205, 'value': 90, 'accuracy': 0.93, 'flag': False, 'weight': 1},
    {'id': 115, 'value': 40, 'accuracy': 0.89, 'flag': True, 'weight': 2}
]

dynamic_thresholds = {
    'primary': 60,
    'secondary': 50
}

# Execute calculation
final_score = calculate_final_score(data_set, dynamic_thresholds)
print(f"Result: {final_score}")