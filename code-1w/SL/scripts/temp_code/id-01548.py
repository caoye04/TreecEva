def analyze_signal(data, threshold=0.7):
    """Irrelevant signal processing function (dead code path)"""
    filtered = [x for x in data if abs(x) > threshold]
    return [x * 2 for x in filtered if x != 0]


def compute_entropy(seq):
    """Distractor: computes entropy but not used in main logic"""
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 6)

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 512
DEFAULT_TIMEOUT = 30
DEBUG_MODE = True

# Actual relevant data structures
baseline_metrics = [0.85, 0.92, 0.78, 0.96, 0.81]
weights = [5, 3, 4, 2, 6]

# Decoy list comprehensions with unused results
_ = [x ** 2 for x in range(10) if x % 3 == 0]
_ = [(i, val) for i, val in enumerate(baseline_metrics) if val > 0.8]

# Misleading intermediate computation (unused)
shadow_score = sum(w * (m ** 2) for m, w in zip(baseline_metrics, weights)) / sum(weights)

# Bit manipulation red herring (no actual impact)
flag_register = 0
flag_register |= (1 << 3)
flag_register ^= (1 << 1)
parity_check = bin(flag_register).count('1') % 2

# Unused nested function that looks important
def validate_consistency(trace, level=2):
    depth_mask = (1 << level) - 1
    checksum = 0
    for i, val in enumerate(trace):
        if i & depth_mask == 0:
            checksum ^= int(val * 100)
    return checksum

# Simulated diagnostic log (distractor)
diagnostic_log = {
    'stages_passed': 4,
    'errors_detected': 0,
    'final_flag': False
}

# Real computation begins here — deeply nested and mixed with distractions
extra_adjustments = {
    'gain': 1.05,
    'bias': -0.02,
    'enable_scaling': True
}

adjusted_metrics = []
for i, (metric, weight) in enumerate(zip(baseline_metrics, weights)):
    temp = metric
    if i % 2 == 0:
        temp += 0.01 * (i + 1)
    else:
        temp -= 0.005 * i
    
    # Apply fake conditional branch (looks impactful but minor)
    if temp > 0.85:
        temp = min(temp * extra_adjustments['gain'] + extra_adjustments['bias'], 0.99)
    
    adjusted_metrics.append(round(temp, 6))

# List comprehension with filtering (actual use)
valid_indices = [i for i, m in enumerate(adjusted_metrics) if m > 0.75]
filtered_metrics = [adjusted_metrics[i] for i in valid_indices]
filtered_weights = [weights[i] for i in valid_indices]

# Simulate complex data transformation using zip and enumerate
aggregation_buffer = []
for idx, (m, w) in enumerate(zip(filtered_metrics, filtered_weights)):
    contribution = m * w
    if idx > 0:
        # Introduce XOR-based weighting (bitwise distraction)
        shift = (w ^ idx) % 3
        contribution *= (1.1 ** shift)
    aggregation_buffer.append(contribution)

# Final aggregation logic (key statement)
def aggregate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    total_weight = sum(weights)
    raw_average = weighted_sum / total_weight
    
    # Secondary adjustment based on combinatorics of valid metrics
    n = len(metrics)
    combination_factor = (n * (n + 1)) // 2 if n > 1 else 1
    adjusted_average = raw_average * (1 + 0.01 * (combination_factor % 4))
    
    return round(adjusted_average, 6)

# Critical execution point
final_score = aggregate_performance(adjusted_metrics, weights)

# Print required output
print(f"Result: {final_score}")