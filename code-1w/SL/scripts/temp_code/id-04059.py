def analyze_trends(values):
    trend_scores = [1 if values[i] < values[i+1] else -1 for i in range(len(values)-1)]
    return sum(trend_scores)

seasons = ['spring', 'summer', 'autumn', 'winter']
daily_temps = [15, 18, 22, 25, 24, 20, 17]

# Irrelevant temperature categorization (distractor)
categorized = {}
for temp in daily_temps:
    if temp < 18:
        categorized[temp] = 'cool'
    elif temp < 24:
        categorized[temp] = 'warm'
    else:
        categorized[temp] = 'hot'

# Misleading secondary analysis (dead computation)
avg_temp = sum(daily_temps) / len(daily_temps)
temp_variance = sum((t - avg_temp) ** 2 for t in daily_temps) / len(daily_temps)

# Real data pipeline starts here
raw_metrics = [23, 45, 12, 67, 34, 89, 23]
filtered_metrics = [x for x in raw_metrics if x > 20]
sorted_metrics = sorted(filtered_metrics, reverse=True)

# Simulate metric decay over time (actual relevant logic)
decayed_values = [sorted_metrics[i] * (0.9 ** i) for i in range(len(sorted_metrics))]

# Auxiliary function with plausible but unused result
def compute_baseline(data):
    return sum(data[:3]) / 3

baseline = compute_baseline(decayed_values)  # Not used later

# Another distraction: mapping to arbitrary labels
label_map = {v: chr(65 + i) for i, v in enumerate(sorted_metrics)}

# Core logic hidden among distractions
def evaluate_performance(data):
    growth_factor = 1.1
    adjustment = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            adjustment += val * growth_factor
        else:
            adjustment -= val * 0.1
    return int(adjustment)

metric_data = decayed_values[:5]  # Use first 5 decayed values
final_score = evaluate_performance(metric_data)
print(f"Target result: {final_score}")