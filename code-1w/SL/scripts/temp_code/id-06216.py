def process_metrics(data, limit):
    temp_log = []
    cumulative = 0
    overflow_flag = False
    efficiency_score = 0
    penalty_factor = 1.5

    for record in data:
        raw_value = record['value']
        category = record['type']
        adjusted = raw_value * 0.9 if category == 'A' else raw_value * 1.1

        if adjusted > 1000:
            temp_log.append(f'High: {adjusted}')
            continue

        temp_log.append(f'Processed: {adjusted}')
        cumulative += adjusted

        if cumulative > 5000 and not overflow_flag:
            cumulative *= 0.8
            overflow_flag = True

    filtered_values = [v['value'] for v in data if v['value'] < limit]
    outlier_count = len([v for v in data if v['value'] > 900])

    # Irrelevant statistical distraction
    avg_filtered = sum(filtered_values) / len(filtered_values) if filtered_values else 0
    variance_proxy = sum((x - avg_filtered) ** 2 for x in filtered_values) / len(filtered_values) if filtered_values else 0

    base_efficiency = cumulative * 0.75
    adjustment = (outlier_count * 10) if outlier_count > 3 else 0
    efficiency_score = int(base_efficiency - adjustment)

    secondary_check = set(item['type'] for item in data)
    expected_types = {'A', 'B', 'C'}
    type_completeness = len(expected_types - secondary_check)

    # Dummy corrective scaling (not used)
    if type_completeness > 0:
        efficiency_score = max(0, efficiency_score - 50 * type_completeness)

    # Final output computation
    final_output = efficiency_score + (variance_proxy * 0.1)
    
    return int(final_output)

# Input data
raw_data = [
    {'value': 450, 'type': 'A'},
    {'value': 320, 'type': 'B'},
    {'value': 510, 'type': 'A'},
    {'value': 290, 'type': 'C'},
    {'value': 680, 'type': 'B'},
    {'value': 470, 'type': 'A'},
    {'value': 950, 'type': 'C'},  # This will be skipped due to adjusted > 1000
    {'value': 380, 'type': 'B'}
]
threshold = 500

# Execution
final_output = process_metrics(raw_data, threshold)
efficiency_score = final_output  # capture at key point
print(f"Result: {efficiency_score}")