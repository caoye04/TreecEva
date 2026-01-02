def preprocess_input(raw):
    # Irrelevant preprocessing (distractor)
    cleaned = [x for x in raw if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    return normalized

# Misleading data transformation chain
def transform_series(values):
    shifted = [v << 1 for v in values]  # Bitwise left shift (red herring)
    toggled = [s ^ 5 for s in shifted]  # XOR with constant (decoy)
    return toggled

# Unused recursive function (dead code path)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Decoy statistical function that isn't used in final calculation
def get_variance(arr):
    mean = sum(arr) / len(arr)
    return sum((x - mean) ** 2 for x in arr) / len(arr)

# Core logic hidden among distractions
def evaluate_metric(entries, config):
    indexed = enumerate(entries)
    paired = zip([k for k in config.keys()], [v for v in config.values()])
    score_map = {key: val * 2 for key, val in paired}
    
    temp_scores = []
    for i, entry in indexed:
        if i % 2 == 0:
            temp_scores.append(entry * 3)
        else:
            temp_scores.append(entry + 1)
    
    # Actual relevant manipulation
    adjusted = [t | 1 for t in temp_scores]  # OR with 1 (bitwise relevance)
    return adjusted

# Main scoring function intertwined with noise
def calculate_final_score(dataset, factors):
    # Distractor: complex but unused dictionary comprehension
    _unused_lookup = {
        f'key_{i}': {'value': j ** 2, 'active': (j % 2 == 0)} 
        for i, j in enumerate(sorted(factors.values()))
    }
    
    # Real computation begins
    base_values = [x for x in dataset if isinstance(x, int)]
    filtered = list(filter(lambda z: z > 10, base_values))  # Filter step
    
    # Weight application using dictionary and zip
    weight_keys = ['w1', 'w2', 'w3']
    weights_mapped = dict(zip(weight_keys, factors.values()))
    
    multiplier = weights_mapped['w1'] + 0.5
    
    intermediate = []
    for idx, val in enumerate(filtered):
        if idx < 2:
            intermediate.append(val * multiplier)
        else:
            intermediate.append(val - 5)

    # Nested conditional with bit operation twist
    processed = []
    for p in intermediate:
        if p > 20:
            p = p & (~1)  # Clear least significant bit
        elif p == 20:
            p = p ^ 1
        else:
            p = p | 1
        processed.append(p)
    
    # Final aggregation buried in complexity
    aggregate = sum(processed)
    penalty = len([p for p in processed if p % 3 == 0]) * 2
    final_score = int(aggregate - penalty)  # Key assignment point
    
    return final_score

# Global irrelevant constants (red herrings)
MAX_BUFFER = 1024
DEBUG_MODE = False
DEFAULT_TIMEOUT = 30

# Input data with mixed relevance
raw_data = [5, 12, 18, 7, 22, 14, 'invalid', 30, None, 25]
weights_config = {
    'w1': 1.2,
    'w2': 0.8,
    'w3': 1.5
}

# Preprocessing call (unused result)
cleaned_data = preprocess_input([12, 18, 22, 14, 30, 25])

# Transform series (result not used)
distorted = transform_series([1, 2, 3, 4])

# Evaluate metric — actually contributes to logic
evaluation_input = [12, 18, 22, 14, 30, 25]
score_parts = evaluate_metric(evaluation_input, weights_config)

# Critical execution point
final_score = calculate_final_score(raw_data, weights_config)

print(f"Target result: {final_score}")