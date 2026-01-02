def evaluate_performance(data, importance):
    adjusted = []
    temp_sum = 0
    noise_accum = 0

    for i in range(len(data)):
        if i % 2 == 0:
            temp_sum += data[i] * importance[i]
            adjusted.append(data[i] * 1.1)
        else:
            temp_sum -= data[i] * 0.1
            noise_accum += data[i] % 3

    # Irrelevant transformation (distractor)
    transformed = [x ** 0.5 for x in adjusted if x > 0]
    normalized = [x / sum(adjusted) for x in adjusted]

    # Secondary path with dead computation
    proxy_value = 0
    for val in transformed:
        proxy_value += val * 0.01  # negligible impact

    # Key slicing operation
    segment = normalized[1:3]
    segment_avg = sum(segment) / len(segment)

    # Final calculation - only temp_sum is actually used
    result = int(temp_sum + 0.5)  # rounding to nearest integer

    return result

# Main execution
metrics = [85, 90, 78, 92, 88]
weights = [0.3, 0.2, 0.25, 0.15, 0.1]

# Dummy preprocessing (misleading)
copy_metrics = metrics[:]
for i in range(len(copy_metrics)):
    copy_metrics[i] = copy_metrics[i] + 5 if i % 2 == 0 else copy_metrics[i] - 2

# Unused statistical calculation
mean_metric = sum(metrics) / len(metrics)
deviations = [(x - mean_metric) ** 2 for x in metrics]
variance = sum(deviations) / len(deviations)

# Critical call
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")