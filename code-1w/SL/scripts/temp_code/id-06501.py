def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_records = [entry for entry in logs if entry.get('status') == 'active']
    inactive_count = total_entries - len(valid_records)

    # Irrelevant transformation
    normalized = [str(x['value']).upper() for x in valid_records if 'value' in x]
    temp_sum = sum(int(x[0]) for x in normalized if x and x[0].isdigit())

    return len(valid_records), temp_sum


def calculate_metrics(data_list):
    count = 0
    values = []
    for i, item in enumerate(data_list):
        if i % 2 == 0:
            count += 1
            values.append(item ** 2)
        else:
            values.append(item // 2)

    avg_val = sum(values) / len(values) if values else 0
    adjusted = [v for v in values if v > avg_val]
    return count, len(adjusted), avg_val


def evaluate_performance(p, e):
    base = p * 10
    penalty = e * 5 if e > 0 else 0
    bonus = 10 if p > 20 and e == 0 else 0
    return base - penalty + bonus

# Simulated dataset
activity_log = [
    {'id': 'A001', 'status': 'active', 'value': '30'},
    {'id': 'A002', 'status': 'inactive', 'value': '15'},
    {'id': 'A003', 'status': 'active', 'value': 'abc'},
    {'id': 'A004', 'status': 'active', 'value': '72'},
    {'id': 'A005', 'status': 'active', 'value': '9'}
]

numbers = [4, 9, 6, 11, 8]

# Intermediate irrelevant computations
record_count, _ = analyze_efficiency(activity_log)
count_even_indexed, above_avg_count, mean_val = calculate_metrics(numbers)

# Key data preparation with distractors
productivity = sum([len(item['id']) for item in activity_log if item['status'] == 'active'])
error_strings = ['ERR01', 'WARN05', 'ERR01']
errors = len(set(error_strings))  # De-duplicated count

# Dead code - never used
if record_count > 3:
    shadow_metric = mean_val * above_avg_count
    for _ in range(2):
        shadow_metric -= 1

# Core evaluation point
final_score = evaluate_performance(productivity, errors)
print(f"Target result: {final_score}")