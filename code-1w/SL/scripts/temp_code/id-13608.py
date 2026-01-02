from collections import defaultdict, Counter
from itertools import zip_longest
import math

# Simulated sensor fusion system for autonomous drone navigation

def analyze_stability(readings):
    # Irrelevant helper: analyzes gyroscopic stability (dead-end)
    if len(readings) < 3:
        return 0.0
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return round(math.exp(-variance), 4)

def calculate_entropy(sequence):
    # Misleading distractor: computes Shannon entropy (not used in final result)
    freqs = Counter(sequence)
    total = len(sequence)
    return -sum((count/total) * math.log2(count/total) for count in freqs.values())

def normalize_vector(vec):
    # Red herring function: normalizes a vector (used only on decoy data)
    magnitude = math.sqrt(sum(x**2 for x in vec))
    return [round(x/magnitude, 6) for x in vec] if magnitude > 0 else vec

def recursive_filter(values, threshold, depth=0):
    # Seemingly important but ultimately unused recursive transformation
    if depth >= 3 or not values:
        return [v for v in values if v > threshold * 0.7]
    filtered = [v for v in values if v > threshold]
    return recursive_filter(filtered, threshold * 0.9, depth + 1)

def validate_calibration(signal_log):
    # Unused validation chain that looks critical
    if not signal_log:
        return False
    status_map = defaultdict(lambda: 'unknown')
    for idx, val in enumerate(signal_log):
        status_map[idx] = 'valid' if 0.1 <= val <= 0.9 else 'invalid'
    return dict(status_map)

# Real computation begins here — buried among distractions
raw_metrics = [85, 92, 78, 96, 88]
decoys = {'a': [1.2, 3.4], 'b': 'unused', 'c': (lambda x: x**3)(4)}

# Core weight system — key to actual answer
base_weights = [0.1, 0.2, 0.3, 0.25, 0.15]
temp_adjustment = list(map(lambda w: w * 1.1, base_weights))  # Intermediate distraction
metric_weights = [round(w * 0.95, 3) for w in temp_adjustment]  # Actual weights used

# Phantom data structures
phantom_matrix = [[i*j for j in range(4)] for i in range(4)]
shadow_buffer = bytearray(b'\x00' * 16)

# Simulated outcome mapping — only specific indices matter
raw_outcomes = []
for idx, score in enumerate(raw_metrics):
    if idx % 2 == 0:
        # Only even indices contribute meaningfully
        adjusted = score * (1 + 0.05 * idx)
    else:
        adjusted = score * 0.95
    raw_outcomes.append(round(adjusted))

# Fake aggregation path
aggregation_modes = ('sum', 'weighted', 'median')
mode_selector = {m: i for i, m in enumerate(aggregation_modes)}
selected_mode = 'weighted'  # Looks configurable, but hardcoded

# Critical evaluation function — buried late in code
def evaluate_performance(weights, outcomes):
    # Only first four elements are actually used
    trimmed_weights = weights[:4]
    trimmed_outcomes = outcomes[:4]
    
    # Normalize weights to ensure sum to 1.0 (real step)
    weight_sum = sum(trimmed_weights)
    normalized_weights = [w / weight_sum for w in trimmed_weights]
    
    # Compute weighted score — this determines final answer
    cumulative = 0.0
    for i in range(len(normalized_weights)):
        cumulative += normalized_weights[i] * trimmed_outcomes[i]
    
    # Apply final nonlinear boost (deterministic)
    final = cumulative * (1.0 + 0.1 * math.sin(math.pi / 6))
    return round(final, 6)

# Decoy call that seems important
_ = validate_calibration([0.5, 0.7, 0.3])
_ = recursive_filter([10, 20, 5, 8], 7)

# Key assignment — the target of the question
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print required output
print(f"Target result: {final_score}")