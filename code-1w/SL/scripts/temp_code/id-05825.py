def analyze_trends(data, threshold=0.5):
    trends = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1] if data[i-1] != 0 else 0
        trends.append(1 if change > threshold else 0)
    return trends

# Simulated sensor readings over time
readings = [100, 108, 115, 112, 125, 130, 128, 140]

trend_flags = analyze_trends(readings, threshold=0.05)

# Irrelevant transformation - red herring
smoothed = [round((readings[i] + readings[i+1]) / 2, 2) for i in range(len(readings)-1)]

# Secondary metric: volatility
volatility = sum(abs(readings[i] - readings[i-1]) for i in range(1, len(readings)))
adjusted_volatility = volatility * 0.1  # Not directly used

# System status classification (distractor logic)
status_codes = {0: 'STABLE', 1: 'FLUCTUATING'}
current_status = status_codes.get(sum(trend_flags) % 2, 'UNKNOWN')

# Core evaluation metrics
metric_a = sum(trend_flags)  # Number of positive trend shifts
metric_b = len([x for x in readings if x > 110])  # Readings above baseline
metric_c = adjusted_volatility // 5  # Discretized volatility level

# Weight configuration (misleading comment)
# Weights were supposed to be normalized but aren't - intentional trap
weights = [0.4, 0.35, 0.25]  # These do not sum to 1.0

# Additional distraction: historical average comparison
historical_avg = 118
deviation_score = abs(sum(readings) / len(readings) - historical_avg) * 0.5

# Evaluate performance using weighted combination
# Despite distractions, only metrics a, b, c and weights matter here
def evaluate_performance(metrics, w):
    temp_result = 0
    for i in range(len(metrics)):
        temp_result += metrics[i] * w[i] * 10  # Scale up contribution
    return int(temp_result)  # Final integer score

metrics = [metric_a, metric_b, metric_c]
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")