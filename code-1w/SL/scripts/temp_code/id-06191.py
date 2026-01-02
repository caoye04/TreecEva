from collections import defaultdict, Counter
import math

# Simulated system performance data
timestamps = [100, 105, 110, 115, 120, 125, 130]
raw_metrics = [85, 90, 70, 65, 95, 80, 75]

# Irrelevant auxiliary data (distractor)
system_logs = defaultdict(lambda: 'INFO')
for t in timestamps:
    system_logs[t] = 'DEBUG'

# Misleading transformation path (dead code path)
def legacy_transform(x):
    return [val * 1.05 for val in x if val > 75]

legacy_data = legacy_transform(raw_metrics)  # Unused

# Secondary distractor: frequency analysis of values
value_counts = Counter(raw_metrics)
dominant_value = value_counts.most_common(1)[0][0]  # 85 or 75? (distraction)

# Auxiliary calculation with red herring result
offset_correction = sum([t // 10 for t in timestamps]) % 7  # Evaluates to 1, but misleading

# Core processing function with nested logic
def normalize(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [(v - mean_val) / (std_dev + 1e-8) for v in values]  # Avoid division by zero

# Noise injection simulation (not actually used in final path)
noisy_normalized = [round(x + 0.1, 2) for x in normalize(raw_metrics)]  # Distractor

# Threshold modulation based on time pattern (irrelevant)
trend_factor = 1
for i in range(1, len(timestamps)):
    if timestamps[i] - timestamps[i-1] > 4:
        trend_factor *= 1.01

# Real processing begins here — conditional filtering
filtered_metrics = []
for val in raw_metrics:
    if val >= 70:
        filtered_metrics.append(val)
    else:
        # Early drop mimics fault tolerance
        continue

# Aggregation via multiple steps
aggregated = defaultdict(int)
for idx, val in enumerate(filtered_metrics):
    bucket = idx % 3
    aggregated[bucket] += val

# Compute composite index (intermediate, partially relevant)
composite_index = 0
for k in aggregated:
    composite_index += aggregated[k] * (k + 1)

# Bit manipulation layer (adds complexity, some distraction)
binary_weight = (composite_index >> 3) & 0b1111  # Extract bits 3-6
adjusted_index = composite_index ^ binary_weight  # XOR adjustment

# Conditional scaling
if adjusted_index > 300:
    adjusted_index = int(adjusted_index * 0.95)
else:
    adjusted_index = int(adjusted_index * 1.05)

# Base threshold derived from normalized dispersion (real signal)
norm_vals = normalize(raw_metrics)
base_threshold = int(abs(sum(norm_vals[:len(norm_vals)//2]) - sum(norm_vals[len(norm_vals)//2:])) * 100)

# Metric data structure with mixed content
metric_data = {
    'values': filtered_metrics,
    'count': len(filtered_metrics),
    'sum': sum(filtered_metrics),
    'base_ref': dominant_value,  # Red herring: not used in final calc
    'offset': offset_correction,  # Another decoy
    'trend': trend_factor
}

# Evaluation logic with early returns and branching
def evaluate_performance(data, threshold):
    if data['count'] == 0:
        return 0
    
    initial_score = data['sum'] // data['count']
    
    # Additional weight from aggregation
    bonus = 0
    for k, v in aggregated.items():
        if v > threshold * 2:
            bonus += k * 5
    
    # Conditional penalty
    if data['count'] < 5:
        bonus -= 10
    
    # Final adjustment using bit-level property of adjusted_index
    flag_bit = (adjusted_index >> 2) & 1  # Use a stable bit state
    if flag_bit:
        bonus += 5
    
    final_raw = initial_score + bonus
    
    # Clamp and scale
    final_raw = max(50, min(final_raw, 150))
    
    # Final non-linear transformation
    return int(math.floor(final_raw * (1 + (threshold / 200))))

# Execution point of interest
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Target result: {final_score}")