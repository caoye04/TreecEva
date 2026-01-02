def analyze_trend(data):
    trend_values = [data[i+1] - data[i] for i in range(len(data)-1)]
    avg_change = sum(trend_values) / len(trend_values) if trend_values else 0
    volatility = sum(abs(x - avg_change) for x in trend_values) / len(trend_values) if trend_values else 0
    return avg_change, volatility

# Simulated sensor readings over time
temperature_readings = [20, 22, 25, 24, 23, 26, 28, 27]

# Analyze temperature trend (distraction: not directly used)
trend, variation = analyze_trend(temperature_readings)

# Core performance metrics from system logs
metrics = {
    'response_time': 120,      # ms
    'error_rate': 0.05,        # percentage
    'throughput': 85,         # requests/sec
    'availability': 0.997     # uptime ratio
}

# Weight mapping for scoring (used in evaluation)
weights = {
    'response_time': 0.3,
    'error_rate': 0.25,
    'throughput': 0.2,
    'availability': 0.25
}

# Normalize metrics to a 0-1 scale (inversely for negative indicators)
normalized_metrics = {}
normalized_metrics['response_time'] = max(0, 1 - (metrics['response_time'] - 50) / 150)  # ideal < 50ms
normalized_metrics['error_rate'] = max(0, 1 - metrics['error_rate'] / 0.1)              # ideal < 10%
normalized_metrics['throughput'] = min(1, metrics['throughput'] / 100)                # ideal >= 100
normalized_metrics['availability'] = min(1, metrics['availability'] / 0.995)            # ideal >= 99.5%

# Compute weighted score using dictionary and list comprehension
score_components = {key: normalized_metrics[key] * weights[key] for key in weights}
raw_total = sum(score_components.values())

# Apply non-linear adjustment based on throughput threshold (additional logic)
if metrics['throughput'] > 80:
    bonus_factor = 1.1
else:
    bonus_factor = 1.0

adjusted_total = raw_total * bonus_factor

# Secondary adjustment based on error rate quartile (distraction branch)
effective_error_level = 'low' if metrics['error_rate'] < 0.03 else 'moderate' if metrics['error_rate'] < 0.07 else 'high'
penalty_adjustment = 0.98 if effective_error_level == 'high' else 1.0  # no penalty in this case

# Final performance score computation
calibration_offset = 5  # minor baseline shift
intermediate_result = adjusted_total * 100 + calibration_offset

# Additional irrelevant calculation simulating logging overhead
log_entry_count = 0
for entry in temperature_readings:
    if entry > 25:
        log_entry_count += 1
simulated_load = log_entry_count * 0.03  # unused variable

# Critical execution point
temp_diagnostic = (trend * 10) // 1  # distractor using earlier analysis
final_score = int(intermediate_result * penalty_adjustment)

print(f"Result: {final_score}")