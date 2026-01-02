import itertools

# Simulated system performance metrics (real data)
data_points = [120, 150, 130, 160, 140]
base_load = sum(data_points) / len(data_points)
adjusted_load = base_load * 1.1

def normalize(x, low, high):
    return (x - low) / (high - low)

def false_positive_filter(stream):
    # Irrelevant filtering function (dead-end)
    return [x for x in stream if x > 0]

def rolling_average(series, window=3):
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs

def calculate_entropy(values):
    # Distractor: unused complex calculation
    total = sum(values)
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

current_entropy = calculate_entropy(data_points)  # Red herring

# System health indicators (mixed relevance)
health_flags = [True, False, True, True, False]
flag_analysis = {i: flag for i, flag in enumerate(health_flags)}

# Weighted evaluation setup
metrics = [
    ('response_time', 145),
    ('throughput', 155),
    ('stability', 135),
    ('latency', 125),
    ('bandwidth', 165)
]

weights = [0.2, 0.25, 0.15, 0.1, 0.3]  # Must sum to 1.0

# Misleading intermediate aggregation
temp_aggregate = 0
for i, val in enumerate([m[1] for m in metrics]):
    temp_aggregate += val * (0.1 if i % 2 == 0 else 0.05)

# Real processing begins here
metric_values = [m[1] for m in metrics]
normalized_metrics = [normalize(v, 120, 170) for v in metric_values]

# Use of enumerate and zip (required Python features)
weighted_components = []
for idx, (metric, norm_val) in enumerate(zip(metrics, normalized_metrics)):
    weight = weights[idx] if idx < len(weights) else 0.05
    contribution = norm_val * weight
    weighted_components.append(contribution)

# Secondary distraction: unused transformation chain
shifted_pairs = list(itertools.pairwise(normalized_metrics))  # Requires Python 3.10+
pair_sums = [a + b for a, b in shifted_pairs]

# Simulated redundancy check
duplicate_check = list(itertools.combinations(normalized_metrics, 2))
redundancy_score = len(duplicate_check) / 10.0  # Not used

# Core evaluation logic (depends on prior steps)
def evaluate_performance(met, wts):
    raw_vals = [item[1] for item in met]
    norm_vals = [normalize(v, 120, 170) for v in raw_vals]
    total = 0.0
    for i, nv in enumerate(norm_vals):
        if i < len(wts):
            total += nv * wts[i]
        else:
            total += nv * 0.05  # fallback
    return int(total * 1000)  # Scale up for precision

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Output the result as required
print(f"Result: {final_score}")