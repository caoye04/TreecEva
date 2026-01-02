from collections import defaultdict

# Simulated sensor data with timestamps and readings
timestamped_readings = [
    (1623456000, 23.5), (1623456060, 23.7), (1623456120, 24.1),
    (1623456180, 24.3), (1623456240, 24.0), (1623456300, 23.9),
    (1623456360, 24.2), (1623456420, 24.5), (1623456480, 24.7),
    (1623456540, 25.0)
]

# Irrelevant auxiliary function for noise filtering (not used in final path)
def filter_noise(data, threshold=0.5):
    return [x for x in data if abs(x[1] - sum(d[1] for d in data)/len(data)) < threshold]

# Data aggregation by hour using defaultdict
hourly_aggregates = defaultdict(list)
for ts, val in timestamped_readings:
    hour_key = ts // 3600
    hourly_aggregates[hour_key].append(val)

# Compute average per hour
averages = {}
for hour, vals in hourly_aggregates.items():
    averages[hour] = sum(vals) / len(vals)

# Extract sequence of averages in chronological order
ordered_averages = [v for k, v in sorted(averages.items())]

# Misleading transformation: normalize to z-scores (not actually needed)
mean_all = sum(ordered_averages) / len(ordered_averages)
variance = sum((x - mean_all) ** 2 for x in ordered_averages) / len(ordered_averages)
std_dev = variance ** 0.5
z_scores = [(x - mean_all) / std_dev for x in ordered_averages] if std_dev != 0 else [0]*len(ordered_averages)

# Slice only the middle portion for processing (simulate window analysis)
middle_window = ordered_averages[1:-1]  # Exclude first and last

# Simulate trend detection via slope approximation
trend_slopes = []
for i in range(1, len(middle_window)):
    slope = middle_window[i] - middle_window[i-1]
    trend_slopes.append(slope)

# Count upward trends
upward_trends = sum(1 for s in trend_slopes if s > 0)

# Weighted contribution based on trend frequency
adjustment_factor = 1 + (upward_trends / len(trend_slopes) * 0.1) if trend_slopes else 1

# Auxiliary calculation: peak deviation (distractor)
peak_deviation = max(ordered_averages) - min(ordered_averages)
expected_deviation = 1.5
penalty = 0.02 * max(0, peak_deviation - expected_deviation)

# Actual core logic: compute stability index from middle window
stability_index = 0
if middle_window:
    mean_mid = sum(middle_window) / len(middle_window)
    variability = sum(abs(x - mean_mid) for x in middle_window)
    stability_index = 100 - (variability * 10)

# Secondary metric: duration multiplier (constant here)
duration_multiplier = len(timestamped_readings) / 600.0  # 10 minutes → 1.0

# Processed data container (key input structure)
processed_data = {
    'base_stability': stability_index,
    'duration_factor': duration_multiplier,
    'adjustment': adjustment_factor,
    'penalty': penalty,
    'raw_count': len(middle_window)
}

# Function to compute final score
def calculate_final_score(data):
    score = data['base_stability']
    score *= data['duration_factor']
    score *= data['adjustment']
    score -= data['penalty'] * 5
    if data['raw_count'] >= 5:
        score += 2.5  # bonus for sufficient samples
    return round(score, 4)

# Execute critical statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")