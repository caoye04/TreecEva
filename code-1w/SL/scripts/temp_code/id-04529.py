def evaluate_performance(days_present, raw_metrics):
    base_threshold = 75
    bonus_factor = 1.2
    penalty_rate = 0.8
    
    # Compute attendance compliance
    attendance = len(days_present) if days_present else 0
    compliant = attendance >= base_threshold
    
    # Irrelevant temperature scaling (distractor)
    temp_scaling = 0.95
    adjusted_temp = 23 * temp_scaling + 7
    climate_factor = adjusted_temp / 30  # Not actually used later

    # Process performance metrics using set operations to remove duplicates
    metric_set = set(raw_metrics)
    filtered_metrics = [m for m in metric_set if m > 0]  # Remove negative noise
    
    # Sort and compute median as stability index
    sorted_metrics = sorted(filtered_metrics)
    mid = len(sorted_metrics) // 2
    if len(sorted_metrics) % 2 == 0:
        median_stability = (sorted_metrics[mid-1] + sorted_metrics[mid]) / 2
    else:
        median_stability = sorted_metrics[mid]
    
    # Compute efficiency ratio (sum over unique count)
    efficiency_ratio = sum(filtered_metrics) / len(filtered_metrics) if filtered_metrics else 0
    
    # Auxiliary computation: peak frequency analysis (semi-relevant)
    peak_count = 0
    for val in raw_metrics:
        if val > efficiency_ratio * 1.1:
            peak_count += 1
    peak_frequency = peak_count / len(raw_metrics) if raw_metrics else 0
    
    # Distractor: unused normalization pass
    normalized_metrics = []
    max_metric = max(raw_metrics) if raw_metrics else 1
    for x in raw_metrics:
        norm_x = x / max_metric
        if norm_x > 0.5:
            normalized_metrics.append(norm_x * 100)
    # End of dead code block

    # Core scoring logic
    base_score = median_stability * efficiency_ratio
    if compliant:
        base_score *= bonus_factor
    else:
        base_score *= penalty_rate

    # Final adjustment based on data richness
    richness_factor = len(filtered_metrics) / (len(raw_metrics) + 1)
    final_score = base_score * (1 + 0.1 * richness_factor)

    return int(final_score)

# Simulated input data
attendance_days = list(range(80))  # 80 days present
performance_data = [85, 90, -5, 87, 92, 88, 90, 85, -3, 87, 94, 89, 91, 86, 88]

# Key execution point
final_score = evaluate_performance(attendance_days, performance_data)
print(f"Result: {final_score}")