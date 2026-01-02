def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics)) * 100) for m in metrics]
    
    # Semi-relevant preprocessing
    weighted = []
    for i, val in enumerate(metrics):
        weight = 0.8 if val >= thresholds[i % len(thresholds)] else 0.5
        weighted.append(val * weight)

    # Key computation: count how many exceed dynamic threshold
    base_ref = sum(weighted) / len(weighted)
    adjusted_metrics = [x for x in weighted if x > base_ref * 0.9]
    
    # Distractor: unused complex structure
    stats_summary = {
        'peak': max(weighted),
        'valley': min(weighted),
        'span': len(weighted),
        'quality_flag': all(m > 0 for m in metrics)
    }

    # Nested logic with modular arithmetic and accumulation
    accumulator = 0
    cycle_tracker = 0
    for idx, item in enumerate(adjusted_metrics):
        if idx % 2 == 0:
            accumulator += item // (idx + 1)
        else:
            cycle_tracker += 1
            if item % 4 == 0:  # modular filter
                accumulator += item % 7
    
    # Secondary distractor: dead logic path (never executed due to data)
    fallback_values = [x for x in metrics if x < 0]
    if fallback_values and len(fallback_values) > 10:
        accumulator -= sum(fallback_values)

    # Final aggregation with tuple unpacking (relevant)
    multiplier, offset = (2, -5)
    final_score = int(accumulator * multiplier + offset)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
performance_data = [88, 92, 76, 95, 85, 70, 90, 82]
threshold_levels = [80, 85, 75]

# Execute
result = analyze_performance(performance_data, threshold_levels)