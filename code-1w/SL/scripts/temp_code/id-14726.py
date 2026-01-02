def calculate_performance(data):
    # Irrelevant preprocessing: normalize timestamps (not used in result)
    timestamps = [entry['timestamp'] for entry in data]
    avg_time = sum(timestamps) / len(timestamps)
    normalized_times = [(t - avg_time) ** 2 for t in timestamps]

    # Relevant data extraction
    values = [entry['value'] for entry in data if entry['active']]

    # Misleading statistical distraction
    mean_val = sum(values) / len(values) if values else 0
    variance = sum((v - mean_val) ** 2 for v in values) / len(values) if values else 0
    std_dev = variance ** 0.5

    # Semi-relevant transformation with slicing
    filtered = values[1:-1]  # Exclude first and last
    adjusted = [v * 0.9 for v in filtered]

    # Core logic: compute weighted score using list comprehension and conditionals
    weights = [0.5 if i % 2 == 0 else 1.5 for i in range(len(adjusted))]
    weighted_sum = sum(adjusted[i] * weights[i] for i in range(len(adjusted)))

    # Additional distraction: simulate unused anomaly detection
    anomalies = []
    for v in values:
        if v > mean_val + 2 * std_dev:
            anomalies.append(v)
    # Dead code path - never accessed
    if False:
        anomalies = [a * -1 for a in anomalies]

    # Final computation: average of weighted sum and max adjusted value
    max_adj = max(adjusted) if adjusted else 0
    final_score = (weighted_sum + max_adj) / 2

    return final_score

# Input data setup
test_entries = [
    {'value': 10, 'active': True, 'timestamp': 100},
    {'value': 20, 'active': True, 'timestamp': 105},
    {'value': 5, 'active': False, 'timestamp': 110},  # inactive
    {'value': 30, 'active': True, 'timestamp': 115},
    {'value': 25, 'active': True, 'timestamp': 120},
    {'value': 40, 'active': True, 'timestamp': 125}
]

# Execution
interim_result = sum(entry['value'] for entry in test_entries)  # red herring
baseline = len([e for e in test_entries if e['active']])  # another distraction
final_score = calculate_performance(test_entries)
print(f"Target result: {final_score}")