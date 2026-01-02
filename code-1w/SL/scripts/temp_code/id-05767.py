def evaluate_performance(metrics, weights):
    # Precompute weighted components
    raw_scores = {}
    for k in metrics:
        if k in weights:
            raw_scores[k] = metrics[k] * weights[k]
    
    # Irrelevant transformation: frequency analysis (dead computation)
    freq_analysis = {}
    total_chars = 0
    for key in metrics.keys():
        freq_analysis[key] = len(key) ** 2
        total_chars += len(key)
    scale_factor = total_chars / (1 + min(freq_analysis.values())) if freq_analysis else 1
    
    # Semi-relevant: normalize scores
    normalized = {}
    max_raw = max(raw_scores.values()) if raw_scores else 1
    for k in raw_scores:
        normalized[k] = raw_scores[k] / max_raw
    
    # Bitwise interference: encode keys (not used later)
    encoded_keys = {}
    for k in metrics:
        hash_val = 0
        for c in k:
            hash_val ^= ord(c) << 2
        encoded_keys[k] = hash_val & 0xFFFF
    
    # Conditional expression to adjust for efficiency metric
    efficiency_bonus = 1.1 if metrics.get('efficiency', 0) > 0.8 else 0.95
    
    # Aggregate score with conditional weighting
    aggregate = 0.0
    for k in normalized:
        adjustment = 1.05 if normalized[k] > 0.7 else 0.98
        aggregate += normalized[k] * adjustment
    
    # Final scoring with sorting side-path (distractor)
    sorted_norms = sorted(normalized.values(), reverse=True)
    decayed_sum = sum(v * (0.9 ** i) for i, v in enumerate(sorted_norms))
    
    # Actual final score computation (key logic)
    base_final = sum(normalized.values()) * efficiency_bonus
    final_score = int(base_final * 100)  # Scale and discretize
    
    # Dead code: unused diagnostic report
    diagnostics = {
        'version': '2.1',
        'processed': len(normalized),
        'outliers': [v for v in normalized.values() if v < 0.3],
        'consistency': sorted_norms[0] / sorted_norms[-1] if len(sorted_norms) > 1 else 1
    }
    
    return final_score

# Input data
metrics = {
    'accuracy': 0.92,
    'efficiency': 0.85,
    'latency': 0.78,
    'throughput': 0.88,
    'stability': 0.91
}

weights = {
    'accuracy': 0.3,
    'efficiency': 0.25,
    'latency': 0.15,
    'throughput': 0.2,
    'stability': 0.1
}

# Execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")