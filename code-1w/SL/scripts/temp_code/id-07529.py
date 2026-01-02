def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1] if data[i-1] != 0 else 0
        trend.append('up' if change > threshold else 'down' if change < -threshold else 'stable')
    return trend

baseline = [100, 105, 103, 107, 110]
readings = [112, 108, 115, 119, 125]

# Irrelevant transformation - distractor
transformed = [x * 1.02 for x in readings if x > 110]
offset = sum(transformed) / len(transformed) if transformed else 0

# Misleading intermediate calculation
predicted_growth = (readings[-1] - baseline[0]) * 0.1
adjustment_factor = 1.05 if predicted_growth > 10 else 0.95

# Core logic with conditional expressions and accumulation
def calculate_performance(base, current):
    diffs = [(curr - base[i]) / base[i] for i, curr in enumerate(current) if i < len(base)]
    valid_diffs = [d for d in diffs if abs(d) < 0.5]  # Filter outliers
    
    # Conditional expression usage
    score_modifier = 1.2 if len(valid_diffs) >= 3 else 0.8
    
    # Accumulation with semi-relevant state tracking
    total_drift = 0
    drift_log = []
    for d in diffs:
        total_drift += abs(d)
        drift_log.append(abs(d))
    
    # Secondary irrelevant computation - adds cognitive load
    avg_drift = total_drift / len(drift_log) if drift_log else 0
    volatility = sum((x - avg_drift)**2 for x in drift_log) / len(drift_log) if drift_log else 0
    
    # Final score depends only on sum of valid relative changes and modifier
    raw_score = sum(valid_diffs) * 100
    final = raw_score * score_modifier
    
    # Dead code path - never executed but looks relevant
    if False:
        final -= volatility * 10
        
    return int(final)

# Execute key statement
trend_analysis = analyze_trend(readings)
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")