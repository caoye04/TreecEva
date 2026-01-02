def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x for x in data if x > threshold]


def preprocess_signals(signals):
    """Another decoy function with complex but unused logic."""
    processed = []
    for i, s in enumerate(signals):
        if i % 2 == 0:
            processed.append(s ** 2)
        else:
            processed.append(s // 3)
    return [p for p in processed if p > 0]


def transform_coordinates(coords):
    """Unused geometric transformation to add confusion."""
    return [(c[0] * 1.5, c[1] * 0.8) for c in coords]


def calculate_entropy(sequence):
    from math import log2
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
SYSTEM_MODE = 'diagnostic'

# Decoy data structures
logs = [
    {'timestamp': 1001, 'event': 'init', 'level': 'INFO'},
    {'timestamp': 1005, 'event': 'read', 'level': 'DEBUG'},
    {'timestamp': 1010, 'event': 'write', 'level': 'WARNING'}
]

status_flags = {1: 'active', 2: 'pending', 4: 'locked', 8: 'archived'}
flag_combination = 3 | 4 & ~8  # Bitwise red herring

# Real input data (buried among distractions)
metrics = [0.85, 0.92, 0.78, 0.96, 0.81]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Complex-looking but irrelevant list transformations
shifted_metrics = [m * 1.05 for m in metrics][1:] + [metrics[0]]
sorted_pairs = sorted(zip(weights, metrics), key=lambda x: x[1], reverse=True)
double_enum = [(i, j, a * b) for i, a in enumerate(metrics) for j, b in enumerate(weights) if i == j]

# Simulate noise filtering (unused)
filtered_data = [x for x, w in zip(metrics, weights) if w >= 0.15]

# Core logic buried in abstraction
matrix = [[m * w for w in weights] for m in metrics]
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))

# More decoys: set operations and dictionary mapping
unique_weights = set(weights)
normalized_map = {w: w / sum(weights) for w in weights}
weight_classes = {k: 'high' if k > 0.2 else 'low' for k in unique_weights}

# Actual computation hidden in misleading context
scaling_factor = 1.0
if len(metrics) % 2 == 1:
    scaling_factor *= 1.1
if sum(weights) == 1.0:
    scaling_factor *= 1.05  # Valid condition

# Real answer computation — non-obvious due to surrounding noise
weighted_sum = sum(m * w for m, w in zip(metrics, weights))
adjusted_mean = weighted_sum * scaling_factor

# Additional red herring: conditional overwriting that doesn't trigger
if any(m < 0.7 for m in metrics):
    adjusted_mean = 0.5 * adjusted_mean  # Dead code path

# Final result disguised as part of system diagnostics
final_score = int(round(adjusted_mean * 1000))  # <-- Key assignment point

# Unused tuple unpacking and slicing for language feature inclusion
_, *middle_vals, _ = sorted(metrics)
indexed_items = list(enumerate(shifted_metrics[::2]))

# Another decoy function call
entropy_val = calculate_entropy([1, 1, 0, 1, 0, 0, 1])

# Print final result as required
print(f"Result: {final_score}")