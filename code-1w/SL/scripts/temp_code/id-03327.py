import itertools

# Simulated sensor data processing with performance scoring
raw_readings = [105, 215, 187, 94, 312, 267, 134, 190, 205]

# Irrelevant transformation: temperature normalization (unused later)
temp_scaled = [(x - 25) * 0.8 for x in raw_readings]

def apply_filter(data, threshold=150):
    # Filters out values below threshold and applies square root
    filtered = [int(x ** 0.5) for x in data if x > threshold]
    return filtered

def generate_pairs(lst):
    # Creates overlapping pairs (distractor function - not used in main logic)
    return list(itertools.combinations(lst, 2))

def compute_entropy(data):
    # Calculates approximate entropy using frequency counts (red herring)
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, but looks plausible
    return round(entropy, 4)

# Key preprocessing path
processed = apply_filter(raw_readings)

# Bit manipulation layer (used in final calculation)
bit_flags = [x ^ 3 for x in processed]  # XOR each with 3
activated = sum([1 for x in bit_flags if x & 1])  # Count odd numbers

# Set operations to remove duplicates and intersect with benchmark range
unique_vals = set(bit_flags)
benchmark_range = set(range(5, 25))
significant_metrics = list(unique_vals & benchmark_range)  # Intersection

# Slicing distraction: reverse every third element (unused)
reversed_slice = significant_metrics[::-3]

# Weight assignment (some weights are decoys)
weights = {
    'activation': 1.7,
    'stability': 0.9,
    'amplitude': 2.3,
    'baseline': 1.1,  # unused weight
    'tolerance': 0.7   # unused weight
}

# Performance metrics derived from multiple sources
metrics = {
    'activation': activated,
    'stability': sum(significant_metrics) / len(significant_metrics) if significant_metrics else 0,
    'amplitude': max(significant_metrics) * 2 if significant_metrics else 0
}

# Dead code path: recursive smoothing (never called)
def smooth_recursive(data, depth=0):
    if depth >= 3 or len(data) < 2:
        return data
    smoothed = [(data[i] + data[i+1]) // 2 for i in range(len(data)-1)]
    return smooth_recursive(smoothed, depth + 1)

# Core evaluation function
def evaluate_performance(met, wgt):
    score = 0
    # Only use specific keys intentionally
    if 'activation' in met:
        score += met['activation'] * wgt['activation']
    if 'stability' in met:
        score += met['stability'] * wgt['stability']
    if 'amplitude' in met:
        score += met['amplitude'] * wgt['amplitude']
    # Deliberately ignores other weights
    return int(score)

# Final computation
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")