def analyze_trend(data, window):
    trend_values = []
    for i in range(len(data) - window + 1):
        segment = data[i:i + window]
        avg = sum(segment) / len(segment)
        trend_values.append(avg)
    return trend_values

# Simulate sensor data drift correction
raw_readings = [12.5, 13.0, 11.8, 14.2, 15.0, 13.7, 12.9, 14.5, 16.0, 15.2]
baseline_shift = 0.3
adjusted_readings = [x - baseline_shift for x in raw_readings]

# Extract moving averages
smoothed_data = analyze_trend(adjusted_readings, 3)

# Misleading auxiliary computation (distractor)
deviation_proxy = 0
for val in raw_readings:
    deviation_proxy += abs(val - sum(raw_readings)/len(raw_readings))
deviation_proxy /= len(raw_readings)

# Core evaluation metrics
metrics = {
    'stability': smoothed_data[-1] - smoothed_data[0],
    'peak_count': len([x for x in adjusted_readings if x > 14.0]),
    'consistency_ratio': len(smoothed_data) / len(adjusted_readings),
    'outlier_flags': set([i for i, x in enumerate(adjusted_readings) if abs(x - 13.5) > 2.0])
}

# Secondary distractor: unused complex structure
temp_analysis = {}
for i in range(len(smoothed_data)):
    temp_analysis[f'window_{i}'] = {
        'center': smoothed_data[i],
        'neighbors': smoothed_data[max(0,i-1):min(i+2, len(smoothed_data))],
        'weight': 0.9 ** i
    }

threshold = 1.5

# Evaluate performance based on multiple criteria
relevance_filter = {k: v for k, v in metrics.items() if k in ['stability', 'peak_count', 'consistency_ratio']}
score_components = []

if metrics['stability'] > threshold:
    score_components.append(25)
else:
    score_components.append(15)

if metrics['peak_count'] >= 4:
    score_components.append(30)
else:
    score_components.append(10)

# Use of slicing and set operation (required Python features)
historical_benchmarks = [1.2, 1.8, 1.4, 1.6, 1.5, 1.7, 1.3]
prior_valid = set(historical_benchmarks[1:-1])  # slice excluding first and last
current_set = {round(metrics['stability'], 1)}
overlap = prior_valid & current_set  # set intersection

if overlap:
    score_components.append(20)
else:
    score_components.append(5)

if metrics['consistency_ratio'] > 0.6:
    score_components.append(15)
else:
    score_components.append(5)

# Final aggregation
calibration_offset = sum([len(temp_analysis[k]['neighbors']) for k in temp_analysis]) * 0.05  # red herring calculation
effective_score = sum(score_components) + calibration_offset  # minor influence, but misleading

final_score = int(round(effective_score))

print(f"Result: {final_score}")