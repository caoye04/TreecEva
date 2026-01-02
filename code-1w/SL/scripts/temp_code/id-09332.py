import itertools

# Simulated system performance metrics
def collect_metrics():
    raw_data = [15, 23, 8, 42, 19, 7, 31]
    offset = 5
    processed = [x + offset for x in raw_data]
    filtered = [x for x in processed if x > 25]
    return {f'node_{i}': val for i, val in enumerate(filtered)}

def calculate_efficiency(nodes):
    total = sum(nodes.values())
    count = len(nodes)
    average = total / count if count else 0
    efficiency = average * 0.85  # arbitrary scaling
    return efficiency

def generate_synthetic_load(base):
    # Irrelevant function - red herring
    return [base ** i % 100 for i in range(10)]

def analyze_redundancy(pattern):
    # Dead code path - never used
    from collections import defaultdict
    counts = defaultdict(int)
    for p in pattern:
        counts[p] += 1
    return dict(counts)

def extract_diagnostic_codes(data):
    # Distractor computation
    codes = []
    for k, v in data.items():
        if 'node_2' in k:
            codes.append(v * 2)
        elif 'node_3' in k:
            codes.append(v + 10)
    return codes  # never used

def transform_key_sequence(seq):
    # Unused transformation logic
    shifted = [(x << 2) & 255 for x in seq]
    return [x ^ 170 for x in shifted]

def validate_integrity(checksum, values):
    # Misleading validation
    computed = sum(values) % 256
    return computed == checksum

def compute_fallback_threshold(values):
    # Decoy fallback mechanism
    sorted_vals = sorted(values, reverse=True)
    return sorted_vals[2] if len(sorted_vals) > 2 else 0

def evaluate_performance(metrics, reference):
    # Core logic disguised among distractors
    baseline = reference['baseline']
    peak = reference['peak']
    adjustment_factor = (peak - baseline) / 100.0
    
    # Real calculation chain
    raw_scores = list(metrics.values())
    boosted = list(map(lambda x: x * adjustment_factor, raw_scores))
    capped = [min(x, 45.0) for x in boosted]
    
    # Conditional branching with relevance
    if len(capped) > 3:
        subset = capped[:3]
    else:
        subset = capped + [10.0] * (3 - len(capped))
    
    # Use of itertools - required feature
    rolling_window = list(itertools.accumulate(subset, func=lambda a, b: a * 0.9 + b))
    smoothed = rolling_window[-1]
    
    # Final computation
    multiplier = 2.5 if smoothed > 30 else 1.8
    final = smoothed * multiplier
    
    # Introduce irrelevant variables to increase interference
    temp_debug = [x * 2 + 1 for x in raw_scores]  # unused
    dummy_lookup = {i: chr(65 + i) for i in range(10)}  # decoy dict
    shadow_copy = metrics.copy()  # never accessed
    
    return int(final)

# Orchestration block
if __name__ == '__main__':
    # Primary data sources
    benchmark_data = {
        'baseline': 18,
        'peak': 68,
        'version': '3.1.4',
        'nodes_active': 7
    }
    
    # Collect real input
    metrics = collect_metrics()
    
    # Generate unused synthetic data (distractor)
    load_profile = generate_synthetic_load(7)
    diagnostic_traces = extract_diagnostic_codes(metrics)
    
    # Core execution point
    final_score = evaluate_performance(metrics, benchmark_data)
    
    # Print required result
    print(f"Result: {final_score}")