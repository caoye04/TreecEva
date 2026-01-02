def analyze_data(records):
    totals = {}
    for r in records:
        key, values = r[0], r[1]
        if key not in totals:
            totals[key] = 0
        totals[key] += sum(v for v in values if v > 0)
    return totals

# Irrelevant helper function (decoy)
def compute_hash(data):
    h = 0
    for char in str(data):
        h = (h * 31 + ord(char)) % 10007
    return h

# Unused transformation (dead code path)
def transform_sequence(seq):
    return [x ** 2 - x for x in seq if x % 2 == 0]

# Misleading intermediate calculation (red herring)
baseline_offset = sum([i * 2 for i in range(15)]) // 3

# Simulated system metrics with mixed data types
raw_metrics = [
    ('latency', [120, -1, 115, 118, 0]),
    ('throughput', [890, 902, -5, 898, 910]),
    ('errors', [3, 0, 1, 0, 2]),
    ('memory', [4500, 4600, -50, 4550, 4700])
]

# Extract positive readings only
filtered_metrics = analyze_data(raw_metrics)

# Additional distraction: fake normalization (not used in final path)
normalized = {k: v / (v + 100) for k, v in filtered_metrics.items()}

# Weight assignment with decoy entries
all_weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'errors': 0.35,
    'memory': 0.1,
    'bandwidth': 0.05,  # unused weight (distractor)
    'timeout': 0.02   # unused weight (distractor)
}

# Subset of relevant weights
weights = {k: v for k, v in all_weights.items() if k in filtered_metrics}

# Spurious list processing (irrelevant)
data_points = [(i, i**2) for i in range(10)]
indexed = dict(enumerate(data_points))
combined = [a + b for a, b in zip(indexed.values(), indexed.values())]

# Fake correlation matrix (dead code)
correlation = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        if i != j:
            correlation[i][j] = (i + j) % 3

# Core logic hidden among noise
metric_sums = []
for name, vals in raw_metrics:
    total = 0
    for v in vals:
        if v > 0:  # ignore negative or zero readings
            total += v
    metric_sums.append(total)

# Create mapping consistent with filtered_metrics
metrics = dict(zip([m[0] for m in raw_metrics], metric_sums))

# Another red herring: set operations with no impact
unique_values = set()
for vals in [m[1] for m in raw_metrics]:
    unique_values.update(set(vals))
pruned_set = {x for x in unique_values if x > 0 and x % 10 == 0}
dropped_count = len(unique_values) - len(pruned_set)

# Critical computation buried in distractions
effective_total = 0
for k in metrics:
    if k in weights:
        effective_total += metrics[k] * weights[k]

# Final evaluation using correct weighted sum
def evaluate_performance(met, wgt):
    score = 0
    for key in met:
        if key in wgt:
            score += met[key] * wgt[key]
    adjustment = 0
    # Conditional tweak based on error count (subtle but valid)
    if 'errors' in met and met['errors'] < 5:
        adjustment = 10
    return int(score) + adjustment

# Execute main logic
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Target result: {final_score}")