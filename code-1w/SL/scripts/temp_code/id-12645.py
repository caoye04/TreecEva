def analyze_trends(data, threshold=0.5):
    trend_flags = []
    cumulative = 0
    for i, value in enumerate(data):
        if value > threshold:
            trend_flags.append((i, value ** 2))
            cumulative += value * 0.1
        else:
            trend_flags.append((i, -value))
    return trend_flags, cumulative


def filter_outliers(pairs, factor=1.5):
    values = [abs(pair[1]) for pair in pairs]
    median_val = sorted(values)[len(values) // 2]
    filtered = [p for p in pairs if abs(p[1]) <= factor * median_val]
    outlier_count = len(pairs) - len(filtered)
    return filtered, outlier_count


def aggregate_performance(metrics, importance_weights):
    adjusted = 0
    temp_store = []
    
    # Simulate multi-step processing with distractions
    base_shift = sum(importance_weights) * 0.01
    
    for idx, (key_metric, weight) in enumerate(zip(metrics, importance_weights)):
        shifted = key_metric + base_shift
        if idx % 2 == 0:
            processed = shifted * weight ** 0.5
        else:
            processed = shifted / (weight + 1)
        temp_store.append(processed)
    
    # Dummy operations that don't affect final result
    temp_sum = sum(temp_store)
    temp_avg = temp_sum / len(temp_store) if temp_store else 0
    deviation_check = [x - temp_avg for x in temp_store]
    
    # Actual result computation
    weighted_total = 0
    for val in temp_store:
        weighted_total += val * 1.1  # uniform scaling
    
    final_component = int(weighted_total)  # deterministic integer conversion
    
    # Irrelevant secondary logic (dead-end)
    debug_snapshot = {"temp_sum": temp_sum, "version": "v2.3"}
    log_entry = f"Processed batch: {final_component}"
    
    return final_component

# Main execution sequence
raw_inputs = [0.8, 0.3, 1.2, 0.4, 0.9, 1.5, 0.2]
weights = [0.7, 1.3, 0.9, 1.1, 0.8]

# Step 1: Analyze raw data trends
flagged_data, activity_level = analyze_trends(raw_inputs, threshold=0.4)

# Step 2: Remove statistical outliers
cleaned_data, dropped = filter_outliers(flagged_data, factor=1.8)

# Step 3: Extract primary performance indicators
extracted_metrics = []
for index, val in cleaned_data:
    if index % 2 == 0:
        extracted_metrics.append(val * 0.5)
    else:
        extracted_metrics.append(val * 0.3)

# Distractor variables
normalization_factor = sum(extracted_metrics) * 0.05
auxiliary_cache = {k: v for k, v in enumerate([normalization_factor]*5)}
simulated_delay_ms = 127

# Step 4: Aggregate final score
final_score = aggregate_performance(extracted_metrics, weights)

# Output target result
print(f"Result: {final_score}")