def analyze_performance(metrics, thresholds):
    alert_count = 0
    normalized = []
    temp_sum = 0

    for i, val in enumerate(metrics):
        if val > thresholds[i % len(thresholds)]:
            alert_count += 1
        normalized_val = (val - min(metrics)) / (max(metrics) - min(metrics) + 1e-8)
        normalized.append(normalized_val)
        temp_sum += val * (i + 1)

    scaling_factor = 1.0 if sum(normalized) < 2.0 else 0.5
    adjusted = [x * scaling_factor for x in normalized]
    return adjusted, alert_count, temp_sum


def filter_outliers(data, limit=3):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= limit * std_dev]
    outlier_count = len(data) - len(filtered)
    return filtered, outlier_count


def calculate_final_score(entries):
    base_scores = []    
    debug_trace = []
    cumulative = 0

    for idx, item in enumerate(entries):
        weight = 0.8 + (idx * 0.1) % 0.3
        raw_score = item * weight
        base_scores.append(raw_score)
        
        # Distractor computation: tracking index patterns
        cycle_marker = (idx + 1) % 4
        debug_trace.append(cycle_marker)
        cumulative += raw_score * cycle_marker

    # Real computation path
    avg_base = sum(base_scores) / len(base_scores) if base_scores else 0
    penalty = len([x for x in debug_trace if x == 0]) * 0.25
    final_score = avg_base - penalty

    # Dead code path (irrelevant)
    if len(entries) > 100:
        fallback = sum(entries) / 1000
        final_score = fallback

    return round(final_score, 4)

# Main execution
raw_metrics = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91, 87, 79, 93]
thresh_levels = [80, 85, 75]

processed, _, _ = analyze_performance(raw_metrics, thresh_levels)
filtered_data, _ = filter_outliers(processed, limit=2)

# Key transformation using list comprehension and zip
enhanced_data = [x * 2.1 for x, idx in zip(filtered_data, range(len(filtered_data))) if idx % 2 == 0]
duplicated_segment = [x for x in enhanced_data for _ in (0, 1)][:len(enhanced_data)]  # Irrelevant duplication

final_score = calculate_final_score(processed_data=enhanced_data)
print(f"Target result: {final_score}")