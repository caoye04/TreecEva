def analyze_signal(readings):
    filtered = [x for x in readings if abs(x) > 0.5]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

readings = [0.1, 0.7, -0.6, 1.2, 0.3, -0.9, 0.0, 1.5, -1.1]

# Irrelevant transformation chain (distractor)
transformed = []
for i, val in enumerate(readings):
    if i % 2 == 0:
        transformed.append(val * 1.1)
    else:
        transformed.append(val + 0.2)

# Dead code path: never called
def deprecated_filter(seq):
    return [x for x in seq if x != 0]

# Unused bitwise manipulation (red herring)
mask = 0b101010
shifted_mask = mask << 3
inverted = ~shifted_mask & 0b1111111

# Simulated sensor weights (some are decoys)
weight_map = {
    's1': 0.8,
    's2': 0.5,
    's3': 1.2,  # unused in final logic
    'aux': 0.1   # irrelevant
}

weights = [0.8, 0.5]  # actual weights used

# Simulate trend detection with list comprehension and zip
baseline = [0.65, 0.72, 1.15, -0.88, 1.48, -1.09]
offsets = [0.05, -0.02, 0.05, -0.02, 0.02, -0.01]
trend_data = [a + b for a, b in zip(baseline, offsets)]

# Accumulation with conditional adjustment (relevant)
correction_factor = 1.0
if len(trend_data) > 5:
    correction_factor = 0.95

trend_data = [x * correction_factor for x in trend_data]

# Dummy set operations (distraction)
unique_values = set()
for x in trend_data:
    rounded = round(x, 2)
    unique_values.add(rounded)

# Secondary dead-end computation
snapshot = (sum(transformed[:4]) // 1, len(weight_map))
dummy_checksum = snapshot[0] ^ snapshot[1]

# Core aggregation function (used)
def aggregate_metrics(series, factors):
    total = 0.0
    for i, (val, weight) in enumerate(zip(series, factors)):
        if i % 2 == 0:
            total += val * weight
        else:
            total -= val * weight  # alternating sign pattern
    return round(total, 4)

# Misleading recursive red herring (never executed)
def recursive_sum(n):
    return n + recursive_sum(n-1) if n > 0 else 0

# Key execution point
final_diagnostic = aggregate_metrics(trend_data, weights)
print(f"Result: {final_diagnostic}")