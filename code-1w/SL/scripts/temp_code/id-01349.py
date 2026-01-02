from collections import defaultdict

# Simulate resource monitoring system for a distributed cache
baseline_capacity = 42
scaling_factor = 1.75
trend_history = []
window_size = 5
threshold_multiplier = 0.88
diagnostic_log = defaultdict(int)

# Raw input data: hourly usage (simulated)
usage_data = [38, 45, 47, 44, 50, 52, 49, 60, 63, 58, 55, 61]

# Secondary derived metrics (some used, some not)
stability_score = 0.0
cumulative_load = 0
spike_count = 0
smoothed_values = []

for hour, load in enumerate(usage_data):
    # Irrelevant diagnostic tracking
    diagnostic_log['total_hours'] += 1
    diagnostic_log['peak_seen'] = max(diagnostic_log['peak_seen'], load) if diagnostic_log['total_hours'] > 1 else load

    # Core trend processing
    cumulative_load += load
    if load > baseline_capacity * scaling_factor:
        spike_count += 1

    # Smoothing with irrelevant side computation
    if len(smoothed_values) > 0:
        smoothed = (smoothed_values[-1] * 0.6 + load * 0.4)
    else:
        smoothed = load * 0.9
    smoothed_values.append(smoothed)

    # Only every third hour is recorded for trend analysis (downsampling)
    if (hour + 1) % 3 == 0:
        trend_history.append(load)

# Final trend logic with key decision point
usage_trend = trend_history  # Effective usage pattern after filtering

# Additional irrelevant pre-computations
if len(usage_trend) > 0:
    avg_trend = sum(usage_trend) / len(usage_trend)
    trend_deviation = [abs(x - avg_trend) for x in usage_trend]
    stability_score = sum(trend_deviation) / len(trend_deviation) if trend_deviation else 0

# Key assignment with conditional logic
peak_capacity = max(usage_trend[-window_size:]) if len(usage_trend) >= window_size else baseline_capacity

# Dead code branch - never executed due to prior logic
if len(usage_trend) < 2:
    peak_capacity = baseline_capacity * 2

# Unused final adjustment attempt
final_margin = (peak_capacity - baseline_capacity) * threshold_multiplier

print(f"Result: {peak_capacity}")