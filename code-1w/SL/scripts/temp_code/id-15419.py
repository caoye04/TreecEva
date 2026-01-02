import itertools

# Simulate sensor readings from a distributed environmental monitoring system
def generate_readings(baseline, noise_level, count):
    return [baseline + ((i * 7) % 5) - noise_level for i in range(count)]

# Misleading auxiliary function - never called in execution path
def legacy_calibrate(data):
    adjusted = [x * 0.98 + 3 for x in data]
    return [max(0, x) for x in adjusted]

# Decoy transformation - looks important but unused
def frequency_encode(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    return [freq_map[v] for v in values]

# Core processing pipeline
readings_a = generate_readings(23.5, 2.1, 12)
readings_b = generate_readings(18.7, 1.8, 12)

# Combine using time-synchronized windowing (irrelevant intermediate)
sync_pairs = list(zip(readings_a, readings_b))
aggregated = [abs(a - b) * 1.05 for a, b in sync_pairs if a > 15 or b < 20]

# Distractor: complex but unused statistical calculation
temporal_trend = sum((b - a) ** 2 for a, b in zip(readings_a, readings_a[1:])) / len(readings_a)

# Real signal extraction: detect anomalies above threshold
thresholds = {"low": 4.2, "medium": 8.7, "high": 13.5}
raw_margins = [max(0, x - thresholds['medium']) for x in aggregated]

# Mask generation using bitwise pattern (red herring)
bit_flags = [(int(x) & 7) ^ 3 for x in raw_margins if x > 1]
flag_sum = sum(bit_flags)  # Dead-end computation

# Actual logic begins: filter and accumulate valid events
filtered_events = [x for x in raw_margins if x > 0.5]

# Multi-step accumulation with conditional scaling
scaled_events = []
for idx, val in enumerate(filtered_events):
    if idx % 3 == 0:
        scaled_events.append(val * 1.2)
    elif idx % 5 == 0:
        scaled_events.append(val * 0.85)
    else:
        scaled_events.append(val)

# Secondary filtering based on dynamic criterion
dynamic_floor = sum(scaled_events) / len(scaled_events) * 0.65 if scaled_events else 0
qualified = [x for x in scaled_events if x > dynamic_floor]

# Construct results using combinatorics (looks heavy but necessary)
result_pairs = list(itertools.combinations(qualified, 2))
results = []
for pair in result_pairs:
    diff = abs(pair[0] - pair[1])
    prod = pair[0] * pair[1] * 0.01
    results.append(diff + prod)

# Final aggregation with threshold-based gating
def process_outcomes(outcomes, limits):
    if not outcomes:
        return 0
    cap = limits['high']
    clipped = [min(x, cap) for x in outcomes]
    base_total = sum(clipped)
    
    # Apply diminishing returns
    adjustment = 0
    if base_total > 50:
        adjustment = sum(1 / (i + 1) for i in range(int(base_total) - 50)) if base_total > 50 else 0
    
    # Critical line: this is where final_score gets computed
    return int(base_total - adjustment)

final_score = process_outcomes(results, thresholds)

# Irrelevant visualization prep (dead code path)
plot_data = [[i, val] for i, val in enumerate(aggregated) if i % 2 == 0]

# Unused dictionary transformation
summary_stats = {
    'count': len(plot_data),
    'peak': max(aggregated) if aggregated else 0,
    'entropy': flag_sum / (len(bit_flags) + 1)
}

# Output the target result
print(f"Target result: {final_score}")