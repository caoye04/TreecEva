from collections import defaultdict, Counter

# Simulate daily sensor readings over a week with some noise
daily_readings = [
    [20.1, 19.8, 20.3, 20.0, 20.2, 19.9, 20.1],  # Mon
    [21.5, 21.7, 21.3, 21.6, 29.9, 21.4, 21.5],  # Tue (one anomaly)
    [22.0, 22.2, 21.9, 22.1, 22.0, 22.3, 22.0],  # Wed
    [23.1, 23.0, 23.2, 23.3, 23.1, 23.0, 23.2],  # Thu
    [24.5, 24.7, 24.6, 24.8, 24.4, 24.6, 24.5],  # Fri
    [25.0, 25.2, 25.1, 25.3, 25.0, 25.2, 25.1],  # Sat
    [26.1, 26.0, 26.2, 26.1, 26.3, 26.0, 26.2]   # Sun
]

# Misleading data: irrelevant sensor types
temperature_offsets = {'A': 0.1, 'B': -0.2, 'C': 0.3}
sensor_weights = defaultdict(lambda: 1.0)
for k in temperature_offsets:
    sensor_weights[k] += 0.05

# Track weekly trends and anomalies
anomalies_per_day = []
smoothed_averages = []
overall_trend = []

for i, day in enumerate(daily_readings):
    # Filter outliers (>25 is invalid except for intentional false pattern)
    valid_readings = [x for x in day if abs(x - sum(day)/len(day)) < 2]
    
    # Compute moving median as robust average
    sorted_vals = sorted(valid_readings)
    mid = len(sorted_vals) // 2
    median_val = (sorted_vals[mid] + sorted_vals[~mid]) / 2
    
    # Detect anomalies (deviation > 0.4 from median)
    daily_anomalies = sum(1 for x in day if abs(x - median_val) > 0.4)
    anomalies_per_day.append(daily_anomalies)
    
    # Apply fake correction factor (unused later)
    corrected_median = median_val * (1 + 0.01 * (i % 3))
    smoothed_averages.append(corrected_median)
    
    # Accumulate trend slope
    if i > 0:
        delta = smoothed_averages[-1] - smoothed_averages[-2]
        overall_trend.append(round(delta, 2))

# Analyze pattern frequency in trend changes
trend_counter = Counter(overall_trend)
frequent_trends = [k for k, v in trend_counter.items() if v >= 2]

# Compute cumulative growth rate (fake metric)
cumulative_drift = sum(overall_trend) * 100

# Real logic begins: assess stability score based on anomaly counts and variance
stability_scores = []
for i, day in enumerate(daily_readings):
    base_avg = sum(day) / len(day)
    variance = sum((x - base_avg)**2 for x in day) / len(day)
    penalty = anomalies_per_day[i] * 2.5
    score = 100 - variance * 2 - penalty
    stability_scores.append(max(score, 0))

# Secondary distraction: analyze reading digit patterns
digit_distribution = defaultdict(int)
for day in daily_readings:
    for val in day:
        for digit in str(val).replace('.', ''):
            digit_distribution[int(digit)] += 1
top_digits = sorted(digit_distribution, key=digit_distribution.get, reverse=True)[:3]

# Final scoring uses only stability trend, not digits or drift
base_final = sum(stability_scores) / len(stability_scores)
bonus = 5 if len(frequent_trends) > 0 else 0
penalty_flag = any(x > 3 for x in anomalies_per_day)
deduction = 10 if penalty_flag else 0

# Key statement
final_score = int(base_final + bonus - deduction)

# Irrelevant final transformation
final_score_hex = hex(final_score)
final_score_bin = bin(final_score)

print(f"Result: {final_score}")