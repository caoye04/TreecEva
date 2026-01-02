import itertools

def analyze_trends(data, threshold=5):
    trend_lines = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trend_lines.append((i-1, i))
    return trend_lines

def filter_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]

def compute_entropy(arr):
    from math import log2
    total = sum(arr)
    if total == 0:
        return 0
    probs = [x / total for x in arr if x > 0]
    return -sum(p * log2(p) for p in probs)

def generate_pairs(seq):
    # Irrelevant utility function
    return list(itertools.combinations(seq, 2))

def merge_metrics(a, b, c, weight=(0.4, 0.3, 0.3)):
    # Complex weighting with red herring parameters
    temp_debug = [x * weight[0] for x in a]  # unused
    debug_log = {'stage1': sum(a), 'stage2': sum(b)}  # decoy
    return [a[i]*weight[0] + b[i]*weight[1] + c[i]*weight[2] for i in range(len(a))]

def evaluate_performance(metrics, baseline):
    adjusted = [m - baseline[i % len(baseline)] for i, m in enumerate(metrics)]
    amplified = [x * 1.75 for x in adjusted]  # amplification factor
    
    # Distractor: complex transformation chain
    transformed = []
    for val in amplified:
        if val < 0:
            transformed.append(abs(val) ** 0.5 * -1)
        else:
            transformed.append(val ** 0.5)
    
    # Real logic begins here
    signs = [1 if x >= 0 else -1 for x in transformed]
    magnitudes = [abs(x) for x in transformed]
    normalized = [m / (1 + m) for m in magnitudes]  # squash to [0,1)
    signed_norm = [signs[i] * normalized[i] for i in range(len(normalized))]
    
    # Final aggregation
    raw_total = sum(signed_norm)
    penalty_factor = len([x for x in signed_norm if x < 0]) * 0.1
    final_score = int(raw_total * 100 - penalty_factor * 50)  # deterministic integer
    
    # Dead code path - never reached due to return
    if final_score < 0:
        recovery_mode = True
        final_score += 200
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated sensor metrics over time
    raw_data = [8, 12, 5, 19, 3, 7, 14, 6, 9, 11]
    base_ref = [4, 6, 3, 8, 2]
    
    # Irrelevant preprocessing
    trends = analyze_trends(raw_data)
    clean_data = filter_outliers(raw_data, factor=2.0)
    entropy = compute_entropy(raw_data)
    
    # Generate meaningless pairs
    pairs = generate_pairs([1, 2, 3, 4])
    
    # Construct metrics through layered distraction
    part_a = [x * 2 for x in raw_data if x > 5]
    part_b = [x + 1 for x in base_ref]
    part_c = [x % 7 for x in raw_data[:len(base_ref)]]
    
    # Merge with decoy weights
    merged = merge_metrics(part_a, part_b, part_c, weight=(0.4, 0.3, 0.3))
    
    # Core evaluation
    metrics = [abs(m * 1.3) for m in merged[:len(base_ref)]]
    final_score = evaluate_performance(metrics, base_ref)
    
    # Critical print statement
    print(f"Result: {final_score}")