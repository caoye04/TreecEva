import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 1.8, 4.5, 2.7, 3.6, 4.1, 2.9, 3.3]
decoy_flags = [False, True, False, True, False]

# Irrelevant transformation: string-based red herring
timestamp_labels = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7']
labeled_data = [f'{label}:{val}' for label, val in zip(timestamp_labels, raw_readings)]
filtered_strings = [s for s in labeled_data if 'T' in s and ':' in s]

# Distractor: unused complex structure
class SignalCache:
    def __init__(self):
        self.entries = {}
        self.counter = 0

    def add(self, k, v):
        self.entries[k] = v
        self.counter += 1

# Unused function — dead code path
def legacy_normalize(x):
    return [val / max(x) for val in x]

# Real signal processing begins
scaling_factor = 1.75
amplified = [x * scaling_factor for x in raw_readings]

# Apply non-linear correction using logarithmic warp
warped = [math.log(v + 1) for v in amplified]

# Compute moving average (window = 2) for smoothing
trend_smoothed = []
for i in range(len(warped) - 1):
    trend_smoothed.append((warped[i] + warped[i+1]) / 2)

trend_smoothed.append(warped[-1])  # Append last point

# Threshold detection: count how many exceed dynamic threshold
dynamic_threshold = sum(trend_smoothed) / len(trend_smoothed)
spike_count = 0
for val in trend_smoothed:
    if val > dynamic_threshold:
        spike_count += 1

# Decoy computation: set operations with no impact
observed_tags = set(['A', 'B', 'C'])
predicted_tags = set(['B', 'C', 'D', 'E'])
overlap = observed_tags & predicted_tags

# Bit manipulation red herring
bitmask = 0b101010
shifted_mask = bitmask << 3
masked_diagnostics = spike_count ^ shifted_mask

# Actual critical data path
baseline_reference = 2.5
adjusted_readings = [max(0, x - baseline_reference) for x in trend_smoothed]

# Group into high/low categories
high_activity = [x for x in adjusted_readings if x > 0.5]
low_activity = [x for x in adjusted_readings if x <= 0.5]

# Compute final metric: weighted combination
activity_score = len(high_activity) * 1.5 + len(low_activity) * 0.5

# Secondary metric: variance of adjusted readings
mean_adj = sum(adjusted_readings) / len(adjusted_readings)
variance = sum((x - mean_adj) ** 2 for x in adjusted_readings) / len(adjusted_readings)

# Final processing function
def analyze_signal(data_list):
    base = sum(data_list)
    penalty = math.sqrt(len(data_list))
    return int(base * penalty)  # Truncated integer result

# Processed data used in final call
processed_data = [activity_score, variance, spike_count, mean_adj]

# Dead code: never called
def debug_trace_path(values):
    return [round(v * 1.1, 2) for v in values]

# Misleading intermediate print (not actual answer)
intermediate_result = masked_diagnostics * 2

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Output the required result
print(f"Target result: {final_diagnostic}")