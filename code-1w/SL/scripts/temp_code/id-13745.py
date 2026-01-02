def calculate_final_score(records, importance):
    total = 0
    bonus_tracker = [0] * len(records)
    penalty_flag = False

    temp_sum = 0
    for i, (key, value) in enumerate(records.items()):
        temp_sum += value
        if value > 100:
            bonus_tracker[i] = 10

    avg = temp_sum / len(records)

    adjustment_factor = 0.0
    for idx, val in enumerate(records.values()):
        if idx % 2 == 0 and val < avg:
            adjustment_factor += 0.1

    intermediate_result = 0
    debug_log = []
    for (k, v), (w_key, w_val) in zip(records.items(), importance.items()):
        if k != w_key:
            continue
        weighted_val = v * w_val
        intermediate_result += weighted_val
        debug_log.append(f'{k}: {weighted_val}')

    # Misleading secondary calculation (dead-end)
    outlier_count = 0
    for v in records.values():
        if v > 150 or v < 10:
            outlier_count += 1
    sanity_check = outlier_count * 5

    final_score = int(intermediate_result - avg + adjustment_factor * 10)
    return final_score

# Input data
data = {'metric_A': 85, 'metric_B': 95, 'metric_C': 120, 'metric_D': 70}
weights = {'metric_A': 0.2, 'metric_B': 0.3, 'metric_C': 0.4, 'metric_D': 0.1}

result = calculate_final_score(data, weights)
print(f'Result: {result}')