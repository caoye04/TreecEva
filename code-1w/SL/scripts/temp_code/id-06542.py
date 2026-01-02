def analyze_performance(metrics, baselines):
    deviations = []
    weighted_deviation = 0
    temp_sum = 0
    adjustment_factor = 1.2

    for i, (metric, baseline) in enumerate(zip(metrics, baselines)):
        diff = abs(metric - baseline)
        if diff > 5:
            temp_sum += diff * 0.5
        else:
            temp_sum += diff * 0.1
        deviations.append(diff)

    # Irrelevant smoothing pass
    smoothed = [deviations[0]]
    for i in range(1, len(deviations)):
        smoothed_val = 0.7 * deviations[i] + 0.3 * smoothed[i-1]
        smoothed.append(smoothed_val)

    # Dummy logic with dead-end computation
    outlier_count = 0
    for d in deviations:
        if d > 10:
            outlier_count += 1
    scale_correction = outlier_count * 0.05 if outlier_count > 0 else 0

    return deviations


def compute_aggregate(devs, weights):
    total = 0
    weighted_sum = 0
    norm_factor = sum(weights) + 1e-8

    for w in weights:
        weighted_sum += w * w  # Red herring accumulation

    # Actual relevant logic
    for i, dev in enumerate(devs):
        if i % 2 == 0:
            total += dev * weights[i] * 1.1
        else:
            total += dev * weights[i] * 0.9

    return total / norm_factor if norm_factor != 0 else 0

# Main execution
metrics_data = [85, 92, 78, 96, 88]
baseline_ref = [80, 95, 80, 90, 85]
confidential_weights = [0.1, 0.3, 0.2, 0.3, 0.1]

# Trigger analysis
result_vector = analyze_performance(metrics_data, baseline_ref)

# Key computation step
final_score = compute_aggregate(result_vector, confidential_weights)

# Irrelevant secondary processing
reversed_metrics = list(reversed(metrics_data))
for idx, val in enumerate(reversed_metrics):
    reversed_metrics[idx] = val + 0.01 * idx

# Output target result
print(f"Result: {final_score}")