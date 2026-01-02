def analyze_signal(samples, threshold=0.5):
    above_threshold = [s for s in samples if s > threshold]
    below_threshold = [s for s in samples if s <= threshold]
    ratio = len(above_threshold) / len(below_threshold) if below_threshold else 0
    return ratio


def transform_coordinates(coords):
    # Irrelevant transformation
    return [(y * 2, x // 3) for x, y in coords if x > 0 and y < 100]


def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Misleading initialization
baseline_metrics = {'alpha': 0.85, 'beta': 1.2, 'gamma': 0.9}
signal_samples = [0.3, 0.6, 0.7, 0.4, 0.8, 0.2, 0.9]
coordinate_grid = [(10, 5), (15, 8), (0, 3), (-5, 12)]
raw_sequence = [1, 1, 0, 1, 0, 0, 1, 1, 1]

# Distractor: unused function
def deprecated_normalizer(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

# Simulated telemetry data with red herring fields
telemetry = {
    'readings': [0.4, 0.7, 0.6, 0.3, 0.8],
    'timestamps': [100, 101, 102, 103, 104],
    'checksum': 'ignored',
    'version': 'legacy'
}

# Key data structure
metric_data = [
    {'type': 'latency', 'value': 0.63},
    {'type': 'throughput', 'value': 0.71},
    {'type': 'jitter', 'value': 0.49},
    {'type': 'loss', 'value': 0.51}
]

# Unused recursive decoy
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Conditional expression with slicing distraction
is_stable = len(signal_samples) > 5 else False
snapshot = signal_samples[1:4] if is_stable else [0]

# Bit manipulation red herring
flag_register = 0b1010
flag_register ^= 0b1100  # Toggle bits
flag_register |= 0b0001

# Real computation begins here — hidden among distractions
base_threshold = 0.55

# Extract values above threshold using conditional logic and slicing
high_values = [entry['value'] for entry in metric_data if entry['value'] > base_threshold]
live_count = len(high_values)

# Combinatorics distractor: calculate pairs (unused)
potential_pairs = live_count * (live_count - 1) // 2 if live_count > 1 else 0

# Entropy used as a legitimate sub-component
binary_flag = [1 if m['value'] > base_threshold else 0 for m in metric_data]
uncertainty = compute_entropy(binary_flag)

# Core logic: conditional weighting based on entropy
weight_factor = 2.0 if uncertainty > 0.9 else 1.5

# Final performance score calculation
raw_sum = sum(entry['value'] for entry in metric_data)
adjusted_sum = raw_sum * weight_factor

# Normalize by number of metrics (legitimate step)
normalized_avg = adjusted_sum / len(metric_data)

# Secondary adjustment based on live count (actual dependency)
scaling_factor = live_count or 1
interim_score = normalized_avg * scaling_factor

# Apply non-linear boost (logarithmic)
from math import log
boosted_score = interim_score * log(1 + scaling_factor)

# Final decision gate using boolean logic and comparison chain
evaluation_status = (
    boosted_score > base_threshold * 10 and 
    len(high_values) >= 2
)

# Final assignment — key statement
final_score = boosted_score if evaluation_status else -1 * boosted_score

# Print result for observable output
print(f"Result: {final_score}")