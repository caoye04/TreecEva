def analyze_trends(data, threshold=0.5):
    above_threshold = list(filter(lambda x: x > threshold, data))
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(data) if data else 0
    return trend_ratio

# Simulated sensor readings (normalized)
sensor_readings = [0.62, 0.48, 0.71, 0.33, 0.89, 0.51, 0.29]

# Secondary metric: volatility index
volatility = sum(abs(sensor_readings[i] - sensor_readings[i-1]) for i in range(1, len(sensor_readings)))
adjusted_volatility = volatility / (len(sensor_readings) - 1) if len(sensor_readings) > 1 else 0

# Irrelevant statistical distraction
deviation_squared = [round((x - 0.5)**2, 4) for x in sensor_readings]
mean_deviation = round(sum(deviation_squared) / len(deviation_squared), 4)

# Core performance metrics
trend_strength = analyze_trends(sensor_readings, 0.5)
consistency = 1 - adjusted_volatility
coverage = len(sensor_readings) / 10  # Assume max expected readings = 10

# Weighting scheme
weights = (0.4, 0.35, 0.25)  # Trend, Consistency, Coverage
metrics = (trend_strength, consistency, coverage)

# Aggregation function using lambda
aggregate_performance = lambda m, w: round(sum(m[i] * w[i] for i in range(len(m))), 4)

# Final computation
final_score = aggregate_performance(metrics, weights)

# Distractor: unused alternate aggregation
alt_score = max(metrics) * 0.6 + min(metrics) * 0.4
buffer_zone = (min(metrics), max(metrics))

# Output result
Result: {final_score}