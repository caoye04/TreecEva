from itertools import combinations

# Simulate sensor data aggregation and filtering for environmental monitoring
raw_readings = [105, 92, 118, 87, 95, 120, 103]

# Irrelevant preprocessing: generate all pairs (distractor)
pairwise_diffs = [abs(a - b) for a, b in combinations(raw_readings, 2)]
max_pair_diff = max(pairwise_diffs)  # Misleading metric, not used later

# Filter out outliers using interquartile range logic
sorted_readings = sorted(raw_readings)
q1 = sorted_readings[1]
q3 = sorted_readings[5]
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

filtered_readings = [x for x in raw_readings if lower_bound <= x <= upper_bound]

# Compute rolling average over valid windows (semi-relevant)
window_averages = []
for i in range(len(filtered_readings) - 2):
    window_averages.append(sum(filtered_readings[i:i+3]) / 3)

# Extract trend direction (positive or negative changes)
trend_changes = [1 if window_averages[i] < window_averages[i+1] else -1 for i in range(len(window_averages)-1)]
positive_trends = sum(1 for t in trend_changes if t == 1)
negative_trends = sum(1 for t in trend_changes if t == -1)

# Weighted scoring system based on stability and central tendency
def calculate_weighted_average(metrics, weights):
    return sum(m * w for m, w in zip(metrics, weights))

# Key metrics derived from filtered data
mean_value = sum(filtered_readings) / len(filtered_readings)
std_deviation_proxy = sum((x - mean_value)**2 for x in filtered_readings) / len(filtered_readings)
stability_score = len(window_averages)  # More stable readings -> longer window list

# Relevant metrics for final score
relevant_metrics = [
    mean_value,
    100 - std_deviation_proxy,  # Inverse variance as quality proxy
    positive_trends / (positive_trends + negative_trends) * 100 if (positive_trends + negative_trends) > 0 else 50
]

# Static weights (calibrated from historical performance)
weights = [0.4, 0.35, 0.25]

# Dead code path: alternative scoring (never called)
def legacy_scoring(data):
    return max(data) - min(data)

# Unused helper: adds noise but isn't invoked
def add_jitter(value, factor=0.01):
    return value + random.uniform(-factor, factor)

# Final computation step
final_score = calculate_weighted_average(relevant_metrics, weights)

# Print result for extraction
print(f"Result: {final_score}")