from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated system metrics from distributed nodes
telemetry_data = [
    [15, 23, 38, 12, 45],
    [18, 20, 35, 14, 47],
    [14, 25, 37, 13, 44],
    [16, 22, 36, 15, 46]
]

# Irrelevant backup data — distractor
telemetry_backup = [[x for x in reversed(row)] for row in telemetry_data]

# Aggregate node metrics by index (column-wise)
aggregated_metrics = [sum(col) for col in zip_longest(*telemetry_data, fillvalue=0)]

# Misleading normalization — not used in final path
normalized_metrics = [round(x / len(telemetry_data), 2) for x in aggregated_metrics]

# Historical baselines — red herring
baseline_thresholds = [15, 22, 36, 13, 45]
below_baseline = [agg < base for agg, base in zip(aggregated_metrics, baseline_thresholds)]

# Bitwise analysis of metric stability (irrelevant to final score)
stability_flags = 0
for i, (val, thresh) in enumerate(zip(aggregated_metrics, baseline_thresholds)):
    if val >= thresh:
        stability_flags |= (1 << i)  # Set bit if above threshold

# Decoy function — never called
def compute_legacy_score(data):
    total = 0
    for row in data:
        for val in row:
            if val % 3 == 0:
                total += val // 3
    return total

# Another decoy: complex but unused transformation
shifted_data = []
for i, row in enumerate(telemetry_data):
    shifted_row = [row[(j + i) % len(row)] for j in range(len(row))]
    shifted_data.append(shifted_row)

# Extract frequency of key performance indicators
event_stream = [event for sublist in telemetry_data for event in sublist]
frequency_map = Counter(event_stream)

# Identify dominant events (occur more than 2 times)
dominant_events = {k: v for k, v in frequency_map.items() if v > 2}

# Filtered high-impact events — used later
high_impact = [k for k, v in dominant_events.items() if k > 35]

# Secondary filter: must be odd numbers
qualified_impact = [x for x in high_impact if x % 2 == 1]

# Weight assignment per metric dimension
metric_weights = {
    'latency': 0.15,
    'throughput': 0.25,
    'consistency': 0.20,
    'availability': 0.10,
    'reliability': 0.30
}

# Raw outcome scores derived from aggregated metrics
raw_outcomes = {
    'latency': aggregated_metrics[0],
    'throughput': aggregated_metrics[1],
    'consistency': aggregated_metrics[2],
    'availability': aggregated_metrics[3],
    'reliability': aggregated_metrics[4]
}

# Conditional adjustment based on qualified impact presence
adjustment_factor = 1.0
if len(qualified_impact) > 0 and sum(qualified_impact) > 100:
    adjustment_factor = 0.9
else:
    temp_sum = 0
    for num in qualified_impact:
        temp_sum += num * 2  # Dead computation path — never reached
    adjustment_factor = 1.1

# Actual evaluation logic
weight_sum = sum(metric_weights.values())
adjusted_weights = {k: v / weight_sum for k, v in metric_weights.items()}

outcome_sum = sum(raw_outcomes[k] * adjusted_weights[k] for k in raw_outcomes)
penalty = 5 if False in below_baseline else 0  # Uses below_baseline (computed earlier)

# Final performance score calculation
core_score = outcome_sum - penalty
final_score = int(core_score * adjustment_factor)

# Output result as required
print(f"Result: {final_score}")