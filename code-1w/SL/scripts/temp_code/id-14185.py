from collections import defaultdict

# Simulate server load monitoring across regions and time slots
time_slots = [f't{i}' for i in range(6)]
regions = ['us-west', 'us-east', 'eu-central', 'ap-south']

# Track request counts per region over time
request_log = [
    ('us-west', 't0', 120), ('us-east', 't0', 95),  ('eu-central', 't0', 87),
    ('us-west', 't1', 145), ('ap-south', 't1', 110), ('us-east', 't1', 93),
    ('eu-central', 't2', 134), ('us-west', 't2', 167), ('ap-south', 't2', 105),
    ('us-east', 't3', 118), ('us-west', 't3', 155), ('eu-central', 't3', 126),
    ('ap-south', 't4', 138), ('us-east', 't4', 102), ('us-west', 't4', 173),
    ('eu-central', 't5', 140), ('us-west', 't5', 189), ('ap-south', 't5', 152)
]

# Main tracker for peak usage analysis
usage_tracker = defaultdict(int)
baseline_threshold = 100
excess_events = []

# Secondary structure for redundant analytics (distractor)
region_momentums = {r: 0 for r in regions}
consecutive_high = {r: 0 for r in regions}

# Accumulate total requests per region
for region, timestamp, count in request_log:
    usage_tracker[region] += count

    # Distractor: momentum tracking (not used in final answer)
    if count > baseline_threshold:
        region_momentums[region] += 1
        consecutive_high[region] += 1
    else:
        consecutive_high[region] = 0

    # Distractor: event logging for high-load anomalies
    if count > 140:
        excess_events.append((region, timestamp, count))

# Compute rolling adjustments (irrelevant to final result)
adjustment_factor = 0
for reg, total in usage_tracker.items():
    if total > 500:
        adjustment_factor += total * 0.05

# Normalize some fake metric (dead computation)
normalized_scores = {}
total_load = sum(usage_tracker.values())
for r in regions:
    raw = usage_tracker[r]
    normalized = (raw - baseline_threshold * 6) / total_load if total_load > 0 else 0
    normalized_scores[r] = round(normalized, 3)

# Key statement: determine peak capacity from accumulated usage
peak_capacity = max(usage_tracker.values()) if usage_tracker else 0

# Print result for evaluation
print(f"Result: {peak_capacity}")