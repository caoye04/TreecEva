def analyze_performance(metrics, thresholds):
    alert_flags = []
    normalized = []
    temp_sum = 0

    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        deviation = metric - threshold
        if deviation > 0:
            flag = f'ALERT_HIGH_{i}'
            alert_flags.append(flag)
        else:
            flag = f'NORMAL_{i}'
        temp_sum += abs(deviation) * (i + 1)
        normalized.append(abs(deviation))

    scaling_factor = len(alert_flags) + 1
    adjusted_total = 0
    for val in normalized:
        adjusted_total += val * scaling_factor

    outlier_count = 0
    for val in metrics:
        if val > 100 or val < 0:  # unrealistic metric values
            outlier_count += 1

    # Irrelevant list processing
    dummy_pairs = list(zip(metrics, [x * 2 for x in metrics]))
    cumulative = 0
    for idx, _ in enumerate(dummy_pairs):
        cumulative += idx * 0.5  # Distractor computation

    return temp_sum, adjusted_total, scaling_factor


def compute_aggregate(data_stream):
    base_weights = [1, 2, 3, 4]
    processed = [x ** 0.5 for x in data_stream if x > 0]
    filtered = [val for val in processed if val >= 2]

    sum_filtered = sum(filtered)
    count_filtered = len(filtered)

    # Simulate multi-step scoring
    raw_score = 0
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            raw_score += val * base_weights[i % 4]
        else:
            raw_score -= val / (base_weights[i % 4] + 1)

    penalty = 0
    for val in data_stream:
        if val < 0:
            penalty += 10

    # Dummy recursion for distraction (no impact)
    def recursive_trace(n):
        if n <= 1:
            return 1
        return recursive_trace(n - 2) + 1 if n > 2 else recursive_trace(n - 1)

    _ = recursive_trace(7)  # Dead-end call

    temp_result = analyze_performance(data_stream, [50, 55, 60, 65])
    auxiliary_score = temp_result[1]
    scaling = temp_result[2]

    final_score = int((raw_score / (scaling + 1)) - penalty + 50)

    # Additional red herring: unused variable with complex derivation
    derived_insight = sum([a * b for a, b in zip(processed, processed[::-1])]) / (len(processed) or 1)

    return final_score

# Main execution
sensor_data = [81, 49, 100, 36]
final_score = compute_aggregate(sensor_data)
print(f"Result: {final_score}")