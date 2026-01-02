def analyze_system_efficiency(data_log):
    base_factor = 0.85
    penalty_rate = 0.15
    temp_offset = 0.02
    efficiency_list = []

    for entry in data_log:
        raw_value = entry['value']
        timestamp = entry['time']
        if timestamp % 10 == 0:
            adjusted = raw_value * base_factor
        else:
            adjusted = raw_value * (base_factor - penalty_rate)
        efficiency_list.append(round(adjusted + temp_offset, 4))

    return sum(efficiency_list)


def calculate_redundant_metric(x):
    # Dead function - not used in final calculation
    return sum(i**2 for i in x if i % 3 == 0)

# Simulated sensor readings over time
data_log = [
    {'value': 120, 'time': 10},
    {'value': 150, 'time': 11},
    {'value': 130, 'time': 12},
    {'value': 160, 'time': 20},
    {'value': 140, 'time': 21}
]

# Irrelevant preprocessing step (distractor)
preliminary_scores = [x['value'] // 10 for x in data_log]
baseline_shift = sum(preliminary_scores) / len(preliminary_scores)

# Core metrics for performance evaluation
metrics = {
    'efficiency': analyze_system_efficiency(data_log),
    'stability': len([x for x in data_log if x['value'] > 135]),
    'response_time': sum(x['time'] for x in data_log) / len(data_log)
}

# Weight mapping using dictionary and lambda
benchmark_weights = {
    'efficiency': lambda w: w * 0.6,
    'stability': lambda w: w * 0.3,
    'response_time': lambda w: w * 0.1
}

# Auxiliary computation that doesn't affect result (distractor)
outlier_count = 0
for entry in data_log:
    if entry['value'] > 145:
        outlier_count += 1
        break

# Conditional expression to determine adjustment
adjustment = 5 if outlier_count > 0 else 0

# Final weighting using dictionary operations and lambdas
total_weighted = 0
for key, weight_func in benchmark_weights.items():
    normalized = metrics[key] / 10  # Normalize all metrics
    total_weighted += weight_func(normalized)

# Apply adjustment (irrelevant since no outlier triggers it)
final_score = int(total_weighted * 100) + adjustment

# Print result as required
print(f"Result: {final_score}")