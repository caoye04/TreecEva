from itertools import compress, cycle

def analyze_signal(data, threshold=0.75):
    """Irrelevant signal processing function (dead code path)."""
    filtered = [x for x in data if x > threshold]
    return [f'{x:.3f}' for x in filtered]

def generate_sequence(n):
    """Unused sequence generator (distractor)."""
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def normalize(values):
    """Normalize values to unit range."""
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0.5] * len(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def calculate_entropy(weights):
    """Calculate entropy of weight distribution (misleading intermediate)."""
    from math import log2
    return -sum(w * log2(w) for w in weights if w > 0)

def validate_integrity(index_map, keys):
    """Dead logic branch - never actually used."""
    return all(k in index_map for k in keys)

def evaluate_performance(metrics, weights):
    # Core logic begins: score based on weighted normalized performance
    norm_metrics = normalize(metrics)
    
    # Apply cyclic weighting via itertools.cycle
    weighted = []
    weight_cycle = cycle(weights)
    for m in norm_metrics:
        weight = next(weight_cycle)
        weighted.append(m * weight)
    
    base_score = sum(weighted)
    
    # Additional adjustment using enumerate and zip
    adjustments = []
    for i, (m, w) in enumerate(zip(norm_metrics, weights)):
        if i % 2 == 0:
            adjustments.append(m * w * 0.1)
        else:
            adjustments.append(-m * w * 0.05)
    
    adjustment_sum = sum(adjustments)
    temp_score = base_score + adjustment_sum
    
    # Secondary correction based on metric clustering
    clusters = [[], [], []]
    for idx, val in enumerate(norm_metrics):
        clusters[idx % 3].append(val)
    
    cluster_avgs = [sum(c)/len(c) if c else 0 for c in clusters]
    
    # Decoy usage of itertools.compress
    selector = [True, False, True]
    selected_avgs = list(compress(cluster_avgs, selector))
    cluster_bonus = sum(selected_avgs) * 0.05  # Minor influence
    
    final_score = temp_score + cluster_bonus
    
    # Red herring: unused transformation
    transformed = [round(x**0.5, 4) for x in norm_metrics if x > 0.5]
    
    # Final clamp and scaling
    if final_score > 1.0:
        final_score = 0.95 + (final_score - 1.0) * 0.1
    elif final_score < 0.0:
        final_score = 0.05 - (0.0 - final_score) * 0.1
        
    return round(final_score * 100000, 6)  # Scale to large integer-like decimal

# Main execution
if __name__ == '__main__':
    # Irrelevant data
    raw_signals = [0.82, 0.67, 0.91, 0.73, 0.88]
    _ = analyze_signal(raw_signals)
    
    # Unused generated sequence
    fib_like = generate_sequence(10)
    
    # Key input data
    metrics = [85, 90, 78, 92, 88, 76, 95]
    weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.05, 0.15]
    
    # Dead variables and decoy operations
    index_mapping = {f'key_{i}': i*2 for i in range(len(metrics))}
    key_list = [f'key_{i}' for i in range(len(metrics))]
    _ = validate_integrity(index_mapping, key_list)
    
    entropy = calculate_entropy(normalize(weights))
    
    # Critical statement
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")