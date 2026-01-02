def evaluate_performance(metrics, baseline):
    # Irrelevant transformation
    temp_data = [x * 1.05 for x in metrics]
    temp_data = temp_data[::-1]  # Reverse order - unused later

    # Distractor variables
    adjusted_metrics = []
    normalization_factor = sum(metrics) / len(metrics)
    offset_correction = 0.98

    for val in metrics:
        if val >= baseline:
            adjusted_metrics.append(val * offset_correction)
        else:
            adjusted_metrics.append(val * 1.02)

    # Another red herring: complex-looking but unused calculation
    outlier_count = 0
    deviations = [(m - normalization_factor) ** 2 for m in metrics]
    variance = sum(deviations) / len(deviations) if deviations else 0
    for d in deviations:
        if d > variance * 1.5:
            outlier_count += 1

    # Actual logic begins here — only this part matters
    slice_window = adjusted_metrics[1:4]  # Use only middle three values
    aggregate = 0
    weight = 1
    for val in slice_window:
        aggregate += val * weight
        weight += 1

    # Final computation
    final_score = int(aggregate // 1.5)

    # This print must be present
    print(f"Result: {final_score}")
    return final_score

# Input data
metrics = [85, 92, 78, 96, 88]
baseline = 80
final_score = evaluate_performance(metrics, baseline)