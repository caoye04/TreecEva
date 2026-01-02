import itertools

def analyze_sequence(pattern, depth):
    if depth <= 0:
        return 0
    count = 0
    for i in range(len(pattern)):
        if pattern[i] == 'A':
            count += (i + 1) * depth
        elif pattern[i] == 'B':
            count -= depth // 2
    return count + analyze_sequence(pattern[1:], depth - 1)

def generate_metrics(base, factor):
    metrics = []
    temp = base
    for _ in range(5):
        temp = (temp * factor + 3) % 17
        metrics.append(temp)
    return metrics

def filter_outliers(data, limit=10):
    # Irrelevant filtering - never used
    return [x for x in data if abs(x - sum(data)/len(data)) < limit]

def compute_entropy(sequence):
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(sequence)
    for f in freq.values():
        p = f / total
        entropy -= p * log2(p)
    return round(entropy, 6)

def evaluate_performance(metrics, threshold):
    score = 0
    adjustments = { 'high': 3, 'low': -2, 'mid': 1 }
    
    # Real logic begins
    raw_sum = sum(metrics)
    
    # Distractor: complex unused transformation
    transformed = [((x >> 2) ^ 5) + (x % 4) for x in metrics]
    secondary_check = any(x > 12 for x in transformed)
    
    # Meaningful branching
    if raw_sum > threshold:
        score += adjustments['high']
    else:
        score += adjustments['low']
    
    # Bit manipulation red herring
    bit_analysis = 0
    for m in metrics:
        bit_analysis ^= (m << 1) & 0b1111
    
    # Conditional expression with decoy effect
    status = 'optimal' if all(m % 2 == 1 for m in metrics) else 'review'
    if status == 'optimal':  # Never true due to generation logic
        score += 10
    
    # Real contributor: combinatorics via itertools
    pairs = list(itertools.combinations(metrics, 2))
    valid_pairs = [p for p in pairs if (p[0] + p[1]) % 3 == 0]
    score += len(valid_pairs)
    
    # Dictionary-based weight map (partially used)
    weights = {i: val % 3 for i, val in enumerate(metrics)}
    bonus = sum(weights.values()) // 2
    score += bonus
    
    # Critical execution point
    final_score = score * 2 - 5
    
    # Dead code path (never reached)
    if bit_analysis < 0:
        final_score = -999
    
    return final_score

# Main execution flow
base_pattern = "ABAC"  # Used in analyze_sequence (distractor)
depth_control = 3

# Unused recursive analysis (red herring)
irrelevant_diagnostic = analyze_sequence(base_pattern, depth_control)

# Generate real input data
metric_data = generate_metrics(7, 4)

# Decoy data structure
log_snapshot = {
    'timestamp': 1678886400,
    'source': 'sensor-alpha',
    'readings': metric_data.copy(),
    'checksum': sum(x**2 for x in metric_data)
}

# Control flag with misleading name
adaptive_mode_enabled = False

# Threshold derived from entropy (but entropy not actually adaptive)
base_threshold = int(compute_entropy(metric_data) * 10)

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

# Output result
print(f"Result: {final_score}")