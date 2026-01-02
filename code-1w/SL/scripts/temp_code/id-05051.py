def analyze_component(data, threshold=0.5):
    if len(data) == 0:
        return 0
    avg = sum(data) / len(data)
    if avg > threshold:
        return avg * 1.5
    else:
        return avg * 0.8

# Irrelevant helper function (decoy)
def compute_entropy(values):
    import math
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

# Unused but plausible-looking transformation
def transform_signal(signal):
    return [s ** 2 for s in signal if s > 0]

# Simulate sensor readings (distraction)
sensor_logs = {
    'sensor_a': [0.1, 0.4, 0.3],
    'sensor_b': [0.6, 0.7, 0.8],
    'sensor_c': [0.2, 0.1, 0.3]
}

# Fake aggregation (dead code path)
aggregated_sensors = {}
for key, readings in sensor_logs.items():
    if sum(readings) / len(readings) > 0.5:
        aggregated_sensors[key] = 'stable'
    else:
        aggregated_sensors[key] = 'unstable'

# Real metric computation begins here
baseline_metrics = [0.6, 0.4, 0.9, 0.7]

# Apply conditional scaling based on trend
adjusted_metrics = []
for m in baseline_metrics:
    if m > 0.65:
        adjusted_metrics.append(m * 1.2)
    elif m < 0.5:
        adjusted_metrics.append(m * 0.85)
    else:
        adjusted_metrics.append(m * 1.05)

# Weight vector with red herring elements
weights_config = {
    'w1': 0.3,
    'w2': 0.4,
    'w3': 0.2,
    'w4': 0.1,
    'temporal_factor': 0.95,  # unused distraction
    'calibration_offset': 0.05   # unused distraction
}

# Distractor: irrelevant list processing
temp_data = [x for x in range(8)]
doubled_temp = [t * 2 for t in temp_data if t % 2 == 0]
summed_temp = sum(doubled_temp) // 2  # dead-end calculation

# Conditional expression used appropriately
metrics = [m if m <= 0.8 else 0.8 for m in adjusted_metrics]

# Dictionary-based dynamic weighting
weight_keys = ['w1', 'w2', 'w3', 'w4']
weights = [weights_config[k] for k in weight_keys]

# Core logic: weighted combination
weighted_sum = sum(metrics[i] * weights[i] for i in range(len(metrics)))
normalizer = sum(weights)

# Secondary adjustment using recursion (simple)
def dampen_value(val, depth):
    if depth <= 0 or val < 0.1:
        return val
    return 0.95 * dampen_value(val, depth - 1)

normalized_score = weighted_sum / normalizer
final_adjustment = dampen_value(normalized_score, 3)

# Linear search for threshold crossing (redundant check - distractor)
threshold_met = False
for idx in range(len(metrics)):
    if metrics[idx] > 0.75:
        threshold_met = True
        break  # early exit not actually needed

# This flag does nothing (misleading control flow)
if threshold_met:
    final_adjustment *= 1.02

# Key assignment point
final_score = int(final_adjustment * 10000) / 10000  # round to 5 decimal places

# Output requirement
print(f"Result: {final_score}")