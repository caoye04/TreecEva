def analyze_trends(data, baseline):
    trend_scores = []
    adjustment_factor = 0.85
    for i, point in enumerate(data):
        if i == 0:
            trend_scores.append(0)
            continue
        diff = point - data[i-1]
        normalized_diff = diff / (data[i-1] + 1e-5)
        score = normalized_diff * 100
        trend_scores.append(score)
    
    # Irrelevant smoothing (distractor)
    smoothed = [trend_scores[0]]
    for j in range(1, len(trend_scores)):
        smooth_val = 0.7 * trend_scores[j] + 0.3 * smoothed[-1]
        smoothed.append(smooth_val)
    
    return trend_scores

# Simulate sensor drift compensation (mostly irrelevant)
def compensate_drift(raw_values):
    compensated = []
    drift_rate = 0.02
    for t, v in enumerate(raw_values):
        corrected = v - drift_rate * t
        compensated.append(corrected)
    return compensated

# Core evaluation logic
def evaluate_performance(metrics, thresholds):
    status_flags = [1 if m >= t else 0 for m, t in zip(metrics, thresholds)]
    
    # Bitwise manipulation for mode detection (semi-relevant)
    mode_key = 0
    for flag in status_flags:
        mode_key = (mode_key << 1) | flag
    
    # Conditional expression with lambda filtering
    filter_func = lambda x: x > 0.5
    filtered_metrics = list(filter(filter_func, metrics))
    
    # Key computation path
    base_score = sum(metrics) * 10
    bonus = len(filtered_metrics) * 5 if all(status_flags) else 0
    penalty = sum([1 for s in status_flags if not s]) * 3
    
    # Dead code branch (distractor)
    if len(metrics) > 100:
        extra_adjustment = 0
        for k in range(len(metrics)):
            if metrics[k] < 0:
                extra_adjustment += 1
        base_score -= extra_adjustment

    intermediate_result = base_score + bonus - penalty
    
    # Secondary adjustment based on trend analysis
    trends = analyze_trends(metrics, baseline=1.0)
    volatility = sum(abs(t) for t in trends[1:]) / (len(trends) - 1) if len(trends) > 1 else 0
    
    # Final scoring with conditional penalty
    final_score = intermediate_result - (volatility * 2) if volatility > 10 else intermediate_result + 5
    
    # Unused variable (distractor)
    theoretical_max = len(metrics) * 100 + bonus
    
    return int(final_score)

# Input data
metrics = [0.85, 0.92, 0.78, 0.96, 0.88, 0.91, 0.83, 0.89]
thresholds = [0.8 for _ in metrics]

# Irrelevant preprocessing (distractor)
raw_readings = [m * 100 + 5 for m in metrics]
compensated_readings = compensate_drift(raw_readings)

# Execution point of interest
final_score = evaluate_performance(metrics, thresholds)
print(f"Result: {final_score}")