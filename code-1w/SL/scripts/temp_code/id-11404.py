import itertools

def analyze_sequence(data):
    # Irrelevant helper: counts vowels in stringified numbers (dead path)
    count = 0
    for item in data:
        if isinstance(item, str):
            count += sum(1 for c in item if c.lower() in 'aeiou')
    return count

def preprocess_signals(raw_logs):
    # Distractor function: processes log timestamps but unused in final chain
    timestamps = [entry['time'] for entry in raw_logs if 'time' in entry]
    avg_gap = sum(abs(a - b) for a, b in zip(timestamps, timestamps[1:])) / len(timestamps) if len(timestamps) > 1 else 0
    return [t % 3600 for t in timestamps], avg_gap

def transform_features(values):
    # Real transformation: applies bit manipulation and scaling
    transformed = []
    shift_key = 3
    for v in values:
        temp = (v << 2) ^ 5
        temp = (temp >> shift_key) + 7
        transformed.append(temp)
    return transformed

def filter_outliers(stream, threshold=150):
    # Mixed relevance: used indirectly via control flow
    clean = []
    for x in stream:
        if abs(x) < threshold or (x & 1):  # Keep small values or odd ones
            clean.append(x)
    return clean

def compute_entropy(arr):
    # Decoy metric: calculates entropy but not used in final score
    from math import log2
    freq = {}
    for a in arr:
        freq[a] = freq.get(a, 0) + 1
    total = len(arr)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def generate_combinations(elements):
    # Irrelevant: generates pairs but never used
    return list(itertools.combinations(elements, 2))

def validate_integrity(checksum, data):
    # Security red herring: looks important but bypassed
    calculated = sum(data) % 256
    return calculated == checksum

def recursive_reduce(n):
    # Relevant recursion: computes a derived weight factor
    if n <= 1:
        return 1
    return n - recursive_reduce(n - 2)

def evaluate_performance(metrics, config):
    # Core logic with distractions embedded
    
    # Step 1: Extract relevant base metrics
    base_values = [metrics['input_rate'], metrics['throughput'], metrics['latency']]  # latency is negative impact
    
    # Step 2: Transform using bit operations
    processed = transform_features(base_values)
    
    # Step 3: Apply filtering (only some values pass)
    filtered = filter_outliers(processed)
    
    # Step 4: Calculate composite index using list comprehension
    weights = [recursive_reduce(i+3) for i in range(len(filtered))]
    weighted_sum = sum(f * w for f, w in zip(filtered, weights))
    
    # Step 5: Incorporate configuration multipliers
    multiplier = config['scale_factor']
    if config['enable_enhancement'] and len(filtered) >= 2:
        enhancement = (filtered[0] + filtered[1]) / 4
        weighted_sum += enhancement
    
    # Step 6: Apply decay based on system age (logical branch)
    system_age = config['system_age']
    decay_factor = 1.0
    if system_age > 0:
        decay_factor = max(0.5, 1.0 - (system_age * 0.05))
    
    adjusted = weighted_sum * decay_factor
    
    # Step 7: Normalize against benchmark ceiling
    ceiling = 850
    normalized = (adjusted / ceiling) * 100
    
    # Step 8: Final nonlinear boost (sigmoid-like)
    import math
    final_score = int((normalized * (1 + math.exp(-normalized / 50))) / 2)
    
    # === DISTRACTOR VARIABLES BELOW ===
    # Fake dependencies
    temp_analysis = analyze_sequence([str(x) for x in base_values])
    log_data = [{'time': 100*i} for i in range(1, 5)]
    _, gap_metric = preprocess_signals(log_data)
    entropy_val = compute_entropy(filtered)
    combos = generate_combinations(filtered)
    integrity = validate_integrity(127, filtered)
    
    # Unused transformations
    dummy_shift = [(x << 1) ^ 3 for x in base_values]
    double_filtered = [x for x in filtered if x > 20]
    
    # Dead logic branch
    if len(combos) > 10:
        final_score -= 50
    else:
        pass  # Placeholder to mislead control flow analysis
    
    # Another decoy calculation
    peak = max(base_values) if base_values else 0
    penalty = 0
    if peak > 1000:
        penalty = (peak - 1000) // 100
    final_score -= penalty  # But peak never exceeds 1000
    
    return final_score

# Main execution
if __name__ == '__main__':
    metrics = {
        'input_rate': 48,
        'throughput': 62,
        'latency': 18,
        'redundancy': 91,  # Unused field
        'checksum': 127     # Red herring
    }
    
    benchmark_data = {
        'scale_factor': 1.8,
        'enable_enhancement': True,
        'system_age': 6,
        'version': '2.1b',  # Unused
        'debug_mode': False  # Unused
    }
    
    # Trigger key computation
    final_score = evaluate_performance(metrics, benchmark_data)
    
    # Print result as required
    print(f"Target result: {final_score}")