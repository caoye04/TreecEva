def evaluate_performance(metrics, base):
    temp_result = []
    outlier_count = 0
    scaling_factor = 1.75
    adjustment_threshold = 30

    for val in metrics:
        if val < 0:
            continue
        adjusted = val * scaling_factor
        if adjusted > adjustment_threshold:
            adjusted -= 5
        temp_result.append(round(adjusted))

    # Irrelevant string processing (distractor)
    log_prefix = "PERF"
    version_tag = "v2.1"
    tag_parts = (log_prefix + version_tag).split('v')
    version_number = float("1." + tag_parts[1]) if len(tag_parts) > 1 else 1.0

    # Dead code path (distractor)
    temp_state = set()
    for c in version_tag:
        if c.isdigit():
            temp_state.add(c)

    # Actual computation starts here
    base_set = set(base)
    metric_set_filtered = [x for x in temp_result if x >= 10]
    common_elements = base_set.intersection(set(metric_set_filtered))

    aggregate = sum(metric_set_filtered)
    penalty = 0
    for item in common_elements:
        if item % 2 == 0:
            penalty += item // 4

    # Misleading intermediate calculation
    avg_base = sum(base) / len(base) if base else 0
    dummy_correction = avg_base * 0.15

    final_score = aggregate - penalty + len(common_elements)
    return int(final_score)

# Input data
baseline_data = [12, 15, 18, 22, 28]
raw_metrics = [-5, 10, 16, 20, 35]

# Transform raw metrics with slicing and string-based filtering (mixed paradigm)
valid_str = ''.join([str(int(x * 0.5)) for x in raw_metrics if x > 0])
threshold_digit = int(valid_str[1]) if len(valid_str) > 1 else 5
metric_set = [int(valid_str[i:i+2]) for i in range(0, len(valid_str), 2) if int(valid_str[i:i+2]) >= threshold_digit]

# Key execution point
final_score = evaluate_performance(metric_set, baseline_data)
print(f"Result: {final_score}")