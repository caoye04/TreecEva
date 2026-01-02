from collections import defaultdict, Counter

def analyze_pattern(sequence):
    freq = Counter(sequence)
    return sum(k * v for k, v in freq.items() if v > 1)

def preprocess_data(raw):
    cleaned = [x for x in raw if x > 0]
    shifted = [x << 1 for x in cleaned]
    return [x for x in shifted if x % 3 == 0]

def dummy_transformation(data):
    # Irrelevant transformation path (dead code)
    result = []
    for x in data:
        result.append(x ** 2 + 1)
    return result

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def filter_outliers(arr):
    avg = sum(arr) / len(arr)
    dev = [(x - avg) ** 2 for x in arr]
    variance = sum(dev) / len(dev)
    std = variance ** 0.5
    return [x for x in arr if abs(x - avg) <= 2 * std]

def generate_weight_map(keys):
    # Distractor: builds a complex structure not fully used
    weight_map = defaultdict(float)
    for i, k in enumerate(keys):
        weight_map[k] = 0.1 * (i + 1) ** 0.5
    weight_map['bonus'] = 0.25
    return dict(weight_map)

def evaluate_component(x, threshold=5):
    if x < threshold:
        return x * 1.5
    elif x == threshold:
        return x * 2
    else:
        return x * 0.8 + 3

def main_logic():
    # Real input data
    raw_input = [2, -1, 3, 4, 5, 6, 2, 8, 9, -5, 3]
    processed = preprocess_data(raw_input)
    
    # Extract frequency-based pattern score (red herring)
    pattern_score = analyze_pattern(processed)
    
    # Actual relevant metrics
    base_metrics = [7, 5, 9, 3, 8]
    filtered_metrics = filter_outliers(base_metrics)
    
    # Apply real transformation
    evaluated = [evaluate_component(x) for x in filtered_metrics]
    
    # Entropy computed but only for distraction
    entropy = compute_entropy(evaluated)
    
    # Generate weights (partially used)
    keys = ['a', 'b', 'c', 'd', 'e']
    weights = generate_weight_map(keys)
    
    # Critical assignment: some weights are ignored, only first five matter
    final_weights = [weights.get(k, 0.1) for k in keys[:len(evaluated)]]
    
    # Normalize weights to sum to 1.0
    w_sum = sum(final_weights)
    final_weights = [w / w_sum for w in final_weights]
    
    # Combine metrics and weights
    def evaluate_performance(mets, wts):
        return sum(m * w for m, w in zip(mets, wts))
    
    # Key statement
    final_score = evaluate_performance(evaluated, final_weights)
    
    # Unused variables - distractions
    temp_result = dummy_transformation(processed)
    extra_data = {k: v for k, v in enumerate(zip(processed, temp_result))}
    anomaly_count = len(raw_input) - len(processed)
    
    # Print final result as required
    print(f"Result: {final_score}")
    
    return final_score

# Execution entry point
result = main_logic()