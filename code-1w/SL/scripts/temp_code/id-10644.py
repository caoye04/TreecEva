def analyze_component(signal, threshold=0.5):
    """Irrelevant analysis function (distractor)"""
    if len(signal) == 0:
        return 0.0
    peaks = [i for i in range(1, len(signal)-1) if signal[i] > max(signal[i-1], signal[i+1])]
    return len(peaks) / len(signal)


def compute_entropy(data):
    """Another distractor: computes entropy but not used in main logic"""
    from math import log2
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return entropy

# Simulated system metrics (some relevant, some misleading)
raw_metrics = [0.78, 0.82, 0.65, 0.91, 0.54, 0.73, 0.88, 0.69]
dummy_signal = [0.1, 0.4, 0.9, 0.3, 0.2]

# Irrelevant transformations (dead code paths)
smoothed = raw_metrics[1::2]  # slicing - relevant later
noisy_copy = raw_metrics + [x * 0.1 for x in raw_metrics[:3]]
filtered_metrics = [x for x in raw_metrics if x > 0.6]  # distractor list

# Unused weight variants (misleading)
alt_weights = [0.1, 0.3, 0.2, 0.4]
temp_weights = [w ** 2 for w in alt_weights]

# Key weights used in computation
weights = [0.25, 0.25, 0.15, 0.35]  # sum to 1.0

# Conditional manipulation based on irrelevant condition (red herring)
count_above = sum(1 for m in raw_metrics if m > 0.7)
if count_above > 3:
    weights[0] += 0.05
    weights[1] -= 0.05  # compensates, net neutral

# Core data transformation chain
base_slice = raw_metrics[::2]  # slicing: [0.78, 0.65, 0.54, 0.88]
adjusted_slice = [x + 0.02 for x in base_slice]  # minor adjustment
trimmed = adjusted_slice[1:-1]  # slice again: [0.67, 0.56]

# Simulate multiple performance dimensions
accuracy = sum(trimmed) / len(trimmed)
precision = (raw_metrics[1] + raw_metrics[3]) / 2
recall = raw_metrics[6]
latency_penalty = 0.9 - raw_metrics[4]

# Composite metric construction
composite_parts = [
    accuracy * 1.1,
    precision * 0.9,
    recall * 1.05,
    latency_penalty * 0.8
]

# Aggregate using weighted sum
metrics = [accuracy, precision, recall, latency_penalty]

# Dead code: function never called
def normalize_vector(vec):
    norm = sum(x**2 for x in vec) ** 0.5
    return [x/norm for x in vec]

# Actual aggregation function
def aggregate_performance(mets, wts):
    if len(mets) != len(wts):
        raise ValueError("Mismatched lengths")
    total = 0.0
    for i in range(len(mets)):
        total += mets[i] * wts[i]
    return round(total, 6)

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Misleading final adjustments (not executed)
# if final_score > 0.75:
#     final_score *= 0.95

# Output result
print(f"Result: {final_score}")