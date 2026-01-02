from collections import defaultdict

# Simulate user activity logs with redundant and misleading fields
def preprocess_logs(raw_logs):
    temp_counts = defaultdict(int)
    action_weights = {'click': 1, 'hover': 0.5, 'scroll': 0.75, 'keypress': 2}
    invalid_flags = []
    total_entries = 0
    weighted_sum = 0

    for log in raw_logs:
        event_type = log.get('action')
        timestamp = log.get('ts')  # Unused but looks important
        device_id = log.get('device', 'unknown')
        if event_type in action_weights:
            temp_counts[event_type] += 1
            weighted_sum += action_weights[event_type]
            total_entries += 1
        else:
            invalid_flags.append(device_id)

    # Distractor computation: rarely affects final result
    avg_weight = weighted_sum / total_entries if total_entries > 0 else 0
    excess_flag_count = len([f for f in invalid_flags if 'mobile' in f])  # Misleading path

    return {
        'counts': dict(temp_counts),
        'total_valid': total_entries,
        'raw_weighted': weighted_sum,
        'average_weight': avg_weight
    }

# Secondary processing with red herring transformations
def transform_features(data):
    feature_map = {}
    squared_totals = []
    running_product = 1

    for key, value in data['counts'].items():
        transformed = (value + 1) ** 2  # Smoothing and amplification
        feature_map[key] = transformed
        squared_totals.append(transformed)
        if value % 2 == 0:
            running_product *= (value + 1)  # Dead-end calculation

    # Extra distraction: unused normalization attempt
    normalized_features = [s / (sum(squared_totals) + 1e-8) for s in squared_totals]

    data['features'] = feature_map
    data['squares'] = squared_totals
    data['product_trace'] = running_product  # Irrelevant to final score

    return data

# Final scoring logic — depends only on specific derived values
def calculate_final_score(processed_data):
    base = processed_data['raw_weighted']
    bonus = 0
    counts = processed_data['counts']

    # Core logic: bonus for balanced interaction diversity
    action_types_present = len(counts)
    if action_types_present >= 3:
        bonus += 10
    elif action_types_present == 2:
        bonus += 5

    # Penalty for overuse of low-value actions
    low_value_ratio = (counts.get('hover', 0) + counts.get('scroll', 0)) / processed_data['total_valid']
    if low_value_ratio > 0.6:
        bonus -= 8

    return int(base + bonus)

# Main execution flow
if __name__ == '__main__':
    # Realistic input: user interaction logs with noise fields
    logs = [
        {'action': 'click', 'ts': 1712345670, 'device': 'desktop-chrome'},
        {'action': 'hover', 'ts': 1712345671, 'device': 'mobile-safari'},
        {'action': 'scroll', 'ts': 1712345672, 'device': 'tablet-firefox'},
        {'action': 'click', 'ts': 1712345673, 'device': 'desktop-chrome'},
        {'action': 'keypress', 'ts': 1712345674, 'device': 'desktop-chrome'},
        {'action': 'hover', 'ts': 1712345675, 'device': 'mobile-safari'},
        {'action': 'hover', 'ts': 1712345676, 'device': 'mobile-safari'},
        {'action': 'scroll', 'ts': 1712345677, 'device': 'tablet-firefox'},
        {'action': 'click', 'ts': 1712345678, 'device': 'desktop-chrome'}
    ]

    # Step-by-step processing pipeline
    cleaned = preprocess_logs(logs)
    processed_data = transform_features(cleaned)
    final_score = calculate_final_score(processed_data)

    print(f"Result: {final_score}")