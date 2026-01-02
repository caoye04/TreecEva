import itertools

def analyze_sequence(patterns):
    # Irrelevant function - dead code path
    return sum(len(p) for p in patterns if len(p) % 2 == 0)

def preprocess_inputs(data_stream):
    # Distractor computation: transforms data but not used in final result
    shifted = [(x >> 2) ^ 3 for x in data_stream]
    filtered = [x for x in shifted if x > 5]
    return filtered + [len(filtered)]

def compute_weighted_sum(values, weights):
    # Misleading intermediate: looks important but unused
    weighted = 0
    for i in range(min(len(values), len(weights))):
        weighted += values[i] * weights[i]
    return weighted

def calculate_entropy(sequence):
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return round(entropy, 6)

def validate_integrity(checksums):
    # Decoy function with complex logic that doesn't affect outcome
    cumulative = 0
    for c in checksums:
        if c < 0:
            cumulative ^= (c & 0xFF)
        else:
            cumulative += (c << 1) % 17
    return cumulative % 100 == 0

def evaluate_performance(metrics, benchmark_data):
    # Core logic embedded within noise
    base = 0
    for k, v in metrics.items():
        if 'latency' in k:
            base += v * 0.3
        elif 'throughput' in k:
            base += v * 0.7
    
    # Key transformation using itertools
    pairs = list(itertools.combinations(benchmark_data, 2))
    adjustments = 0
    for a, b in pairs:
        if a < b:
            adjustments += (b - a) // 4
        else:
            adjustments -= (a - b) // 5
    
    # Conditional override based on hidden rule
    threshold = calculate_entropy(benchmark_data)
    if threshold > 2.0:
        adjustments = adjustments // 2  # Subtle correction
    
    # Final score depends only on this path
    final_score = int(base + adjustments)
    
    # Red herring: many variables defined but not all used
    temp_result = final_score * 2  # unused
    normalized = temp_result % 999  # unused
    
    return final_score

# Simulated input data
metrics = {
    'latency_avg_ms': 120,
    'latency_peak_ms': 250,  # distractor key
    'throughput_rps': 80,
    'throughput_max': 95     # distractor key
}

benchmark_data = [12, 15, 12, 18, 15, 21, 12]

# Unused but plausible-looking preprocessing
signal_chain = [x * 2 + 1 for x in benchmark_data]
data_trace = preprocess_inputs(signal_chain)
weight_vector = [0.1, 0.3, 0.6]  # unused
side_metrics = compute_weighted_sum(benchmark_data, weight_vector)

# Trigger integrity check (irrelevant to result)
checksums = [sum(benchmark_data), len(benchmark_data), -1]
valid = validate_integrity(checksums)

# Actual execution point of interest
final_score = evaluate_performance(metrics, benchmark_data)

# Print required output
print(f"Result: {final_score}")