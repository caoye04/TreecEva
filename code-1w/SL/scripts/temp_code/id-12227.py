def analyze_trend(data, threshold=0.5):
    trend_scores = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        score = 1 if diff > threshold else (-1 if diff < -threshold else 0)
        trend_scores.append(score)
    
    # Irrelevant aggregation (distractor)
    pos_count = sum(1 for x in trend_scores if x == 1)
    neg_count = sum(1 for x in trend_scores if x == -1)
    net_trend = pos_count - neg_count

    smoothed = [sum(data[max(0, i-1):i+2]) / min(i+2, 3) for i in range(len(data))]
    volatility = sum(abs(smoothed[i+1] - smoothed[i]) for i in range(len(smoothed)-1))
    
    return trend_scores, volatility


def compute_baseline_adjustment(base, factor=1.05):
    # Semi-relevant adjustment (only base matters in final logic)
    adjusted = base * factor
    normalized = adjusted / (1 + factor)
    return int(normalized)


def evaluate_performance(metrics, weights):
    raw_product = sum(m * w for m, w in zip(metrics, weights))
    penalty = 0
    
    if len(metrics) > 3:
        excess = len(metrics) - 3
        penalty += excess * 0.5
    
    # Key distraction: complex slicing and unused transformation
    temp_slice = metrics[1:-1] if len(metrics) > 2 else metrics
    transformed = [x ** 0.5 for x in temp_slice if x > 0]
    dummy_aggregate = sum(transformed) * 0.1 if transformed else 0  # unused
    
    # Actual key computation path
    base_score = raw_product - penalty
    adjustment = compute_baseline_adjustment(base_score)
    
    # Final logic step
    final_score = int(base_score) + adjustment
    
    # Dead code branch (misleading control flow)
    if final_score < 0:
        final_score = abs(final_score)
    elif final_score == 0:
        final_score = 10
    # Note: due to input values, this block doesn't trigger
    
    return final_score

# Main execution
raw_data = [0.8, 1.2, 1.6, 2.1, 2.5]
trends, vol = analyze_trend(raw_data, threshold=0.4)

# Generate metrics from trend analysis
metric_pool = [sum(trends), len(trends), vol, trends.count(1), trends.count(-1)]
weights = [1.2, 0.8, 0.5, 0.3, 0.2]

# Apply weighting and process
filtered_metrics = metric_pool[:4]  # only first 4 used
trimmed_weights = weights[:4]

# Insert irrelevant string processing (red herring)
log_id = "PERF-2023"
parts = log_id.split('-')
year = int(parts[1]) if len(parts) > 1 else 2020
offset = year % 100  # unused

# Core call
final_score = evaluate_performance(filtered_metrics, trimmed_weights)
print(f"Result: {final_score}")