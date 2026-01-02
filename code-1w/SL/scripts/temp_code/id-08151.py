from collections import defaultdict
from itertools import combinations

# Simulate sensor data aggregation and anomaly-adjusted scoring
raw_readings = [105, 200, 180, 99, 210, 195, 140, 160, 170, 155]
threshold = 100
count_stats = defaultdict(int)
adjusted_values = []
outlier_flags = []

# Step 1: Classify readings and adjust anomalies
for idx, val in enumerate(raw_readings):
    if val > threshold:
        count_stats['above_threshold'] += 1
        # Adjustment: reduce high values by 5% to dampen spikes
        adjusted_val = val * 0.95
    else:
        count_stats['below_threshold'] += 1
        adjusted_val = val * 1.1  # boost low values
    adjusted_values.append(round(adjusted_val))
    outlier_flags.append(abs(val - 150) > 60)  # arbitrary deviation check

# Irrelevant: Generate all pairs (distractor, not used later)
dummy_pairs = list(combinations(adjusted_values, 2))
total_pairs = len(dummy_pairs)  # unused beyond this

# Step 2: Apply moving average filter (window size 3)
smoothed = []
for i in range(len(adjusted_values)):
    if i < 2:
        smoothed.append(adjusted_values[i])
    else:
        window_avg = sum(adjusted_values[i-2:i+1]) / 3
        smoothed.append(round(window_avg))

# Step 3: Detect upward trends
upward_trends = 0
for i in range(1, len(smoothed)):
    if smoothed[i] > smoothed[i-1]:
        upward_trends += 1

# Step 4: Compute base score as median of smoothed
sorted_vals = sorted(smoothed)
mid = len(sorted_vals) // 2
if len(sorted_vals) % 2 == 0:
    base_score = (sorted_vals[mid-1] + sorted_vals[mid]) / 2
else:
    base_score = sorted_vals[mid]

# Step 5: Adjust score based on trend strength
trend_factor = 1 + (upward_trends / len(smoothed)) * 0.1
preliminary_score = base_score * trend_factor

# Distractor variables
noise_level = sum(1 for f in outlier_flags if f) * 0.5
normalization_offset = 10  # unused correction term
scaling_constant = 2.718  # red herring, looks important

# Step 6: Final adjustment using conditional logic
def calculate_final_score(data_chunk):
    raw_sum = sum(data_chunk)
    penalty = 0
    if raw_sum > 1500:
        penalty = 50
    elif raw_sum < 1200:
        penalty = 20
    return int(raw_sum - penalty)

processed_data = smoothed[::2]  # every other element
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")