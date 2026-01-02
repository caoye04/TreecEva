def analyze_trends(data, threshold=0.5):
    trends = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1] if data[i-1] != 0 else 0
        if abs(change) > threshold:
            trends.append('volatile')
        elif change > 0:
            trends.append('up')
        else:
            trends.append('down')
    return trends

# Simulate sensor readings over time
temperature_readings = [20, 22, 21, 25, 30, 29, 31, 33]
humidity_readings = [45, 47, 55, 60, 58, 62, 65, 70]

# Misleading intermediate analysis
temp_trends = analyze_trends(temperature_readings, 0.1)
humid_trends = analyze_trends(humidity_readings, 0.1)

# Irrelevant aggregation
stability_count = {k: temp_trends.count(k) + humid_trends.count(k) for k in set(temp_trends + humid_trends)}

# Real computation begins: system health metrics
metrics = {
    'temp_stable': temp_trends.count('up') + temp_trends.count('down'),
    'humid_spike': len([t for t in humid_trends if t == 'volatile']),
    'baseline_dev': sum(1 for t in temperature_readings if t > 25)
}

# Weighting scheme (some weights are red herrings)
weights = {
    'temp_stable': 0.3,
    'humid_spike': -0.5,
    'baseline_dev': 0.8,
    'false_metric': 1.2  # unused weight
}

# Auxiliary function with slicing distraction
def compute_rolling_avg(lst, window=3):
    return [sum(lst[i:i+window]) / window for i in range(len(lst)-window+1)]

rolling_temp = compute_rolling_avg(temperature_readings)
rolling_humid = compute_rolling_avg(humidity_readings)

# Distractor: set operations on trend labels
trend_set_a = set(temp_trends[:4])
trend_set_b = set(humid_trends[4:])
overlap = trend_set_a & trend_set_b

# Core logic masked by prior noise
def evaluate_performance(metrs, wts):
    score = 0
    for key in wts:
        if key in metrs:
            score += metrs[key] * wts[key]
    # Additional adjustment based on data history
    recent_high_temp = len([t for t in temperature_readings[-3:] if t > 30])
    if recent_high_temp >= 2:
        score -= 1.5
    return round(score, 4)

# Critical execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")