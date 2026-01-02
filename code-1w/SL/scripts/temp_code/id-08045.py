def analyze_trend(data, threshold=5.0):
    moving_avg = [sum(data[i:i+3]) / 3 for i in range(len(data) - 2)]
    trend_signal = sum(1 for x in moving_avg if x > threshold)
    return trend_signal

# Irrelevant helper function (dead code path)
def compute_entropy(seq):
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return round(entropy, 4)

# Unused complex transformation
def transform_coordinates(coords):
    transformed = []
    for x, y in coords:
        r = (x**2 + y**2)**0.5
        theta = __import__('math').atan2(y, x)
        transformed.append((r * 0.9, theta + 0.1))
    return transformed

# Real computation begins
raw_metrics = [85, 90, 78, 92, 88]
weight_map = {'p1': 0.2, 'p2': 0.3, 'p3': 0.15, 'p4': 0.25, 'p5': 0.1}
weights = list(weight_map.values())

# Distractor: fake normalization
normalized_metrics = [m / 100 for m in raw_metrics]
adjusted_metrics = [m + 5 for m in normalized_metrics]  # Misleading adjustment

# Real scaling using z-score (but only some matter)
deviation_factor = (sum((x - sum(raw_metrics)/len(raw_metrics))**2 for x in raw_metrics) / len(raw_metrics)) ** 0.5
z_scores = [(x - sum(raw_metrics)/len(raw_metrics)) / deviation_factor for x in raw_metrics]

# Use enumerate and zip meaningfully
indexed_weights = {i: w for i, w in enumerate(weights)}
metrics = [raw_metrics[i] * 0.8 for i in range(len(raw_metrics))]  # Apply relevance factor

# Decoy accumulation
fake_total = 0
for idx, val in enumerate(raw_metrics):
    if idx % 2 == 0:
        fake_total += val * 0.1

# Set operations as distractors
active_indices = set(range(len(raw_metrics)))
dropped_indices = {2, 4}
used_indices = active_indices - dropped_indices

# Another red herring: dictionary manipulation
evaluation_log = {}
for i, m in enumerate(metrics):
    evaluation_log[f'entry_{i}'] = {
        'raw': raw_metrics[i],
        'scaled': m,
        'weight': weights[i] if i < len(weights) else 0
    }

# Critical data transformation with zip and enumerate
combined = []
for i, (m, w) in enumerate(zip(metrics, weights)):
    if i not in dropped_indices:
        combined.append(m * w)

# Auxiliary sum (distractor)
baseline = sum(normalized_metrics) * 10

# Real aggregation logic
aggregate_performance = lambda mets, wgts: sum(m * w for m, w in zip(mets, wgts))

# Final computation
final_score = aggregate_performance(metrics, weights)

# Print required result
print(f"Result: {final_score}")