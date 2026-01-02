from collections import defaultdict

# Simulate time-series server load analysis across zones
def analyze_server_load(log_data):
    raw_counts = defaultdict(int)
    temp_aggregates = []
    normalization_factor = 0.85
    offset_correction = 2

    # Parse and count occurrences per zone
    for entry in log_data:
        zone, usage_str = entry.split(':')
        usage = float(usage_str)
        raw_counts[zone] += usage
        temp_aggregates.append(usage ** 0.5)

    # Normalize counts with dummy adjustment
    normalized_values = []
    for zone in sorted(raw_counts.keys()):
        adjusted = raw_counts[zone] * normalization_factor + offset_correction
        normalized_values.append(adjusted)

    # Secondary processing: filter and scale
    filtered_caps = [val for val in normalized_values if val > 3.0]
    scaled_caps = [round(x * 1.1, 2) for x in filtered_caps]

    # Irrelevant smoothing operation (distractor)
    smoothed = []
    for i, val in enumerate(scaled_caps):
        prev = smoothed[i-1] if i > 0 else val
        smoothed.append(round((prev + val) / 2, 2))

    # Core computation path
    usage_levels = []
    for idx, (zone, raw_val) in enumerate(raw_counts.items()):
        contribution = raw_val * (idx + 1)
        penalty = len(zone) * 0.1
        net_effect = contribution - penalty
        if net_effect > 0:
            usage_levels.append(net_effect)

    # Key statement
    peak_capacity = max(usage_levels)

    # Unrelated diagnostic trace (dead code for final answer)
    diagnostics = []
    for a, b in zip(temp_aggregates, enumerate(smoothed)):
        diagnostics.append(a + b[1])

    return peak_capacity

# Input data
logs = [
    'alpha:4.2', 'beta:3.8', 'gamma:5.1', 'delta:2.9',
    'alpha:1.1', 'beta:4.4', 'gamma:3.3', 'delta:6.7'
]

result = analyze_server_load(logs)
print(f"Result: {result}")