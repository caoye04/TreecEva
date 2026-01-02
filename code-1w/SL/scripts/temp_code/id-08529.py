import itertools

def preprocess_entry(entry):
    # Normalize and transform raw sensor data
    normalized = [(x - min(entry)) / (max(entry) - min(entry) + 1e-9) for x in entry]
    return [round(x * 100) for x in normalized]

def calculate_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def evaluate_performance(weights, data):
    # Irrelevant helper: computes unused statistic
    def compute_redundant_metric(seq):
        xor_chain = 0
        for i in range(len(seq)):
            xor_chain ^= i * seq[i] % 7
        return xor_chain

    processed_batches = [preprocess_entry(batch) for batch in data]
    
    # Misleading intermediate: looks important but only used in dead branch
    batch_variances = [max(pb) - min(pb) for pb in processed_batches]
    avg_variance = sum(batch_variances) / len(batch_variances)

    # Key computation path
    flattened = list(itertools.chain.from_iterable(processed_batches))
    entropy = calculate_entropy(flattened)
    
    # Simulate weighted scoring across dimensions
    base_scores = {
        'consistency': 85,
        'coverage': len(flattened),
        'stability': 100 - (max(flattened) - min(flattened)) // 2
    }
    
    # Dead code path with misleading logic
    if avg_variance > 1000:  # Never true
        redundant = compute_redundant_metric(flattened)
        base_scores['consistency'] -= redundant

    # Actual score calculation
    dynamic_weight = lambda w: w * 0.9 if w < 0.3 else w * 1.1
    adjusted_weights = [dynamic_weight(w) for w in weights]
    weight_sum = sum(adjusted_weights)
    normalized_weights = [w / weight_sum for w in adjusted_weights]

    final_score = 0
    for i, (key, base) in enumerate(base_scores.items()):<key>
        contribution = base * normalized_weights[i % len(normalized_weights)]
        final_score += contribution

    # Add entropy bonus scaled by stability factor
    stability_factor = base_scores['stability'] / 100
    final_score += entropy * stability_factor * 5

    return int(round(final_score))

# Input data
metric_weights = [0.25, 0.35, 0.4]
raw_data = [
    [12, 15, 14, 18, 13],
    [11, 16, 19, 10, 14],
    [13, 17, 15, 12, 16]
]

# Execution point
final_score = evaluate_performance(metric_weights, raw_data)
print(f"Result: {final_score}")