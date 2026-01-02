def analyze_metrics(raw_data):
    base_threshold = 42
    adjustment_factor = 1.5
    temp_result = 0
    secondary_cache = []

    for entry in raw_data:
        if 'flag' in entry and entry['flag'] == True:
            temp_result += entry.get('value', 0) * adjustment_factor
        else:
            temp_result -= entry.get('penalty', 1)

    return int(temp_result // 1)


def filter_outliers(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return {v for v in values if abs(v - mean_val) <= 2 * std_dev}


def evaluate_performance(metrics):
    baseline = 100
    decay_rate = 0.1
    bonus = 0
    penalty_counter = 0

    active_metrics = set()
    historical_flags = [False, True, False]

    for m in metrics:
        if m > baseline:
            active_metrics.add(m)
            bonus += 5
        elif m < baseline * 0.5:
            penalty_counter += 1
        else:
            continue

    # Simulate conditional suppression
    if len(active_metrics) > 3 and not historical_flags[2]:
        bonus += 10

    score_component_a = len(active_metrics) * 7
    score_component_b = bonus * 2
    score_component_c = max(0, 50 - (penalty_counter * 8))

    # Irrelevant transformation
    temp_array = [score_component_a] * 2
    temp_array.append(score_component_b)
    _ = sorted(temp_array, reverse=True)[0]  # unused

    final_score = score_component_a + score_component_b + score_component_c

    # Dead code branch (never executed due to constant condition)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {final_score}')

    return final_score

# Main execution flow
raw_input = [
    {'value': 10, 'flag': True},
    {'value': 15},
    {'value': 20, 'flag': True},
    {'value': 5},
    {'value': 30, 'flag': True},
    {'penalty': 3}
]

interim = analyze_metrics(raw_input)
metric_pool = [interim, 55, 60, 65, 70, 40, 35, 80]
metric_set = filter_outliers(metric_pool)

final_score = evaluate_performance(metric_set)
print(f'Target result: {final_score}')