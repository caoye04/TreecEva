def analyze_system_load(usage_log):
    total_entries = len(usage_log)
    peak_usage = max(usage_log)
    avg_usage = sum(usage_log) / total_entries
    high_load_threshold = 85
    overload_count = sum(1 for x in usage_log if x > high_load_threshold)
    warning_issued = overload_count > 5
    return warning_issued, avg_usage


def transform_metrics(raw_data):
    processed = [x * 1.75 for x in raw_data if x % 2 == 1]
    shifted = [x + 10 for x in processed]
    normalized = [min(x, 95) for x in shifted]
    return normalized


def filter_outliers(values, limit=100):
    if not values:
        return []
    mean_val = sum(values) / len(values)
    deviances = [abs(v - mean_val) for v in values]
    threshold = sum(deviances) / len(deviances) * 1.5
    filtered = [v for v in values if abs(v - mean_val) <= threshold]
    return filtered or [mean_val]


def compute_entropy(data):
    from math import log2
    if not data:
        return 0.0
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)


def evaluate_performance(metrics):
    base_score = 50
    adjustment = 0
    
    # Core logic path
    if len(metrics) > 3:
        adjustment += 15
    if sum(metrics) > 200:
        adjustment += 20
    
    metric_set_sorted = sorted(metrics)
    mid_values = metric_set_sorted[1:-1] if len(metric_set_sorted) > 2 else metric_set_sorted
    
    if len(mid_values) >= 2 and mid_values[-1] - mid_values[0] < 10:
        adjustment += 25
    
    # Irrelevant entropy computation (distractor)
    _ = compute_entropy(metrics)
    
    # Decoy conditional with no real impact
    performance_flag = False
    if all(m > 10 for m in metrics):
        performance_flag = True
        temp_adjust = 0
        for m in metrics:
            if m > 25:
                temp_adjust += 3
        # This doesn't affect anything

    # Conditional expression (Python feature)
    penalty = 30 if any(m < 5 for m in metrics) else 0
    
    final_score = base_score + adjustment - penalty
    
    # Dead code path (misleading)
    redundant_calc = None
    if final_score < 0:
        redundant_calc = [final_score ** 2 for _ in range(5)]
    
    return final_score

# Simulated telemetry data (irrelevant to final result)
data_stream = [88, 76, 92, 81, 79, 85, 90, 87]
valid_records = [x for x in data_stream if x > 70]
system_warnings, average_load = analyze_system_load(valid_records)

# Raw input that feeds into relevant logic
raw_diagnostics = [12, 18, 22, 26]
processed_diagnostics = transform_metrics(raw_diagnostics)
cleaned_metrics = filter_outliers(processed_diagnostics)

# Set used in conditional logic (core relevance)
metric_set = {int(x) for x in cleaned_metrics}  # {21, 33, 39}

# Extra set operations (some irrelevant)
auxiliary_set = {20, 21, 30, 33}
disjoint_check = metric_set.isdisjoint(auxiliary_set)
overlap_count = len(metric_set & auxiliary_set)

# Key execution point
final_score = evaluate_performance(metric_set)

# Output result as required
print(f"Result: {final_score}")