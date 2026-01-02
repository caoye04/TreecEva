def analyze_trends(data, threshold=5):
    trend_indices = []
    temp_sum = 0
    for i, value in enumerate(data):
        if value > threshold:
            trend_indices.append(i)
            temp_sum += value
    return trend_indices, temp_sum


def calculate_baseline(ref_data):
    mean_val = sum(ref_data) / len(ref_data)
    adjusted = [x - mean_val for x in ref_data]
    return adjusted


def filter_outliers(values, limit=100):
    # Irrelevant filtering for distraction
    return [v for v in values if abs(v) < limit]


def evaluate_performance(metrics, weights):
    weighted_sum = 0
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    temp_results = []
    for idx, (metric, weight) in enumerate(zip(metrics, normalized_weights)):
        if metric < 0:
            metric = 0  # clamp negatives
        contribution = metric * weight
        temp_results.append(contribution)
        weighted_sum += contribution
    
    # Dummy tracking variables
    result_log = {}
    for i, res in enumerate(temp_results):
        result_log[f'step_{i}'] = round(res, 4)
    
    # Secondary computation that does nothing
    dummy_aggregate = 0
    for x in temp_results:
        dummy_aggregate += x ** 0.5 if x > 0 else 0
    
    return int(round(weighted_sum * 100))

# Main execution
raw_input = [8, 12, 5, 15, 3, 9]
reference_cycle = [4, 6, 5, 7, 5]

# Step 1: Extract significant trend indices and sum
indices, observed_sum = analyze_trends(raw_input, threshold=6)

# Step 2: Compute baseline adjustment (distractor)
drift_correction = calculate_baseline(reference_cycle)
adjusted_metrics = [raw_input[i] + drift_correction[i % len(drift_correction)] for i in range(len(raw_input))]

# Step 3: Apply irrelevant filtering
filtered_metrics = filter_outliers(adjusted_metrics, limit=10)

# Step 4: Use only original raw_input for actual logic (bypass filtered_metrics)
active_metrics = [raw_input[i] for i in indices]  # Only high-performing periods

# Step 5: Prepare weights based on position in trend
weight_scheme = [1.5, 2.0, 1.0, 2.5]  # corresponds to index positions
trimmed_weights = weight_scheme[:len(active_metrics)]

# Step 6: Evaluate final performance score
final_score = evaluate_performance(active_metrics, trimmed_weights)

# Log intermediate states (unused)
summary_report = {
    'trend_count': len(indices),
    'raw_total': sum(raw_input),
    'adjusted_total': sum(adjusted_metrics),
    'dummy_aggregate': int(dummy_aggregate) if 'dummy_aggregate' in locals() else 0
}

print(f"Result: {final_score}")