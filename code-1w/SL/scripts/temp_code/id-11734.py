def analyze_performance(metrics, thresholds):
    raw_scores = [m['value'] for m in metrics]
    categories = [m['category'] for m in metrics]
    
    # Normalize scores relative to thresholds
    normalized = []
    temp_sum = 0
    for i, score in enumerate(raw_scores):
        norm = score / thresholds[i] if thresholds[i] != 0 else 0
        normalized.append(round(norm, 3))
        temp_sum += score  # irrelevant accumulator

    # Compute auxiliary stats (mostly distractions)
    avg_raw = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    peak_threshold = max(thresholds) if thresholds else 0
    category_count = len(set(categories))

    # Simulate weighting by importance (only some affect final result)
    weights = []
    for idx, cat in enumerate(categories):
        if cat == 'latency':
            weights.append(1.5)
        elif cat == 'throughput':
            weights.append(1.8)
        else:
            weights.append(1.0)
    
    weighted_norm = []
    for n, w in zip(normalized, weights):
        weighted_norm.append(n * w)

    # Secondary normalization
    total_weight = sum(weights)
    adjusted_norm = [wn / total_weight for wn in weighted_norm]

    # Misleading transformation
    transformed = []
    for x in adjusted_norm:
        if x > 0.7:
            transformed.append(x ** 0.5)
        else:
            transformed.append(x)
    dummy_filter = [t for t in transformed if t > 0.5]  # unused

    # Key computation branch
    baseline = sum(adjusted_norm) / len(adjusted_norm)
    adjustment_factor = 1.0
    if baseline < 0.8:
        adjustment_factor += 0.1
    if len(dummy_filter) > 2:
        adjustment_factor += 0.05  # never reached due to data

    # Final aggregation
    clipped_ratings = [min(val, 1.2) for val in adjusted_norm]
    normalized_ratings = [max(nr, 0.3) for nr in clipped_ratings]
    
    final_score = max(normalized_ratings) * adjustment_factor
    
    # Irrelevant logging
    log_entry = f"Processed {len(metrics)} metrics with {category_count} categories."
    debug_values = {'sum_raw': temp_sum, 'peak': peak_threshold, 'avg': avg_raw}
    
    print(f"Result: {final_score}")

# Input data
metrics_data = [
    {'category': 'latency', 'value': 75},
    {'category': 'throughput', 'value': 90},
    {'category': 'error_rate', 'value': 45},
    {'category': 'latency', 'value': 80},
    {'category': 'throughput', 'value': 95}
]
thresholds_data = [80, 100, 60, 85, 110]

analyze_performance(metrics_data, thresholds_data)