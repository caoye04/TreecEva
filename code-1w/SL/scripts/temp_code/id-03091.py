def analyze_trends(raw_values, baseline):
    deviations = [(v - baseline) for v in raw_values]
    squared_devs = [d ** 2 for d in deviations]
    avg_sq_dev = sum(squared_devs) / len(squared_devs)
    return avg_sq_dev


def normalize_entries(entries):
    max_val = max(entries)
    min_val = min(entries)
    range_val = max_val - min_val if max_val != min_val else 1
    return [(e - min_val) / range_val for e in entries]


def filter_outliers(data, threshold=2.5):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [x for x in data if abs(x - mean) / std_dev <= threshold]


def evaluate_performance(weights, values):
    weighted_sum = sum(w * v for w, v in zip(weights, values))
    penalty = 0.0
    if len(values) > 5:
        sorted_vals = sorted(values)
        mid_idx = len(sorted_vals) // 2
        median_val = sorted_vals[mid_idx]
        if median_val < 0.3:
            penalty += 0.1 * weighted_sum
    return int(weighted_sum - penalty)

# Simulated sensor input data
sensor_readings = [105, 210, 190, 240, 185, 220, 170]

# Baseline calibration offset
base_offset = 150

# Step 1: Analyze trend deviation from baseline
deviation_metric = analyze_trends(sensor_readings, base_offset)

# Step 2: Normalize readings for uniform scaling
normalized_readings = normalize_entries(sensor_readings)

# Step 3: Filter out statistical outliers (though none expected here)
cleaned_readings = filter_outliers(normalized_readings, threshold=3.0)

# Step 4: Define metric weights based on importance
metric_importance = [0.1, 0.15, 0.2, 0.05, 0.1, 0.25, 0.15]

# Misleading distractor: unused alternate weight set
dummy_weights = [0.2] * 7  # Not used in final calculation

# Intermediate tracking variables (some redundant)
data_length = len(cleaned_readings)
sum_normalized = sum(cleaned_readings)
avg_normalized = sum_normalized / data_length if data_length else 0

# Key transformation: truncate to first 7 elements (redundant since already length 7)
trimmed_data = cleaned_readings[:7]

# Apply secondary adjustment: invert values if average too high
adjusted_data = [1 - x if avg_normalized > 0.6 else x for x in trimmed_data]

# Recompute normalization post-adjustment (unnecessary but included)
re_normalized = normalize_entries(adjusted_data)

# Final performance evaluation using original normalized data, not adjusted
final_score = evaluate_performance(metric_importance, normalized_readings)

# Print result for extraction
print(f"Result: {final_score}")