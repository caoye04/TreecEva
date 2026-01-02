import math

def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return sum(1 for x in data if x > threshold) / len(data)

def dummy_transformation(x):
    """Dead code path - never used."""
    return (x ** 2 + 3 * x + 1) % 100

def bitwise_flag_check(value):
    # Meaningful distractor: used to calculate intermediate but not final result
    flags = {
        'high': (value & 1) != 0,
        'mid': (value & 2) != 0,
        'low': (value & 4) != 0
    }
    return sum(k for k, v in enumerate(flags.values()) if v)  # unused return

def compute_entropy(values):
    """Unused advanced calculation - red herring."""
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def slice_and_process(arr, start=1, end=-1):
    # Slicing operation (required)
    segment = arr[start:end]
    adjusted = [x * 1.5 for x in segment]
    return adjusted

def evaluate_performance(metrics, weights):
    # Core logic begins here
    temp_results = {}
    
    # Irrelevant preprocessing
    noise_filter = lambda x: x if x > 0 else 0  # lambda function (required)
    cleaned = [noise_filter(x) for x in metrics['raw']]
    
    # Distractor: complex but unused transformation
    transformed = {
        'shifted': [((x << 2) ^ 5) & 255 for x in cleaned],  # bitwise and slicing-like logic
        'stats': {
            'max': max(cleaned),
            'min': min(cleaned),
            'range': max(cleaned) - min(cleaned)
        }
    }
    
    # Actual relevant computation starts
    base_scores = []
    for i, val in enumerate(metrics['factors']):
        if i % 2 == 0:
            base_scores.append(val ** 1.5)
        else:
            base_scores.append(math.sqrt(val * 2))
    
    # Dictionary operations (required)
    score_map = {i: score for i, score in enumerate(base_scores)}
    weight_map = {idx: w for idx, w in enumerate(weights)}
    
    # Main weighted aggregation
    aggregate = 0
    for idx in range(len(base_scores)):
        if idx in score_map and idx in weight_map:
            contribution = score_map[idx] * weight_map[idx]
            if contribution > 0.5:  # filtering condition
                aggregate += contribution

    # Secondary adjustment using modular arithmetic
    adjustment_factor = 0
    for k in sorted(score_map.keys()):
        adjustment_factor += (k * score_map[k]) % 7
    
    # Combine results
    preliminary = aggregate + (adjustment_factor * 0.1)
    
    # Final nonlinear scaling
    final_score = int(preliminary * 100) / 100.0  # normalize to 2 decimals
    
    # Dead code branch - misleading
    if final_score < 0:
        final_score *= -1  # never reached
    
    return final_score

# Primary data input
metrics = {
    'raw': [0.8, -0.2, 0.9, 0.1, 0.7],
    'factors': [4, 9, 16, 25],
    'meta': {
        'version': '2.1',
        'active': True,
        'flags': [1, 0, 1]
    }
}

weights = [0.3, 0.5, 0.4, 0.6]

# Unused slicing example - distractor
historical_data = [10, 20, 30, 40, 50]
slice_result = slice_and_process(historical_data, 1, 4)

# Another decoy variable
entropy_value = compute_entropy([4, 5, 6])

# Key execution point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")