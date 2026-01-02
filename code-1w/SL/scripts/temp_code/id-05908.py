from collections import defaultdict, Counter
import math

# Irrelevant utility functions (distractors)
def normalize_vector(vec):
    norm = sum(x ** 2 for x in vec) ** 0.5
    return [x / norm for x in vec] if norm else vec
def entropy(labels):
    counts = Counter(labels)
    total = len(labels)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def transform_key(key):
    # Complex but ultimately unused transformation
    shifted = ''.join(chr((ord(c) - ord('a') + 5) % 26 + ord('a')) for c in key)
    return shifted[::-1]

# Relevant data structures
baseline = {
    'accuracy': 0.85,
    'latency': 120,
    'throughput': 480,
    'errors': 3
}

metric_data = [
    {'accuracy': 0.87, 'latency': 110, 'throughput': 520, 'errors': 2},
    {'accuracy': 0.83, 'latency': 130, 'throughput': 460, 'errors': 4},
    {'accuracy': 0.90, 'latency': 115, 'throughput': 500, 'errors': 1}
]

# Decoy statistical aggregator (never called)
def aggregate_metrics(metrics_list):
    agg = defaultdict(float)
    for m in metrics_list:
        for k, v in m.items():
            agg[k] += v / len(metrics_list)
    return dict(agg)

# Unused recursive bit manipulation (red herring)
def bit_reversed(n, width=8):
    return int(bin(n)[2:].zfill(width)[::-1], 2)

def analyze_pattern(sequence):
    result = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            result ^= bit_reversed(val % 256)
        else:
            result += (val >> 3) & 0xFF
    return result

# Real logic begins here
weight_map = lambda w: {k: w[k] * 1.5 if k == 'accuracy' else w[k] * 0.5 for k in w}

adjusted_baseline = weight_map(baseline)

# Simulate environmental interference factors (some used, some not)
environment_factor = 1.05
temperature_bias = 0.98  # never used
humidity_offset = 0.02   # dead code

# Core evaluation function with nested logic
def evaluate_performance(metrics, base):
    scores = []
    for entry in metrics:
        raw_score = 0
        # Accuracy contributes positively
        if entry['accuracy'] >= base['accuracy']:
            raw_score += 20 * (entry['accuracy'] - base['accuracy']) * 100
        
        # Latency penalty
        latency_diff = entry['latency'] - base['latency']
        if latency_diff < 0:
            raw_score += 15
        elif latency_diff > 0:
            raw_score -= abs(latency_diff) * 0.5
        
        # Throughput bonus
        throughput_ratio = entry['throughput'] / base['throughput']
        raw_score += 10 * (throughput_ratio - 1) * 100
        
        # Error penalty (non-linear)
        error_diff = entry['errors'] - base['errors']
        if error_diff < 0:
            raw_score += 12 * abs(error_diff)
        elif error_diff > 0:
            raw_score -= 25 * error_diff
        
        # Apply environment factor (only real use of environment_factor)
        raw_score *= environment_factor
        
        # Early exit red herring (this condition never triggers)
        if raw_score > 1000:
            return -999  # decoy outcome
            
        scores.append(raw_score)
    
    # Aggregate using slicing and filtering
    valid_scores = [s for s in scores if s > -500]  # filter decoy
    trimmed = sorted(valid_scores)[1:-1] if len(valid_scores) > 2 else valid_scores  # trim outliers
    
    # Final computation
    final_avg = sum(trimmed) / len(trimmed) if trimmed else 0
    
    # Additional transformation
    performance_index = max(0, final_avg) ** 0.5 * 2.5
    
    # The actual answer derivation
    complexity_penalty = len(metrics) * 1.2
    return int(performance_index - complexity_penalty)

# Misleading pre-computation (looks important but unused)
total_entropy = entropy([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
vector_norm = normalize_vector([1, 2, 3, 4])

# Key execution point
final_score = evaluate_performance(metric_data, baseline)

# Output result as required
print(f"Target result: {final_score}")