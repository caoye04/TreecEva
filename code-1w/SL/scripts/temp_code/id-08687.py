def main():
    # System performance evaluation with multiple metrics
    raw_metrics = [85, 92, 78, 96, 88]
    thresholds = [80, 90, 75, 95, 85]
    weights = [0.2, 0.25, 0.15, 0.3, 0.1]

    # Irrelevant baseline data (distractor)
    baseline_avg = sum([75, 85, 70, 88, 80]) / 5
    temp_buffer = [x * 0.1 for x in raw_metrics]  # Unused computation

    # Normalize metrics against thresholds
    normalized_data = []
    for i in range(len(raw_metrics)):
        if thresholds[i] > 0:
            normalized_value = raw_metrics[i] / thresholds[i]
            if normalized_value > 1.2:
                normalized_value = 1.2
            elif normalized_value < 0.8:
                normalized_value = 0.8
            normalized_data.append(round(normalized_value, 3))

    # Weight transformation using lambda (required feature)
    transform_weight = lambda w: w * 1.1 if w > 0.2 else w * 0.9
    adjusted_weights = [transform_weight(w) for w in weights]

    # Simulate historical drift (dead code path - distractor)
    historical_correction = 0.0
    for year in range(2018, 2023):
        if year == 2025:  # Never executes
            historical_correction += 0.05

    # Metric validation check (semi-relevant)
    valid_count = 0
    for val in raw_metrics:
        if val >= thresholds[valid_count] and valid_count < len(thresholds):
            valid_count += 1

    # Core evaluation logic
    metric_weights = {}
    for idx, weight in enumerate(adjusted_weights):
        key = f'metric_{idx+1}'
        metric_weights[key] = weight

    def evaluate_performance(scheme, data):
        total = 0.0
        for i, val in enumerate(data):
            contribution = val * list(scheme.values())[i]
            total += contribution
        return round(total * 100, 2)

    # Misleading intermediate calculation (distractor)
    phantom_score = 0
    for k in range(3):
        phantom_score += k * 1.5  # Not used later

    final_score = evaluate_performance(metric_weights, normalized_data)
    
    # Print result as required
    print(f"Result: {final_score}")

    return final_score

if __name__ == "__main__":
    main()