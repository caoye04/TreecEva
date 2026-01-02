from collections import defaultdict, Counter

# Simulate sensor readings with timestamped data
timestamped_readings = [
    (100, [23.5, 24.1, 25.0, 23.9]),
    (101, [24.2, 24.0, 23.8, 24.1]),
    (102, [25.1, 25.3, 25.0, 24.9]),
    (103, [26.0, 25.8, 26.2, 25.9])
]

# Misleading auxiliary data (distractor)
redundant_stats = defaultdict(float)
for ts, vals in timestamped_readings:
    redundant_stats[ts] += sum(vals) / len(vals)

# Track anomaly counts per threshold (semi-relevant)
anomaly_counters = {thresh: 0 for thresh in [24.0, 24.5, 25.0]}
all_values = [val for _, vals in timestamped_readings for val in vals]

for temp in all_values:
    for t in anomaly_counters:
        if temp > t:
            anomaly_counters[t] += 1

# Secondary processing with zip and enumerate (relevant + distractor)
indexed_deltas = []
prev_avg = None
for i, (ts, vals) in enumerate(timestamped_readings):
    current_avg = sum(vals) / len(vals)
    if prev_avg is not None:
        delta = current_avg - prev_avg
        indexed_deltas.append((i, delta))
    prev_avg = current_avg

# Compute moving trend using conditional expression (relevant)
trend_magnitude = sum([abs(delta) for _, delta in indexed_deltas]) if indexed_deltas else 0.0

# Auxiliary confusion: frequency analysis of rounded values (mostly irrelevant)
rounded_freq = Counter([round(v) for v in all_values])
frequent_rounded = max(rounded_freq, key=lambda x: rounded_freq[x])

# Core logic: weighted score based on anomalies above 25.0 and trend
base_anomaly_score = anomaly_counters[25.0] * 10
adjustment_factor = 1.5 if trend_magnitude > 1.0 else 0.8

# Distractor: unused complex calculation
phantom_metric = sum([v ** 0.5 for v in all_values if v > 25.0]) / (len(all_values) or 1)

# Final aggregation — key computation
stability_bonus = 5 if all(v < 26.5 for v in all_values) else 0
critical_threshold_exceedances = sum(1 for v in all_values if v >= 25.0)
penalty = critical_threshold_exceedances * 2

final_score = base_anomaly_score + stability_bonus - penalty
final_score = int(final_score * adjustment_factor)  # Apply trend-based scaling

print(f"Result: {final_score}")