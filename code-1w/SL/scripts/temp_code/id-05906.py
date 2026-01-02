def analyze_data(records):
    total_entries = len(records)
    valid_count = 0
    error_flags = []
    temp_sums = []

    for record in records:
        if 'status' in record and record['status'] == 'active':
            valid_count += 1
            if 'values' in record:
                temp_sums.append(sum(record['values']))
        else:
            error_flags.append(record.get('error_code', 'UNKNOWN'))

    avg_temp = sum(temp_sums) / len(temp_sums) if temp_sums else 0
    return valid_count, avg_temp, error_flags


def calculate_risk_profile(data):
    risk_factors = set()
    low_threshold = 10
    high_threshold = 100
    dummy_counter = 0

    for item in data:
        dummy_counter += 1
        if isinstance(item, dict) and 'risk_level' in item:
            level = item['risk_level']
            if level > high_threshold:
                risk_factors.add('CRITICAL')
            elif level > low_threshold:
                risk_factors.add('ELEVATED')
            else:
                risk_factors.add('NORMAL')

    # Irrelevant transformation
    transformed = [x * 2 for x in range(5) if x % 2 == 0]
    discarded_result = sum(transformed) * 0.5

    return risk_factors


def compute_baseline_metrics(entries):
    baseline = 0
    peak = float('-inf')
    trough = float('inf')
    history = []

    for e in entries:
        if 'value' in e:
            val = e['value']
            baseline += val
            history.append(val)
            if val > peak:
                peak = val
            if val < trough:
                trough = val

    average = baseline / len(history) if history else 0
    volatility = (peak - trough) / average if average != 0 else 0

    return {
        'baseline': baseline,
        'volatility': volatility,
        'trend': 'UP' if history and history[-1] > history[0] else 'DOWN'
    }


def filter_redundant_items(items):
    seen = set()
    unique_items = []
    duplicates_removed = 0

    for item in items:
        identifier = item.get('id')
        if identifier not in seen:
            seen.add(identifier)
            unique_items.append(item)
        else:
            duplicates_removed += 1

    # Dead code path — never accessed in logic flow
    if duplicates_removed < 0:
        raise ValueError("Impossible negative removal")

    return unique_items


def evaluate_performance(metrics):
    score = 0
    multiplier = 1

    if 'accuracy' in metrics:
        score += metrics['accuracy'] * 10
    if 'precision' in metrics:
        score += metrics['precision'] * 8
    if 'recall' in metrics:
        score += metrics['recall'] * 7

    if 'stability' in metrics and metrics['stability'] > 0.9:
        multiplier += 0.5
    if 'latency' in metrics and metrics['latency'] < 50:
        multiplier += 0.3

    return int(score * multiplier)

# Main execution block with decoy data structures
decoys = [
    {'name': 'junk', 'payload': [9, 8, 7], 'flag': False},
    {'name': 'trash', 'payload': [], 'flag': True}
]

auxiliary_data = [
    {'risk_level': 15},
    {'risk_level': 5},
    {'risk_level': 105}
]

input_records = [
    {'status': 'active', 'values': [10, 20, 30]},
    {'status': 'inactive', 'error_code': 'ERR_404'},
    {'status': 'active', 'values': [15, 25]}
]

raw_entries = [
    {'value': 100},
    {'value': 200},
    {'value': 50}
]

item_list = [
    {'id': 1, 'data': 'A'},
    {'id': 2, 'data': 'B'},
    {'id': 1, 'data': 'C'}
]

# Execute real pipelines
valid_cnt, avg_tmp, errors = analyze_data(input_records)
metric_set = compute_baseline_metrics(raw_entries)

# Inject irrelevant calls
_ = calculate_risk_profile(auxiliary_data)
_ = filter_redundant_items(item_list)

# Modify metric_set with additional derived values
metric_set['accuracy'] = 0.85
metric_set['precision'] = 0.78
metric_set['recall'] = 0.92
metric_set['stability'] = 0.93
metric_set['latency'] = 45

# Critical statement
final_score = evaluate_performance(metric_set)

print(f"Result: {final_score}")