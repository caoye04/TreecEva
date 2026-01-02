from itertools import combinations

def analyze_trends(data_points, threshold=5):
    trend_count = 0
    temp_accumulator = 0
    for i in range(1, len(data_points)):
        diff = data_points[i] - data_points[i-1]
        if abs(diff) > threshold:
            trend_count += 1
        temp_accumulator += diff  
    return trend_count

# Simulate sensor readings over time
sensor_readings = [12, 15, 14, 20, 25, 23, 30, 35, 33]
baseline_data = sorted([x * 2 for x in sensor_readings if x % 2 == 1])

# Extraneous transformation with no impact on final result
dummy_transform = [x ** 0.5 for x in sensor_readings if x > 20]

# Define performance metrics using set operations
metric_set = set()
for r in range(2, 4):
    for combo in combinations(baseline_data, r):
        if sum(combo) % 7 == 0:
            metric_set.add(sum(combo))

# Secondary analysis with misleading intermediate calculations
candidate_peaks = []
running_total = 0
for val in sensor_readings:
    running_total += val
    if val > 25:
        candidate_peaks.append(running_total // val)

# Irrelevant function call that doesn't affect outcome
def compute_variance(values):
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)

variance_noise = compute_variance(baseline_data[:5])

# Core evaluation logic
prev_metric = 0
for m in sorted(metric_set, reverse=True):
    if m < 100:
        prev_metric = m
        break

adjusted_baseline = [x for x in baseline_data if x > 15]

# Final performance score calculation
evaluation_log = []
score_weights = {'trend': 0.4, 'coverage': 0.6}

primary_trend = analyze_trends(sensor_readings)
coverage_metric = len(metric_set.intersection(set(adjusted_baseline)))

final_score = 0
for key in score_weights:
    if key == 'trend':
        final_score += primary_trend * score_weights[key]
    elif key == 'coverage':
        final_score += coverage_metric * score_weights[key]

# Distractor: unused conditional block
if len(dummy_transform) > 5:
    final_score *= 1.1

# Print final result as required
print(f"Result: {final_score}")